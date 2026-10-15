"""Deterministic, non-semantic repository catalogue support for rl_conveyor.

This module indexes paths and verbatim status records.  It deliberately does
not decide whether mathematical prose is true, current, superseded, or global.
"""

from __future__ import annotations

import hashlib
import json
import os
import re
import subprocess
import tempfile
from pathlib import Path, PurePosixPath


SESSION_FORMAT = "rl-session-catalog-v1"
RESULT_FORMAT = "rl-result-locator-v1"
METADATA_FORMAT = "rl-knowledge-index-v1"

PAIR_PATTERNS = (
    ("session-state filename", re.compile(r"RL0*(\d+)_SESSION_STATE_AND_RL0*(\d+)_KICKOFF", re.I)),
    ("from/to path", re.compile(r"from_RL0*(\d+)_to_RL0*(\d+)", re.I)),
    ("handover path", re.compile(r"RL0*(\d+)_to_RL0*(\d+)(?:_|\b)", re.I)),
)
ENTRYPOINT_NAMES = {"START_HERE.md", "README_START_HERE.md", "README_HANDOVER.md"}
SUPPORT_MARKERS = (
    "inherited", "parent_rl", "baseline_rl", "continuation", "allmd",
    "recovered_bundles", "audit_sources", "_bundle_transport", "unpacked",
    "provenance", "unfinished",
)
ROLE_EXCLUSIONS = {
    "main_report": (
        "START_HERE", "README", "SESSION_STATE", "KICKOFF", "TARGET",
        "LEDGER", "REVIEW", "VERIFICATION", "RED_TEAM", "MANIFEST",
        "SHA256", "CHECKSUM", "PROMPT", "RUN", "SOURCE_BUNDLE",
    ),
}


class CatalogError(RuntimeError):
    pass


class _BuildContext:
    """Invocation-local file facts; never survives one catalogue render."""

    def __init__(self, root: Path):
        self.root = root.resolve()
        self.resolved_paths: dict[Path, Path] = {}
        self.repo_paths: dict[Path, str] = {}
        self.contents: dict[Path, bytes] = {}
        self.digests: dict[Path, str] = {}
        self.fingerprints: dict[Path, tuple[int, int, int, int, int]] = {}
        self.file_lists: dict[str, tuple[str, ...]] = {}

    @staticmethod
    def _fingerprint(path: Path) -> tuple[int, int, int, int, int]:
        details = path.stat()
        return (
            details.st_dev,
            details.st_ino,
            details.st_mode,
            details.st_size,
            details.st_mtime_ns,
        )

    def resolve(self, path: Path) -> Path:
        resolved = self.resolved_paths.get(path)
        if resolved is None:
            resolved = path.resolve()
            self.resolved_paths[path] = resolved
            self.resolved_paths[resolved] = resolved
        return resolved

    def observe(self, path: Path) -> Path:
        path = self.resolve(path)
        if path not in self.fingerprints:
            try:
                path.relative_to(self.root)
                self.fingerprints[path] = self._fingerprint(path)
            except (ValueError, OSError) as error:
                raise CatalogError("catalogue input is missing or escapes repository: %s" % path) from error
        return path

    def read_bytes(self, path: Path) -> bytes:
        path = self.observe(path)
        if path not in self.contents:
            try:
                self.contents[path] = path.read_bytes()
            except OSError as error:
                raise CatalogError("cannot read catalogue input %s: %s" % (path, error)) from error
        return self.contents[path]

    def digest(self, path: Path) -> str:
        path = self.observe(path)
        if path not in self.digests:
            self.digests[path] = hashlib.sha256(self.read_bytes(path)).hexdigest()
        return self.digests[path]

    def size(self, path: Path) -> int:
        path = self.observe(path)
        return self.fingerprints[path][3]

    def repo_path(self, path: Path) -> str:
        cached = self.repo_paths.get(path)
        if cached is not None:
            return cached
        resolved = self.resolve(path)
        cached = self.repo_paths.get(resolved)
        if cached is None:
            try:
                cached = resolved.relative_to(self.root).as_posix()
            except ValueError as error:
                raise CatalogError("path escapes repository: %s" % path) from error
            self.repo_paths[resolved] = cached
        self.repo_paths[path] = cached
        return cached

    def assert_unchanged(self):
        for path, expected in self.fingerprints.items():
            try:
                actual = self._fingerprint(path)
            except OSError as error:
                raise CatalogError("catalogue input changed during generation: %s" % path) from error
            if actual != expected:
                raise CatalogError("catalogue input changed during generation: %s" % path)
        for prefix, expected in self.file_lists.items():
            actual = tuple(_git_file_names(self.root, prefix))
            if actual != expected:
                raise CatalogError("catalogue input set changed during generation: %s" % prefix)


_ACTIVE_CONTEXT: _BuildContext | None = None


def sha256_path(path: Path) -> str:
    if _ACTIVE_CONTEXT is not None:
        return _ACTIVE_CONTEXT.digest(path)
    value = hashlib.sha256()
    with path.open("rb") as source:
        for block in iter(lambda: source.read(1024 * 1024), b""):
            value.update(block)
    return value.hexdigest()


def _read_text(path: Path, errors="strict") -> str:
    if _ACTIVE_CONTEXT is not None:
        try:
            return _ACTIVE_CONTEXT.read_bytes(path).decode("utf-8", errors=errors)
        except UnicodeError as error:
            raise CatalogError("cannot decode catalogue input %s: %s" % (path, error)) from error
    try:
        return path.read_text(encoding="utf-8", errors=errors)
    except (OSError, UnicodeError) as error:
        raise CatalogError("cannot read catalogue input %s: %s" % (path, error)) from error


def parse_rl_identifier(value: str) -> int:
    match = re.fullmatch(r"(?i)RL0*(\d+)", value.strip())
    if not match:
        raise CatalogError("RL identifier must look like RL174")
    return int(match.group(1))


def _git_file_names(root: Path, prefix: str) -> list[str]:
    run = subprocess.run(
        ["git", "ls-files", "-z", "--cached", "--others", "--exclude-standard", "--", prefix],
        cwd=root,
        capture_output=True,
    )
    if run.returncode:
        raise CatalogError(run.stderr.decode("utf-8", "replace").strip() or "git ls-files failed")
    paths = []
    for raw in run.stdout.split(b"\0"):
        if not raw:
            continue
        relative = raw.decode("utf-8", "surrogateescape")
        path = root / relative
        if path.is_file():
            paths.append(relative)
    return sorted(paths)


def _git_files(root: Path, prefix: str) -> list[Path]:
    names = _git_file_names(root, prefix)
    if _ACTIVE_CONTEXT is not None:
        _ACTIVE_CONTEXT.file_lists[prefix] = tuple(names)
    return [root / name for name in names]


def _repo_path(root: Path, path: Path) -> str:
    if _ACTIVE_CONTEXT is not None:
        return _ACTIVE_CONTEXT.repo_path(path)
    try:
        return path.resolve().relative_to(root.resolve()).as_posix()
    except ValueError as error:
        raise CatalogError("path escapes repository: %s" % path) from error


def _content_identity(root: Path, files: list[Path]) -> dict:
    total = 0
    digest = hashlib.sha256()
    unique = sorted(set(files), key=lambda item: _repo_path(root, item))
    for path in unique:
        relative = _repo_path(root, path)
        size = _ACTIVE_CONTEXT.size(path) if _ACTIVE_CONTEXT is not None else path.stat().st_size
        total += size
        digest.update(relative.encode("utf-8", "surrogateescape"))
        digest.update(b"\0")
        digest.update(str(size).encode("ascii"))
        digest.update(b"\0")
        digest.update(sha256_path(path).encode("ascii"))
        digest.update(b"\n")
    return {"file_count": len(unique), "bytes": total, "sha256": digest.hexdigest()}


def _support_penalty(container: Path, path: Path) -> int:
    parts = [part.lower() for part in path.relative_to(container).parts[:-1]]
    return sum(1 for part in parts if any(marker in part for marker in SUPPORT_MARKERS))


def _dedupe_paths(root: Path, container: Path, paths: list[Path]) -> list[Path]:
    if not paths:
        return []
    minimum = min(_support_penalty(container, path) for path in paths)
    candidates = [path for path in paths if _support_penalty(container, path) == minimum]
    chosen: dict[str, Path] = {}
    for path in sorted(candidates, key=lambda item: (len(item.parts), _repo_path(root, item))):
        chosen.setdefault(sha256_path(path), path)
    return sorted(chosen.values(), key=lambda item: _repo_path(root, item))


def _role(path: Path) -> str | None:
    name = path.name.upper()
    if path.suffix.lower() == ".md":
        if ("CORRECTION" in name or "DEMOTION" in name) and "LEDGER" in name:
            return "correction_ledger"
        if "CERTIFIED_FACTS" in name or "PROOF_LEDGER" in name or "PROOF_STATUS" in name or "PROOF_STATE" in name:
            return "proof_ledger"
        if "SESSION_STATE" in name or ("HANDOVER" in name and "README" not in name and "MANIFEST" not in name):
            return "session_state"
        if "TARGET" in name or "KICKOFF_PROMPT" in name or "OPEN_FRONTIER" in name or "OPEN_OBLIGATION" in name:
            return "target"
        if path.name in ENTRYPOINT_NAMES:
            return "entrypoint"
        if "FRESH_UNPACK" in name or "RELEASE_VERIFICATION" in name:
            return "fresh_unpack"
    if path.suffix.lower() == ".zip":
        return "bundle"
    if name.endswith(".ZIP.SHA256") or name.endswith(".SHA256"):
        return "sidecar"
    if name in {"SHA256SUMS.TXT", "SHASUMS.TXT", "SHANSUMS.TXT"} or "MANIFEST" in name:
        return "manifest"
    if re.search(r"(^VERIFY.*\.PY$|^RUN_.*VERIFIER.*\.SH$|VERIFIERS?\.SH$)", name):
        return "verifier"
    if name == "SOURCE_BUNDLE.MD":
        return "source_bundle"
    return None


def _explicit_pairs(container: Path, files: list[Path]) -> list[dict]:
    records = []
    seen = set()
    for path in files:
        if _support_penalty(container, path):
            continue
        relative = path.relative_to(container).as_posix()
        for method, pattern in PAIR_PATTERNS:
            for match in pattern.finditer(relative):
                completed, incoming = int(match.group(1)), int(match.group(2))
                key = (completed, incoming, relative, method)
                if key not in seen:
                    records.append({
                        "completed_rl": completed,
                        "incoming_rl": incoming,
                        "method": method,
                        "source_path": relative,
                    })
                    seen.add(key)
        if path.name in ENTRYPOINT_NAMES and path.suffix.lower() == ".md":
            text = _read_text(path, errors="replace")
            pattern = re.compile(
                r"freezes\s+(?:the\s+)?completed\s+RL0*(\d+).*?launch(?:es|ing)\s+RL0*(\d+)",
                re.I | re.S,
            )
            match = pattern.search(text[:5000])
            if match:
                completed, incoming = int(match.group(1)), int(match.group(2))
                key = (completed, incoming, relative, "entrypoint declaration")
                if key not in seen:
                    records.append({
                        "completed_rl": completed,
                        "incoming_rl": incoming,
                        "method": "entrypoint declaration",
                        "source_path": relative,
                    })
                    seen.add(key)
    return sorted(records, key=lambda item: (
        item["completed_rl"], item["incoming_rl"], item["source_path"], item["method"]
    ))


def _generation_root(container: Path, relative_source: str) -> str:
    parts = Path(relative_source).parts
    if len(parts) <= 1:
        return "."
    return parts[0]


def _files_for_roots(
    container: Path,
    files: list[Path],
    roots: list[str],
    other_generation_roots: set[str] | None = None,
) -> list[Path]:
    other_generation_roots = other_generation_roots or set()
    selected = []
    for path in files:
        relative = path.relative_to(container)
        # A flat handover still owns its verification/certificate subdirectories.
        # Do not absorb another explicitly located generation or support package.
        if "." in roots and (
            len(relative.parts) == 1
            or (relative.parts[0] not in other_generation_roots
                and relative.parts[0].lower() in {"verification", "verifiers", "certificates"}
                and not _support_penalty(container, path)
            )
        ):
            selected.append(path)
            continue
        if relative.parts and relative.parts[0] in roots:
            selected.append(path)
    return sorted(set(selected), key=lambda item: item.as_posix())


def _extract_references(root: Path, entrypoints: list[Path]) -> list[Path]:
    found = []
    for entrypoint in entrypoints:
        text = _read_text(entrypoint, errors="replace")
        tokens = re.findall(r"`([^`]+)`", text)
        tokens += re.findall(r"\[[^\]]+\]\(([^)]+)\)", text)
        for token in tokens:
            token = token.strip().split("#", 1)[0]
            if (
                not token or "\n" in token or len(token) > 500 or "://" in token
                or token.startswith("python3 ") or token.startswith("bash ")
                or not re.fullmatch(r"[A-Za-z0-9_./+()\- ]+\.[A-Za-z0-9]+", token)
            ):
                continue
            if token.startswith("./"):
                token = token[2:]
            relative = PurePosixPath(token)
            if relative.is_absolute() or ".." in relative.parts or "\\" in token:
                continue
            candidate = (entrypoint.parent / Path(*relative.parts)).resolve()
            try:
                candidate.relative_to(root.resolve())
            except ValueError:
                continue
            if candidate.is_file():
                found.append(candidate)
    return sorted(set(found), key=lambda item: _repo_path(root, item))


def _archive_references(root: Path, source_bundle_paths: list[Path]) -> list[str]:
    found = set()
    for source in source_bundle_paths:
        text = _read_text(source, errors="replace")
        for match in re.finditer(r"`?(Archive/[^`\s)]+)`?", text):
            candidate = match.group(1).rstrip(".,")
            if (root / candidate).exists():
                found.add(candidate)
    return sorted(found)


def _main_reports(completed: int | None, files: list[Path], references: list[Path]) -> list[Path]:
    candidates = []
    for path in references:
        if path.suffix.lower() == ".md" and _role(path) is None:
            candidates.append(path)
    if candidates:
        return candidates
    for path in files:
        name = path.name.upper()
        if path.suffix.lower() != ".md" or any(token in name for token in ROLE_EXCLUSIONS["main_report"]):
            continue
        if completed is None or re.search(r"(?:^|_)RL0*%d(?:_|\b)" % completed, name, re.I):
            candidates.append(path)
    return candidates


def _dates(paths: list[Path]) -> list[str]:
    values = set()
    for path in paths:
        values.update(re.findall(r"20\d\d-\d\d-\d\d", path.as_posix()))
    return sorted(values)


def _recorded_title(container: Path, roots: list[str], reports: list[Path]) -> tuple[str | None, list[str]]:
    candidates = [root for root in roots if root != "."]
    candidates.extend(path.stem for path in reports)
    candidates = sorted(dict.fromkeys(candidates))
    return (candidates[0] if len(candidates) == 1 else None, candidates)


def _container_number(container: Path) -> int:
    match = re.fullmatch(r"RL0*(\d+)", container.name, re.I)
    if not match:
        raise CatalogError("invalid session container: %s" % container)
    return int(match.group(1))


def _make_generation_entry(
    root: Path,
    container: Path,
    container_files: list[Path],
    container_identity: dict,
    pair: tuple[int, int] | None,
    pair_records: list[dict],
    pair_count: int,
) -> dict:
    completed, incoming = pair if pair else (None, None)
    roots = sorted({_generation_root(container, item["source_path"]) for item in pair_records}) if pair_records else ["."]
    other_roots = set()
    if "." in roots and pair_count > 1:
        other_roots = {
            _generation_root(container, item["source_path"])
            for item in _explicit_pairs(container, container_files)
            if (item["completed_rl"], item["incoming_rl"]) != pair
        } - set(roots)
    generation_files = _files_for_roots(container, container_files, roots, other_roots)
    if not generation_files:
        generation_files = container_files

    roles: dict[str, list[Path]] = {}
    for path in generation_files:
        role = _role(path)
        if role:
            roles.setdefault(role, []).append(path)
        name = path.name.upper()
        if role == "correction_ledger" and ("PROOF" in name or "CERTIFIED_FACTS" in name):
            roles.setdefault("proof_ledger", []).append(path)
    for role, paths in list(roles.items()):
        roles[role] = _dedupe_paths(root, container, paths)

    entrypoints = roles.get("entrypoint", [])
    references = _extract_references(root, entrypoints)
    reports = _dedupe_paths(root, container, _main_reports(completed, generation_files, references))
    certificate_roots = set()
    for path in generation_files:
        if _support_penalty(container, path):
            continue
        for parent in [path.parent, *path.parents]:
            if parent == container.parent:
                break
            name = parent.name.upper()
            if "CERTIFICATE" in name or name == "VERIFICATION":
                certificate_roots.add(parent)
                break

    role_paths = {
        "entrypoint_paths": entrypoints,
        "startup_reference_paths": references,
        "main_report_paths": reports,
        "session_state_handover_paths": roles.get("session_state", []),
        "target_paths": roles.get("target", []),
        "proof_ledger_paths": roles.get("proof_ledger", []),
        "correction_demotion_ledger_paths": roles.get("correction_ledger", []),
        "verifier_paths": roles.get("verifier", []),
        "certificate_roots": sorted(certificate_roots, key=lambda item: _repo_path(root, item)),
        "bundle_paths": roles.get("bundle", []),
        "sidecar_paths": roles.get("sidecar", []),
        "manifest_paths": roles.get("manifest", []),
        "fresh_unpack_paths": roles.get("fresh_unpack", []),
        "source_bundle_paths": roles.get("source_bundle", []),
    }
    container_rl = _container_number(container)
    if pair_count > 1:
        layout = "multi-generation-container"
    elif completed is None:
        layout = "legacy-unresolved"
    elif container_rl == incoming:
        layout = "incoming-labelled-container"
    elif container_rl == completed:
        layout = "completed-labelled-container"
    else:
        layout = "offset-or-legacy-container"
    all_locator_paths = [path for paths in role_paths.values() for path in paths]
    date_values = _dates(list(generation_files) + all_locator_paths)
    title, title_candidates = _recorded_title(container, roots, reports)
    generation_id = (
        "RL%d-to-RL%d@%s" % (completed, incoming, container.name)
        if pair else "unresolved@%s" % container.name
    )
    entry = {
        "format": SESSION_FORMAT,
        "record_type": "generation",
        "generation_id": generation_id,
        "container_path": _repo_path(root, container),
        "container_rl": container_rl,
        "generation_paths": [
            _repo_path(root, container if item == "." else container / item) for item in roots
        ],
        "layout_kind": layout,
        "completed_rl": completed,
        "incoming_rl": incoming,
        "relationship_evidence": [
            {**item, "source_path": _repo_path(root, container / item["source_path"])}
            for item in pair_records
        ],
        "date": date_values[-1] if date_values else None,
        "date_candidates": date_values,
        "recorded_title": title,
        "recorded_title_candidates": title_candidates,
        "container_identity": container_identity,
        "source_generation_identity": _content_identity(root, generation_files),
        "archive_source_paths": _archive_references(root, roles.get("source_bundle", [])),
        "predecessor_generation_ids": [],
        "successor_generation_ids": [],
        "ambiguities": [],
    }
    for key, paths in role_paths.items():
        entry[key] = [_repo_path(root, path) for path in paths]
    if pair is None:
        entry["ambiguities"].append("No explicit completed/incoming transition pair was found; this is a locator, not an inferred RL transition.")
    if len(roots) > 1:
        entry["ambiguities"].append("Multiple physical roots encode this transition; all are retained as aliases.")
    return entry


def build_session_catalog(root: Path) -> list[dict]:
    sessions = root / "sessions"
    if not sessions.is_dir():
        raise CatalogError("sessions/ is missing")
    files = _git_files(root, "sessions")
    by_container: dict[Path, list[Path]] = {}
    for path in files:
        relative = path.relative_to(sessions)
        if not relative.parts or not re.fullmatch(r"RL\d+", relative.parts[0], re.I):
            continue
        container = sessions / relative.parts[0]
        by_container.setdefault(container, []).append(path)

    entries = []
    for container in sorted(by_container, key=lambda item: _container_number(item)):
        container_files = by_container[container]
        container_identity = _content_identity(root, container_files)
        pair_evidence = _explicit_pairs(container, container_files)
        pairs = sorted({(item["completed_rl"], item["incoming_rl"]) for item in pair_evidence})
        if pairs:
            for pair in pairs:
                evidence = [item for item in pair_evidence if (item["completed_rl"], item["incoming_rl"]) == pair]
                entries.append(_make_generation_entry(
                    root, container, container_files, container_identity, pair, evidence, len(pairs)
                ))
        else:
            entries.append(_make_generation_entry(
                root, container, container_files, container_identity, None, [], 0
            ))

    covered_rls = {
        value
        for entry in entries
        for value in (entry["container_rl"], entry["completed_rl"], entry["incoming_rl"])
        if value is not None
    }
    mention_candidates: dict[int, list[Path]] = {}
    for container_files in by_container.values():
        for path in container_files:
            relative = path.relative_to(sessions).as_posix()
            for value in re.findall(r"(?i)RL0*(\d+)", relative):
                number = int(value)
                if number not in covered_rls:
                    mention_candidates.setdefault(number, []).append(path)
    for number, paths in sorted(mention_candidates.items()):
        chosen = sorted(set(paths), key=lambda path: (
            sum(1 for part in path.parts if any(marker in part.lower() for marker in SUPPORT_MARKERS)),
            len(path.parts),
            _repo_path(root, path),
        ))[:5]
        if not chosen:
            continue
        first_relative = chosen[0].relative_to(sessions)
        container = sessions / first_relative.parts[0]
        container_path = _repo_path(root, container)
        empty_keys = (
            "entrypoint_paths", "startup_reference_paths", "main_report_paths",
            "session_state_handover_paths", "target_paths", "proof_ledger_paths",
            "correction_demotion_ledger_paths", "verifier_paths", "certificate_roots",
            "bundle_paths", "sidecar_paths", "manifest_paths", "fresh_unpack_paths",
            "source_bundle_paths",
        )
        embedded = {
            "format": SESSION_FORMAT,
            "record_type": "embedded_locator",
            "generation_id": "RL%d-embedded@%s" % (number, container.name),
            "container_path": container_path,
            "container_rl": _container_number(container),
            "generation_paths": sorted({_repo_path(root, path.parent) for path in chosen}),
            "layout_kind": "embedded-only-locator",
            "completed_rl": None,
            "incoming_rl": None,
            "mentioned_rls": [number],
            "relationship_evidence": [
                {
                    "completed_rl": None,
                    "incoming_rl": None,
                    "method": "path label only",
                    "source_path": _repo_path(root, path),
                }
                for path in chosen
            ],
            "date": None,
            "date_candidates": _dates(chosen),
            "recorded_title": None,
            "recorded_title_candidates": [],
            "container_identity": next(
                entry["container_identity"] for entry in entries if entry["container_path"] == container_path
            ),
            "source_generation_identity": _content_identity(root, chosen),
            "archive_source_paths": [],
            "predecessor_generation_ids": [],
            "successor_generation_ids": [],
            "ambiguities": [
                "This RL label is embedded in cumulative historical material. No completed/incoming transition role is inferred."
            ],
        }
        for key in empty_keys:
            embedded[key] = []
        entries.append(embedded)

    for entry in entries:
        completed, incoming = entry["completed_rl"], entry["incoming_rl"]
        if completed is not None:
            entry["predecessor_generation_ids"] = sorted(
                other["generation_id"] for other in entries
                if other["incoming_rl"] == completed and other["generation_id"] != entry["generation_id"]
            )
        if incoming is not None:
            entry["successor_generation_ids"] = sorted(
                other["generation_id"] for other in entries
                if other["completed_rl"] == incoming and other["generation_id"] != entry["generation_id"]
            )
        entry.setdefault("mentioned_rls", sorted({
            value for value in (entry["container_rl"], completed, incoming) if value is not None
        }))
    return sorted(entries, key=lambda item: (
        item["completed_rl"] is None,
        item["completed_rl"] if item["completed_rl"] is not None else item["container_rl"],
        item["incoming_rl"] if item["incoming_rl"] is not None else -1,
        item["container_path"],
    ))


def _source_kind(path: str) -> str:
    name = Path(path).name.upper()
    if "CORRECTION" in name or "DEMOTION" in name:
        if "PROOF" in name or "CERTIFIED_FACTS" in name:
            return "combined_proof_correction_ledger"
        return "correction_demotion_ledger"
    if "SESSION_STATE" in name or "HANDOVER" in name:
        return "session_state_handover"
    return "proof_status_ledger"


def _normalise_space(value: str) -> str:
    return " ".join(value.replace("\u00a0", " ").split())


def normalise_query(value: str) -> str:
    return " ".join(re.findall(r"[a-z0-9]+", value.casefold()))


def _classification_heading(headings: list[str]) -> str | None:
    markers = (
        "proved", "analytic", "certificate", "correction", "demotion", "barrier",
        "dead", "open", "conjecture", "status", "classification", "inherited",
        "computational evidence", "obligation", "closure ledger",
    )
    for heading in reversed(headings):
        if any(marker in heading.casefold() for marker in markers):
            return heading
    return None


def _aliases(text: str, name: str | None) -> list[str]:
    values = set(re.findall(r"\bRL\d+(?:[.\-][A-Za-z0-9]+)+\b", text, re.I))
    values.update(re.findall(r"`([A-Za-z][A-Za-z0-9_.\-]{1,40})`", text))
    if name:
        values.add(name)
    return sorted(values, key=lambda item: item.casefold())


def _record(
    source: dict,
    source_path: Path,
    line_start: int,
    line_end: int,
    name: str | None,
    text: str,
    classification: str | None,
    headings: list[str],
) -> dict:
    relative = source["source_path"]
    compact = _normalise_space(text)
    identity_seed = "%s:%d:%d:%s" % (relative, line_start, line_end, compact)
    correction_record = (
        bool(classification and re.search(r"correction|demotion", classification, re.I))
        or bool(re.search(r"\bDEMOTED\b|\bCORRECTED\b", compact, re.I))
    )
    return {
        "format": RESULT_FORMAT,
        "record_id": hashlib.sha256(identity_seed.encode("utf-8")).hexdigest()[:20],
        "name": _normalise_space(name) if name else None,
        "aliases": _aliases(compact, name),
        "recorded_classification": _normalise_space(classification) if classification else None,
        "recorded_text": compact,
        "section_path": headings[:],
        "source_path": relative,
        "source_line_start": line_start,
        "source_line_end": line_end,
        "source_sha256": sha256_path(source_path),
        "source_kind": source["source_kind"],
        "source_scope": source["source_scope"],
        "generation_id": source.get("generation_id"),
        "completed_rl": source.get("completed_rl"),
        "incoming_rl": source.get("incoming_rl"),
        "is_correction_source": source["source_kind"] == "correction_demotion_ledger",
        "is_correction_or_demotion_record": correction_record,
        "verifier_paths": source.get("verifier_paths", []),
        "certificate_roots": source.get("certificate_roots", []),
    }


def _split_markdown_row(line: str) -> list[str]:
    value = line.strip()
    if value.startswith("|"):
        value = value[1:]
    if value.endswith("|"):
        value = value[:-1]
    cells = []
    current = []
    in_code = False
    escaped = False
    for character in value:
        if escaped:
            current.append(character)
            escaped = False
            continue
        if character == "\\":
            current.append(character)
            escaped = True
            continue
        if character == "`":
            in_code = not in_code
            current.append(character)
            continue
        if character == "|" and not in_code:
            cells.append("".join(current))
            current = []
            continue
        current.append(character)
    cells.append("".join(current))
    return cells


def _parse_markdown_records(root: Path, source: dict) -> list[dict]:
    path = root / source["source_path"]
    lines = _read_text(path, errors="replace").splitlines()
    headings: list[str] = []
    records = []
    index = 0
    fence: str | None = None
    while index < len(lines):
        raw = lines[index]
        fence_match = re.match(r"^\s{0,3}(`{3,}|~{3,})", raw)
        if fence is not None:
            if re.fullmatch(r"\s{0,3}" + re.escape(fence[0]) + "{" + str(len(fence)) + r",}\s*", raw):
                fence = None
            index += 1
            continue
        if fence_match:
            fence = fence_match.group(1)
            index += 1
            continue
        heading = re.match(r"^(#{1,6})\s+(.+?)\s*$", raw)
        if heading:
            level = len(heading.group(1))
            title = _normalise_space(re.sub(r"[*_`]", "", heading.group(2)))
            headings = headings[: level - 1]
            headings.append(title)
            if re.search(r"\bRL\d+(?:[.\-][A-Za-z0-9]+)+\b", title, re.I):
                records.append(_record(
                    source, path, index + 1, index + 1, title, raw,
                    _classification_heading(headings[:-1]), headings,
                ))
            index += 1
            continue

        if raw.lstrip().startswith("|") and index + 1 < len(lines) and re.match(r"^\s*\|?\s*:?-+", lines[index + 1]):
            headers = [_normalise_space(cell).casefold() for cell in _split_markdown_row(raw)]
            index += 2
            while index < len(lines) and lines[index].lstrip().startswith("|"):
                cells = [_normalise_space(cell) for cell in _split_markdown_row(lines[index])]
                values = dict(zip(headers, cells))
                name = next((values[key] for key in ("id", "name", "claim", "result", "sector") if values.get(key)), None)
                classification = next((values[key] for key in ("classification", "class", "status", "evidence") if values.get(key)), None)
                if name or classification:
                    records.append(_record(
                        source, path, index + 1, index + 1, name, lines[index],
                        classification or _classification_heading(headings), headings,
                    ))
                index += 1
            continue

        bullet = re.match(r"^\s*(?:[-*+]\s+|\d+[.)]\s+)(.+)$", raw)
        if bullet:
            start = index
            block = [bullet.group(1)]
            index += 1
            while index < len(lines):
                continuation = lines[index]
                if not continuation.strip() or re.match(r"^\s*(?:[-*+]\s+|\d+[.)]\s+|#{1,6}\s+|\|)", continuation):
                    break
                if continuation.startswith(" ") or continuation.startswith("\t"):
                    block.append(continuation.strip())
                    index += 1
                else:
                    break
            text = " ".join(block)
            bold = re.match(r"^\*\*([^*]{1,160})\*\*", text)
            identifier = re.search(r"\bRL\d+(?:[.\-][A-Za-z0-9]+)+\b", text, re.I)
            name = bold.group(1).rstrip(":. ") if bold else (identifier.group(0) if identifier else None)
            classification = _classification_heading(headings)
            explicit = re.search(r"\*\*(?:Class|Classification|Status)\s*:\*\*\s*([^.;]+)", text, re.I)
            if explicit:
                classification = explicit.group(1)
            if name or classification or source["source_kind"] == "correction_demotion_ledger":
                records.append(_record(
                    source, path, start + 1, index, name, text, classification, headings,
                ))
            continue

        explicit = re.match(r"^\s*\*\*(?:Class|Classification|Status)\s*:\*\*\s*(.+)$", raw, re.I)
        if explicit:
            name = headings[-1] if headings else None
            records.append(_record(
                source, path, index + 1, index + 1, name, raw, explicit.group(1), headings,
            ))
            index += 1
            continue

        # Modern canonical ledgers also use ordinary paragraphs. Preserve the
        # complete paragraph and its recorded heading, including qualifications
        # and nonpromotion statements; never infer a mathematical classification.
        if (raw.strip() and not raw.startswith(("    ", "\t"))
                and not raw.lstrip().startswith(("|", ">"))
                and not re.fullmatch(r"\s*([-*_])(?:\s*\1){2,}\s*", raw)):
            start = index
            block = [raw]
            index += 1
            while index < len(lines):
                continuation = lines[index]
                if (not continuation.strip()
                        or continuation.startswith(("    ", "\t"))
                        or re.match(r"^\s*(?:[-*+]\s+|\d+[.)]\s+|#{1,6}\s+|\||>|`{3,}|~{3,})", continuation)
                        or re.match(r"^\s*\*\*(?:Class|Classification|Status)\s*:", continuation, re.I)
                        or re.fullmatch(r"\s*([-*_])(?:\s*\1){2,}\s*", continuation)):
                    break
                block.append(continuation)
                index += 1
            text = "\n".join(block)
            bold = re.match(r"^\*\*([^*]{1,160})\*\*", text)
            identifier = re.search(r"\bRL\d+(?:[.\-][A-Za-z0-9]+)+\b", text, re.I)
            name = bold.group(1).rstrip(":. ") if bold else (identifier.group(0) if identifier else None)
            records.append(_record(
                source, path, start + 1, index, name, text,
                _classification_heading(headings), headings,
            ))
            continue
        index += 1
    return records


def _authoritative_sources(root: Path) -> list[dict]:
    files = _git_files(root, "authoritative")
    sources = []
    verifier_paths = [_repo_path(root, path) for path in files if _role(path) == "verifier"]
    certificate_roots = sorted({
        _repo_path(root, parent)
        for path in files
        for parent in path.parents
        if parent != root and ("CERTIFICATE" in parent.name.upper() or parent.name.upper() == "VERIFICATION")
    })
    for path in files:
        role = _role(path)
        if role not in {"proof_ledger", "correction_ledger", "session_state"}:
            continue
        sources.append({
            "source_path": _repo_path(root, path),
            "source_kind": _source_kind(_repo_path(root, path)),
            "source_scope": "authoritative",
            "generation_id": "current-authoritative",
            "completed_rl": None,
            "incoming_rl": None,
            "verifier_paths": verifier_paths,
            "certificate_roots": certificate_roots,
        })
    return sources


def build_result_catalog(root: Path, sessions: list[dict]) -> tuple[list[dict], list[dict]]:
    sources = _authoritative_sources(root)
    for entry in sessions:
        for key in ("proof_ledger_paths", "correction_demotion_ledger_paths", "session_state_handover_paths"):
            for path in entry[key]:
                sources.append({
                    "source_path": path,
                    "source_kind": _source_kind(path),
                    "source_scope": "session",
                    "generation_id": entry["generation_id"],
                    "completed_rl": entry["completed_rl"],
                    "incoming_rl": entry["incoming_rl"],
                    "verifier_paths": entry["verifier_paths"],
                    "certificate_roots": entry["certificate_roots"],
                })

    chosen: dict[str, dict] = {}
    for source in sorted(sources, key=lambda item: (
        item["source_scope"] != "authoritative",
        len(Path(item["source_path"]).parts),
        item["source_path"],
    )):
        path = root / source["source_path"]
        if not path.is_file():
            continue
        chosen.setdefault(sha256_path(path), source)
    unique_sources = sorted(chosen.values(), key=lambda item: (
        item["source_scope"] != "authoritative", item["source_path"]
    ))
    records = []
    for source in unique_sources:
        records.extend(_parse_markdown_records(root, source))
    records.sort(key=lambda item: (
        item["source_scope"] != "authoritative",
        -(item["completed_rl"] if item["completed_rl"] is not None else -1),
        item["source_path"], item["source_line_start"], item["record_id"],
    ))
    return records, unique_sources


def _jsonl_bytes(records: list[dict]) -> bytes:
    return b"".join(
        (json.dumps(record, sort_keys=True, ensure_ascii=False, separators=(",", ":")) + "\n").encode("utf-8")
        for record in records
    )


def _build_index_bytes(root: Path) -> dict[str, bytes]:
    sessions = build_session_catalog(root)
    results, sources = build_result_catalog(root, sessions)
    session_bytes = _jsonl_bytes(sessions)
    result_bytes = _jsonl_bytes(results)
    container_paths = sorted({entry["container_path"] for entry in sessions})
    explicit_completed = sorted({entry["completed_rl"] for entry in sessions if entry["completed_rl"] is not None})
    explicit_incoming = sorted({entry["incoming_rl"] for entry in sessions if entry["incoming_rl"] is not None})
    located_rls = sorted({number for entry in sessions for number in entry.get("mentioned_rls", [])})
    maximum_rl = max(located_rls) if located_rls else -1
    metadata = {
        "format": METADATA_FORMAT,
        "generator": "tools/rl_conveyor.py index-build",
        "container_count": len(container_paths),
        "generation_record_count": len(sessions),
        "explicit_completed_rls": explicit_completed,
        "explicit_incoming_rls": explicit_incoming,
        "located_rls": located_rls,
        "unlocated_rls": [number for number in range(maximum_rl + 1) if number not in located_rls],
        "unresolved_container_paths": sorted({
            entry["container_path"] for entry in sessions
            if entry["record_type"] == "generation" and entry["completed_rl"] is None
        }),
        "result_source_count": len(sources),
        "result_record_count": len(results),
        "session_catalog_sha256": hashlib.sha256(session_bytes).hexdigest(),
        "result_catalog_sha256": hashlib.sha256(result_bytes).hexdigest(),
    }
    metadata_bytes = (json.dumps(metadata, indent=2, sort_keys=True) + "\n").encode("utf-8")
    return {
        "session_catalog.jsonl": session_bytes,
        "result_catalog.jsonl": result_bytes,
        "index_metadata.json": metadata_bytes,
    }


def _render_index_bytes(root: Path) -> tuple[dict[str, bytes], tuple[str, ...]]:
    global _ACTIVE_CONTEXT
    if _ACTIVE_CONTEXT is not None:
        raise CatalogError("nested catalogue generation is not supported")
    context = _BuildContext(root)
    _ACTIVE_CONTEXT = context
    try:
        rendered = _build_index_bytes(root)
        context.assert_unchanged()
        inputs = tuple(sorted(context.repo_path(path) for path in context.fingerprints))
        return rendered, inputs
    finally:
        _ACTIVE_CONTEXT = None


def build_index_bytes(root: Path) -> dict[str, bytes]:
    return _render_index_bytes(root)[0]


def _atomic_write(path: Path, content: bytes):
    descriptor = None
    temporary = None
    try:
        descriptor, raw_temporary = tempfile.mkstemp(
            prefix=".%s." % path.name, suffix=".tmp", dir=str(path.parent)
        )
        temporary = Path(raw_temporary)
        with os.fdopen(descriptor, "wb") as target:
            descriptor = None
            target.write(content)
            target.flush()
            os.fsync(target.fileno())
        os.replace(str(temporary), str(path))
        temporary = None
    except OSError as error:
        raise CatalogError("cannot atomically publish %s: %s" % (path, error)) from error
    finally:
        if descriptor is not None:
            os.close(descriptor)
        if temporary is not None:
            try:
                temporary.unlink()
            except FileNotFoundError:
                pass


def write_indexes(root: Path) -> dict:
    knowledge = root / "knowledge"
    knowledge.mkdir(parents=True, exist_ok=True)
    rendered = build_index_bytes(root)
    # Publish the catalogues first and their hash/count metadata last. Each
    # replacement is atomic, and byte-identical outputs retain their mtimes.
    for name in ("session_catalog.jsonl", "result_catalog.jsonl", "index_metadata.json"):
        path = knowledge / name
        content = rendered[name]
        try:
            unchanged = path.is_file() and path.read_bytes() == content
        except OSError as error:
            raise CatalogError("cannot compare generated index %s: %s" % (path, error)) from error
        if not unchanged:
            _atomic_write(path, content)
    metadata = json.loads(rendered["index_metadata.json"])
    return metadata


def root_start_contract_issues(root: Path) -> list[str]:
    path = root / "START_HERE.md"
    if not path.is_file():
        return ["root START_HERE.md is missing"]
    text = _read_text(path, errors="replace")
    issues = []
    if re.search(r"\bRL\d+\b", text):
        issues.append("root START_HERE.md contains a hard-coded live RL number")
    for required in ("tools/rl_conveyor.py startup", "authoritative/START_HERE.md"):
        if required not in text:
            issues.append("root START_HERE.md lacks stable pointer: " + required)
    return issues


def _git_names(root: Path, *args: str) -> set[str]:
    run = subprocess.run(["git", *args], cwd=root, capture_output=True)
    if run.returncode:
        raise CatalogError(run.stderr.decode("utf-8", "replace").strip() or "git command failed")
    return {
        raw.decode("utf-8", "surrogateescape")
        for raw in run.stdout.split(b"\0") if raw
    }


def _staged_tree_issues(root: Path, inputs: tuple[str, ...]) -> list[dict]:
    generated = {
        "knowledge/session_catalog.jsonl",
        "knowledge/result_catalog.jsonl",
        "knowledge/index_metadata.json",
    }
    required = set(inputs) | generated | {"START_HERE.md"}
    prefixes = ("sessions", "authoritative", "START_HERE.md", *sorted(generated))
    cached = _git_names(root, "ls-files", "-z", "--cached", "--", *prefixes)
    issues = []
    missing = sorted(required - cached)
    if missing:
        issues.append({
            "path": "git-index",
            "reason": "catalogue inputs or outputs are not staged/tracked: " + ", ".join(missing[:10]),
        })
    unstaged = sorted(_git_names(root, "diff", "--name-only", "-z", "--", *prefixes))
    if unstaged:
        issues.append({
            "path": "git-index",
            "reason": "catalogue inputs or outputs differ between index and worktree: "
            + ", ".join(unstaged[:10]),
        })
    return issues


def validate_indexes(root: Path, staged: bool = False) -> dict:
    knowledge = root / "knowledge"
    rendered, inputs = _render_index_bytes(root)
    mismatches = []
    for name, expected in rendered.items():
        path = knowledge / name
        if not path.is_file():
            mismatches.append({"path": _repo_path(root, path), "reason": "missing"})
        elif path.read_bytes() != expected:
            mismatches.append({"path": _repo_path(root, path), "reason": "stale or modified"})
    for issue in root_start_contract_issues(root):
        mismatches.append({"path": "START_HERE.md", "reason": issue})
    if staged:
        mismatches.extend(_staged_tree_issues(root, inputs))
    metadata = json.loads(rendered["index_metadata.json"])
    metadata["current"] = not mismatches
    metadata["mismatches"] = mismatches
    metadata["root_start_contract_current"] = not any(
        item["path"] == "START_HERE.md" for item in mismatches
    )
    return metadata


def iter_jsonl(path: Path, expected_format: str):
    if not path.is_file():
        raise CatalogError("knowledge index is missing; run index-build")
    try:
        with path.open("r", encoding="utf-8") as source:
            for line_number, line in enumerate(source, 1):
                if not line.strip():
                    continue
                try:
                    record = json.loads(line)
                except json.JSONDecodeError as error:
                    raise CatalogError("invalid JSONL at %s:%d" % (path, line_number)) from error
                if not isinstance(record, dict) or record.get("format") != expected_format:
                    raise CatalogError("unexpected index format at %s:%d" % (path, line_number))
                yield record
    except UnicodeError as error:
        raise CatalogError("invalid UTF-8 in knowledge index: %s" % path) from error
    except OSError as error:
        raise CatalogError("cannot read knowledge index %s: %s" % (path, error)) from error


def load_jsonl(path: Path, expected_format: str) -> list[dict]:
    return list(iter_jsonl(path, expected_format))


def query_sessions(root: Path, rl: int) -> dict:
    records = load_jsonl(root / "knowledge" / "session_catalog.jsonl", SESSION_FORMAT)
    completed = [item for item in records if item["completed_rl"] == rl]
    incoming = [item for item in records if item["incoming_rl"] == rl]
    containers = [item for item in records if item["container_rl"] == rl]
    embedded = [
        item for item in records
        if item.get("record_type") == "embedded_locator" and rl in item.get("mentioned_rls", [])
    ]
    return {
        "query_rl": rl,
        "completed_generation_records": completed,
        "incoming_generation_records": incoming,
        "container_label_records": containers,
        "embedded_locator_records": embedded,
        "note": "Container labels are locators, not inferred completed-RL identifiers.",
    }


def query_results(root: Path, query: str, limit: int = 20) -> dict:
    if not query.strip():
        raise CatalogError("result query must not be empty")
    if limit < 1:
        raise CatalogError("result limit must be positive")
    needle = normalise_query(query)
    if not needle:
        raise CatalogError("result query must contain a letter or number")
    matches = []
    for record in iter_jsonl(root / "knowledge" / "result_catalog.jsonl", RESULT_FORMAT):
        identity_values = [record.get("name") or "", *(record.get("aliases") or [])]
        fields = [record.get("name") or "", record.get("recorded_text") or "", *(record.get("aliases") or [])]
        haystack = normalise_query(" ".join(fields))
        if needle in haystack:
            exact = needle in {normalise_query(value) for value in identity_values}
            matches.append((record, exact, normalise_query(record.get("name") or "")))
    exact_records = [record for record, exact, _ in matches if exact]
    nonexact_records = [record for record, exact, _ in matches if not exact]
    corrections = [
        record for record, _, _ in matches if record["is_correction_or_demotion_record"]
    ]
    ordered = exact_records + nonexact_records
    grouped: dict[str, list[dict]] = {}
    for item, _, key in matches:
        if key:
            grouped.setdefault(key, []).append(item)
    conflicts = []
    for name, items in sorted(grouped.items()):
        classifications = sorted({
            item["recorded_classification"] for item in items if item["recorded_classification"]
        })
        if len(classifications) > 1:
            conflicts.append({
                "normalised_name": name,
                "recorded_classifications": classifications,
                "source_pointers": [
                    "%s:%d" % (item["source_path"], item["source_line_start"]) for item in items
                ],
            })
    return {
        "query": query,
        "match_count": len(matches),
        "matches": ordered[:limit],
        "correction_or_demotion_matches": corrections[:limit],
        "recorded_classification_conflicts": conflicts,
        "review_marker": "REQUIRES_FUTURE_MATHEMATICAL_REVIEW" if conflicts else None,
        "preferred_full_provenance_source": ordered[0]["source_path"] if ordered else None,
        "truncated": len(matches) > limit,
        "status_policy": "Recorded classifications are verbatim locators. Conflicts are returned, never adjudicated.",
    }
