#!/usr/bin/env python3
"""Fail-closed startup/verification fallback for connector-produced flat authority.

This helper is intentionally narrow. It is used only when `authoritative/`
is a committed flat Git-tree handover with no ZIP/sidecar transport and the
legacy `rl_conveyor.py` packaging schema therefore cannot identify the active
target. It does not promote or modify authoritative proof state.
"""

import hashlib
import json
import os
import re
import shlex
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
AUTH = ROOT / "authoritative"
TIMEOUT = 180


class Failure(RuntimeError):
    pass


def git(*args):
    try:
        run = subprocess.run(
            ["git", *args], cwd=ROOT, text=True, capture_output=True, timeout=30
        )
    except (OSError, subprocess.TimeoutExpired) as error:
        raise Failure("git command failed: %s" % error) from error
    if run.returncode:
        raise Failure(run.stderr.strip() or "git command failed")
    return run.stdout.strip()


def digest(path):
    h = hashlib.sha256()
    with path.open("rb") as source:
        for block in iter(lambda: source.read(1024 * 1024), b""):
            h.update(block)
    return h.hexdigest()


def remote_identity():
    local_head = git("rev-parse", "HEAD")
    branch = git("symbolic-ref", "--quiet", "--short", "HEAD")
    remote = git("config", "--get", "branch.%s.remote" % branch) or "origin"
    if remote == ".":
        remote = "origin"
    output = git("ls-remote", "--symref", remote, "HEAD")
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
        raise Failure("cannot establish the live remote/default-branch HEAD")
    if local_head.lower() != base_head:
        raise Failure("local HEAD does not match the live remote/default-branch HEAD")
    return remote, base_ref, base_head


def parse_start_here():
    entrypoint = AUTH / "START_HERE.md"
    if not entrypoint.is_file():
        raise Failure("authoritative/START_HERE.md is missing")
    text = entrypoint.read_text(encoding="utf-8")
    declarations = [
        int(value) for value in re.findall(
            r"(?mi)^#\s+RL0*(\d+)\s+authoritative\s+start\s*$", text
        )
    ]
    declarations.extend(
        int(value) for value in re.findall(
            r"(?i)\bRL0*(\d+)\s+is\s+the\s+unique\s+incoming\s+research\s+session\b",
            text,
        )
    )
    if not declarations or len(set(declarations)) != 1:
        raise Failure("START_HERE.md must unambiguously declare one incoming RL")
    current_rl = declarations[0]

    target_tokens = []
    referenced_files = []
    commands = []
    for token in re.findall(r"`([^`]+)`", text):
        token = token.strip()
        if token.startswith("python3 "):
            commands.append(token)
            continue
        if re.fullmatch(r"[A-Za-z0-9_./-]+\.(?:md|txt|json|py)", token, re.I):
            referenced_files.append(token)
            name = Path(token).name
            target_match = re.match(r"(?i)^RL0*(\d+).*TARGET.*\.md$", name)
            if target_match and int(target_match.group(1)) == current_rl:
                target_tokens.append(token)

    target_tokens = list(dict.fromkeys(target_tokens))
    if len(target_tokens) != 1:
        raise Failure(
            "START_HERE.md must explicitly name exactly one target for RL%d" % current_rl
        )
    target = AUTH / target_tokens[0]
    if not target.is_file():
        raise Failure("declared incoming target is missing: " + target_tokens[0])
    for candidate in AUTH.rglob("*TARGET*.md"):
        number = re.match(r"(?i)^RL0*(\d+)(?:_|\b)", candidate.name)
        if not number:
            raise Failure("unnumbered target in authoritative/: " + candidate.name)
        if int(number.group(1)) >= current_rl and candidate != target:
            raise Failure("ambiguous current or future target: " + candidate.name)

    for relative in dict.fromkeys(referenced_files):
        candidate = AUTH / relative
        if not candidate.exists():
            raise Failure("START_HERE.md references a missing authority file: " + relative)

    predecessor = AUTH / (
        "RL%d_SESSION_STATE_AND_RL%d_KICKOFF.md" % (current_rl - 1, current_rl)
    )
    closeout_verification = AUTH / (
        "RL%d_CLOSEOUT_VERIFICATION.md" % (current_rl - 1)
    )
    frozen_session = ROOT / "sessions" / ("RL%d" % (current_rl - 1))
    if not predecessor.is_file():
        raise Failure("flat authority lacks the unique predecessor kickoff record")
    if not closeout_verification.is_file():
        raise Failure("flat authority lacks predecessor closeout verification")
    if not frozen_session.is_dir():
        raise Failure("completed predecessor session is not frozen under sessions/")

    return current_rl, target, commands


def require_flat_transport(current_rl):
    """Allow only paired, hash-checked packages older than the handover generation."""
    if list(AUTH.glob("*_BUNDLE_TRANSPORT")):
        raise Failure("bundle transport is present; use tools/rl_conveyor.py instead")
    bundles = {path.name: path for path in AUTH.glob("*.zip")}
    sidecars = {path.name[:-7]: path for path in AUTH.glob("*.zip.sha256")}
    if set(bundles) != set(sidecars):
        raise Failure("historical ZIP/sidecar pair is incomplete")
    for name, bundle in bundles.items():
        match = re.fullmatch(r"RL0*(\d+)_HANDOVER_BUNDLE\.zip", name, re.I)
        if not match or int(match.group(1)) >= current_rl - 1:
            raise Failure("current or unrecognized packaged authority is present")
        records = sidecars[name].read_text(encoding="utf-8").splitlines()
        if len(records) != 1:
            raise Failure("historical ZIP sidecar must contain one checksum")
        checksum = re.fullmatch(r"([0-9a-fA-F]{64})  ([A-Za-z0-9_.-]+)", records[0])
        if not checksum or checksum.group(2) != name:
            raise Failure("historical ZIP sidecar names the wrong bundle")
        if digest(bundle) != checksum.group(1).lower():
            raise Failure("historical ZIP checksum mismatch: " + name)


def declared_verifier_commands(commands):
    accepted = []
    saw_verify = False
    saw_red_team = False
    for command in commands:
        try:
            parts = shlex.split(command)
        except ValueError as error:
            raise Failure("malformed START_HERE command: %s" % error) from error
        if len(parts) != 3 or parts[0] != "python3" or parts[1] != "-I":
            continue
        relative = Path(parts[2])
        if relative.is_absolute() or ".." in relative.parts:
            raise Failure("unsafe verifier path in START_HERE.md")
        script = AUTH / relative
        try:
            script.relative_to(AUTH / "verification")
        except ValueError as error:
            raise Failure("portable verifier must live under authoritative/verification") from error
        if not script.is_file() or script.is_symlink():
            raise Failure("declared verifier is missing or unsafe: " + parts[2])
        name = script.name
        if name.startswith("verify_"):
            saw_verify = True
        elif name.startswith("red_team_"):
            saw_red_team = True
        else:
            raise Failure("unexpected executable in START_HERE portable checks: " + name)
        accepted.append(script)
    if not accepted or not saw_verify or not saw_red_team:
        raise Failure("flat authority must declare both verifier and red-team portable checks")
    return list(dict.fromkeys(accepted))


def run_verifiers(scripts):
    environment = {
        key: value for key, value in os.environ.items()
        if key not in {"PYTHONHOME", "PYTHONPATH"}
    }
    environment.update({
        "PYTHONDONTWRITEBYTECODE": "1",
        "PYTHONNOUSERSITE": "1",
        "PYTHONSAFEPATH": "1",
    })
    outputs = []
    for script in scripts:
        try:
            run = subprocess.run(
                [sys.executable, "-I", str(script)],
                cwd=AUTH,
                text=True,
                capture_output=True,
                timeout=TIMEOUT,
                env=environment,
            )
        except subprocess.TimeoutExpired as error:
            raise Failure("portable check timed out: " + script.name) from error
        except OSError as error:
            raise Failure("portable check could not run: %s" % error) from error
        output = (run.stdout + run.stderr).strip()
        if run.returncode:
            raise Failure("portable check failed: %s\n%s" % (script.name, output))
        outputs.append({"script": script.name, "output": output})
    return outputs


def snapshot(base_head, current_rl, target):
    tree_oid = git("rev-parse", "HEAD:authoritative")
    status = git("status", "--porcelain", "--untracked-files=all", "--", "authoritative")
    if status:
        raise Failure("authoritative/ differs from committed HEAD")
    records = []
    for line in git("ls-tree", "-r", "HEAD", "authoritative").splitlines():
        metadata, path = line.split("\t", 1)
        mode, kind, oid = metadata.split()
        if kind != "blob":
            raise Failure("authoritative tree contains a non-blob leaf")
        local = ROOT / path
        if not local.is_file() or local.is_symlink():
            raise Failure("authoritative working tree contains a missing/unsafe file: " + path)
        records.append({
            "path": path,
            "mode": mode,
            "blob_oid": oid,
            "sha256": digest(local),
        })
    if not records:
        raise Failure("authoritative/ contains no committed files")
    return {
        "format": "rl-flat-authority-snapshot-v1",
        "base_head": base_head,
        "current_rl": current_rl,
        "target": target.relative_to(ROOT).as_posix(),
        "authoritative_tree_oid": tree_oid,
        "entries": records,
    }


def init_checkpoint(value):
    rl = value["current_rl"]
    work = ROOT / ".rl-work" / ("RL%d" % rl)
    snapshot_path = work / "authoritative-snapshot.json"
    if work.exists():
        if not snapshot_path.is_file():
            raise Failure("existing RL checkpoint lacks its authority snapshot")
        old = json.loads(snapshot_path.read_text(encoding="utf-8"))
        if old != value["snapshot"]:
            raise Failure("existing RL checkpoint belongs to different authority")
        return work, False
    work.mkdir(parents=True)
    (work / "artifacts").mkdir()
    snapshot_path.write_text(
        json.dumps(value["snapshot"], indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    state = {
        "format": "rl-local-checkpoint-v1",
        "base_head": value["base_head"],
        "current_rl": rl,
        "authoritative_target": value["target"],
        "created_at_utc": datetime.now(timezone.utc).isoformat(),
        "last_fully_verified_checkpoint": "Flat committed authority verified; declared verifier and red team passed; no new mathematics started.",
        "new_results": [],
        "promoted_exact_certificate_ranges": [],
        "incomplete_or_unverified_ranges": [],
        "corrections_or_demotions": [],
        "verifier_runs": [item["script"] for item in value["verifier_outputs"]],
        "failed_or_abandoned_routes": [],
        "next_step": "Read the authoritative target.",
        "stop_and_repair_active": False,
    }
    (work / "STATE.json").write_text(
        json.dumps(state, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )
    (work / "commands.log").write_text(
        "# Flat-authority preflight passed; append reproducible research commands here.\n",
        encoding="utf-8",
    )
    (work / "CHECKPOINT.md").write_text(
        "# Local RL checkpoint (NOT AUTHORITATIVE)\n\n"
        "- BASE_HEAD: `%s`\n- Current incoming RL: `RL%d`\n- Target: `%s`\n"
        "- Last fully verified state: committed flat authority plus declared verifier/red team passed.\n"
        "- Stop-and-repair active: no.\n- Next step: read the target and begin research.\n\n"
        "This ignored directory is a resumability aid, never proof state or a promotion candidate.\n"
        % (value["base_head"], rl, value["target"]),
        encoding="utf-8",
    )
    return work, True


def main():
    try:
        current_rl, target, commands = parse_start_here()
        require_flat_transport(current_rl)
        remote, base_ref, base_head = remote_identity()
        scripts = declared_verifier_commands(commands)
        verifier_outputs = run_verifiers(scripts)
        snap = snapshot(base_head, current_rl, target)
        value = {
            "incoming_rl": current_rl,
            "current_rl": current_rl,
            "handover_generation": current_rl - 1,
            "target": target.relative_to(ROOT).as_posix(),
            "transport_kind": "committed_flat_git_tree",
            "base_remote": remote,
            "base_ref": base_ref,
            "base_head": base_head,
            "authoritative_tree_oid": snap["authoritative_tree_oid"],
            "snapshot": snap,
            "verifier_outputs": verifier_outputs,
        }
        work, created = init_checkpoint(value)
        print("FLAT_AUTHORITY_PREFLIGHT_GREEN")
        print("Incoming: RL%d" % current_rl)
        print("Target: %s" % value["target"])
        print("Transport: committed flat Git tree")
        print("BASE_HEAD: %s" % base_head)
        print("authoritative tree: %s" % snap["authoritative_tree_oid"])
        for item in verifier_outputs:
            first = item["output"].splitlines()[0] if item["output"] else "PASS"
            print("%s: %s" % (item["script"], first))
        print("checkpoint: %s (%s)" % (work.relative_to(ROOT), "created" if created else "reused"))
        print("Flat connector handover startup gate: PASS")
    except (Failure, OSError, UnicodeError, json.JSONDecodeError) as error:
        print("flat-authority preflight: FAIL: %s" % error, file=sys.stderr)
        raise SystemExit(1)


if __name__ == "__main__":
    main()
