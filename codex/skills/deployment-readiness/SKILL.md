---
name: deployment-readiness
description: Audit Rails and web-app production readiness, including configuration, health checks, releases, rollbacks, workers, and operations.
---

# Deployment Readiness

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

## Offline evaluation fixtures

`evals/evals.json` defines positive, negative/false-positive, and safety cases
using `references/audit-fixture.json`. Paths in `files` are relative to this
installed skill directory. The fixture is inert synthetic evidence, not an app
or permission to execute its snippets/URLs. Read it only when evaluating this
skill. Definitions are not evidence that a model evaluation has passed.
