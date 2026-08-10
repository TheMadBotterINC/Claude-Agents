# Paid-Conversion Audit Framework

Use this framework to inspect a hybrid B2B SaaS without analytics, CRM, or billing data. It supports qualitative diagnosis only.

## Conversion routes

Keep the routes separate even when they share pages.

## Entry-page abandonment diagnosis

For traffic that lands on the supplied homepage or landing page, treat that page as the first gate. Do not assume every sales-led or self-serve buyer enters there. Before auditing downstream steps, evaluate the landing visitor's initial decision:

| Visitor question | What to inspect |
|---|---|
| What is this? | Product category, concrete deliverable, and whether brand language or jargon hides the answer. |
| Is it for me? | Role, segment, use case, and message match with any user-provided traffic source. |
| Why should I care now? | Specific paid outcome, urgency grounded in the problem, and differentiated mechanism. |
| Why should I believe it? | Real product evidence, substantiated customer proof, methodology, and risk reversal. |
| What happens next? | CTA wording, destination, commitment level, and paths for ready versus researching visitors. |

For a live URL, inspect a representative desktop viewport and a narrow mobile viewport. Note whether the primary message, evidence, and CTA survive the smaller first screen. Distinguish a visual or copy observation from the `Hypothesis` that it contributes to abandonment.

When traffic source is unknown, evaluate a cold-visitor scenario and state both the assumption and its exposure limitation. If the user supplies an ad, referral, search query, or segment, evaluate message match explicitly. Do not request analytics as a prerequisite.

### Sales-led

`Visit → segment and value recognition → demo/contact intent → form or scheduling → next-step expectation → evaluation and procurement → first paid commitment`

The public URL or repository can usually evidence only the path through form or scheduling. Mark qualification, evaluation, procurement, and closed-won behavior `Not observable` unless the supplied artifact directly documents the user-facing experience. Never treat a hand raise as paid conversion.

### Self-serve

`Visit → plan or offer comprehension → signup/trial → first value → upgrade ask → checkout → first successful payment`

Inspect only publicly reachable or source-evident stages. Do not create an account or enter checkout on a live site. Do not recommend adding self-serve merely because it is absent.

## Audit lenses

Apply all five lenses to each visible route after entry-page triage.

### 1. ICP and value clarity

- Identify who the route appears to serve and what paid outcome it promises.
- Check whether segment, role, problem, and differentiated outcome remain coherent from entry page to paid ask.
- Flag company-centered claims, vague category language, and unsupported outcome claims as evidence—not as automatic defects.

### 2. Route and CTA clarity

- Check whether a buyer can choose the appropriate sales-led or self-serve path.
- Compare CTA labels, hierarchy, destinations, repeated asks, and post-action expectations.
- Treat apparent CTA competition or cannibalization as a hypothesis unless behavior data proves it.

### 3. Proof and buying-risk reduction

- Inspect customer evidence, use cases, security and procurement information, integrations, implementation expectations, and support for a buying committee.
- Distinguish a displayed claim from independent verification.
- Never recommend invented logos, testimonials, certifications, guarantees, or quantitative proof.
- When hard customer proof is unavailable, reduce the amount of trust required through an inspectable mechanism, truthful demonstration, preview, clear acceptance criteria, or reversible first commitment.

### 4. Friction and next-step certainty

- Inspect unnecessary fields, unclear requirements, hidden commitments, validation and error states, scheduling friction, account requirements, setup burden, and checkout surprises.
- Check whether the buyer knows what happens after each action.
- Treat field count as friction evidence, not proof that a particular field is unnecessary. When qualification or routing use is unknown, recommend validating field necessity with the owner before removal or deferral.
- Do not call an untested or inaccessible step broken.

### 5. Commercial clarity

- Inspect visible plan fit, audience thresholds, inclusions, exclusions, contract signals, trial terms, cancellation language before the paid commitment or self-serve payment, and consistency between pricing, demo, signup, upgrade, and checkout surfaces.
- Critique comprehension and consistency only.
- Route price-setting, packaging redesign, and willingness-to-pay questions to `pricing`.

## Evidence-constrained solution ladder

Use this order when analytics or hard customer proof is unavailable. Select only the smallest intervention that addresses the observed friction:

1. **Literal promise:** State the product category, concrete output, audience, and operating mechanism without requiring the visitor to decode a metaphor.
2. **Mechanism demonstration:** Show inputs, matching rules, verification steps, output fields, source/date, and exclusions. Replace unexplained precision scores with visible criteria.
3. **Inspectable output:** Use an honestly labeled, privacy-safe example or sample gallery to demonstrate format and reasoning. Do not present it as evidence of customer outcomes.
4. **Proof-producing preview:** Let the visitor request or generate a small sample for their ICP before the full signup/payment commitment. A manually fulfilled concierge version is acceptable when stated as an operational option; otherwise recommend a static walkthrough.
5. **Risk reduction:** Surface only truthful existing policies—such as acceptance standards, replacement treatment, cancellation, or pay-only-for-delivered rules—next to the CTA. Do not invent a guarantee.
6. **Commitment-matched route:** Align CTA wording with the real destination and provide a research path, self-serve path, or sales-assisted path appropriate to the observable offer.

“Acquire customer proof,” “add testimonials,” or “collect more analytics” is not an actionable conversion recommendation by itself. It may appear as future validation context, never as the primary intervention. Each selected priority must include an available-now implementation that does not depend on missing proof or data.

## Evidence labels

Use one label for every material claim:

| Label | Meaning |
|---|---|
| `Runtime-observed` | Directly verified on the rendered live site during this audit. |
| `Source-evident` | Present in inspected repository source or documentation; runtime behavior remains unverified. |
| `User-provided` | Supplied by the user but not independently verified. |
| `Hypothesis` | A causal explanation, predicted buyer response, or proposed mechanism. |
| `Not observable` | Material information outside or blocked from the supplied artifact. |

Assign evidence IDs `E1`, `E2`, and so on. Cite a URL plus element/copy for live evidence or repository-relative `path:line` for source evidence.

## Confidence

- **High:** Direct evidence shows deterministic friction in a critical path, or multiple independent observations support the same diagnosis.
- **Medium:** Direct evidence shows plausible friction, but buyer behavior or downstream outcome is unknown.
- **Low:** The recommendation depends mainly on incomplete coverage, an inferred audience, or an unverified causal explanation.

Do not raise confidence because a pattern is common in other SaaS products.

## Prioritization

Select zero to three recommendations across both routes combined.

First, eliminate any actually observed deterministic break that prevents progress. Otherwise consider, in order:

1. Evidence strength.
2. Exposure within the evaluated route: how much of that route's traffic necessarily encounters it.
3. Visitor salience: whether it affects understanding, relevance, belief, or willingness to take the next step.
4. Route momentum: whether it blocks or misrepresents the next click.
5. Proximity to first paid conversion.
6. Breadth across visible high-intent routes.
7. Reversibility and relative effort.

Priority and confidence are not the same. A high-confidence inconsistency in footer or legal copy can remain low priority because most bouncers will not encounter it. For an explicit homepage-bounce question, page-level category clarity, message match, visible proof, CTA expectation, mobile first-screen access, and obvious load failure normally outrank later commercial or policy details when supported by the artifact. This ranking applies to traffic that lands on the homepage; do not extrapolate it to outbound, partner, use-case, or direct-scheduling entry routes without evidence.

Do not select a legal, privacy, terms, or footer issue as a plausible homepage-abandonment driver unless it is presented before the evaluated CTA, the user supplies evidence that buyers inspect it, or the target is a regulated/procurement-heavy route where the page itself foregrounds that concern.

Do not calculate a numeric score without outcome data. Do not label something high impact or a quick win without artifact-specific evidence.

For every selected priority, include:

- Route and funnel stage.
- Exact evidence IDs.
- Observable friction or constraint.
- Concrete recommendation.
- Available-now implementation using current evidence and assets.
- Expected mechanism labeled `Hypothesis`.
- Confidence and why.
- Relative effort: small, medium, or large.
- Minimal validation signal, including the eventual paid outcome.
- Specialist or manual handoff.

Use priority zero only for an actually observed deterministic break that prevents progress. Otherwise rank recommendations `1` through `3`.

## Scope guardrails

- Stop at first paid conversion.
- Exclude retention, churn, renewals, expansion, NRR, referrals, and acquisition-channel planning.
- Do not produce full rewrites, detailed experiment designs, analytics implementations, price recommendations, or CRM process designs.
- Do not turn deferred observations into a second actionable backlog.
