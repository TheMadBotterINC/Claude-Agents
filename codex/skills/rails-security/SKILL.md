---
name: rails-security
description: Defensive Rails security auditor for authorized review of the user's own Rails apps. Use when asked to security-review, audit, harden, threat-check, or investigate Rails vulnerabilities involving auth, authorization, IDOR, injection, XSS, CSRF, SSRF, mass assignment, unsafe deserialization, exposed secrets, dependency CVEs, sessions, cookies, headers, or logging.
---

# Rails Security

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
2. Run configured scanners when available: `bin/brakeman`, `bundle exec brakeman`, `bundle audit check --update`, or equivalent project scripts.
3. Triage scanner output: remove false positives, keep real issues, and preserve enough evidence for each retained finding.
4. If scanners are absent and installation is not approved, continue with manual pattern searches and clearly state scanner coverage was unavailable.

## Manual Review

Systematically inspect every untrusted-input surface:

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
