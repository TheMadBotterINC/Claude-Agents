---
name: background-jobs-auditor
description: Background job and queue auditor for Rails apps using Sidekiq, GoodJob, DelayedJob, Solid Queue, Active Job, cron, or schedulers. Use when asked to review jobs, queues, retries, idempotency, locking, scheduled work, race conditions, job payloads, dead jobs, worker deployment, or async failure handling.
---

# Background Jobs Auditor

## Overview

Use this skill to evaluate whether asynchronous work is reliable, observable, idempotent, and safely deployed.

## Workflow

1. Identify queue backend and scheduler: Sidekiq, GoodJob, Solid Queue, DelayedJob, Active Job, Whenever, cron, Heroku Scheduler, or platform jobs.
2. Read job classes, mailers, callbacks that enqueue jobs, service objects, queue config, retry/dead-letter config, and worker deployment config.
3. Check job arguments, serialization, tenant/user scoping, idempotency, locking, retries, timeouts, error handling, and external API behavior.
4. Inspect scheduled tasks for overlap, missed runs, environment assumptions, and safe reentrancy.
5. Save the report to `docs/audits/background_jobs_auditor_report.md`, using a date or scope suffix if needed.

## Findings To Prioritize

- Non-idempotent jobs that can double-charge, double-email, duplicate records, or corrupt state on retry.
- Jobs missing tenant/account scoping or authorization-sensitive context.
- Unbounded jobs, large payloads, N+1-heavy jobs, or jobs that can exhaust memory/timeouts.
- Missing retry strategy, dead-job handling, alerts, or failure visibility.
- Scheduled tasks that overlap, run in the wrong environment, or cannot be replayed safely.
- Worker processes or queues missing from deployment config.
- External API jobs lacking timeout, backoff, circuit-breaker, or compensation behavior.

## Reporting Rules

- Order findings by data/business impact and failure likelihood.
- For each finding include job/scheduler location, failure mode, retry/idempotency risk, and concrete fix.
- Recommend tests for risky jobs, especially retry and duplicate-execution behavior.
- Separate deploy/config gaps from code-level job design issues.
- Do not enqueue or execute real jobs against external services without explicit permission.
