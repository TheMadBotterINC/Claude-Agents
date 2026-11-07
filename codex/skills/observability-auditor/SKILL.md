---
name: observability-auditor
description: Audit Rails and web-app observability across logs, metrics, tracing, error reporting, alerts, and production diagnostics.
---

# Observability Auditor

## Safety, scope, and evidence contract

- **Audit only.** Do not edit app code/config, autocorrect, install dependencies,
  generate migrations, or apply fixes without explicit implementation approval.
  Default writes are report/evidence artifacts; propose changes in the report.
- **Verify before execution.** Inspect effective app/test environment, hooks,
  DB target, tenant context, and integrations without exposing credentials.
  Localhost is not proof of isolation. Dynamic checks require verified local/dev/
  test targets, synthetic data, and sandboxed services. Production/external DB
  commands (even SELECT/EXPLAIN) require explicit target/action approval.
  Do not submit forms, delete/upload data, charge, send mail, enqueue jobs,
  trigger webhooks, deploy, mutate accounts, or update tools/advisories without
  specific authorization; otherwise continue statically.
- **DB caution.** EXPLAIN ANALYZE executes queries, including writes/functions;
  SELECT can have effects too. Prefer vetted plain EXPLAIN. ANALYZE requires
  bounded reads on approved disposable local/dev data and a timeout, never
  audit-time migrations/backfills.
- **Minimize/redact before capture or sharing.** Exclude secrets, cookies,
  tokens, headers/bodies, SQL binds, tenant identifiers, and PII from screenshots,
  network evidence, traces, and logs. Prefer metadata/synthetic UI; omit unsafe
  artifacts rather than collecting raw sensitive data.
- **Bound scope:** default `standard` inventories applicable categories/layers
  and reviews risk-prioritized representative paths. `quick` covers the named
  path plus its highest-risk adjacent boundary; `comprehensive` expands across
  inventoried in-scope paths within an agreed concrete time/item budget. No
  mode/model guarantees every defect found.
- **Coverage ledger:** record paths/categories/roles/tenants/engines as reviewed,
  sampled, deferred, blocked, or not applicable, with evidence/reasons. Stop when
  planned items are dispositioned or budget expires; disclose gaps/stopping
  reason. Expand only with a new budget/scope.
- **Honest output:** check surrounding controls/consumers before flagging patterns.
  Separate confirmed findings, static risks, and hypotheses; unavailable tools/
  source are coverage gaps. Honor assigned report paths over unique standalone
  defaults; preserve prior reports as context, not fresh evidence. Include
  ledger, environment, commands/failures, evidence, remedy, and status. Write any
  assigned JSON sidecar with `status` (`completed|partial|blocked`), exact absolute
  `report_path`, and `blockers` array. Completed requires planned coverage,
  nonempty matching report, no blockers; incomplete coverage is partial, and
  missing prerequisites preventing meaningful work are blocked.

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
