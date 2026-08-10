---
name: b2b-saas-paid-conversion-audit
description: One-time, read-only audit of the observable path to first paid conversion for an existing sales-led B2B SaaS with an optional self-serve route. Use when the user asks why a B2B SaaS homepage or entry page may be losing visitors, requests an end-to-end paid-conversion diagnosis, or supplies one reachable HTTP(S) URL or local repository root for a conversion audit. Prioritize cold-visitor comprehension, trust, and next-click momentum before lower-exposure downstream inconsistencies. Produce recommendations only in one Markdown report on the user's Desktop, with at most three priorities. Do not use for a broad GTM roadmap, launch plan, recurring growth work, analytics or CRM analysis, retention or expansion, implementation, or an isolated post-click form, onboarding, paywall, or price-setting request.
---

# B2B SaaS Paid Conversion Audit

## Audit contract

Audit the current, observable path to first paid conversion across both sales-led and self-serve routes. Recommend changes; do not implement them.

Treat the supplied entry page as the first conversion gate for visitors who actually land there; do not assume it is the entry point for every route or traffic source. For a live homepage or an explicit bounce/exit question, diagnose the first 5–10 seconds before mapping the rest of the route:

- Can a cold visitor identify the category, intended buyer, paid outcome, differentiation, and next step?
- Does the visible proof substantiate the central promise?
- Does each CTA accurately describe its destination and offer a sensible path for both ready and researching buyers?
- Does the first viewport work on desktop and mobile?

Without user-supplied behavior data, call these `plausible abandonment drivers` or `bounce hypotheses`, never measured causes. State that entry-page exposure is conditional on the evaluated traffic actually landing there. Do not allow a certain but low-exposure footer, legal, or policy issue to outrank a high-exposure entry-page problem merely because the former is easier to prove.

Treat missing analytics, customer outcomes, testimonials, and case studies as design constraints—not reasons to defer the audit. When the user confirms that only page-level abandonment is available, accept that evidence boundary and recommend changes the team can make now from the observable page.

If hard customer proof is unavailable:

- Never make “collect proof,” “wait for customer results,” or “get testimonials” a standalone priority or prerequisite.
- Never invent logos, outcomes, counts, scores, guarantees, or testimonials.
- Substitute an honest mechanism demonstration, inspectable sample format, proof-producing preview, transparent matching criteria, concrete risk reversal already supported by policy, or lower-commitment route.
- Give every selected priority an available-now implementation. If a personalized preview or guarantee depends on unknown operations, name the dependency and include a static or manually fulfilled fallback.

Treat first paid conversion as the boundary:

- Sales-led: the first signed paid commitment or closed-won purchase.
- Self-serve: the first successful payment.

Inspect activation only when it plausibly mediates first paid conversion. Exclude retention, churn, renewals, expansion, NRR, acquisition-channel strategy, and general GTM planning.

Use this skill instead of a stage specialist when the request spans the overall multi-surface path to first paid conversion or explicitly asks why the supplied B2B SaaS entry page may be losing visitors before paid conversion. Route isolated post-click form, signup, onboarding, paywall, price-setting, or CRM implementation requests to the corresponding specialist.

## Input gate

Require exactly one inspectable target:

- One reachable `http://` or `https://` URL; or
- One existing local repository directory.

Do not run from a conversational product description alone. If the target is missing, invalid, or ambiguous, ask for one URL or repository root and stop. Do not request analytics, CRM, billing, warehouse, or connector access.

Infer the mode from the target. Do not browse a production URL merely because one appears inside a supplied repository.

## Output contract

Create exactly one Markdown report. Default to:

`~/Desktop/{target-slug}-paid-conversion-audit-{YYYY-MM-DD}.md`

Resolve `~` to the current user's actual home directory. Honor an explicit alternate output directory when the user provides one. If the Desktop is absent or writing there requires approval, request the required access; never silently substitute another directory.

Never overwrite an existing report. Add `-2`, `-3`, and so on before `.md`. Do not create persistent notes, screenshots, crawls, state, or other audit artifacts.

If a supplied URL proves unreachable, create a concise `Blocked` report documenting the attempt and request a reachable URL or repository root. If no valid target was supplied at all, do not create a report.

## Required references

Read these files before inspecting the target:

- [Audit framework](references/audit-framework.md) for route maps, evidence labels, lenses, and prioritization.
- [Report template](references/report-template.md) for the required artifact structure.

Then read exactly one mode-specific playbook:

- For a URL, read [Live URL playbook](references/live-url-playbook.md).
- For a repository, read [Repository root playbook](references/repo-root-playbook.md).

## Workflow

1. **Validate the target and output path.** Confirm one input mode, the product slug, and the resolved report path. Preserve any user-supplied facts as `User-provided`.
2. **Triage the entry page when it is in scope.** For a homepage, landing page, or explicit bounce question, inspect the first viewport and first meaningful scroll before following the funnel. For live URLs, render a representative desktop and mobile viewport. Record the cold-visitor answer to: what is it, who is it for, why now, why believe it, and what happens after the click. For another supplied surface, do not invent a homepage diagnosis.
3. **Inspect read-only.** Follow the applicable playbook. Limit inspection to conversion-relevant surfaces through first paid conversion.
4. **Map both routes separately.** Trace the sales-led route and the self-serve route when each is visible. Never treat demo booking, signup, or activation as paid conversion.
5. **Build the evidence ledger.** Label every material statement `Runtime-observed`, `Source-evident`, `User-provided`, `Hypothesis`, or `Not observable`. Cite exact URLs or repository-relative `path:line` locations.
6. **Identify plausible abandonment drivers and downstream friction.** Use the audit framework. Separate what every entry-page visitor sees from issues exposed only after engagement. Record unavailable analytics or hard proof as a constraint, not a blocker. Do not infer that an inaccessible or out-of-repo capability is absent.
7. **Select zero to three priorities.** Rank across both routes combined. Weight exposure, visitor salience, and next-click momentum before mere proximity to payment. Prefer fewer when evidence is weak. Require an immediately actionable version for every priority; do not defer the primary action until proof or analytics exist. Do not hide extra recommendations in quick wins, tests, or an idea bank.
8. **Write the report.** Follow the report template. Make each recommendation concrete enough to hand to the appropriate specialist without performing the work.
9. **Verify the artifact.** Re-open the saved file, confirm all required sections, confirm no more than three priorities, and confirm no target files or live systems changed.
10. **Respond concisely.** Link the absolute report path and name the first priority and confidence. Do not reproduce the full report in chat.

## Read-only safety

For every audit:

- Do not edit product code, configuration, content, tests, or data.
- Do not configure analytics, launch experiments, create branches, commit, or publish.
- Do not access connectors or private business systems.
- Do not use real personal, company, or payment data.
- Do not recommend deceptive claims, fabricated proof, fake scarcity, forced continuity, or dark patterns.

For a live URL, never submit contact, demo, signup, trial, scheduling, or payment forms; create an account; reserve a meeting; trigger email or SMS; or complete a purchase.

For a repository, never install dependencies, start services, execute arbitrary project code, run migrations or seeds, or read secrets, customer data, logs, database dumps, or credential stores.

The report is the only permitted mutation.

## Claim discipline

Treat URL and source inspection as qualitative evidence, not measured funnel performance.

- Never claim `the bottleneck`, `biggest leak`, measured causality, conversion lift, revenue at stake, or expected uplift without user-supplied outcome data that directly supports the calculation.
- Prefer `highest-priority observable friction` or `most plausible paid-conversion constraint`.
- When the user reports bounce without supplying segmented behavior data, say `most plausible homepage abandonment driver`, not `the reason visitors bounce`.
- Rank confidence and priority separately. A directly observed low-exposure inconsistency can be high confidence yet low priority.
- Do not rank footer, legal, privacy, or policy language as a homepage-bounce driver unless it is surfaced in the evaluated decision path or user-supplied evidence shows buyers engage with it.
- Do not turn unavailable analytics, testimonials, customer outcomes, or case studies into a blocking request. Recommend an honest proof substitute and an available-now page intervention.
- When disbelief is the leading diagnosis, Priority 1 must change what the visitor can inspect now; it cannot ask the business to obtain proof later.
- Never fabricate conversion rates, traffic, ACV, sales-cycle data, lead quality, benchmarks, buyer intent, ICP, or downstream behavior.
- Treat demo requests, contact forms, and booked meetings as hand-raise proxies. Sales-led closed-won performance is ordinarily `Not observable` from a URL or repository.
- Treat rendered public behavior as `Runtime-observed`; treat code as `Source-evident`. Do not describe source inspection as runtime verification.
- Treat company-authored claims as `User-provided` or `Source-evident claims`, not independently proven facts.
- Treat any prediction about buyer response as a `Hypothesis`.
- Say `not visible`, `not in the inspected repository`, or `not tested`; never convert those limitations into absence findings.
- Do not prescribe removing or deferring specific sales-qualification fields unless their use is observable or the user confirms it. Recommend a field-necessity review when internal purpose is unknown.

## Specialist boundaries

Name a handoff in the report when useful, but do not execute it:

- `cro` or `copywriting`: one public page, message hierarchy, or page copy.
- `signup`: account or trial registration.
- `onboarding`: pre-payment activation and time to value.
- `paywalls`: in-product upgrade prompts or trial expiry.
- `pricing`: price points, packaging, value metrics, and willingness-to-pay research.
- `analytics`: measurement implementation.
- `ab-testing`: experiment design and statistical method.
- `revops`: internal lead lifecycle, CRM routing, qualification, and sales handoff.
- `sales-enablement`: demo narrative, objection handling, and buying collateral.
- `product-workflow-auditor` or `ux-tester`: broader workflow completeness or exhaustive UX/browser QA.

Do not assume these skills are installed. Name the capability as a manual handoff when a specialist is unavailable.

## Quality bar

- Keep sales-led and self-serve maps distinct.
- Lead with the visitor's entry-page decision: understand, believe, continue, or leave.
- Prefer high-exposure category, promise, proof, and CTA problems over low-exposure completeness issues when diagnosing homepage abandonment.
- Convert every diagnosis into a concrete page, copy, offer, demonstration, or route change that can begin with the evidence and assets currently available.
- When hard proof is absent, reduce the amount of trust required instead of telling the user to wait for trust assets.
- Trace every priority to a plausible first-paid-conversion mechanism.
- Ground every diagnosis in cited evidence.
- Be decisive about sequence and explicit about uncertainty.
- Prefer one well-supported priority over three generic ones.
- Stop after the report is written and verified.
