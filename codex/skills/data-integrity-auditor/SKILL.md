---
name: data-integrity-auditor
description: Data integrity auditor for Rails applications. Use when asked to review database constraints, model validations, foreign keys, uniqueness, nullability, enums, state machines, callbacks, orphaned records, migration safety, data backfills, transactional consistency, race conditions, or application invariants.
---

# Data Integrity Auditor

## Overview

Use this skill to find ways the application can create invalid, inconsistent, orphaned, or unrecoverable data. Focus on invariants that should be enforced in the database, application, or both.

## Workflow

1. Read `db/schema.rb` or `structure.sql`, migrations, models, validations, associations, callbacks, enums, state machines, service objects, imports, seeds, and data tasks.
2. Compare model-level expectations with DB constraints: nullability, foreign keys, uniqueness, checks, enums, defaults, and cascade behavior.
3. Inspect writes that span multiple records for transactions, locking, idempotency, and rollback behavior.
4. Review migrations and backfills for safety: locking, reversibility, batching, defaults, data cleanup, and deployment ordering.
5. Save the report to `docs/audits/data_integrity_auditor_report.md`, using a date or scope suffix if needed.

## Findings To Prioritize

- Business-critical uniqueness/foreign-key/nullability enforced only in Rails or not at all.
- Race-prone validations without matching unique indexes or locks.
- Orphaned records, unsafe dependent behavior, or missing cascade/nullify decisions.
- Invalid enum/state transitions, stale status columns, or callbacks that leave partial state.
- Multi-record writes without transactions or with external side effects inside transactions.
- Unsafe migrations that lock large tables, rewrite data eagerly, or cannot be rolled back.
- Imports/backfills that can duplicate, skip, or partially apply data.

## Reporting Rules

- Order findings by corruption risk, blast radius, and recovery difficulty.
- For each finding include invariant, current enforcement gap, failure scenario, and concrete fix.
- Recommend exact Rails migration patterns where appropriate, but do not run migrations without permission.
- Include tests to prove the invariant and race condition when relevant.
- Separate data cleanup tasks from schema/code changes.
