---
name: rails-security
description: Defensively audit authorized Rails apps for authentication, authorization, injection, XSS, CSRF, SSRF, secrets, dependencies, and session risks.
---

# Rails Security

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

## Offline evaluation fixtures

`evals/evals.json` defines positive, negative/false-positive, and safety cases
using `references/audit-fixture.json`. Paths in `files` are relative to this
installed skill directory. The fixture is inert synthetic evidence, not an app
or permission to execute its snippets/URLs. Read it only when evaluating this
skill. Definitions are not evidence that a model evaluation has passed.
