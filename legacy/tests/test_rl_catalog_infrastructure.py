import json
import subprocess
import sys
import unittest
from pathlib import Path
from tempfile import TemporaryDirectory
from unittest.mock import patch


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))

import rl_catalog  # noqa: E402


class CatalogueInfrastructureTests(unittest.TestCase):
    def setUp(self):
        temporary = TemporaryDirectory()
        self.addCleanup(temporary.cleanup)
        self.root = Path(temporary.name)

    def write(self, relative, content):
        path = self.root / relative
        path.parent.mkdir(parents=True, exist_ok=True)
        if isinstance(content, bytes):
            path.write_bytes(content)
        else:
            path.write_text(content, encoding="utf-8")
        return path

    @staticmethod
    def rendered():
        return {
            "session_catalog.jsonl": b"session\n",
            "result_catalog.jsonl": b"result\n",
            "index_metadata.json": b"{}\n",
        }

    def test_index_publication_is_metadata_last_and_second_build_is_noop(self):
        with patch.object(rl_catalog, "build_index_bytes", return_value=self.rendered()):
            calls = []
            original = rl_catalog._atomic_write

            def recording(path, content):
                calls.append(path.name)
                return original(path, content)

            with patch.object(rl_catalog, "_atomic_write", side_effect=recording):
                rl_catalog.write_indexes(self.root)
            self.assertEqual(
                calls,
                ["session_catalog.jsonl", "result_catalog.jsonl", "index_metadata.json"],
            )
            mtimes = {
                name: (self.root / "knowledge" / name).stat().st_mtime_ns
                for name in self.rendered()
            }
            with patch.object(rl_catalog, "_atomic_write") as atomic:
                rl_catalog.write_indexes(self.root)
            atomic.assert_not_called()
            self.assertEqual(
                mtimes,
                {
                    name: (self.root / "knowledge" / name).stat().st_mtime_ns
                    for name in self.rendered()
                },
            )

    def test_failed_atomic_replace_does_not_truncate_existing_file(self):
        path = self.write("knowledge/index_metadata.json", b"old\n")
        with patch.object(rl_catalog.os, "replace", side_effect=OSError("fixture failure")):
            with self.assertRaises(rl_catalog.CatalogError):
                rl_catalog._atomic_write(path, b"new\n")
        self.assertEqual(path.read_bytes(), b"old\n")
        self.assertFalse(list(path.parent.glob(".index_metadata.json.*.tmp")))

    def test_build_context_detects_input_change(self):
        path = self.write("sessions/RL1/input.md", "one\n")
        context = rl_catalog._BuildContext(self.root)
        self.assertEqual(context.read_bytes(path), b"one\n")
        path.write_text("changed and longer\n", encoding="utf-8")
        with self.assertRaises(rl_catalog.CatalogError):
            context.assert_unchanged()

    def test_reference_traversal_is_ignored_without_lstrip_rewrite(self):
        entrypoint = self.write(
            "sessions/RL1/START_HERE.md",
            "`./inside.md`\n`../outside.md`\n`./../outside.md`\n",
        )
        inside = self.write("sessions/RL1/inside.md", "inside\n")
        self.write("sessions/outside.md", "outside\n")
        self.assertEqual(rl_catalog._extract_references(self.root, [entrypoint]), [inside.resolve()])

    def test_staged_tree_check_rejects_missing_and_unstaged_inputs(self):
        for relative in (
            "START_HERE.md",
            "sessions/RL1/input.md",
            "authoritative/input.md",
            "knowledge/session_catalog.jsonl",
            "knowledge/result_catalog.jsonl",
            "knowledge/index_metadata.json",
        ):
            self.write(relative, "fixture\n")
        subprocess.run(["git", "init", "-q"], cwd=self.root, check=True)
        subprocess.run(["git", "add", "."], cwd=self.root, check=True)
        inputs = ("sessions/RL1/input.md", "authoritative/input.md")
        self.assertEqual(rl_catalog._staged_tree_issues(self.root, inputs), [])
        (self.root / "sessions/RL1/input.md").write_text("unstaged\n", encoding="utf-8")
        issues = rl_catalog._staged_tree_issues(self.root, inputs)
        self.assertTrue(any("differ between index and worktree" in item["reason"] for item in issues))
        missing = self.write("sessions/RL1/new.md", "new\n")
        self.assertTrue(missing.is_file())
        issues = rl_catalog._staged_tree_issues(self.root, inputs + ("sessions/RL1/new.md",))
        self.assertTrue(any("not staged/tracked" in item["reason"] for item in issues))

    def test_result_query_streams_valid_objects_and_rejects_non_objects(self):
        path = self.root / "knowledge/result_catalog.jsonl"
        path.parent.mkdir(parents=True)
        records = [
            {
                "format": rl_catalog.RESULT_FORMAT,
                "name": "Alpha",
                "aliases": ["A"],
                "recorded_text": "Alpha result",
                "is_correction_or_demotion_record": False,
                "recorded_classification": "fixture",
                "source_path": "sessions/RL1/a.md",
                "source_line_start": 1,
            },
            {
                "format": rl_catalog.RESULT_FORMAT,
                "name": "Beta",
                "aliases": [],
                "recorded_text": "mentions Alpha",
                "is_correction_or_demotion_record": True,
                "recorded_classification": "fixture correction",
                "source_path": "sessions/RL1/b.md",
                "source_line_start": 2,
            },
        ]
        path.write_text("".join(json.dumps(item) + "\n" for item in records), encoding="utf-8")
        result = rl_catalog.query_results(self.root, "Alpha", 10)
        self.assertEqual(result["match_count"], 2)
        self.assertEqual(result["matches"][0]["name"], "Alpha")
        path.write_text("[]\n", encoding="utf-8")
        with self.assertRaises(rl_catalog.CatalogError):
            list(rl_catalog.iter_jsonl(path, rl_catalog.RESULT_FORMAT))


if __name__ == "__main__":
    unittest.main()
