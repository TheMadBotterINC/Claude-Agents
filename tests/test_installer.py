"""Test installation against a disposable repository and home directory."""

import json
import os
from pathlib import Path
import shutil
import subprocess
import tempfile
import unittest


ROOT = Path(__file__).resolve().parents[1]


class InstallerTests(unittest.TestCase):
    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory()
        self.addCleanup(self.temporary.cleanup)
        self.root = Path(self.temporary.name).resolve()
        self.repo = self.root / "repo"
        (self.repo / "scripts").mkdir(parents=True)
        shutil.copy2(ROOT / "install.sh", self.repo / "install.sh")
        shutil.copy2(
            ROOT / "scripts/install.py", self.repo / "scripts/install.py",
        )
        for directory, file in (
            ("reviewer", "reviewer.md"), ("shared", "audit-conventions.md"),
            ("skills/architecture", "SKILL.md"),
            ("codex/skills/security", "SKILL.md"),
        ):
            folder = self.repo / directory
            folder.mkdir(parents=True)
            (folder / file).write_text(f"fixture: {directory}\n")
        self.home = self.root / "home"
        self.codex = self.root / "custom-codex"
        self.dest = self.codex / "skills/security"
        self.env = {
            **os.environ,
            "HOME": str(self.home), "CODEX_HOME": str(self.codex),
        }

    def invoke(self, *args):
        return subprocess.run(
            ["bash", str(self.repo / "install.sh"), *args],
            env=self.env, capture_output=True, text=True, timeout=10,
        )

    def test_list_does_not_create_any_directories(self):
        proc = self.invoke("--list")
        self.assertEqual(proc.returncode, 0, proc.stderr)
        self.assertFalse(self.home.exists())
        self.assertFalse(self.codex.exists())

    def test_links_are_reinstallable_and_use_custom_codex_home(self):
        for _ in range(2):
            proc = self.invoke()
            self.assertEqual(proc.returncode, 0, proc.stderr)
        self.assertTrue(self.dest.is_symlink())
        self.assertEqual(
            self.dest.resolve(), self.repo / "codex/skills/security",
        )
        agent = self.home / ".claude/agents/reviewer.md"
        self.assertTrue(agent.is_symlink())

    def test_unmanaged_collision_aborts_before_any_writes(self):
        self.dest.mkdir(parents=True)
        original = self.dest / "mine.txt"
        original.write_text("my private skill")
        proc = self.invoke()
        self.assertEqual(proc.returncode, 1)
        self.assertIn("unmanaged", proc.stderr)
        self.assertEqual(original.read_text(), "my private skill")
        self.assertFalse(self.home.exists())

    def test_foreign_symlink_and_target_are_preserved(self):
        foreign = self.root / "foreign"
        foreign.mkdir()
        (foreign / "mine.txt").write_text("preserve")
        self.dest.parent.mkdir(parents=True)
        self.dest.symlink_to(foreign)
        proc = self.invoke("--copy")
        self.assertEqual(proc.returncode, 1)
        self.assertTrue(self.dest.is_symlink())
        self.assertEqual((foreign / "mine.txt").read_text(), "preserve")

    def test_legacy_link_converts_to_copy_without_changing_source(self):
        source = self.repo / "codex/skills/security"
        self.dest.parent.mkdir(parents=True)
        self.dest.symlink_to(source)
        before = (source / "SKILL.md").read_bytes()
        proc = self.invoke("--copy")
        self.assertEqual(proc.returncode, 0, proc.stderr)
        self.assertFalse(self.dest.is_symlink())
        self.assertEqual((source / "SKILL.md").read_bytes(), before)
        self.assertEqual((self.dest / "SKILL.md").read_bytes(), before)

    def test_managed_copy_updates_and_can_convert_back_to_link(self):
        self.assertEqual(self.invoke("--copy").returncode, 0)
        source = self.repo / "codex/skills/security/SKILL.md"
        source.write_text("new upstream text")
        proc = self.invoke("--copy")
        self.assertEqual(proc.returncode, 0, proc.stderr)
        self.assertEqual(
            (self.dest / "SKILL.md").read_text(), "new upstream text",
        )
        proc = self.invoke()
        self.assertEqual(proc.returncode, 0, proc.stderr)
        self.assertTrue(self.dest.is_symlink())

    def test_modified_copy_is_never_overwritten(self):
        self.assertEqual(self.invoke("--copy").returncode, 0)
        (self.dest / "SKILL.md").write_text("local customization")
        proc = self.invoke("--copy")
        self.assertEqual(proc.returncode, 1)
        self.assertEqual(
            (self.dest / "SKILL.md").read_text(), "local customization",
        )

    def test_agent_file_collision_is_preserved(self):
        agent = self.home / ".claude/agents/reviewer.md"
        agent.parent.mkdir(parents=True)
        agent.write_text("unmanaged agent")
        proc = self.invoke()
        self.assertEqual(proc.returncode, 1)
        self.assertEqual(agent.read_text(), "unmanaged agent")
        self.assertFalse(self.codex.exists())

    def test_copy_update_does_not_leave_nested_directories(self):
        self.invoke("--copy")
        self.invoke("--copy")
        self.assertFalse((self.dest / "security").exists())
        self.assertEqual(list(self.dest.iterdir()), [self.dest / "SKILL.md"])

    def test_receipt_records_owned_entries(self):
        self.invoke()
        receipt = json.loads(
            (self.home / ".claude/.claude-agents-install.json").read_text(),
        )
        self.assertEqual(len(receipt["entries"]), 4)


if __name__ == "__main__":
    unittest.main()
