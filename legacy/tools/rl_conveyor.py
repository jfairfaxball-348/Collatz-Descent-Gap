#!/usr/bin/env python3
"""Fail-closed, non-promoting utilities for the RL research conveyor."""

import argparse
import base64
import binascii
import hashlib
import io
import json
import os
import re
import shlex
import shutil
import stat
import subprocess
import sys
import tarfile
import tempfile
import zipfile
from datetime import datetime, timezone
from pathlib import Path, PurePosixPath

from rl_catalog import (
    CatalogError,
    parse_rl_identifier,
    query_results,
    query_sessions,
    validate_indexes,
    write_indexes,
)

ROOT = Path(__file__).resolve().parents[1]
AUTH = ROOT / "authoritative"
GIT_TIMEOUT_SECONDS = 30
RECONSTRUCTION_TIMEOUT_SECONDS = 60
VERIFIER_TIMEOUT_SECONDS = 120
DIRECT_TREE_TRANSPORTS = {
    "direct Git tree plus deterministic ZIP reconstruction",
    "lossless_git_tree_plus_deterministic_reconstruction",
}
DIRECT_TREE_MANIFEST_V1_FIELDS = {
    "canonical_zip",
    "canonical_zip_sha256",
    "completed_package_tree_sha",
    "completed_rl",
    "incoming_rl",
    "incoming_rl_started",
    "reconstruction_script",
    "transport",
}
DIRECT_TREE_MANIFEST_V2_FIELDS = {
    "canonical_zip",
    "canonical_zip_sha256",
    "completed_package_tree",
    "completed_rl",
    "incoming_rl",
    "incoming_status",
    "transport",
}
SNAPSHOT_FORMAT = "rl-authoritative-snapshot-v2"


class Failure(RuntimeError):
    pass


def git(*args, timeout=GIT_TIMEOUT_SECONDS):
    try:
        run = subprocess.run(
            ["git", *args], cwd=ROOT, text=True, capture_output=True, timeout=timeout
        )
    except (OSError, subprocess.TimeoutExpired) as error:
        raise Failure("git command failed: %s" % error) from error
    if run.returncode:
        raise Failure(run.stderr.strip() or "git command failed")
    return run.stdout


def _git_bytes(*args, timeout=GIT_TIMEOUT_SECONDS):
    try:
        run = subprocess.run(
            ["git", *args], cwd=ROOT, stdout=subprocess.PIPE,
            stderr=subprocess.PIPE, timeout=timeout,
        )
    except (OSError, subprocess.TimeoutExpired) as error:
        raise Failure("git command failed: %s" % error) from error
    if run.returncode:
        message = run.stderr.decode("utf-8", errors="replace").strip()
        raise Failure(message or "git command failed")
    return run.stdout


def _optional_git(*args):
    try:
        return git(*args).strip()
    except Failure:
        return None


def digest(path):
    h = hashlib.sha256()
    with path.open("rb") as source:
        for block in iter(lambda: source.read(1024 * 1024), b""):
            h.update(block)
    return h.hexdigest()


def safe(name):
    if not isinstance(name, str) or not name or "\0" in name or "\\" in name:
        raise Failure("unsafe bundle/manifest path: %r" % name)
    raw_parts = name.split("/")
    if any(part in {"", ".", ".."} for part in raw_parts):
        raise Failure("unsafe bundle/manifest path: %r" % name)
    path = PurePosixPath(name)
    if path.is_absolute() or re.fullmatch(r"[A-Za-z]:", raw_parts[0]):
        raise Failure("unsafe bundle/manifest path: %r" % name)
    return Path(*path.parts)


def safe_manifest_path(name):
    """Accept the checksum convention './path' without erasing traversal."""
    if isinstance(name, str) and name.startswith("./"):
        name = name[2:]
    return safe(name)


def _read_json_object(path, description):
    try:
        value = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, UnicodeError, json.JSONDecodeError) as error:
        raise Failure("cannot read %s: %s" % (description, error)) from error
    if not isinstance(value, dict):
        raise Failure("%s must contain one JSON object" % description)
    return value


def _direct_transport_manifest(path, current_rl, target, expected_name, expected_hash):
    manifest_path = path / "TRANSPORT_MANIFEST.json"
    manifest = _read_json_object(manifest_path, "direct-tree transport manifest")
    fields = set(manifest)
    if fields == DIRECT_TREE_MANIFEST_V1_FIELDS:
        tree_hash = manifest["completed_package_tree_sha"]
        script_value = manifest["reconstruction_script"]
        incoming_not_started = manifest["incoming_rl_started"] is False
    elif fields == DIRECT_TREE_MANIFEST_V2_FIELDS:
        tree_hash = manifest["completed_package_tree"]
        script_value = "reconstruct_rl%d_bundle.py" % manifest["completed_rl"]
        incoming_not_started = manifest["incoming_status"] == "NOT STARTED"
    else:
        expected_variants = (DIRECT_TREE_MANIFEST_V1_FIELDS, DIRECT_TREE_MANIFEST_V2_FIELDS)
        missing = [sorted(expected - fields) for expected in expected_variants]
        extra = [sorted(fields - expected) for expected in expected_variants]
        raise Failure(
            "direct-tree transport manifest fields match no supported schema (missing=%s, extra=%s)"
            % (missing, extra)
        )
    if manifest["transport"] not in DIRECT_TREE_TRANSPORTS:
        raise Failure("unsupported direct-tree transport declaration")
    if manifest["incoming_rl"] != current_rl or manifest["completed_rl"] != current_rl - 1:
        raise Failure("direct-tree transport has the wrong RL sequence")
    if not incoming_not_started:
        raise Failure("direct-tree transport must record the incoming RL as not started")
    canonical = safe(manifest["canonical_zip"]).as_posix()
    if canonical != Path(canonical).name or canonical != expected_name:
        raise Failure("direct-tree canonical ZIP does not match the outer sidecar")
    canonical_hash = manifest["canonical_zip_sha256"]
    if not isinstance(canonical_hash, str) or not re.fullmatch(r"[0-9a-fA-F]{64}", canonical_hash):
        raise Failure("direct-tree canonical ZIP SHA-256 is invalid")
    if canonical_hash.lower() != expected_hash:
        raise Failure("direct-tree canonical ZIP SHA-256 does not match the outer sidecar")
    if not isinstance(tree_hash, str) or not re.fullmatch(r"[0-9a-fA-F]{40}|[0-9a-fA-F]{64}", tree_hash):
        raise Failure("direct-tree package tree identity is invalid")
    script = safe(script_value)
    package = target.parent
    if package == AUTH or package.parent != AUTH:
        raise Failure("the unique target must be inside one active package directory")
    package_relative = package.relative_to(ROOT).as_posix()
    committed_tree = git("rev-parse", "HEAD:%s" % package_relative).strip()
    if committed_tree.lower() != tree_hash.lower():
        raise Failure("direct-tree package tree identity does not match committed authority")
    script_path = package / script
    if not script_path.is_file() or script_path.is_symlink():
        raise Failure("direct-tree reconstruction script is missing or unsafe")
    return {
        **manifest,
        "canonical_zip_sha256": canonical_hash.lower(),
        "completed_package_tree_sha": tree_hash.lower(),
        "package": package,
        "reconstruction_script_path": script,
    }


def _authority_state():
    if not AUTH.is_dir():
        raise Failure("authoritative/ is missing")
    files = [path for path in AUTH.rglob("*") if path.is_file()]
    targets = sorted(AUTH.rglob("*TARGET*.md"))
    sidecars = sorted(AUTH.glob("*.zip.sha256"))
    if len(targets) != 1 or len(sidecars) != 1:
        raise Failure("expected one target and one bundle sidecar in authoritative/")
    target = targets[0]
    target_match = re.match(r"(?i)^RL0*(\d+)(?:_|\b)", target.name)
    if not target_match:
        raise Failure("the unique authoritative target must begin with its incoming RL")
    current_rl = int(target_match.group(1))
    outer = read_sums(sidecars[0])
    if len(outer) != 1:
        raise Failure("outer sidecar must contain exactly one checksum")
    expected_hash, raw_expected_name = outer[0]
    expected_name = safe(raw_expected_name).as_posix()
    if expected_name != Path(expected_name).name:
        raise Failure("outer sidecar must name a top-level ZIP")

    bundles = sorted(AUTH.glob("*.zip"))
    candidate_transports = sorted(
        path for path in AUTH.glob("*_BUNDLE_TRANSPORT") if path.is_dir()
    )
    bundle = AUTH / expected_name
    transport = None
    transport_kind = "physical_zip"
    transport_manifest = None
    if bundles:
        if len(bundles) != 1 or bundles[0].name != expected_name or candidate_transports:
            raise Failure("bundle files or transports are ambiguous")
        bundle = bundles[0]
    else:
        if len(candidate_transports) != 1:
            raise Failure("expected one physical ZIP or one reconstructible bundle transport")
        transport = candidate_transports[0]
        has_parts = (transport / "PART_SHA256SUMS.txt").is_file()
        has_manifest = (transport / "TRANSPORT_MANIFEST.json").is_file()
        if has_parts == has_manifest:
            raise Failure("bundle transport must use exactly one supported scheme")
        if has_parts:
            transport_kind = "base64_parts"
        else:
            transport_kind = "direct_git_tree"
            transport_manifest = _direct_transport_manifest(
                transport, current_rl, target, expected_name, expected_hash
            )

    completed_candidates = {
        int(match.group(1))
        for path in files
        for match in [re.search(r"RL(\d+)_SESSION_STATE_AND_RL(\d+)_KICKOFF", path.name, re.I)]
        if match and int(match.group(2)) == current_rl
    }
    if len(completed_candidates) != 1 or next(iter(completed_candidates)) != current_rl - 1:
        raise Failure("authoritative handover does not identify one predecessor RL")
    return {
        "current_rl": current_rl,
        "handover_generation": next(iter(completed_candidates)),
        "target": target.relative_to(ROOT).as_posix(),
        "active_package": target.parent.relative_to(ROOT).as_posix(),
        "bundle": bundle.relative_to(ROOT).as_posix(),
        "bundle_transport": transport.relative_to(ROOT).as_posix() if transport else None,
        "transport_kind": transport_kind,
        "transport_manifest": transport_manifest,
        "outer_sidecar": sidecars[0].relative_to(ROOT).as_posix(),
        "outer_sha256": expected_hash,
        "outer_sidecar_matches": digest(bundle) == expected_hash if bundle.is_file() else None,
    }


def _remote_identity():
    local_head = git("rev-parse", "HEAD").strip()
    branch = _optional_git("symbolic-ref", "--quiet", "--short", "HEAD")
    remote = None
    if branch:
        remote = _optional_git("config", "--get", "branch.%s.remote" % branch)
    if not remote or remote == ".":
        remotes = [item for item in git("remote").splitlines() if item]
        remote = "origin" if "origin" in remotes else (remotes[0] if len(remotes) == 1 else None)
    if not remote:
        raise Failure("cannot determine the remote used for the default branch")
    try:
        output = git("ls-remote", "--symref", remote, "HEAD")
    except Failure as error:
        raise Failure("cannot establish the live remote/default-branch HEAD: %s" % error) from error
    base_ref = None
    base_head = None
    for line in output.splitlines():
        if line.startswith("ref: ") and line.endswith("\tHEAD"):
            base_ref = line[5:].split("\t", 1)[0]
        elif line.endswith("\tHEAD"):
            candidate = line.split("\t", 1)[0]
            if re.fullmatch(r"[0-9a-fA-F]{40}|[0-9a-fA-F]{64}", candidate):
                base_head = candidate.lower()
    if not base_ref or not base_head:
        raise Failure("live remote did not identify a symbolic default branch and commit")
    return {
        "base_remote": remote,
        "base_ref": base_ref,
        "base_head": base_head,
        "base_head_live": True,
        "local_head": local_head,
        "head_matches_base": local_head == base_head,
    }


def state(require_remote=True):
    incoming = _authority_state()
    if require_remote:
        repository = _remote_identity()
    else:
        repository = {
            "base_remote": None,
            "base_ref": None,
            "base_head": None,
            "base_head_live": False,
            "local_head": git("rev-parse", "HEAD").strip(),
            "head_matches_base": None,
        }
    public_incoming = {key: value for key, value in incoming.items() if key != "transport_manifest"}
    return {
        **repository,
        **public_incoming,
        "working_tree_clean": not bool(
            git("status", "--porcelain", "--untracked-files=all").strip()
        ),
    }


def _index_entries():
    entries = {}
    raw_output = _git_bytes("ls-files", "--stage", "-z", "--", "authoritative")
    for record in raw_output.split(b"\0"):
        if not record:
            continue
        try:
            header, raw_path = record.split(b"\t", 1)
            mode, blob_oid, stage = header.decode("ascii").split()
        except (ValueError, UnicodeError) as error:
            raise Failure("cannot parse authoritative Git index") from error
        path = raw_path.decode("utf-8", "surrogateescape")
        if stage != "0" or path in entries:
            raise Failure("authoritative Git index contains an unresolved or duplicate entry")
        entries[path] = {"mode": mode, "blob_oid": blob_oid}
    return entries


def snapshot():
    incoming = state(require_remote=True)
    if not incoming["head_matches_base"]:
        raise Failure("local HEAD does not match the live remote/default-branch HEAD")
    indexed = _index_entries()
    raw_paths = _git_bytes(
        "ls-files", "-z", "--cached", "--others", "--exclude-standard", "--", "authoritative"
    )
    entries = []
    seen = set()
    for raw in raw_paths.split(b"\0"):
        if not raw:
            continue
        relative = raw.decode("utf-8", "surrogateescape")
        if relative in seen:
            raise Failure("duplicate authoritative path in snapshot: " + relative)
        seen.add(relative)
        path = ROOT / relative
        try:
            details = path.lstat()
        except OSError as error:
            raise Failure("authoritative file is missing: %s" % relative) from error
        if not stat.S_ISREG(details.st_mode) or path.is_symlink():
            raise Failure("authoritative snapshot only supports regular files: " + relative)
        index = indexed.get(relative)
        worktree_mode = "100755" if details.st_mode & stat.S_IXUSR else "100644"
        entries.append({
            "path": relative,
            "tracked": index is not None,
            "mode": index["mode"] if index else worktree_mode,
            "worktree_mode": worktree_mode,
            "blob_oid": index["blob_oid"] if index else None,
            "bytes": details.st_size,
            "sha256": digest(path),
        })
    if not entries:
        raise Failure("no authoritative files")
    return {
        "format": SNAPSHOT_FORMAT,
        "base_remote": incoming["base_remote"],
        "base_ref": incoming["base_ref"],
        "base_head": incoming["base_head"],
        "local_head": incoming["local_head"],
        "current_rl": incoming["current_rl"],
        "tree": "authoritative",
        "authoritative_tree_oid": git("rev-parse", "HEAD:authoritative").strip(),
        "entries": sorted(entries, key=lambda item: item["path"]),
    }


def read_sums(path):
    records = []
    try:
        lines = path.read_text(encoding="utf-8").splitlines()
    except (OSError, UnicodeError) as error:
        raise Failure("cannot read checksum file %s: %s" % (path, error)) from error
    names = set()
    for n, line in enumerate(lines, 1):
        if line.strip():
            bits = line.split(maxsplit=1)
            if len(bits) != 2 or not re.fullmatch(r"[0-9a-fA-F]{64}", bits[0]):
                raise Failure("invalid checksum record at %s:%d" % (path, n))
            name = bits[1].strip().lstrip("*")
            if name in names:
                raise Failure("duplicate checksum path at %s:%d" % (path, n))
            names.add(name)
            records.append((bits[0].lower(), name))
    if not records:
        raise Failure("empty checksum file: " + str(path))
    return records


def _extract_git_tree(package, expected_tree, destination):
    relative = package.relative_to(ROOT).as_posix()
    actual_tree = git("rev-parse", "HEAD:%s" % relative).strip()
    if actual_tree.lower() != expected_tree.lower():
        raise Failure("direct-tree package changed before reconstruction")
    archive_bytes = _git_bytes("archive", "--format=tar", "HEAD:%s" % relative)
    destination.mkdir(parents=True)
    try:
        with tarfile.open(fileobj=io.BytesIO(archive_bytes), mode="r:") as archive:
            seen = set()
            for member in archive.getmembers():
                relative_member = safe(member.name.rstrip("/")) if member.name.rstrip("/") else None
                if relative_member is None:
                    continue
                normalised = relative_member.as_posix()
                folded = normalised.casefold()
                if folded in seen:
                    raise Failure("direct-tree archive contains a duplicate path: " + normalised)
                seen.add(folded)
                if not (member.isdir() or member.isfile()):
                    raise Failure("direct-tree archive contains a non-regular path: " + normalised)
            archive.extractall(destination)
    except (tarfile.TarError, OSError) as error:
        raise Failure("cannot export the committed direct-tree package: %s" % error) from error


def _reconstruct_direct_tree(incoming, temp):
    manifest = incoming["transport_manifest"]
    package = manifest["package"]
    exported_package = Path(temp) / "committed-package" / package.name
    _extract_git_tree(package, manifest["completed_package_tree_sha"], exported_package)
    script = exported_package / manifest["reconstruction_script_path"]
    if not script.is_file() or script.is_symlink():
        raise Failure("reconstruction script is absent from the committed package tree")
    environment = {
        key: value for key, value in os.environ.items()
        if key not in {"PYTHONHOME", "PYTHONPATH"}
    }
    environment.update({
        "PYTHONDONTWRITEBYTECODE": "1",
        "PYTHONNOUSERSITE": "1",
        "PYTHONSAFEPATH": "1",
    })
    try:
        run = subprocess.run(
            [sys.executable, "-I", str(script)],
            cwd=exported_package,
            text=True,
            capture_output=True,
            timeout=RECONSTRUCTION_TIMEOUT_SECONDS,
            env=environment,
        )
    except subprocess.TimeoutExpired as error:
        raise Failure("direct-tree reconstruction timed out") from error
    except OSError as error:
        raise Failure("direct-tree reconstruction could not run: %s" % error) from error
    if run.returncode:
        details = (run.stdout + run.stderr).strip()
        raise Failure("direct-tree reconstruction failed: %s" % (details or run.returncode))
    checked_bundle = exported_package.parent / manifest["canonical_zip"]
    if not checked_bundle.is_file() or checked_bundle.is_symlink():
        raise Failure("direct-tree reconstruction did not create the canonical ZIP")
    try:
        checked_bundle.resolve().relative_to(Path(temp).resolve())
    except ValueError as error:
        raise Failure("direct-tree reconstruction output escaped temporary storage") from error
    return checked_bundle


def _reconstruct_base64(incoming, temp):
    transport = ROOT / (incoming["bundle_transport"] or "")
    records = read_sums(transport / "PART_SHA256SUMS.txt")
    parts = []
    seen = set()
    for expected, name in records:
        relative = safe(name)
        folded = relative.as_posix().casefold()
        if folded in seen:
            raise Failure("bundle transport has a duplicate part path: " + name)
        seen.add(folded)
        part = transport / relative
        if not part.is_file() or part.is_symlink() or digest(part) != expected:
            raise Failure("bundle transport part mismatch: " + name)
        parts.append(part)
    try:
        encoded = "".join(part.read_text(encoding="utf-8").strip() for part in parts)
        raw = base64.b64decode(encoded, validate=True)
    except (OSError, UnicodeError, binascii.Error, ValueError) as error:
        raise Failure("bundle transport Base64 decode failed: %s" % error) from error
    checked_bundle = Path(temp) / incoming["bundle"].split("/")[-1]
    try:
        checked_bundle.write_bytes(raw)
    except OSError as error:
        raise Failure("cannot write reconstructed bundle: %s" % error) from error
    return checked_bundle


def _zip_member_path(info):
    name = info.filename.rstrip("/")
    if not name:
        return None
    relative = safe(name)
    unix_mode = (info.external_attr >> 16) & 0xFFFF
    file_type = stat.S_IFMT(unix_mode)
    if file_type == stat.S_IFLNK:
        raise Failure("fresh-unpack ZIP contains a symbolic link: " + name)
    if file_type not in {0, stat.S_IFREG, stat.S_IFDIR}:
        raise Failure("fresh-unpack ZIP contains a non-regular path: " + name)
    if info.flag_bits & 0x1:
        raise Failure("fresh-unpack ZIP contains an encrypted member: " + name)
    return relative


def _extract_zip(bundle, destination):
    destination.mkdir(parents=True)
    try:
        with zipfile.ZipFile(bundle) as archive:
            members = []
            seen = set()
            for info in archive.infolist():
                relative = _zip_member_path(info)
                if relative is None:
                    continue
                folded = relative.as_posix().casefold()
                if folded in seen:
                    raise Failure("fresh-unpack ZIP contains a duplicate path: " + relative.as_posix())
                seen.add(folded)
                members.append((info, relative))
            for info, relative in members:
                output = destination / relative
                if info.is_dir():
                    output.mkdir(parents=True, exist_ok=True)
                    continue
                output.parent.mkdir(parents=True, exist_ok=True)
                with archive.open(info) as source, output.open("xb") as target:
                    shutil.copyfileobj(source, target)
    except Failure:
        raise
    except (OSError, RuntimeError, zipfile.BadZipFile, zipfile.LargeZipFile) as error:
        raise Failure("fresh-unpack ZIP validation failed: %s" % error) from error


def verify_incoming():
    incoming = _authority_state()
    bundle = ROOT / incoming["bundle"]
    sidecar = ROOT / incoming["outer_sidecar"]
    if sidecar.name != bundle.name + ".sha256":
        raise Failure("bundle sidecar is missing or ambiguous")
    outer = read_sums(sidecar)
    if len(outer) != 1 or safe(outer[0][1]).as_posix() != bundle.name:
        raise Failure("outer SHA-256 sidecar mismatch")
    with tempfile.TemporaryDirectory(prefix="rl-fresh-") as temp:
        if incoming["transport_kind"] == "physical_zip":
            checked_bundle = bundle
        elif incoming["transport_kind"] == "base64_parts":
            checked_bundle = _reconstruct_base64(incoming, temp)
        else:
            checked_bundle = _reconstruct_direct_tree(incoming, temp)
        if digest(checked_bundle) != outer[0][0]:
            raise Failure("outer SHA-256 sidecar mismatch")
        fresh = Path(temp) / "fresh-unpack"
        _extract_zip(checked_bundle, fresh)
        manifests = list(fresh.rglob("SHA256SUMS.txt"))
        if len(manifests) != 1:
            raise Failure("fresh unpack needs exactly one SHA256SUMS.txt")
        manifest = manifests[0]
        manifest_paths = set()
        for expected, name in read_sums(manifest):
            relative = safe_manifest_path(name)
            folded = relative.as_posix().casefold()
            if folded in manifest_paths:
                raise Failure("internal manifest contains a duplicate path: " + name)
            manifest_paths.add(folded)
            checked = manifest.parent / relative
            if not checked.is_file() or checked.is_symlink() or digest(checked) != expected:
                raise Failure("internal manifest mismatch: " + name)
        verifiers = sorted((manifest.parent / "verification").glob("verify_*.py"))
        if not verifiers:
            raise Failure("no portable fast verifier in fresh unpack")
        for verifier in verifiers:
            try:
                run = subprocess.run(
                    [sys.executable, "-I", str(verifier)], cwd=manifest.parent,
                    text=True, capture_output=True, timeout=VERIFIER_TIMEOUT_SECONDS,
                    env={
                        **{key: value for key, value in os.environ.items() if key not in {"PYTHONHOME", "PYTHONPATH"}},
                        "PYTHONDONTWRITEBYTECODE": "1",
                        "PYTHONNOUSERSITE": "1",
                        "PYTHONSAFEPATH": "1",
                    },
                )
            except subprocess.TimeoutExpired as error:
                raise Failure("fresh-unpack verifier timed out: " + verifier.name) from error
            except OSError as error:
                raise Failure("fresh-unpack verifier could not run: %s" % error) from error
            if run.returncode:
                raise Failure("fresh-unpack verifier failed: %s\n%s" % (verifier.name, (run.stdout + run.stderr).strip()))


def write_json(path, value):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def cmd_status(_):
    print(json.dumps(state(), indent=2, sort_keys=True))


def cmd_snapshot(args):
    value = snapshot()
    if args.output:
        output = Path(args.output)
        if not output.is_absolute(): output = ROOT / output
        write_json(output, value)
        print(output)
    else:
        print(json.dumps(value, indent=2, sort_keys=True))


def cmd_check_snapshot(args):
    try:
        old = json.loads(Path(args.snapshot).read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as error:
        raise Failure("cannot read snapshot: %s" % error)
    if old != snapshot():
        raise Failure("authoritative snapshot mismatch; do not promote")
    print("authoritative snapshot: PASS")


def cmd_verify(_):
    verify_incoming()
    print("incoming outer sidecar: PASS")
    print("incoming internal manifest: PASS")
    print("incoming fresh-unpack fast verifier suite: PASS")


def cmd_checkpoint(args):
    incoming = state(); rl = args.rl or incoming["current_rl"]
    if not incoming["working_tree_clean"]:
        raise Failure("refuse to initialize a mathematical checkpoint with tracked or untracked repository changes")
    if rl != incoming["current_rl"]:
        raise Failure("checkpoint RL must equal the current incoming RL")
    work = ROOT / ".rl-work" / ("RL%d" % rl)
    if work.exists():
        raise Failure("refuse to overwrite checkpoint: " + str(work))
    work.mkdir(parents=True); (work / "artifacts").mkdir()
    write_json(work / "authoritative-snapshot.json", snapshot())
    write_json(work / "STATE.json", {
        "format": "rl-local-checkpoint-v1", "base_head": incoming["base_head"], "current_rl": rl,
        "authoritative_target": args.target or incoming["target"], "created_at_utc": datetime.now(timezone.utc).isoformat(),
        "last_fully_verified_checkpoint": "Incoming authoritative verification passed; no new mathematics started.",
        "new_results": [], "promoted_exact_certificate_ranges": [], "incomplete_or_unverified_ranges": [],
        "corrections_or_demotions": [], "verifier_runs": [], "failed_or_abandoned_routes": [],
        "next_step": "Read the authoritative target.", "stop_and_repair_active": False})
    (work / "commands.log").write_text("# Append reproducible commands and outcomes here.\n", encoding="utf-8")
    (work / "CHECKPOINT.md").write_text("# Local RL checkpoint (NOT AUTHORITATIVE)\n\n"
        "- BASE_HEAD: `%s`\n- Current incoming RL: `RL%d`\n- Target: `%s`\n"
        "- Last fully verified state: incoming verification passed; no new mathematics started.\n"
        "- New results / exact ranges / unverified work / corrections: none.\n"
        "- Stop-and-repair active: no.\n- Next step: read the target and log verified milestones.\n\n"
        "This ignored directory is a resumability aid, never proof state or a promotion candidate.\n" % (incoming["base_head"], rl, args.target or incoming["target"]), encoding="utf-8")
    print(work)


def cmd_candidate(args):
    candidate = Path(args.candidate).resolve(); path = candidate / "PROMOTION_MANIFEST.json"
    if not path.is_file(): raise Failure("promotion candidate lacks PROMOTION_MANIFEST.json")
    try: manifest = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as error: raise Failure("cannot read promotion manifest: %s" % error)
    required = {"format", "current_rl", "next_rl", "completed_session", "next_authoritative", "bundle", "sidecar", "fresh_unpack_report", "verifier_commands", "red_team_report"}
    if not isinstance(manifest, dict) or not required.issubset(manifest) or manifest["format"] != "rl-promotion-candidate-v1":
        raise Failure("promotion manifest is incomplete")
    incoming = state()
    if manifest["current_rl"] != incoming["current_rl"] or manifest["next_rl"] != incoming["current_rl"] + 1:
        raise Failure("promotion manifest has the wrong RL sequence")
    if not isinstance(manifest["verifier_commands"], list) or not manifest["verifier_commands"]:
        raise Failure("promotion candidate must list verifier commands")
    for key in required - {"format", "current_rl", "next_rl", "verifier_commands"}:
        if not isinstance(manifest[key], str) or not (candidate / safe(manifest[key])).exists():
            raise Failure("promotion candidate missing artifact: " + key)
    print("promotion candidate completeness: PASS (mathematical judgement still required)")


def cmd_preflight(args):
    cmd_check_snapshot(argparse.Namespace(snapshot=args.snapshot))
    cmd_candidate(argparse.Namespace(candidate=args.candidate))
    print("preflight: PASS (does not stage, move, or commit files)")


def _authoritative_startup_references(active_package):
    entrypoint = AUTH / "START_HERE.md"
    if not entrypoint.is_file():
        raise Failure("authoritative/START_HERE.md is missing")
    try:
        text = entrypoint.read_text(encoding="utf-8")
    except (OSError, UnicodeError) as error:
        raise Failure("cannot read authoritative/START_HERE.md: %s" % error) from error
    reads = []
    commands = []
    for token in re.findall(r"`([^`]+)`", text):
        token = token.strip()
        if token.startswith(("python3 ", "bash ")):
            try:
                parts = shlex.split(token)
            except ValueError as error:
                raise Failure("malformed command in authoritative/START_HERE.md: %s" % error) from error
            if len(parts) >= 2:
                try:
                    script = safe_manifest_path(parts[1])
                except Failure:
                    script = None
                if script is not None:
                    candidate = AUTH / script
                    if candidate.is_file():
                        parts[1] = candidate.relative_to(ROOT).as_posix()
                        parts[2:] = ["authoritative" if item == "." else item for item in parts[2:]]
            commands.append(" ".join(shlex.quote(item) for item in parts))
            continue
        try:
            relative = safe_manifest_path(token.rstrip("/"))
        except Failure:
            continue
        candidate = AUTH / relative
        if candidate.is_file() and candidate.suffix.lower() in {".md", ".json"}:
            reads.append(candidate.relative_to(ROOT).as_posix())
        elif candidate.is_dir() and candidate == active_package:
            package_readme = candidate / "README.md"
            if package_readme.is_file():
                reads.append(package_readme.relative_to(ROOT).as_posix())
    return list(dict.fromkeys(reads)), list(dict.fromkeys(commands))


def _authoritative_status_paths(active_package):
    ledgers = []
    red_teams = []
    verifiers = []
    for path in sorted(active_package.rglob("*")):
        if not path.is_file():
            continue
        name = path.name.upper()
        relative = path.relative_to(ROOT).as_posix()
        if path.suffix.lower() == ".md" and (
            "CERTIFIED_FACTS" in name or "PROOF_LEDGER" in name or (
            ("CORRECTION" in name or "DEMOTION" in name) and "LEDGER" in name
        )):
            ledgers.append(relative)
        if path.suffix.lower() == ".md" and "RED_TEAM" in name:
            red_teams.append(relative)
        if path.suffix.lower() == ".py" and path.parent.name == "verification" and name.startswith("VERIFY_"):
            verifiers.append(relative)
    if not ledgers:
        raise Failure("active authoritative package has no proof/correction ledgers")
    if not red_teams:
        raise Failure("active authoritative package has no red-team report")
    if not verifiers:
        raise Failure("active authoritative package has no portable verifiers")
    return ledgers, red_teams, verifiers


def _index_summary():
    path = ROOT / "knowledge" / "index_metadata.json"
    if not path.is_file():
        return {"present": False, "validation_command": "python3 tools/rl_conveyor.py index-validate"}
    try:
        metadata = json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as error:
        raise Failure("knowledge/index_metadata.json is invalid: %s" % error)
    return {
        "present": True,
        "format": metadata.get("format"),
        "container_count": metadata.get("container_count"),
        "generation_record_count": metadata.get("generation_record_count"),
        "result_record_count": metadata.get("result_record_count"),
        "validation_command": "python3 tools/rl_conveyor.py index-validate",
    }


def startup_state():
    incoming = state(require_remote=True)
    if not incoming["head_matches_base"]:
        raise Failure("local HEAD does not match the live remote/default-branch HEAD")
    active_package = ROOT / incoming["active_package"]
    current_reads, current_commands = _authoritative_startup_references(active_package)
    status_paths, red_team_paths, verifier_paths = _authoritative_status_paths(active_package)
    read_order = list(dict.fromkeys([
        "AGENTS.md",
        "START_HERE.md",
        "authoritative/START_HERE.md",
        *status_paths,
        *red_team_paths,
        *current_reads,
        incoming["target"],
    ]))
    return {
        "base_remote": incoming["base_remote"],
        "base_ref": incoming["base_ref"],
        "base_head": incoming["base_head"],
        "local_head": incoming["local_head"],
        "head_matches_base": incoming["head_matches_base"],
        "incoming_rl": incoming["current_rl"],
        "handover_generation": incoming["handover_generation"],
        "target": incoming["target"],
        "bundle": incoming["bundle"],
        "transport_kind": incoming["transport_kind"],
        "incoming_outer_sidecar_matches": incoming["outer_sidecar_matches"],
        "minimal_read_order": read_order,
        "current_status_paths": status_paths,
        "required_red_team_paths": red_team_paths,
        "required_verifier_paths": verifier_paths,
        "required_commands": [
            "python3 tools/rl_conveyor.py status",
            "python3 tools/rl_conveyor.py verify-incoming",
            *current_commands,
            "python3 tools/rl_conveyor.py init-checkpoint",
        ],
        "history_queries": [
            "python3 tools/rl_conveyor.py session RL<N>",
            "python3 tools/rl_conveyor.py result '<name or alias>'",
        ],
        "normally_excluded_search_surfaces": [
            "sessions/", "Archive/", "ZIP contents", "bundle transports",
            "generated bundle copies", "certificate payloads",
        ],
        "knowledge_index": _index_summary(),
    }


def cmd_startup(args):
    value = startup_state()
    if args.json:
        print(json.dumps(value, indent=2, sort_keys=True))
        return
    print("Incoming: RL%d" % value["incoming_rl"])
    if value["handover_generation"] is not None:
        print("Handover generation: RL%d" % value["handover_generation"])
    print("Target: %s" % value["target"])
    print("Minimal read order:")
    for path in value["minimal_read_order"]:
        print("  " + path)
    print("Required commands:")
    for command in value["required_commands"]:
        print("  " + command)
    print("History is query-only by default: session RL<N> / result <name-or-alias>")
    print("Do not recursively search sessions/, Archive/, bundles, or certificate payloads during normal startup.")


def _first_paths(record, key, limit=3):
    return record.get(key, [])[:limit]


def _print_generation(record, role):
    print("%s: %s" % (role, record["generation_id"]))
    for path in record.get("generation_paths", []):
        print("  root: " + path)
    labels = (
        ("report", "main_report_paths"),
        ("state", "session_state_handover_paths"),
        ("target", "target_paths"),
        ("proof ledger", "proof_ledger_paths"),
        ("correction ledger", "correction_demotion_ledger_paths"),
        ("verifier", "verifier_paths"),
        ("certificate root", "certificate_roots"),
        ("bundle", "bundle_paths"),
    )
    for label, key in labels:
        for path in _first_paths(record, key):
            print("  %s: %s" % (label, path))
    for warning in record.get("ambiguities", []):
        print("  ambiguity: " + warning)


def cmd_session(args):
    try:
        rl = parse_rl_identifier(args.rl)
        value = query_sessions(ROOT, rl)
    except CatalogError as error:
        raise Failure(str(error)) from error
    if args.json:
        print(json.dumps(value, indent=2, sort_keys=True))
        return
    print("Historical locator: RL%d" % rl)
    seen = set()
    for role, key in (
        ("completed generation", "completed_generation_records"),
        ("incoming handover", "incoming_generation_records"),
        ("container label", "container_label_records"),
        ("embedded historical locator", "embedded_locator_records"),
    ):
        for record in value[key]:
            identity = (record["generation_id"], tuple(record["generation_paths"]))
            if identity in seen:
                continue
            seen.add(identity)
            _print_generation(record, role)
    if not seen:
        print("No explicit indexed record. Use an exceptional targeted audit; do not infer from a missing container label.")
    print(value["note"])


def cmd_result(args):
    try:
        value = query_results(ROOT, args.query, args.limit)
    except CatalogError as error:
        raise Failure(str(error)) from error
    if args.json:
        print(json.dumps(value, indent=2, sort_keys=True))
        return
    print("Result locator: %s (%d matches)" % (args.query, value["match_count"]))
    for record in value["matches"]:
        name = record.get("name") or "unnamed recorded entry"
        status = record.get("recorded_classification") or "classification not explicitly encoded"
        print("- %s [%s]" % (name, status))
        print("  %s:%d" % (record["source_path"], record["source_line_start"]))
        print("  source: %s; generation: %s" % (record["source_kind"], record.get("generation_id") or "unknown"))
        if record["is_correction_or_demotion_record"]:
            print("  correction/demotion pointer: yes")
        for path in record.get("verifier_paths", [])[:2]:
            print("  session verifier candidate (not asserted claim-specific): " + path)
        for path in record.get("certificate_roots", [])[:2]:
            print("  session certificate root (not asserted claim-specific): " + path)
    if not value["matches"]:
        print("No conservative indexed match. Use a targeted source audit only if a live dependency requires it.")
    if value["review_marker"]:
        print(value["review_marker"])
    if value["preferred_full_provenance_source"]:
        print("Preferred full-provenance source: " + value["preferred_full_provenance_source"])
    print(value["status_policy"])


def cmd_index_build(args):
    try:
        metadata = write_indexes(ROOT)
    except CatalogError as error:
        raise Failure(str(error)) from error
    if args.json:
        print(json.dumps(metadata, indent=2, sort_keys=True))
    else:
        print(
            "knowledge index: BUILT (%d containers, %d generation locators, %d result locators)"
            % (metadata["container_count"], metadata["generation_record_count"], metadata["result_record_count"])
        )


def cmd_index_validate(args):
    try:
        result = validate_indexes(ROOT, staged=getattr(args, "staged", False))
    except CatalogError as error:
        raise Failure(str(error)) from error
    if not result["current"]:
        details = ", ".join(item["path"] + " (" + item["reason"] + ")" for item in result["mismatches"])
        raise Failure("knowledge index is stale: " + details)
    if args.json:
        print(json.dumps(result, indent=2, sort_keys=True))
    else:
        print(
            "knowledge index: PASS (%d containers, %d generation locators, %d result locators; unlocated labels: %s)"
            % (
                result["container_count"], result["generation_record_count"], result["result_record_count"],
                ", ".join("RL%d" % number for number in result["unlocated_rls"]) or "none",
            )
        )


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(required=True, metavar="COMMAND")
    sub.add_parser("status", help="show current authority and live remote identity").set_defaults(func=cmd_status)
    p = sub.add_parser("snapshot", help="render a fail-closed authoritative snapshot")
    p.add_argument("--output", help="write JSON to this path instead of stdout")
    p.set_defaults(func=cmd_snapshot)
    p = sub.add_parser("check-snapshot", help="compare a saved snapshot with current authority")
    p.add_argument("snapshot")
    p.set_defaults(func=cmd_check_snapshot)
    sub.add_parser("verify-incoming", help="verify transport, fresh unpack, manifest, and fast suite").set_defaults(func=cmd_verify)
    p = sub.add_parser("init-checkpoint", help="create ignored resumability state for the incoming RL")
    p.add_argument("--rl", type=int)
    p.add_argument("--target")
    p.set_defaults(func=cmd_checkpoint)
    p = sub.add_parser("check-promotion", help="check promotion-candidate structure without promoting")
    p.add_argument("candidate")
    p.set_defaults(func=cmd_candidate)
    p = sub.add_parser("preflight", help="check snapshot and promotion candidate without mutation")
    p.add_argument("snapshot")
    p.add_argument("candidate")
    p.set_defaults(func=cmd_preflight)
    p = sub.add_parser("startup", help="show the minimal current-authority startup surface")
    p.add_argument("--json", action="store_true")
    p.set_defaults(func=cmd_startup)
    p = sub.add_parser("session", help="query a historical session locator")
    p.add_argument("rl", help="RL identifier, for example RL231")
    p.add_argument("--json", action="store_true")
    p.set_defaults(func=cmd_session)
    p = sub.add_parser("result", help="query conservative historical result locators")
    p.add_argument("query")
    p.add_argument("--limit", type=int, default=20)
    p.add_argument("--json", action="store_true")
    p.set_defaults(func=cmd_result)
    p = sub.add_parser("index-build", help="regenerate deterministic knowledge catalogues")
    p.add_argument("--json", action="store_true")
    p.set_defaults(func=cmd_index_build)
    p = sub.add_parser("index-validate", help="validate generated catalogues")
    p.add_argument("--staged", action="store_true", help="also require indexed inputs/outputs to match the Git index")
    p.add_argument("--json", action="store_true")
    p.set_defaults(func=cmd_index_validate)
    try: args = parser.parse_args(); args.func(args)
    except Failure as error:
        print("FAIL CLOSED: " + str(error), file=sys.stderr); return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
