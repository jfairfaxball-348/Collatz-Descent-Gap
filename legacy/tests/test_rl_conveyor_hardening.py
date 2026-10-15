import base64
import hashlib
import json
import subprocess
import sys
import unittest
import zipfile
from contextlib import contextmanager
from pathlib import Path
from tempfile import TemporaryDirectory
from types import SimpleNamespace
from unittest.mock import patch


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))

import rl_conveyor  # noqa: E402


class AuthorityFixture:
    def __init__(self, transport):
        self.temporary = TemporaryDirectory()
        self.root = Path(self.temporary.name)
        self.auth = self.root / "authoritative"
        self.package = self.auth / "RL1_Fixture"
        self.transport = transport
        self.canonical_name = "RL1_Fixture.zip"
        self._write_package()
        self._write_transport()
        self._git("init", "-q")
        self._git("config", "user.email", "fixture@example.com")
        self._git("config", "user.name", "Fixture")
        self._git("add", ".")
        self._git("commit", "-qm", "fixture package")
        if transport == "direct":
            tree = self._git("rev-parse", "HEAD:authoritative/RL1_Fixture").strip()
            self._write_direct_manifest(tree, version=2)
            self._git("add", ".")
            self._git("commit", "-qm", "fixture transport")

    def cleanup(self):
        self.temporary.cleanup()

    def _git(self, *args):
        return subprocess.run(
            ["git", *args], cwd=self.root, check=True, text=True,
            capture_output=True,
        ).stdout

    def _write(self, relative, content):
        path = self.root / relative
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(content, encoding="utf-8")
        return path

    def _write_package(self):
        self._write("authoritative/START_HERE.md", "`RL1_Fixture/`\n`RL1_Fixture/RL2_TARGET.md`\n")
        self._write("authoritative/RL1_Fixture/README.md", "# Fixture\n")
        self._write("authoritative/RL1_Fixture/RL2_TARGET.md", "# RL2 target\n")
        self._write(
            "authoritative/RL1_Fixture/RL1_SESSION_STATE_AND_RL2_KICKOFF.md",
            "# Handover\n",
        )
        self._write(
            "authoritative/RL1_Fixture/RL1_CERTIFIED_FACTS_AND_PROOF_LEDGER.md",
            "# Ledger\n",
        )
        self._write(
            "authoritative/RL1_Fixture/RL1_CORRECTION_DEMOTION_LEDGER.md",
            "# Corrections\n",
        )
        self._write(
            "authoritative/RL1_Fixture/RL1_RED_TEAM_REPORT.md",
            "# Red team\n",
        )
        self._write(
            "authoritative/RL1_Fixture/verification/verify_fixture.py",
            "print('fixture verifier: PASS')\n",
        )
        self._write(
            "authoritative/RL1_Fixture/reconstruct_rl1_bundle.py",
            "from pathlib import Path\n"
            "import zipfile\n"
            "root = Path(__file__).resolve().parent\n"
            "out = root.parent / (root.name + '.zip')\n"
            "with zipfile.ZipFile(out, 'w', compression=zipfile.ZIP_STORED) as archive:\n"
            "    for path in sorted(root.rglob('*')):\n"
            "        if path.is_file():\n"
            "            info = zipfile.ZipInfo(path.relative_to(root).as_posix(), (2020, 1, 1, 0, 0, 0))\n"
            "            info.external_attr = (0o100644 & 0xFFFF) << 16\n"
            "            archive.writestr(info, path.read_bytes())\n",
        )
        records = []
        for path in sorted(self.package.rglob("*")):
            if path.is_file():
                relative = path.relative_to(self.package).as_posix()
                records.append("%s  ./%s" % (hashlib.sha256(path.read_bytes()).hexdigest(), relative))
        self._write("authoritative/RL1_Fixture/SHA256SUMS.txt", "\n".join(records) + "\n")
        subprocess.run(
            [sys.executable, str(self.package / "reconstruct_rl1_bundle.py")],
            cwd=self.package, check=True, capture_output=True,
        )
        bundle = self.auth / self.canonical_name
        self.bundle_bytes = bundle.read_bytes()
        self.bundle_hash = hashlib.sha256(self.bundle_bytes).hexdigest()
        bundle.unlink()
        self._write(
            "authoritative/%s.sha256" % self.canonical_name,
            "%s  %s\n" % (self.bundle_hash, self.canonical_name),
        )

    def _write_transport(self):
        if self.transport == "physical":
            (self.auth / self.canonical_name).write_bytes(self.bundle_bytes)
        elif self.transport == "base64":
            directory = self.auth / "RL2_BUNDLE_TRANSPORT"
            directory.mkdir()
            encoded = base64.b64encode(self.bundle_bytes).decode("ascii")
            midpoint = len(encoded) // 2
            parts = [("part-001.b64", encoded[:midpoint]), ("part-002.b64", encoded[midpoint:])]
            checksums = []
            for name, value in parts:
                path = directory / name
                path.write_text(value + "\n", encoding="utf-8")
                checksums.append("%s  %s" % (hashlib.sha256(path.read_bytes()).hexdigest(), name))
            (directory / "PART_SHA256SUMS.txt").write_text("\n".join(checksums) + "\n", encoding="utf-8")
        elif self.transport == "direct":
            (self.auth / "RL2_BUNDLE_TRANSPORT").mkdir()
        else:
            raise ValueError(transport)

    def _write_direct_manifest(self, tree, version=2):
        if version == 1:
            value = {
                "canonical_zip": self.canonical_name,
                "canonical_zip_sha256": self.bundle_hash,
                "completed_package_tree_sha": tree,
                "completed_rl": 1,
                "incoming_rl": 2,
                "incoming_rl_started": False,
                "reconstruction_script": "reconstruct_rl1_bundle.py",
                "transport": "direct Git tree plus deterministic ZIP reconstruction",
            }
        else:
            value = {
                "canonical_zip": self.canonical_name,
                "canonical_zip_sha256": self.bundle_hash,
                "completed_package_tree": tree,
                "completed_rl": 1,
                "incoming_rl": 2,
                "incoming_status": "NOT STARTED",
                "transport": "lossless_git_tree_plus_deterministic_reconstruction",
            }
        path = self.auth / "RL2_BUNDLE_TRANSPORT" / "TRANSPORT_MANIFEST.json"
        path.write_text(json.dumps(value, indent=2, sort_keys=True) + "\n", encoding="utf-8")
        return path

    @contextmanager
    def active(self):
        with patch.object(rl_conveyor, "ROOT", self.root), patch.object(
            rl_conveyor, "AUTH", self.auth
        ):
            yield


class TransportHardeningTests(unittest.TestCase):
    def fixture(self, transport):
        value = AuthorityFixture(transport)
        self.addCleanup(value.cleanup)
        return value

    def test_all_supported_transport_kinds_verify(self):
        for kind in ("physical", "base64", "direct"):
            with self.subTest(kind=kind):
                fixture = self.fixture(kind)
                with fixture.active():
                    self.assertEqual(rl_conveyor._authority_state()["transport_kind"], {
                        "physical": "physical_zip",
                        "base64": "base64_parts",
                        "direct": "direct_git_tree",
                    }[kind])
                    rl_conveyor.verify_incoming()

    def test_legacy_direct_manifest_schema_remains_supported(self):
        fixture = self.fixture("direct")
        tree = fixture._git("rev-parse", "HEAD:authoritative/RL1_Fixture").strip()
        fixture._write_direct_manifest(tree, version=1)
        with fixture.active():
            rl_conveyor.verify_incoming()

    def test_direct_manifest_mismatches_fail_closed(self):
        mutations = {
            "wrong tree": lambda value: value.__setitem__("completed_package_tree", "0" * 40),
            "wrong hash": lambda value: value.__setitem__("canonical_zip_sha256", "0" * 64),
            "wrong incoming": lambda value: value.__setitem__("incoming_rl", 3),
            "started": lambda value: value.__setitem__("incoming_status", "STARTED"),
            "extra field": lambda value: value.__setitem__("unexpected", True),
        }
        for label, mutate in mutations.items():
            with self.subTest(label=label):
                fixture = self.fixture("direct")
                path = fixture.auth / "RL2_BUNDLE_TRANSPORT" / "TRANSPORT_MANIFEST.json"
                value = json.loads(path.read_text(encoding="utf-8"))
                mutate(value)
                path.write_text(json.dumps(value), encoding="utf-8")
                with fixture.active(), self.assertRaises(rl_conveyor.Failure):
                    rl_conveyor.verify_incoming()

    def test_missing_reconstruction_script_fails_closed(self):
        fixture = self.fixture("direct")
        (fixture.package / "reconstruct_rl1_bundle.py").unlink()
        with fixture.active(), self.assertRaises(rl_conveyor.Failure):
            rl_conveyor.verify_incoming()

    def test_reconstruction_failure_and_timeout_fail_closed(self):
        for mode in ("failure", "timeout"):
            with self.subTest(mode=mode):
                fixture = self.fixture("direct")
                original = subprocess.run

                def intercepted(args, *positional, **keywords):
                    if args[:2] == [sys.executable, "-I"]:
                        if mode == "timeout":
                            raise subprocess.TimeoutExpired(args, keywords.get("timeout", 0))
                        return SimpleNamespace(returncode=2, stdout="", stderr="fixture failure")
                    return original(args, *positional, **keywords)

                with fixture.active(), patch.object(rl_conveyor.subprocess, "run", side_effect=intercepted):
                    with self.assertRaises(rl_conveyor.Failure):
                        rl_conveyor.verify_incoming()

    def test_corrupt_and_colliding_zip_members_fail_closed(self):
        fixture = self.fixture("physical")
        bundle = fixture.auth / fixture.canonical_name
        for label, writer in (
            ("corrupt", lambda path: path.write_bytes(b"not a zip")),
            ("case collision", self._write_colliding_zip),
        ):
            with self.subTest(label=label):
                writer(bundle)
                checksum = hashlib.sha256(bundle.read_bytes()).hexdigest()
                (fixture.auth / (fixture.canonical_name + ".sha256")).write_text(
                    "%s  %s\n" % (checksum, fixture.canonical_name), encoding="utf-8"
                )
                with fixture.active(), self.assertRaises(rl_conveyor.Failure):
                    rl_conveyor.verify_incoming()

    @staticmethod
    def _write_colliding_zip(path):
        with zipfile.ZipFile(path, "w") as archive:
            archive.writestr("A", b"one")
            archive.writestr("a", b"two")

    def test_manifest_traversal_is_rejected_without_normalisation(self):
        for value in ("../escape", "./../escape", "/absolute", "C:/absolute", "a\\b"):
            with self.subTest(value=value), self.assertRaises(rl_conveyor.Failure):
                rl_conveyor.safe_manifest_path(value)


class RepositoryIdentityAndSnapshotTests(unittest.TestCase):
    def fixture(self):
        value = AuthorityFixture("physical")
        self.addCleanup(value.cleanup)
        return value

    def test_remote_default_branch_identity_is_reported(self):
        responses = {
            ("rev-parse", "HEAD"): "a" * 40 + "\n",
            ("symbolic-ref", "--quiet", "--short", "HEAD"): "main\n",
            ("config", "--get", "branch.main.remote"): "origin\n",
            ("ls-remote", "--symref", "origin", "HEAD"): (
                "ref: refs/heads/main\tHEAD\n" + "b" * 40 + "\tHEAD\n"
            ),
        }

        def fake_git(*args, **_):
            return responses[args]

        with patch.object(rl_conveyor, "git", side_effect=fake_git):
            identity = rl_conveyor._remote_identity()
        self.assertEqual(identity["base_ref"], "refs/heads/main")
        self.assertEqual(identity["base_head"], "b" * 40)
        self.assertFalse(identity["head_matches_base"])

    def test_snapshot_includes_untracked_authoritative_files_and_detects_change(self):
        fixture = self.fixture()
        head = fixture._git("rev-parse", "HEAD").strip()
        identity = {
            "base_remote": "origin",
            "base_ref": "refs/heads/main",
            "base_head": head,
            "base_head_live": True,
            "local_head": head,
            "head_matches_base": True,
        }
        untracked = fixture.auth / "local-note.txt"
        untracked.write_text("one\n", encoding="utf-8")
        with fixture.active(), patch.object(rl_conveyor, "_remote_identity", return_value=identity):
            first = rl_conveyor.snapshot()
            record = next(item for item in first["entries"] if item["path"].endswith("local-note.txt"))
            self.assertFalse(record["tracked"])
            untracked.write_text("two\n", encoding="utf-8")
            self.assertNotEqual(first, rl_conveyor.snapshot())

    def test_snapshot_refuses_remote_advancement(self):
        fixture = self.fixture()
        head = fixture._git("rev-parse", "HEAD").strip()
        identity = {
            "base_remote": "origin",
            "base_ref": "refs/heads/main",
            "base_head": "f" * 40,
            "base_head_live": True,
            "local_head": head,
            "head_matches_base": False,
        }
        with fixture.active(), patch.object(rl_conveyor, "_remote_identity", return_value=identity):
            with self.assertRaises(rl_conveyor.Failure):
                rl_conveyor.snapshot()

    def test_snapshot_detects_worktree_mode_change(self):
        fixture = self.fixture()
        head = fixture._git("rev-parse", "HEAD").strip()
        identity = {
            "base_remote": "origin",
            "base_ref": "refs/heads/main",
            "base_head": head,
            "base_head_live": True,
            "local_head": head,
            "head_matches_base": True,
        }
        target = fixture.package / "RL2_TARGET.md"
        with fixture.active(), patch.object(rl_conveyor, "_remote_identity", return_value=identity):
            before = rl_conveyor.snapshot()
            target.chmod(0o755)
            after = rl_conveyor.snapshot()
        self.assertNotEqual(before, after)
        changed = next(item for item in after["entries"] if item["path"].endswith("RL2_TARGET.md"))
        self.assertEqual(changed["worktree_mode"], "100755")


if __name__ == "__main__":
    unittest.main()
