---
name: observability-auditor
description: Observability auditor for Rails and web apps. Use when asked to review logging, metrics, tracing, Sentry/Honeybadger/Bugsnag, alerts, dashboards, audit logs, correlation IDs, structured logs, background job visibility, production diagnosability, or whether failures can be detected and debugged quickly.
---

# Observability Auditor

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
