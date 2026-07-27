# Live URL Inspection Playbook

Use this playbook only for a supplied HTTP(S) URL.

## Access and safety

1. Confirm that the URL resolves and renders.
2. Prefer a real browser tool for rendered navigation and forms. Use direct page fetching as a fallback or supplement, and record interaction limitations.
3. Stay on public pages reached from the supplied product. Follow conversion-relevant third-party scheduling, form, identity, or checkout destinations only to inspect the pre-submission experience; record the domain change and stop at the same no-submit boundary. Do not perform competitor or broad market research.
4. Do not authenticate unless the user explicitly supplies test credentials and authorizes their use.
5. Never submit a form, create an account, start a trial, reserve a meeting, trigger a message, enter real data, or complete payment.

If the base URL is unreachable, document the actual failure in a `Blocked` report. Do not manufacture pages or generic findings.

## Mandatory entry-page triage

Inspect the supplied page before following any link:

1. Render a representative desktop first viewport and a narrow mobile first viewport. Use screenshots only as temporary working evidence and delete them before completing the audit.
2. Record what a cold visitor can understand without scrolling: product category, intended buyer, concrete outcome, differentiated mechanism, visible proof, primary CTA, and expected next step.
3. Inspect the first meaningful scroll for product evidence, audience fit, and objection handling.
4. Check whether the CTA label matches its actual public destination without submitting anything.
5. Note obvious load, layout, overflow, legibility, or navigation problems. Do not expand this into a full accessibility or performance audit.

If the user mentions bounce, exits, or homepage abandonment, make the report answer that question first. Treat message, proof, and CTA diagnoses as hypotheses unless user-supplied behavior data establishes a relationship. Footer and legal surfaces may document completeness issues, but do not rank them as bounce causes merely because they are precise and observable.

If the user confirms that page-level homepage abandonment is the only behavioral evidence and that hard customer proof does not exist, accept those limits. Do not stall on requests for deeper analytics or proof assets. Inspect enough of the CTA destination to understand the promised commitment, then recommend immediately buildable homepage changes using the evidence-constrained solution ladder in the audit framework.

## Route discovery

After entry-page triage, follow only conversion-relevant links that are publicly reachable:

- Homepage or primary landing page.
- Relevant product, feature, segment, industry, or use-case pages.
- Pricing or plan comparison.
- Customer stories, proof, integrations, security, procurement, or implementation pages.
- Demo, contact, or scheduling flow up to submission.
- Signup or free-trial entry flow up to submission.
- Public upgrade, plan-selection, checkout, or payment information without entering the transaction.

Inspect enough pages to map both visible routes. Do not turn this into an exhaustive SEO, accessibility, visual-responsive, console, or content audit.

## Evidence capture

For each material observation, record:

- Exact URL.
- Page and element.
- Short copy excerpt or behavior.
- Route and funnel stage.
- Access limitation, if any.

Use `Runtime-observed` only for behavior actually rendered or exercised. If authentication, a third-party provider, or form submission blocks the next step, mark the downstream stage `Not observable`; do not call it absent or broken.

## Live-site limitations

A live public audit can assess the presented experience but ordinarily cannot observe:

- Lead quality, qualification, routing, response time, pipeline progression, proposals, or closed-won.
- Authenticated activation, paywalls, checkout, or payment confirmation.
- Traffic mix, conversion rates, causal effects, or segment performance.

State these limitations explicitly. Recommend the smallest validation signal needed for a selected priority without configuring tracking.
