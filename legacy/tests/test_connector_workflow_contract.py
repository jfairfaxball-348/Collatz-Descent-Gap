import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


class ConnectorWorkflowContractTests(unittest.TestCase):
    def test_binding_contract_requires_bounded_resumable_continue(self):
        text = (ROOT / "AGENTS.md").read_text(encoding="utf-8")
        self.assertIn("bounded continuation work unit", text)
        self.assertIn("reuse the validated incoming authority", text)
        self.assertIn("Do not reread inherited ledgers", text)
        self.assertIn("reuse already-created immutable Git objects", text)

    def test_connector_workflow_preserves_atomicity_and_exact_resume(self):
        text = (ROOT / "docs" / "CONNECTOR_WORKFLOW.md").read_text(encoding="utf-8")
        required = [
            '"format": "rl-connector-resume-v1"',
            '"format": "rl-connector-closeout-v1"',
            "next_exact_operation",
            "do_not_recompute",
            "final live-HEAD comparison",
            "Git blobs, trees, and commits are immutable",
            "complete verified transition or no numbered transition exists",
        ]
        for marker in required:
            with self.subTest(marker=marker):
                self.assertIn(marker, text)

    def test_connector_fast_path_excludes_large_cold_surfaces(self):
        text = (ROOT / "START_HERE.md").read_text(encoding="utf-8")
        self.assertIn("Connector fast path", text)
        self.assertIn("Do not preload `sessions/`, `Archive/`, the generated catalogue JSONL files", text)
        self.assertIn("without rerunning startup", text)


if __name__ == "__main__":
    unittest.main()
