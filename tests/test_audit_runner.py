"""Exercise orchestration with a fake Codex CLI and no network/model."""

import importlib.util
import json
import os
from pathlib import Path
import signal
import subprocess
import sys
import tempfile
import time
import unittest


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "codex/skills/audit-orchestrator/scripts/run_audit_suite.py"
SPEC = importlib.util.spec_from_file_location("audit_runner", SCRIPT)
RUNNER = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(RUNNER)

FAKE_CODEX = """#!/usr/bin/env python3
import json
import os
from pathlib import Path
import sys
import time

prompt = sys.argv[-1]
contract = json.JSONDecoder().raw_decode(prompt.split(
    "Execution contract (these output paths override skill defaults):\\n", 1
)[1])[0]
mode = os.environ.get("FAKE_MODE", "completed")
pid_file = os.environ.get("FAKE_PID_FILE")
if pid_file:
    Path(pid_file).write_text(str(os.getpid()))
if mode == "timeout":
    time.sleep(10)
if mode == "fail":
    sys.exit(7)
if mode != "missing":
    Path(contract["report_path"]).write_text("# Coverage\\nFixture\\n")
    result = {
        "status": mode if mode in {"partial", "blocked"} else "completed",
        "report_path": contract["report_path"],
        "blockers": ["tool missing"] if mode in {"partial", "blocked"} else [],
    }
    Path(contract["result_path"]).write_text(json.dumps(result))
Path(sys.argv[sys.argv.index("--output-last-message") + 1]).write_text("Done")
"""


class RunnerTests(unittest.TestCase):
    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory()
        self.addCleanup(self.temporary.cleanup)
        self.root = Path(self.temporary.name).resolve()
        self.target = self.root / "app"
        self.target.mkdir()
        self.bin = self.root / "bin"
        self.bin.mkdir()
        cli = self.bin / "codex"
        cli.write_text(FAKE_CODEX)
        cli.chmod(0o755)
        self.skills = self.root / "skills"
        for skill in RUNNER.DEFAULT_ORDER:
            directory = self.skills / skill
            directory.mkdir(parents=True)
            (directory / "SKILL.md").write_text(f"name: {skill}\n")
        self.env = {
            **os.environ,
            "PATH": str(self.bin) + os.pathsep + os.environ["PATH"],
        }
        self.run_dir = self.target / "audit-run"

    def invoke(self, *arguments, mode="completed", resume=False):
        args = [
            sys.executable, str(SCRIPT),
            "--skills-dir", str(self.skills),
        ]
        if resume:
            args += ["--resume", str(self.run_dir)]
        else:
            args += [
                "--target", str(self.target), "--run-dir", str(self.run_dir),
            ]
        proc = subprocess.run(
            args + list(arguments), env={**self.env, "FAKE_MODE": mode},
            capture_output=True, text=True, timeout=20,
        )
        path = self.run_dir / "manifest.json"
        manifest = json.loads(path.read_text()) if path.exists() else None
        return proc, manifest

    def test_selection_deduplicates_and_orders(self):
        self.assertEqual(
            RUNNER.selected_skills(
                "rails-code-quality,rails-security,rails-security",
            ),
            ["rails-security", "rails-code-quality"],
        )
        with self.assertRaises(SystemExit):
            RUNNER.selected_skills("made-up-skill")

    def test_reports_and_explicit_prior_handoffs(self):
        proc, manifest = self.invoke(
            "--skills", "rails-security,test-coverage-auditor",
        )
        self.assertEqual(proc.returncode, 0, proc.stderr)
        first, second = manifest["runs"]
        self.assertEqual(first["status"], "completed")
        self.assertEqual(second["prior_reports"], [first["report_path"]])
        self.assertIn(first["report_path"], second["command"][-1])
        self.assertIn("--ephemeral", first["command"])
        self.assertIn(
            str(self.skills / "rails-security/SKILL.md"),
            first["command"][-1],
        )
        self.assertTrue(Path(second["report_path"]).is_file())
        self.assertEqual(manifest["status"], "completed")

    def test_no_artifacts_is_not_completion(self):
        proc, manifest = self.invoke(
            "--skills", "rails-security", mode="missing",
        )
        self.assertEqual(proc.returncode, 1)
        self.assertEqual(manifest["runs"][0]["status"], "failed")

    def test_partial_and_blocked_are_nonzero(self):
        for status in ("partial", "blocked"):
            with self.subTest(status=status):
                self.run_dir = self.target / status
                proc, manifest = self.invoke(
                    "--skills", "rails-security", mode=status,
                )
                self.assertEqual(proc.returncode, 1)
                self.assertEqual(manifest["runs"][0]["status"], status)

    def test_strict_preserves_pending_and_returns_failure(self):
        proc, manifest = self.invoke(
            "--skills", "ux-tester,rails-security", "--strict",
        )
        self.assertEqual(proc.returncode, 1)
        self.assertEqual(
            [entry["status"] for entry in manifest["runs"]],
            ["blocked", "pending"],
        )

    def test_workflow_static_audit_does_not_require_url(self):
        proc, _ = self.invoke("--skills", "product-workflow-auditor")
        self.assertEqual(proc.returncode, 0, proc.stderr)

    def test_timeout_persists_failure(self):
        proc, manifest = self.invoke(
            "--skills", "rails-security", "--timeout", "0.05", mode="timeout",
        )
        self.assertEqual(proc.returncode, 1)
        self.assertIn("timed out", manifest["runs"][0]["blockers"][0])

    def test_resume_skips_verified_reports_and_retries_failed(self):
        self.invoke("--skills", "rails-security,test-coverage-auditor")
        manifest = json.loads((self.run_dir / "manifest.json").read_text())
        first_path = Path(manifest["runs"][0]["report_path"])
        before = first_path.stat().st_mtime_ns
        second = manifest["runs"][1]
        Path(second["report_path"]).unlink()
        proc, resumed = self.invoke(resume=True)
        self.assertEqual(proc.returncode, 0, proc.stderr)
        self.assertEqual(first_path.stat().st_mtime_ns, before)
        self.assertEqual(len(resumed["runs"][0]["attempts"]), 1)
        self.assertEqual(len(resumed["runs"][1]["attempts"]), 2)
        self.assertTrue(resumed["runs"][1]["report_path"].endswith("-2.md"))

    def test_resume_rejects_target_or_scope_changes(self):
        self.invoke("--skills", "rails-security")
        proc, _ = self.invoke("--scope", "quick", resume=True)
        self.assertNotEqual(proc.returncode, 0)
        self.assertIn("Cannot change", proc.stderr)

    def test_default_output_cannot_escape_through_docs_symlink(self):
        outside = self.root / "outside"
        outside.mkdir()
        (self.target / "docs").symlink_to(outside, target_is_directory=True)
        proc = subprocess.run(
            [
                sys.executable, str(SCRIPT), "--target", str(self.target),
                "--skills", "rails-security", "--dry-run",
                "--skills-dir", str(self.skills),
            ],
            env=self.env, capture_output=True, text=True, timeout=10,
        )
        self.assertNotEqual(proc.returncode, 0)
        self.assertIn("inside the target workspace", proc.stderr)
        self.assertEqual(list(outside.iterdir()), [])

    def test_dry_run_preflights_without_launching(self):
        proc, manifest = self.invoke(
            "--skills", "rails-security", "--dry-run", mode="fail",
        )
        self.assertEqual(proc.returncode, 0, proc.stderr)
        self.assertEqual(manifest["runs"][0]["status"], "dry-run")
        self.assertFalse(Path(manifest["runs"][0]["report_path"]).exists())

    def test_missing_skill_is_preflight_blocker(self):
        (self.skills / "rails-security/SKILL.md").unlink()
        proc, manifest = self.invoke("--skills", "rails-security", "--dry-run")
        self.assertEqual(proc.returncode, 1)
        self.assertIn("Installed skill", manifest["runs"][0]["blockers"][0])

    def test_missing_cli_is_preflight_blocker(self):
        (self.bin / "codex").unlink()
        self.env["PATH"] = str(self.bin)
        proc, manifest = self.invoke("--skills", "rails-security", "--dry-run")
        self.assertEqual(proc.returncode, 1)
        self.assertIn(
            "executable not found", manifest["runs"][0]["blockers"][0],
        )

    def test_child_failure_has_durable_manifest(self):
        proc, manifest = self.invoke("--skills", "rails-security", mode="fail")
        self.assertEqual(proc.returncode, 1)
        self.assertEqual(manifest["runs"][0]["returncode"], 7)
        self.assertEqual(
            manifest["runs"][0]["attempts"][0]["status"], "failed",
        )

    def test_invalid_configuration_has_no_run_artifacts(self):
        for flag, value in (
            ("--timeout", "nan"), ("--timeout", "-1"),
            ("--sandbox", "read-only"),
            ("--base-url", "https://user:password@example.test"),
            ("--base-url", "https://example.test?token=secret"),
        ):
            with self.subTest(flag=flag, value=value):
                proc, manifest = self.invoke(
                    "--skills", "rails-security", flag, value,
                )
                self.assertNotEqual(proc.returncode, 0)
                self.assertIsNone(manifest)

    def test_existing_run_directory_is_not_overwritten(self):
        self.invoke("--skills", "rails-security")
        proc, _ = self.invoke("--skills", "rails-security")
        self.assertNotEqual(proc.returncode, 0)

    def test_crash_leftover_attempt_does_not_block_resume(self):
        self.invoke("--skills", "rails-security", "--dry-run")
        path = self.run_dir / "manifest.json"
        manifest = json.loads(path.read_text())
        manifest["runs"][0].update(status="running", attempts=[])
        path.write_text(json.dumps(manifest))
        proc, resumed = self.invoke(resume=True)
        self.assertEqual(proc.returncode, 0, proc.stderr)
        self.assertTrue(resumed["runs"][0]["report_path"].endswith("-2.md"))
        self.assertEqual(
            resumed["runs"][0]["attempts"][0]["status"], "interrupted",
        )

    def test_resume_rejects_artifacts_outside_run_directory(self):
        self.invoke("--skills", "rails-security")
        path = self.run_dir / "manifest.json"
        manifest = json.loads(path.read_text())
        manifest["runs"][0]["result_path"] = str(self.target / "foreign.json")
        path.write_text(json.dumps(manifest))
        proc, _ = self.invoke(resume=True)
        self.assertNotEqual(proc.returncode, 0)
        self.assertIn("escapes run directory", proc.stderr)

    def test_resume_rejects_malformed_manifest(self):
        self.run_dir.mkdir()
        (self.run_dir / "manifest.json").write_text("[]")
        proc, _ = self.invoke(resume=True)
        self.assertNotEqual(proc.returncode, 0)
        self.assertIn("malformed manifest", proc.stderr)

    def test_invalid_sidecars_and_reports_are_rejected(self):
        report = self.target / "report.md"
        result = self.target / "result.json"
        entry = {"report_path": str(report), "result_path": str(result)}
        report.write_text("# Audited fixture")
        for data in (
            [], {"status": "invented"},
            {
                "status": "completed", "report_path": str(report),
                "blockers": ["actually blocked"],
            },
            {
                "status": "completed", "report_path": "some-other-report.md",
                "blockers": [],
            },
            {
                "status": "completed", "report_path": str(report),
                "blockers": "not a list",
            },
        ):
            with self.subTest(data=data):
                result.write_text(json.dumps(data))
                self.assertEqual(RUNNER.validate_result(entry)[0], "failed")
        result.write_text(json.dumps({
            "status": "completed", "report_path": str(report), "blockers": [],
        }))
        report.write_text(" ")
        self.assertEqual(RUNNER.validate_result(entry)[0], "failed")
        report.unlink()
        report.symlink_to(result)
        self.assertEqual(RUNNER.validate_result(entry)[0], "failed")

    def test_rerun_upstream_invalidates_downstream_handoff(self):
        self.invoke("--skills", "rails-security,test-coverage-auditor")
        path = self.run_dir / "manifest.json"
        manifest = json.loads(path.read_text())
        Path(manifest["runs"][0]["report_path"]).unlink()
        proc, resumed = self.invoke(resume=True)
        self.assertEqual(proc.returncode, 0, proc.stderr)
        self.assertEqual(len(resumed["runs"][1]["attempts"]), 2)
        self.assertEqual(
            resumed["runs"][1]["prior_reports"],
            [resumed["runs"][0]["report_path"]],
        )

    def test_interrupt_persists_state_and_stops_child(self):
        self.assert_interruption(signal.SIGINT, 130)

    def test_sigterm_persists_state_and_stops_child(self):
        self.assert_interruption(signal.SIGTERM, 143)

    def assert_interruption(self, signum, expected_code):
        pid_file = self.root / "child.pid"
        proc = subprocess.Popen(
            [
                sys.executable, str(SCRIPT), "--target", str(self.target),
                "--run-dir", str(self.run_dir), "--skills", "rails-security",
                "--skills-dir", str(self.skills),
            ],
            env={
                **self.env, "FAKE_MODE": "timeout",
                "FAKE_PID_FILE": str(pid_file),
            },
            stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True,
        )
        self.addCleanup(lambda: proc.kill() if proc.poll() is None else None)
        path = self.run_dir / "manifest.json"
        deadline = time.monotonic() + 5
        while time.monotonic() < deadline:
            if path.exists():
                manifest = json.loads(path.read_text())
                if (
                    manifest["runs"][0]["status"] == "running"
                    and pid_file.exists()
                ):
                    break
            time.sleep(0.02)
        else:
            self.fail("Runner did not start")
        proc.send_signal(signum)
        _, stderr = proc.communicate(timeout=10)
        self.assertEqual(proc.returncode, expected_code, stderr)
        manifest = json.loads(path.read_text())
        self.assertEqual(manifest["status"], "interrupted")
        self.assertEqual(manifest["runs"][0]["status"], "interrupted")
        with self.assertRaises(ProcessLookupError):
            os.kill(int(pid_file.read_text()), 0)


if __name__ == "__main__":
    unittest.main()
