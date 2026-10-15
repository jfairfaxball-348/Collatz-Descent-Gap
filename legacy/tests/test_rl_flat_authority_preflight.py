import hashlib
import sys
import unittest
from pathlib import Path
from tempfile import TemporaryDirectory
from unittest.mock import patch


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))

import rl_flat_authority_preflight as preflight  # noqa: E402


class FlatAuthorityLayoutTests(unittest.TestCase):
    def setUp(self):
        self.temporary = TemporaryDirectory()
        self.addCleanup(self.temporary.cleanup)
        self.root = Path(self.temporary.name)
        self.auth = self.root / "authoritative"
        self.auth.mkdir()
        root_patch = patch.object(preflight, "ROOT", self.root)
        auth_patch = patch.object(preflight, "AUTH", self.auth)
        root_patch.start()
        auth_patch.start()
        self.addCleanup(root_patch.stop)
        self.addCleanup(auth_patch.stop)
        self.write(
            "authoritative/START_HERE.md",
            "# Authoritative start\n\n"
            "RL338 is CLOSED AND FROZEN. RL339 is the unique incoming research session.\n"
            "Unique live target: `RL339_PARENT_BRIDGE_Q35_CLOSURE_TARGET.md`.\n"
            "- `python3 -I verification/verify_rl338_q35_fast.py`\n"
            "- `python3 -I verification/red_team_rl338_q35.py`\n",
        )
        self.write("authoritative/RL339_PARENT_BRIDGE_Q35_CLOSURE_TARGET.md", "target\n")
        self.write("authoritative/RL337_OLD_TARGET.md", "provenance\n")
        self.write("authoritative/RL338_SESSION_STATE_AND_RL339_KICKOFF.md", "kickoff\n")
        self.write("authoritative/RL338_CLOSEOUT_VERIFICATION.md", "verified\n")
        self.write("authoritative/verification/verify_rl338_q35_fast.py", "print('ok')\n")
        self.write("authoritative/verification/red_team_rl338_q35.py", "print('ok')\n")
        (self.root / "sessions" / "RL338").mkdir(parents=True)

    def write(self, relative, content):
        path = self.root / relative
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(content, encoding="utf-8")
        return path

    def historical_package(self, rl=336, valid=True):
        name = "RL%d_HANDOVER_BUNDLE.zip" % rl
        bundle = self.auth / name
        bundle.write_bytes(b"historical package fixture")
        checksum = hashlib.sha256(bundle.read_bytes()).hexdigest()
        if not valid:
            checksum = "0" * 64
        self.write("authoritative/" + name + ".sha256", checksum + "  " + name + "\n")
        return bundle

    def test_flat_handover_with_historical_files(self):
        self.historical_package()
        current_rl, target, commands = preflight.parse_start_here()
        self.assertEqual(current_rl, 339)
        self.assertEqual(target.name, "RL339_PARENT_BRIDGE_Q35_CLOSURE_TARGET.md")
        self.assertEqual(len(preflight.declared_verifier_commands(commands)), 2)
        preflight.require_flat_transport(current_rl)

    def test_current_package_is_not_flat_transport(self):
        self.historical_package(338)
        with self.assertRaisesRegex(preflight.Failure, "current or unrecognized"):
            preflight.require_flat_transport(339)

    def test_historical_checksum_failure_is_not_bypassed(self):
        self.historical_package(valid=False)
        with self.assertRaisesRegex(preflight.Failure, "checksum mismatch"):
            preflight.require_flat_transport(339)

    def test_unpaired_historical_bundle_is_rejected(self):
        self.historical_package().with_suffix(".zip.sha256").unlink()
        with self.assertRaisesRegex(preflight.Failure, "pair is incomplete"):
            preflight.require_flat_transport(339)

    def test_second_current_target_is_rejected(self):
        self.write("authoritative/RL339_OTHER_TARGET.md", "ambiguous\n")
        with self.assertRaisesRegex(preflight.Failure, "ambiguous current"):
            preflight.parse_start_here()

    def test_conflicting_incoming_declarations_are_rejected(self):
        path = self.auth / "START_HERE.md"
        path.write_text("# RL340 authoritative start\n" + path.read_text(encoding="utf-8"))
        with self.assertRaisesRegex(preflight.Failure, "unambiguously declare"):
            preflight.parse_start_here()


if __name__ == "__main__":
    unittest.main()
