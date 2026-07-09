#!/usr/bin/env python3
"""Launch selected Codex audit skills as isolated codex exec runs."""

from __future__ import annotations

import argparse
import json
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path


SKILL_PROMPTS = {
    "ux-tester": "$ux-tester audit {base_url} across desktop, tablet, and mobile. Write the detailed report under docs/audits/.",
    "product-workflow-auditor": "$product-workflow-auditor audit core product workflows{url_clause}. Write the detailed report under docs/audits/.",
    "web-performance": "$web-performance audit frontend performance for {base_url}. Write the detailed report under docs/audits/.",
    "rails-security": "$rails-security audit this Rails app for security vulnerabilities and hardening opportunities. Write the detailed report under docs/audits/.",
    "multi-tenant-isolation-auditor": "$multi-tenant-isolation-auditor audit tenant isolation and cross-tenant data-leak risks. Write the detailed report under docs/audits/.",
    "data-integrity-auditor": "$data-integrity-auditor audit data integrity, constraints, and migration safety. Write the detailed report under docs/audits/.",
    "activerecord-performance": "$activerecord-performance audit ActiveRecord query performance, N+1s, indexes, and slow SQL. Write the detailed report under docs/audits/.",
    "background-jobs-auditor": "$background-jobs-auditor audit background jobs, queues, retries, idempotency, and scheduled work. Write the detailed report under docs/audits/.",
    "test-coverage-auditor": "$test-coverage-auditor audit test coverage, test health, missing regression tests, and risky untested flows. Write the detailed report under docs/audits/.",
    "observability-auditor": "$observability-auditor audit logging, metrics, tracing, error reporting, alerting, and diagnosability. Write the detailed report under docs/audits/.",
    "deployment-readiness": "$deployment-readiness audit production deployment readiness, operations, rollback, and runtime configuration. Write the detailed report under docs/audits/.",
    "rails-code-quality": "$rails-code-quality review this Rails app for maintainability, conventions, and refactoring opportunities. Write the detailed report under docs/audits/.",
}


DEFAULT_ORDER = [
    "ux-tester",
    "product-workflow-auditor",
    "web-performance",
    "rails-security",
    "multi-tenant-isolation-auditor",
    "data-integrity-auditor",
    "activerecord-performance",
    "background-jobs-auditor",
    "test-coverage-auditor",
    "observability-auditor",
    "deployment-readiness",
    "rails-code-quality",
]


BROWSER_SKILLS = {"ux-tester", "web-performance", "product-workflow-auditor"}


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--target", default=".", help="Project directory to audit.")
    parser.add_argument("--base-url", help="Running app URL for browser-based audits.")
    parser.add_argument(
        "--skills",
        default="all",
        help="Comma-separated skills to run, or 'all'.",
    )
    parser.add_argument(
        "--run-dir",
        help="Output run directory. Defaults to docs/audits/.orchestrator-runs/<timestamp>.",
    )
    parser.add_argument(
        "--sandbox",
        default="workspace-write",
        choices=["read-only", "workspace-write", "danger-full-access"],
        help="Sandbox mode passed to codex exec.",
    )
    parser.add_argument("--model", help="Optional model passed to codex exec.")
    parser.add_argument(
        "--strict",
        action="store_true",
        help="Stop after the first failed or blocked child run.",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Write manifest and commands without launching codex exec.",
    )
    return parser.parse_args()


def selected_skills(raw: str) -> list[str]:
    if raw.strip().lower() == "all":
        return list(DEFAULT_ORDER)

    seen = set()
    result = []
    for item in raw.split(","):
        skill = item.strip()
        if not skill:
            continue
        if skill not in SKILL_PROMPTS:
            known = ", ".join(sorted(SKILL_PROMPTS))
            raise SystemExit(f"Unknown skill '{skill}'. Known skills: {known}")
        if skill not in seen:
            seen.add(skill)
            result.append(skill)
    if not result:
        raise SystemExit("No skills selected.")
    return [skill for skill in DEFAULT_ORDER if skill in seen]


def iso_now() -> str:
    return datetime.now(timezone.utc).isoformat(timespec="seconds")


def run_directory(target: Path, explicit: str | None) -> Path:
    if explicit:
        return Path(explicit).expanduser().resolve()
    stamp = datetime.now().strftime("%Y-%m-%d-%H%M%S")
    return target / "docs" / "audits" / ".orchestrator-runs" / stamp


def prompt_for(skill: str, base_url: str | None) -> str:
    url_clause = f" for {base_url}" if base_url else ""
    return SKILL_PROMPTS[skill].format(base_url=base_url or "", url_clause=url_clause)


def command_for(
    target: Path,
    skill: str,
    prompt: str,
    final_path: Path,
    sandbox: str,
    model: str | None,
) -> list[str]:
    cmd = [
        "codex",
        "exec",
        "-C",
        str(target),
        "--sandbox",
        sandbox,
        "--output-last-message",
        str(final_path),
    ]
    if model:
        cmd.extend(["--model", model])
    cmd.append(prompt)
    return cmd


def main() -> int:
    args = parse_args()
    target = Path(args.target).expanduser().resolve()
    if not target.exists():
        raise SystemExit(f"Target does not exist: {target}")

    skills = selected_skills(args.skills)
    run_dir = run_directory(target, args.run_dir)
    run_dir.mkdir(parents=True, exist_ok=True)

    manifest = {
        "target": str(target),
        "base_url": args.base_url,
        "sandbox": args.sandbox,
        "model": args.model,
        "strict": args.strict,
        "dry_run": args.dry_run,
        "started_at": iso_now(),
        "finished_at": None,
        "runs": [],
    }

    for skill in skills:
        final_path = run_dir / f"{skill}-final.md"
        stdout_path = run_dir / f"{skill}.stdout.log"
        stderr_path = run_dir / f"{skill}.stderr.log"
        status = "pending"
        blocked_reason = None

        if skill in BROWSER_SKILLS and not args.base_url:
            status = "blocked"
            blocked_reason = "base URL required for browser-based audit"

        prompt = prompt_for(skill, args.base_url)
        cmd = command_for(target, skill, prompt, final_path, args.sandbox, args.model)
        entry = {
            "skill": skill,
            "status": status,
            "blocked_reason": blocked_reason,
            "started_at": None,
            "finished_at": None,
            "returncode": None,
            "command": cmd,
            "stdout_log": str(stdout_path),
            "stderr_log": str(stderr_path),
            "final_message": str(final_path),
        }

        if status == "blocked":
            manifest["runs"].append(entry)
            if args.strict:
                break
            continue

        if args.dry_run:
            entry["status"] = "dry-run"
            manifest["runs"].append(entry)
            continue

        entry["status"] = "running"
        entry["started_at"] = iso_now()
        with stdout_path.open("w") as stdout_file, stderr_path.open("w") as stderr_file:
            proc = subprocess.run(cmd, cwd=target, stdout=stdout_file, stderr=stderr_file)
        entry["finished_at"] = iso_now()
        entry["returncode"] = proc.returncode
        entry["status"] = "completed" if proc.returncode == 0 else "failed"
        manifest["runs"].append(entry)

        if proc.returncode != 0 and args.strict:
            break

    manifest["finished_at"] = iso_now()
    manifest_path = run_dir / "manifest.json"
    manifest_path.write_text(json.dumps(manifest, indent=2) + "\n")
    print(manifest_path)
    return 0 if all(run["status"] in {"completed", "dry-run", "blocked"} for run in manifest["runs"]) else 1


if __name__ == "__main__":
    sys.exit(main())
