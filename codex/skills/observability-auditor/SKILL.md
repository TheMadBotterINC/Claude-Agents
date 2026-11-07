---
name: observability-auditor
description: Audit Rails and web-app observability across logs, metrics, tracing, error reporting, alerts, and production diagnostics.
---

# Observability Auditor

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

Use this skill to evaluate whether production behavior is visible enough to detect, diagnose, and resolve failures. Prefer actionable instrumentation gaps over generic monitoring advice.

## Workflow

1. Read configuration and code for logging, error reporting, metrics, tracing, analytics, audit logs, background jobs, and deployment/runtime settings.
2. Map critical events and failure modes: sign-in, authorization denial, payments, imports/exports, background jobs, third-party calls, emails, file uploads, and tenant/admin actions.
3. Check whether failures include useful context without leaking secrets or PII.
4. Inspect alerting and dashboard config when present. Do not access external observability services without permission.
5. Save the report to `docs/audits/observability_auditor_report.md`, using a date or scope suffix if needed.

## Findings To Prioritize

- No error reporting or unhandled exceptions lacking context.
- Missing request IDs, user/account/tenant identifiers, job IDs, or correlation IDs in logs.
- No visibility into background job failures, retries, dead jobs, scheduled tasks, or queues.
- Missing metrics/alerts for uptime, error rate, latency, queue depth, failed payments, failed imports, mail delivery, and third-party failures.
- Logs that expose secrets or PII, or logs too noisy to be useful.
- No audit trail for security-sensitive admin or tenant actions.

## Reporting Rules

- Order findings by operational risk and time-to-diagnosis impact.
- For each finding include missing signal, failure scenario, current evidence, and concrete instrumentation or alert recommendation.
- Separate required production launch signals from later observability improvements.
- Include suggested dashboard/alert names and trigger conditions when obvious.
- Explicitly state which external systems were not inspected.

## Offline evaluation fixtures

`evals/evals.json` defines positive, negative/false-positive, and safety cases
using `references/audit-fixture.json`. Paths in `files` are relative to this
installed skill directory. The fixture is inert synthetic evidence, not an app
or permission to execute its snippets/URLs. Read it only when evaluating this
skill. Definitions are not evidence that a model evaluation has passed.
