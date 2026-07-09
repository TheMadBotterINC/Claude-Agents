---
name: audit-orchestrator
description: Orchestrates multiple local software-business audit skills into a sequential audit plan and consolidated report. Use when asked to run all audits, run a full app audit, coordinate UX/performance/security/code-quality/database audits, choose a subset of audit skills, summarize outputs from several audits, or manage sequential runs of $ux-tester, $web-performance, $rails-security, $activerecord-performance, and $rails-code-quality.
---

# Audit Orchestrator

## Overview

Use this skill to coordinate the local audit suite, run the relevant subskills in a deliberate order, and produce a single high-signal summary that links back to the detailed reports. This skill manages scope, sequencing, deduplication, and final prioritization; the specialist skills own the deep audit work.

## Available Audit Skills

- `$ux-tester`: browser UX, responsiveness, visual polish, interactions, console/network issues. Requires a running app URL and Playwright MCP.
- `$web-performance`: Core Web Vitals, Lighthouse-style metrics, network weight, assets, hydration, bundle/build output. Requires a running app URL and Playwright MCP.
- `$rails-security`: defensive Rails security, auth/authz, IDOR, injection, XSS, CSRF, SSRF, secrets, dependency CVEs, sessions, headers.
- `$activerecord-performance`: Rails database/query performance, N+1s, indexes, over-fetching, unbounded queries, EXPLAIN/query counts.
- `$rails-code-quality`: maintainability, Rails conventions, architecture, RuboCop/Reek, fat models/controllers, callbacks, duplication, dead code.

## Scope Selection

Infer the subset from the user's language:

- "all", "full audit", "comprehensive", "everything", "launch readiness", or "app audit" -> all five skills.
- "frontend", "polish", "QA", "responsive", "browser", or "UX" -> `$ux-tester`; add `$web-performance` when speed, metrics, assets, or Lighthouse are mentioned.
- "performance" alone in a Rails app -> ask whether they mean frontend, database, or both unless the context clearly points one way.
- "security", "hardening", "vulnerability", "auth", "tenant", "secrets", or "CVE" -> `$rails-security`.
- "database", "queries", "N+1", "indexes", "ActiveRecord", or "slow SQL" -> `$activerecord-performance`.
- "quality", "maintainability", "conventions", "refactor", "smells", or "RuboCop" -> `$rails-code-quality`.

If the requested scope is ambiguous and the choice materially affects runtime or required inputs, ask one concise clarification. Otherwise choose the conservative subset and state the assumption.

## Sequencing

Default full-suite order:

1. `$ux-tester` first when a running app URL is available, because visual/browser defects often reveal broken flows and console/network failures.
2. `$web-performance` second, reusing the route map and browser context from UX where possible.
3. `$rails-security` third, before code-quality refactor advice so security fixes remain clearly prioritized.
4. `$activerecord-performance` fourth, after routes and hot paths are known.
5. `$rails-code-quality` last, so maintainability recommendations can account for security and performance findings without crowding them.

For subsets, preserve the relative order above. If browser skills are requested but the app is not running or no URL is provided, ask for the URL or start command before beginning those skills.

## Running The Audit

For each selected skill:

1. Announce which skill is starting and what inputs it needs.
2. Invoke or explicitly follow that skill's workflow by name, for example: "Use `$rails-security` to audit this Rails app..."
3. Let the specialist skill produce its detailed report under `docs/audits/`.
4. Record the report path, tool coverage, blockers, critical findings, and overlap with prior findings.
5. Continue to the next selected skill unless a blocker makes later work unreliable.

Do not run specialist audits in parallel by default. Sequential runs produce cleaner context, avoid browser/tool contention, and make final deduplication easier. If the user explicitly asks for background or parallel work, recommend `codex exec` sessions, Codex app automations, or worktrees and explain the approval/sandbox tradeoffs before starting them.

## Consolidated Output

Save a final summary to `docs/audits/audit_orchestrator_report.md`, using a date or scope suffix if needed. Include:

- Scope: selected skills, skipped skills, assumptions, target URL, and target repo/app.
- Execution log: run order, report paths, tools run, and blockers.
- Top findings: one prioritized list across all audits, ordered by business/user risk.
- Cross-cutting themes: duplicates or related findings across UX, performance, security, database, and code quality.
- Suggested sequence of fixes: immediate blockers, high-risk fixes, quick wins, then larger refactors.
- Verification checklist: how to confirm the top fixes after implementation.

In the final response, include only the consolidated report path, selected skills, critical/high findings, and recommended next actions. Avoid dumping every specialist finding into chat.

## Guardrails

- Respect each specialist skill's safety rules, especially Playwright MCP requirements, secret redaction, DB mutation limits, and install approvals.
- Never modify application code during an audit unless the user explicitly asks for fixes.
- If one audit discovers a blocker that invalidates later measurements, stop the affected later audits and report the dependency.
- Keep Claude agent files untouched; use the Codex skills for orchestration.
