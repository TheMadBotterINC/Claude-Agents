---
name: deployment-readiness
description: Audit Rails and web-app production readiness, including configuration, health checks, releases, rollbacks, workers, and operations.
---

# Deployment Readiness

## Safety, scope, and evidence contract

- **Audit, do not implement.** Do not edit application code/configuration, run
  autocorrect, add dependencies, generate migrations on disk, or apply fixes
  unless the user explicitly requests implementation. Suggested patches belong
  in the report. Report/evidence artifacts are the only default writes.
- **Verify the environment before execution.** Inspect start/test commands and
  hooks, effective app environment, database target, tenant context, and external
  integrations without exposing credentials. A localhost URL alone does not
  prove local data or sandboxed services. Dynamic checks require a verified
  local/dev/test target with synthetic data and isolated integrations. Ask for
  explicit target/action approval before any production or external database
  command, even SELECT or EXPLAIN; otherwise continue statically.
- **No implicit side effects.** Audit permission is not permission to submit
  forms, delete records, send mail, charge payments, upload data, enqueue jobs,
  trigger webhooks, deploy, or mutate accounts. Use approved disposable fixtures
  and stubbed services; ask before any action outside that authorization.
  Do not install tools or update remote vulnerability databases silently.
- **Database execution is not automatically read-only.** EXPLAIN ANALYZE executes
  the query, including writes and called functions, and can create load/locks.
  Even SELECT can invoke side-effecting functions. Prefer plain EXPLAIN after
  inspecting the query; use ANALYZE only for vetted bounded reads on approved
  disposable local/dev data with a timeout. Rollback is not protection from
  external effects. Never run migrations/backfills as part of an audit.
- **Minimize sensitive evidence.** Redact secrets, cookies, Authorization headers,
  query-string tokens, request/response bodies, customer/tenant identifiers, PII,
  SQL bind values, screenshots, traces, and logs before saving or sharing. Prefer
  metadata to full payload capture. Use synthetic accounts and mask UI data
  before capture; if safe redaction is unavailable, omit the artifact and report
  the limitation. Never collect raw sensitive data just to redact it later.
- **Choose a bounded scope.** Use `standard` unless the user/runner selects
  `quick` or `comprehensive`. Quick covers the named path and highest-risk
  adjacent boundary; standard inventories relevant layers and reviews each
  applicable category with risk-prioritized representative paths; comprehensive
  expands to all inventoried in-scope paths and boundaries within an agreed
  time/tool budget. Agree a concrete time or item budget at preflight; runner
  timeout is a ceiling, not a claim of coverage. No mode promises all defects
  found, and none assumes a particular model tier.
- **Keep a coverage ledger.** Record each in-scope path/layer/role/tenant/engine
  and applicable category as reviewed, sampled, deferred, blocked, or not
  applicable, with evidence and reasons. Preserve systematic category coverage
  rather than silently skipping hard areas. Stop when every planned ledger item
  is dispositioned or the agreed budget is reached; report remaining items and
  the stopping reason. Expand only with a new explicit budget/scope.
- **Report honestly.** Separate confirmed findings, static-only risks, and
  hypotheses; include location, evidence, impact, and a proportionate remedy.
  Check surrounding authorization, constraints, framework behavior, and actual
  consumers before flagging a pattern. Missing tools/source are coverage gaps,
  not findings. Finish with `completed` only when planned scope is reviewed;
  use `partial` for incomplete coverage and `blocked` when prerequisites prevent
  meaningful work. A clean sampled review is not proof of absence of defects.
- **Portable output.** Honor a runner-provided report path before any default;
  create only that run's report and evidence, never overwrite prior reports.
  Without a runner, use the skill's default report path with a unique suffix.
  Include scope, ledger, commands/tool failures, environment, stopping reason,
  and status in the report and summarize findings in the final response.
  If the runner assigns a JSON result sidecar, write it at that exact path with
  `status` (`completed|partial|blocked`), `report_path` (the assigned absolute
  report path), and `blockers` (string array). Completed requires a nonempty
  matching report and no blockers; prior reports are read-only context, not
  proof that a check ran in this attempt.

## Overview

Use this skill to decide whether an app is ready to ship and operate safely. Focus on runtime risks, missing operational controls, and failure recovery.

## Workflow

1. Read deployment artifacts: Dockerfiles, Procfiles, app platform config, CI/CD workflows, infra config, env docs, README, runbooks, Rails config, and initializer files.
2. Map runtime dependencies: database, Redis/queues, storage, mail, third-party APIs, credentials, domains, SSL, CDN, cache, and scheduled jobs.
3. Check release mechanics: migrations, asset builds, seeds, boot commands, worker processes, health checks, readiness checks, rollback, and deploy ordering.
4. Check operational posture: logging, error reporting, alerting, backup/restore, maintenance tasks, admin access, and incident instructions.
5. Do not mutate cloud resources or production systems unless explicitly asked.
6. Save the report to `docs/audits/deployment_readiness_report.md`, using a date or scope suffix if needed.

## Findings To Prioritize

- Missing required env vars, credentials, or secret rotation guidance.
- No health/readiness endpoint or checks that miss DB/queue/storage dependencies.
- Unsafe migrations, deploy ordering problems, irreversible data changes, or missing rollback plan.
- Background worker, cron, Action Cable, mailer, or storage processes not represented in deployment config.
- Missing backups, restore verification, error tracking, logs, alerts, or runbook.
- Weak SSL, host authorization, force_ssl, cache headers, CDN, or asset-build configuration.

## Reporting Rules

- Order findings by launch risk: release blocker, high risk, medium, low.
- For each finding include evidence, expected failure mode, and concrete remediation.
- Distinguish required fixes before launch from operational improvements after launch.
- Include a deployment checklist tailored to the detected platform.
- Document any assumptions about the hosting target if platform config is absent.
