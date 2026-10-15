import hashlib
import json
import re
import sys
import unittest
from pathlib import Path
from tempfile import TemporaryDirectory
from types import SimpleNamespace
from unittest.mock import patch


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))

import rl_catalog  # noqa: E402
import rl_conveyor  # noqa: E402
import rl_flat_authority_preflight as flat_preflight  # noqa: E402


class ConveyorKnowledgeIntegrationTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.sessions = rl_catalog.load_jsonl(
            ROOT / "knowledge" / "session_catalog.jsonl", rl_catalog.SESSION_FORMAT
        )
        cls.results = rl_catalog.load_jsonl(
            ROOT / "knowledge" / "result_catalog.jsonl", rl_catalog.RESULT_FORMAT
        )
        cls.catalogue_validation = rl_catalog.validate_indexes(ROOT)
        cls.catalogue_current = cls.catalogue_validation["current"]

    def test_current_rl_comes_from_unique_target(self):
        target_number, target, _ = flat_preflight.parse_start_here()
        targets = [
            path for path in (ROOT / "authoritative").rglob("*TARGET*.md")
            if re.match(r"RL0*%d(?:_|\b)" % target_number, path.name, re.I)
        ]
        self.assertEqual(targets, [target])
        handover_pairs = {
            (int(match.group(1)), int(match.group(2)))
            for path in (ROOT / "authoritative").rglob("*.md")
            for match in [re.search(r"RL(\d+)_SESSION_STATE_AND_RL(\d+)_KICKOFF", path.name, re.I)]
            if match and int(match.group(2)) == target_number
        }
        self.assertEqual(len(handover_pairs), 1)
        completed, incoming = handover_pairs.pop()
        self.assertEqual(target_number, incoming)
        self.assertEqual(incoming, completed + 1)

    def test_every_catalogued_session_container_exists(self):
        physical = {path.as_posix() for path in (ROOT / "sessions").glob("RL*") if path.is_dir()}
        physical = {str(Path("sessions") / Path(path).name) for path in physical}
        indexed = {record["container_path"] for record in self.sessions}
        self.assertTrue(indexed.issubset(physical))
        if self.catalogue_current:
            self.assertEqual(physical, indexed)
        else:
            self.assertTrue(physical - indexed)

    def test_catalogue_ids_and_source_pointers_are_valid_for_cache_generation(self):
        self.assertEqual(len(self.sessions), len({record["generation_id"] for record in self.sessions}))
        self.assertEqual(len(self.results), len({record["record_id"] for record in self.results}))
        for record in self.sessions:
            for key, values in record.items():
                if key.endswith("_paths") or key in {"generation_paths", "certificate_roots"}:
                    for value in values:
                        self.assertTrue((ROOT / value).exists(), (record["generation_id"], key, value))
        for record in self.results:
            path = ROOT / record["source_path"]
            if not path.is_file():
                self.assertFalse(self.catalogue_current, record["source_path"])
                self.assertEqual(record.get("source_scope"), "authoritative", record["source_path"])
            self.assertGreaterEqual(record["source_line_start"], 1)
            self.assertGreaterEqual(record["source_line_end"], record["source_line_start"])

    def test_modern_container_label_is_not_completed_rl(self):
        result = rl_catalog.query_sessions(ROOT, 174)
        completed_paths = {
            record["container_path"] for record in result["completed_generation_records"]
        }
        self.assertIn("sessions/RL175", completed_paths)
        self.assertTrue(any(
            path.endswith("RL174_SESSION_STATE_AND_RL175_KICKOFF_2026-08-29.md")
            for record in result["completed_generation_records"]
            for path in record["session_state_handover_paths"]
        ))

    def test_duplicate_packaging_variants_remain_visible(self):
        result = rl_catalog.query_sessions(ROOT, 162)
        containers = {
            record["container_path"] for record in result["completed_generation_records"]
        }
        self.assertTrue({"sessions/RL162", "sessions/RL163"}.issubset(containers))

    def test_embedded_legacy_rl_has_locator_without_inferred_role(self):
        result = rl_catalog.query_sessions(ROOT, 3)
        self.assertTrue(result["embedded_locator_records"])
        self.assertTrue(all(
            record["completed_rl"] is None and record["incoming_rl"] is None
            for record in result["embedded_locator_records"]
        ))

    def test_named_historical_result_has_verbatim_classification_and_source(self):
        source = (
            "sessions/RL176/RL175_Corrected_P_Shift_Flow_Consumer_2026-08-29/"
            "RL175_CERTIFIED_FACTS_AND_PROOF_LEDGER.md"
        )
        result = rl_catalog.query_results(ROOT, "RL175.4", len(self.results))
        originals = [
            record for record in result["matches"]
            if record["source_path"] == source and record["name"] == "RL175.4"
        ]
        self.assertEqual(len(originals), 1)
        record = originals[0]
        self.assertEqual(record["source_scope"], "session")
        self.assertEqual(record["source_kind"], "proof_status_ledger")
        self.assertEqual((record["completed_rl"], record["incoming_rl"]), (175, 176))
        self.assertEqual(record["recorded_classification"], "New proved analytic mathematics")
        self.assertEqual(
            record["recorded_text"],
            "**RL175.4:** in the physical `h_p=0` branch, `R-Q>5/8`.",
        )
        self.assertEqual((record["source_line_start"], record["source_line_end"]), (10, 10))
        self.assertEqual(record["source_sha256"], hashlib.sha256((ROOT / source).read_bytes()).hexdigest())

    def test_explicit_correction_is_returned_without_adjudication(self):
        result = rl_catalog.query_results(ROOT, "physical-functional identification", 10)
        self.assertTrue(result["correction_or_demotion_matches"])
        self.assertIn("never adjudicated", result["status_policy"])

    def test_table_pipe_does_not_shift_verbatim_classification(self):
        result = rl_catalog.query_results(ROOT, "F4", 5)
        self.assertEqual(result["matches"][0]["recorded_classification"], "analytic")
        self.assertFalse(result["matches"][0]["is_correction_or_demotion_record"])

    def test_result_query_rejects_empty_normalised_input_and_limit(self):
        with self.assertRaises(rl_catalog.CatalogError):
            rl_catalog.query_results(ROOT, "---", 5)
        with self.assertRaises(rl_catalog.CatalogError):
            rl_catalog.query_results(ROOT, "F4", 0)

    def test_main_report_is_not_misclassified_as_correction_ledger(self):
        result = rl_catalog.query_sessions(ROOT, 174)
        records = result["completed_generation_records"]
        paths = [path for record in records for path in record["correction_demotion_ledger_paths"]]
        self.assertTrue(paths)
        self.assertTrue(all("LEDGER" in Path(path).name.upper() for path in paths))

    def test_root_start_here_is_timeless(self):
        text = (ROOT / "START_HERE.md").read_text(encoding="utf-8")
        self.assertIsNone(re.search(r"\bRL\d+\b", text))

    def test_flat_startup_identifies_current_checks_without_historical_target(self):
        current_rl, target, commands = flat_preflight.parse_start_here()
        self.assertTrue(target.name.startswith("RL%d_" % current_rl))
        self.assertEqual(target.parent, ROOT / "authoritative")
        scripts = flat_preflight.declared_verifier_commands(commands)
        self.assertTrue(any(path.name.startswith("verify_") for path in scripts))
        self.assertTrue(any(path.name.startswith("red_team_") for path in scripts))
        self.assertTrue(all(path.parent.name == "verification" for path in scripts))

    def test_checkpoint_initialization_refuses_dirty_repository(self):
        dirty_state = {"current_rl": 176, "working_tree_clean": False}
        with patch.object(rl_conveyor, "state", return_value=dirty_state):
            with self.assertRaises(rl_conveyor.Failure):
                rl_conveyor.cmd_checkpoint(SimpleNamespace(rl=None, target=None))

    def test_generated_index_status_matches_cache_policy(self):
        validation = self.catalogue_validation
        if validation["current"]:
            self.assertEqual(validation["mismatches"], [])
        else:
            self.assertTrue(validation["mismatches"])
            allowed = {
                "knowledge/session_catalog.jsonl",
                "knowledge/result_catalog.jsonl",
                "knowledge/index_metadata.json",
            }
            for mismatch in validation["mismatches"]:
                self.assertIn(mismatch["path"], allowed)
                self.assertIn(mismatch["reason"], {"stale or modified", "missing"})


class CatalogueExtractionRegressionTests(unittest.TestCase):
    def setUp(self):
        temporary = TemporaryDirectory()
        self.addCleanup(temporary.cleanup)
        self.root = Path(temporary.name)

    def write_fixture(self, relative, text):
        path = self.root / relative
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(text, encoding="utf-8")
        return path

    def parse_ledger(self, text):
        path = self.write_fixture("authoritative/FIXTURE_PROOF_LEDGER.md", text)
        source = {
            "source_path": path.relative_to(self.root).as_posix(),
            "source_kind": "proof_status_ledger",
            "source_scope": "authoritative",
        }
        return path, rl_catalog._parse_markdown_records(self.root, source)

    def assert_source_record(self, record, path, start, end, classification, text):
        self.assertEqual(record["source_path"], path.relative_to(self.root).as_posix())
        self.assertEqual((record["source_line_start"], record["source_line_end"]), (start, end))
        self.assertEqual(record["source_sha256"], hashlib.sha256(path.read_bytes()).hexdigest())
        self.assertEqual(record["recorded_classification"], classification)
        self.assertEqual(record["recorded_text"], text)

    def test_modern_paragraph_retains_inherited_heading_and_complete_source_span(self):
        path, records = self.parse_ledger(
            "# Fixture proof ledger\n\n"
            "## Inherited proved analytic mathematics\n\n"
            "**RL206-T1**, unchanged: the cyclic recurrence\n"
            "retains its inherited additive compatibility scope.\n"
            "It does not classify owned quotient residues.\n"
        )
        matches = [record for record in records if "RL206-T1" in record["aliases"]]
        self.assertEqual(len(matches), 1)
        record = matches[0]
        self.assert_source_record(
            record, path, 5, 7, "Inherited proved analytic mathematics",
            "**RL206-T1**, unchanged: the cyclic recurrence retains its inherited "
            "additive compatibility scope. It does not classify owned quotient residues.",
        )
        self.assertEqual(record["source_kind"], "proof_status_ledger")
        self.assertEqual(record["source_scope"], "authoritative")
        self.assertEqual(
            record["section_path"],
            ["Fixture proof ledger", "Inherited proved analytic mathematics"],
        )

    def test_no_new_results_and_not_promoted_prose_keep_literal_status(self):
        path, records = self.parse_ledger(
            "# Fixture proof ledger\n\n"
            "## New result and target status\n\n"
            "**No new RL207 theorem or exact finite certificate is promoted.** The target\n"
            "remains unfinished.\n\n"
            "## Unfinished status\n\n"
            "Both investigations are **NOT PROMOTED** and cannot support a theorem.\n"
            "Fresh proof and verification remain required.\n\n"
            "**Status:** NOT PROMOTED\n"
        )
        by_start = {record["source_line_start"]: record for record in records}
        self.assert_source_record(
            by_start[5], path, 5, 6, "New result and target status",
            "**No new RL207 theorem or exact finite certificate is promoted.** "
            "The target remains unfinished.",
        )
        self.assert_source_record(
            by_start[10], path, 10, 11, "Unfinished status",
            "Both investigations are **NOT PROMOTED** and cannot support a theorem. "
            "Fresh proof and verification remain required.",
        )
        self.assert_source_record(
            by_start[13], path, 13, 13, "NOT PROMOTED", "**Status:** NOT PROMOTED",
        )

    def test_fenced_examples_and_ordinary_reports_are_not_designated_results(self):
        for fence in ("```", "~~~"):
            with self.subTest(fence=fence):
                ledger = self.write_fixture(
                    "authoritative/FIXTURE_PROOF_LEDGER.md",
                    "# Fixture proof ledger\n\n"
                    "## Inherited proved analytic mathematics\n\n"
                    f"{fence}markdown\n"
                    "## New proved analytic mathematics\n"
                    "**RL999-EXAMPLE:** quoted template, not a status record.\n"
                    "**Status:** new theorem\n"
                    f"{fence}\n\n"
                    "**RL206-T1**, unchanged: the actual inherited entry.\n",
                )
                report = self.write_fixture(
                    "authoritative/ORDINARY_REPORT.md",
                    "# Ordinary report\n\n"
                    "## Proved analytic mathematics\n\n"
                    "**RL999-REPORT:** ordinary prose is not a designated ledger.\n",
                )
                with patch.object(rl_catalog, "_git_files", return_value=[ledger, report]):
                    records, sources = rl_catalog.build_result_catalog(self.root, [])
                self.assertEqual(
                    [source["source_path"] for source in sources],
                    [ledger.relative_to(self.root).as_posix()],
                )
                self.assertEqual(len(records), 1)
                self.assert_source_record(
                    records[0], ledger, 11, 11, "Inherited proved analytic mathematics",
                    "**RL206-T1**, unchanged: the actual inherited entry.",
                )
                self.assertFalse(any("RL999" in record["recorded_text"] for record in records))

    def test_flat_session_discovers_nested_checks_without_inactive_generation_pairs(self):
        prefix = "sessions/RL43"
        fixtures = {
            f"{prefix}/RL42_SESSION_STATE_AND_RL43_KICKOFF.md": "# Current handover\n",
            f"{prefix}/RL42_CERTIFIED_FACTS_AND_PROOF_LEDGER.md": "# Current proof ledger\n",
            f"{prefix}/verification/units/verify_fixture.py": "# Canonical nested verifier\n",
            f"{prefix}/certificates/exact/check.json": "{}\n",
            f"{prefix}/drafts/verify_draft.py": "# Not a canonical verifier\n",
            f"{prefix}/provenance/RL41_SESSION_STATE_AND_RL42_KICKOFF.md.txt": "# Inactive provenance\n",
            f"{prefix}/unfinished/RL40_SESSION_STATE_AND_RL41_KICKOFF.md": "# Unfinished checkpoint\n",
        }
        files = [self.write_fixture(relative, text) for relative, text in fixtures.items()]
        with patch.object(rl_catalog, "_git_files", return_value=files):
            records = rl_catalog.build_session_catalog(self.root)
        generations = [record for record in records if record["record_type"] == "generation"]
        self.assertEqual(len(generations), 1)
        record = generations[0]
        self.assertEqual((record["completed_rl"], record["incoming_rl"]), (42, 43))
        self.assertEqual(record["generation_paths"], [prefix])
        self.assertEqual(
            record["verifier_paths"], [f"{prefix}/verification/units/verify_fixture.py"],
        )
        self.assertEqual(
            record["certificate_roots"], [f"{prefix}/certificates", f"{prefix}/verification"],
        )
        self.assertEqual(
            record["session_state_handover_paths"],
            [f"{prefix}/RL42_SESSION_STATE_AND_RL43_KICKOFF.md"],
        )
        self.assertEqual(record["source_generation_identity"]["file_count"], 4)
        self.assertEqual(
            {item["source_path"] for item in record["relationship_evidence"]},
            {f"{prefix}/RL42_SESSION_STATE_AND_RL43_KICKOFF.md"},
        )

    def test_flat_root_does_not_absorb_an_explicit_sibling_generation(self):
        prefix = "sessions/RL43"
        relative_files = (
            f"{prefix}/RL42_SESSION_STATE_AND_RL43_KICKOFF.md",
            f"{prefix}/certificates/result.json",
            f"{prefix}/verification/RL39_SESSION_STATE_AND_RL40_KICKOFF.md",
            f"{prefix}/verification/verify_other_generation.py",
        )
        files = [self.write_fixture(relative, "fixture\n") for relative in relative_files]
        container = self.root / prefix
        selected = rl_catalog._files_for_roots(
            container, files, ["."], other_generation_roots={"verification"},
        )
        self.assertEqual(set(selected), set(files[:2]))
        self.assertEqual(
            set(rl_catalog._files_for_roots(container, files, ["verification"])),
            set(files[2:]),
        )


if __name__ == "__main__":
    unittest.main()
