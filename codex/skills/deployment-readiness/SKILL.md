---
name: deployment-readiness
description: Production deployment readiness auditor for Rails and web apps. Use when asked to check launch readiness, deploy readiness, operations, runtime configuration, env vars, credentials, health checks, logging, background workers, migrations, rollback paths, storage, email, SSL, CDN/cache headers, release process, or runbooks.
---

# Deployment Readiness

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
