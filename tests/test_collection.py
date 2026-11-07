"""Validate repository contracts, not unexecuted model behavior."""

import ast
import importlib.util
import json
from pathlib import Path
import re
import tempfile
import unittest
from unittest.mock import patch


ROOT = Path(__file__).resolve().parents[1]
SKILLS = sorted((ROOT / "codex/skills").glob("*/SKILL.md"))
SPEC = importlib.util.spec_from_file_location(
    "sync_skills", ROOT / "scripts/sync_skills.py",
)
SYNC = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(SYNC)


def metadata(path):
    text = path.read_text()
    if not text.startswith("---\n"):
        raise ValueError(f"Missing frontmatter: {path}")
    header = text.split("---", 2)[1]
    name = re.search(r"^name: ([a-z0-9_-]+)$", header, re.MULTILINE)
    description = re.search(r"^description: (.+)$", header, re.MULTILINE)
    if not name or not description:
        raise ValueError(f"Missing name/description: {path}")
    value = description.group(1)
    if value.startswith('"'):
        # Repository descriptions use JSON-compatible double-quoted scalars.
        value = json.loads(value)
    return name.group(1), value


class CollectionTests(unittest.TestCase):
    def test_skill_names_descriptions_and_interface_metadata(self):
        names = []
        for path in SKILLS:
            with self.subTest(skill=path.parent.name):
                name, description = metadata(path)
                self.assertEqual(name, path.parent.name)
                self.assertTrue(description.strip())
                self.assertLessEqual(len(description.split()), 85)
                names.append(name)
                interface = path.parent / "agents/openai.yaml"
                self.assertTrue(interface.is_file())
                self.assertIn(f"${name}", interface.read_text())
        self.assertEqual(len(names), len(set(names)))

    def test_skill_reference_links_are_portable(self):
        for path in SKILLS:
            links = re.findall(
                r"\]\((references/[^)#]+)(?:#[^)]*)?\)", path.read_text(),
            )
            for link in links:
                with self.subTest(skill=path.parent.name, link=link):
                    self.assertTrue((path.parent / link).is_file())

    def test_evaluation_shapes_and_local_inputs(self):
        definitions = list((ROOT / "codex/skills").glob("*/evals/evals.json"))
        for path in definitions:
            with self.subTest(path=path.relative_to(ROOT)):
                data = json.loads(path.read_text())
                self.assertEqual(data["skill_name"], path.parents[1].name)
                self.assertTrue(data["evals"])
                ids = set()
                for case in data["evals"]:
                    self.assertNotIn(case["id"], ids)
                    ids.add(case["id"])
                    self.assertTrue(case["prompt"].strip())
                    self.assertTrue(case["expected_output"].strip())
                    self.assertTrue(case.get("assertions"))
                    for file in case.get("files", []):
                        self.assertTrue((path.parents[1] / file).is_file())

    def test_trigger_definitions_include_near_misses(self):
        definitions = list(
            (ROOT / "codex/skills").glob("*/evals/triggers.json"),
        )
        self.assertTrue(definitions)
        for path in definitions:
            with self.subTest(path=path.relative_to(ROOT)):
                cases = json.loads(path.read_text())
                self.assertIsInstance(cases, list)
                self.assertEqual(
                    {case["should_trigger"] for case in cases}, {True, False},
                )
                for case in cases:
                    self.assertIsInstance(case["should_trigger"], bool)
                    self.assertTrue(case["query"].strip())

    def test_architecture_resources_match_canonical_source(self):
        self.assertEqual(SYNC.synchronize(check=True), [])

    def test_sync_detects_and_repairs_drift_without_touching_metadata(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary).resolve()
            source, dest = root / "source", root / "dest"
            source.mkdir()
            (dest / "agents").mkdir(parents=True)
            (source / "SKILL.md").write_text("canonical")
            (dest / "SKILL.md").write_text("stale")
            (dest / "removed.txt").write_text("old generated resource")
            interface = dest / "agents/openai.yaml"
            interface.write_text("preserve interface")
            with patch.object(SYNC, "SOURCE", source), patch.object(
                SYNC, "DESTINATION", dest,
            ):
                self.assertEqual(
                    SYNC.synchronize(check=True), ["SKILL.md", "removed.txt"],
                )
                self.assertEqual((dest / "SKILL.md").read_text(), "stale")
                SYNC.synchronize()
                self.assertEqual(SYNC.synchronize(check=True), [])
                self.assertEqual(interface.read_text(), "preserve interface")

    def test_sync_refuses_foreign_file_and_directory_links(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary).resolve()
            source, dest = root / "source", root / "dest"
            source.mkdir()
            dest.mkdir()
            (source / "SKILL.md").write_text("canonical")
            foreign = root / "foreign"
            foreign.write_text("keep this unrelated file")
            (dest / "SKILL.md").symlink_to(foreign)
            with patch.object(SYNC, "SOURCE", source), patch.object(
                SYNC, "DESTINATION", dest,
            ):
                with self.assertRaisesRegex(ValueError, "linked"):
                    SYNC.synchronize()
                self.assertEqual(foreign.read_text(), "keep this unrelated file")
                (dest / "SKILL.md").unlink()
                (dest / "references").symlink_to(
                    source, target_is_directory=True,
                )
                with self.assertRaisesRegex(ValueError, "linked"):
                    SYNC.synchronize()
                self.assertFalse((dest / "SKILL.md").exists())

    def test_python_helpers_parse(self):
        for directory in (ROOT / "scripts", ROOT / "tests"):
            for path in directory.glob("*.py"):
                with self.subTest(file=path.name):
                    ast.parse(path.read_text(), filename=str(path))


if __name__ == "__main__":
    unittest.main()
