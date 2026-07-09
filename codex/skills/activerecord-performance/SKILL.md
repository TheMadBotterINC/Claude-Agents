---
name: activerecord-performance
description: Rails ActiveRecord performance auditor for database-backed Rails apps. Use when asked to audit, profile, speed up, or review Rails query performance, N+1 queries, missing or redundant indexes, over-fetching, unbounded queries, slow SQL, query counts, EXPLAIN plans, or database hot paths.
---

# ActiveRecord Performance

## Overview

Use this skill to find and prove Rails database performance problems. Every reported issue needs evidence: a file location, schema fact, query count, SQL sample, EXPLAIN output, or measured before/after behavior.

## Guardrails

- Work in two passes: static code/schema analysis first, then dynamic confirmation where practical.
- Prefer read-only DB work: `SELECT`, query logs, `EXPLAIN`, and `EXPLAIN ANALYZE` when safe for the local/dev database.
- Do not run migrations, mutate real data, add gems, or modify the Gemfile without explicit user approval.
- If a production or external database might be involved, stop and ask before running any DB command.
- Attribute findings to the host app or the correct mounted Rails engine/customer gem. If engine source is outside the repo and unavailable, report that gap.

## Static Pass

1. Read `Gemfile`, `Gemfile.lock`, `config/database.yml`, `db/schema.rb` or `structure.sql`, models, controllers, jobs, serializers, views, decorators, and query/service objects.
2. Note Rails version, DB adapter, pagination approach, and whether Bullet, Prosopite, rack-mini-profiler, Marginalia, or strict loading are present.
3. Cross-reference associations, foreign keys, common `where`/`order`/`group` shapes, and schema indexes.
4. Search for N+1 patterns: association access inside loops, collection partials, serializers touching associations, per-row counts, and missing `includes`/`preload`.
5. Search for inefficient usage: `.count` in loops, `.present?` loading records, `.all` then Ruby filtering, missing limits, row-by-row updates, over-fetching full records, callback-heavy persistence, and risky `default_scope`.

## Dynamic Pass

1. Confirm how to boot the app, run console/runner, and exercise key paths. Ask for base URL or credentials when needed.
2. Use existing tooling first: logs, Bullet, Prosopite, rack-mini-profiler, request specs, or local scripts.
3. As a no-gem fallback, use ActiveSupport notifications or SQL logs to count queries for focused actions.
4. Capture actual SQL for the worst offenders and run EXPLAIN on heavyweight queries when safe.
5. Re-measure after a proposed small code change only when the user asked for implementation and the change is in scope.

## Reporting Rules

- Save the report to `docs/audits/activerecord_performance_report.md`, using a date or scope suffix if needed.
- Order findings by estimated impact: queries saved, rows avoided, latency reduced, or risk removed.
- For each finding include location, query shape, problem class, evidence, concrete Rails fix, and expected improvement.
- Mark static-only findings clearly when dynamic confirmation was not possible.
- Suggest exact migrations or code changes, but do not run migrations unless the user explicitly asks.
- Include a short section for tool coverage: what ran, what failed, and what could not be measured.

## Common Fix Patterns

Prefer idiomatic Rails fixes: `includes`/`preload`/`eager_load`, `counter_cache`, scoped association preloading, `exists?`, `pluck`/`pick`/`select`, pagination/limits, `find_each`/`in_batches`, `insert_all`/`upsert_all`, composite indexes that match query order, and unique constraints when data integrity implies them.
