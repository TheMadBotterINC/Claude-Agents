---
name: rails-security
description: Defensively audit authorized Rails apps for authentication, authorization, injection, XSS, CSRF, SSRF, secrets, dependencies, and session risks.
---

# Rails Security

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

Use this skill for authorized, defensive Rails security review. Find vulnerabilities, explain impact without weaponized exploit instructions, and give concrete Rails-native remediations.

## Boundaries

- Audit only the user's own/local app unless they explicitly authorize another target.
- Do not test production or external systems without explicit permission.
- If a credential is found, report only the file and key name with the value redacted. Never print, copy, log, or exfiltrate the secret.
- Ask before installing Brakeman, bundler-audit, or modifying Gemfiles/config.
- Attribute findings to the host app or the correct mounted Rails engine/customer gem. Flag engine code that is in scope but unavailable.

## Automated Pass

1. Identify Rails, Ruby, authentication, authorization, tenancy, and dependency posture from `Gemfile`, `Gemfile.lock`, routes, controllers, policies, models, and config.
2. Run configured scanners when available after inspecting project-script hooks: `bin/brakeman`, `bundle exec brakeman`, or `bundle audit check` against the local advisory DB. Ask before network updates such as `--update`; record advisory freshness and use dated sources for CVE/EOL claims.
3. Triage scanner output: remove false positives, keep real issues, and preserve enough evidence for each retained finding.
4. If scanners are absent and installation is not approved, continue with manual pattern searches and clearly state scanner coverage was unavailable.

## Manual Review

Inventory untrusted-input surfaces, then inspect them within the selected scope and ledger:

- Injection: SQL fragments, `find_by_sql`, unsafe `order`, command execution, `Open3`, backticks, and user-controlled SSRF sinks.
- Mass assignment: missing or weak strong params, `permit!`, broad `permit`, and raw params passed to model writes.
- AuthN/AuthZ/IDOR: missing authentication, missing Pundit/CanCan checks, unscoped `find(params[:id])`, tenant leaks, and unsafe `skip_before_action`.
- CSRF/XSS: forgery protection gaps, `html_safe`, `raw`, `<%==`, unsafe sanitize allowlists, `set:html`, and `dangerouslySetInnerHTML`.
- Secrets/logging: committed credentials, `.env` leakage, missing `filter_parameters`, PII in logs, and unsafe debug output.
- Sessions/headers: cookie flags, session store, `force_ssl`, HSTS, CSP, frame options, CORS, and secure header configuration.
- Deserialization/redirects/uploads: `Marshal.load`, unsafe `YAML.load`, open redirects, path traversal, and file upload validation gaps.

## Reporting Rules

- Save the report to `docs/audits/rails_security_report.md`, using a date or scope suffix if needed.
- Order findings by severity: Critical, High, Medium, Low.
- For each finding include location, vulnerability class, OWASP/CWE mapping when practical, impact, evidence source, and concrete fix.
- Keep exploit detail concise and non-operational. Describe what could go wrong, not step-by-step abuse.
- Include scanner/tool status, dependency audit results, and Rails/Ruby EOL or CVE concerns.
- In the final response, lead with critical/high issues and the report path.

## Severity Guidance

Rate higher when an issue affects authentication, authorization, tenant isolation, secret disclosure, remote code execution, payment/PII data, or unauthenticated users. Rate lower for defense-in-depth gaps with no clear exploit path, but still explain the hardening value.
