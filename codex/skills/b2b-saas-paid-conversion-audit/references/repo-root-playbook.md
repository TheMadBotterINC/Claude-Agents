# Repository Root Inspection Playbook

Use this playbook only for a supplied local repository directory.

## Validate and constrain

1. Resolve and validate the exact directory.
2. Stay within that root and obey its repository instructions.
3. Use `rg --files` and `rg` first.
4. Exclude dependencies, vendor code, build output, caches, coverage, logs, database dumps, user uploads, customer data, `.env` files, credentials, and secret stores.
5. Do not install dependencies, start services, execute arbitrary project code, run migrations or seeds, modify files, or commit.

Read an existing `.agents/product-marketing.md` or equivalent context file when present, but do not create or update it.

## Entry-page source triage

Before following downstream source paths, identify the default marketing entry route and inspect its visible copy and component order. Record whether the source makes the product category, intended buyer, paid outcome, differentiation, proof, CTA destination, and next-step expectation explicit. Label these findings `Source-evident`; responsive rendering, first-viewport visibility, load performance, and deployed content remain unverified.

## Inspection order

Inspect only files relevant to the path through first paid conversion:

1. README, product documentation, repository instructions, and application structure.
2. Route definitions, navigation, and the default marketing entry page.
3. Marketing pages, segment/use-case pages, CTA components, product evidence, customer proof, security, and pricing content.
4. Demo/contact/scheduling forms, handlers, success states, and buyer next-step copy.
5. Authentication, signup, trial entry, and pre-payment activation states.
6. Upgrade, paywall, plan-selection, checkout, payment, and confirmation states.
7. Focused tests that clarify intended conversion behavior.

If the marketing site, authenticated product, checkout, or sales workflow lives elsewhere, mark that surface `Not observable`.

## Evidence capture

For each material observation, record:

- Repository-relative `path:line`.
- Relevant symbol, route, component, or copy.
- Route and funnel stage.
- Whether the behavior is explicit or inferred.

Label repository evidence `Source-evident`, never `Runtime-observed`. Treat dynamic rendering, deployed content, external providers, feature flags, authentication state, and runtime success as unverified unless a static deterministic branch proves only the source behavior being described.

Do not browse a production URL merely because the repository contains one.

## Source limitations

Repository inspection can reveal implemented branches and intended copy but ordinarily cannot establish:

- What is deployed or rendered successfully.
- Actual buyer behavior, traffic, conversion, lead quality, pipeline, or payment completion.
- Third-party scheduling, CRM, identity, billing, or payment-provider behavior.
- Which feature flags, plans, experiments, or content variants are active.

Preserve these limitations in confidence and recommendation language.
