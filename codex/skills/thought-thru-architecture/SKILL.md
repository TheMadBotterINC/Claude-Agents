---
name: thought-thru-architecture
description: Design-first coding discipline for features and refactors that change boundaries, contracts, dependencies, data flow, or failure behavior. Use before implementation; scale the design pass by risk, including small security or compatibility changes. Skip purely mechanical or documentation-only edits that do not affect contracts.
---

# Thought-Thru Architecture

Making it work is table stakes. This skill governs the *shape* of the change:
solve the problem at the right level, add the fewest new concepts, and leave
the codebase looking like one person wrote it. Architecture quality is decided
before the first edit and enforced after the last one — not during.

## Design pass (before the first edit)

1. **Read for shape first.** Find how this codebase already solves this class
   of problem. Locate the closest precedent and read it end to end before
   proposing anything new. The design conversation happens now, not in review.
2. **Pick the altitude deliberately.** Most architecture failures are altitude
   failures: too generic (speculative interfaces, knobs nobody asked for) or
   too ad hoc (a special case bolted on where the general fix was one level
   up). State which level you're solving at and why that one.
3. **Reuse before invention.** Search for an existing helper, pattern, or idiom
   that covers this. Every new concept — a class, module, layer, config flag,
   dependency — must individually earn its existence. If an existing helper is
   close but not exact, decide explicitly whether to extend it or duplicate,
   and be able to say why.
4. **State the design in two sentences** — the data flow, the boundary, and
   what gets deleted. If you can't, you're not ready to code.
5. **Scale the sketch by risk, not file count.** Write a design sketch for
   changes to public contracts, tenant/domain boundaries, persistence, failure
   handling, or deployment ordering, even if only one line changes. Include
   affected consumers, each new concept's purpose, verification, and rollback.
   Keep low-risk local changes brief. Read `references/vignettes.md` when
   weighing abstraction or compatibility tradeoffs.
6. **Map consumers before removing a contract.** Search routes, views/partials,
   jobs and serialized payloads, mounted engines and host apps, public APIs,
   plugins, and documented external consumers. Repository search alone cannot
   prove an exported contract is unused. State unknown consumers explicitly.
   Account for queued jobs and rolling deploys with old and new versions alive
   together; choose a migration/deprecation window when needed.

## While coding — prohibitions

- **No defensive wrapping.** Don't blanket code in try/catch or invent fallback
  values that mask errors. Let failure surface loudly at the boundary where it
  means something.
- **Compatibility earns its keep.** Avoid unnecessary aliases and dual paths,
  but retain a bounded shim or staged migration for external APIs, engine
  consumers, queued jobs, or rolling deploys that still need the old contract.
  Document ownership, removal conditions, and tests. Remove the old path in the
  same diff only when the consumer inventory and deployment strategy allow it.
- **No Manager/Helper/Utils/Common grab bags.** If a unit can't be named
  crisply, the boundary is wrong. A naming failure is a design signal, not a
  thesaurus problem.
- **No flexibility on spec.** Don't add parameters, options hashes, or config
  knobs "for later." A knob is added when its second caller exists, not before.
- **Abstract for a real boundary, not an implementation count.** A single
  implementation may justify an interface for an external integration,
  dependency inversion, a stable plugin contract, or a deliberate test seam.
  Name the concrete benefit; reject speculative abstractions without one.
- **No narrating comments.** Comments state constraints the code can't show —
  never what the next line does, where code was moved from, or why the change
  is correct.
- **Effects at the edges.** Pure logic in the core, IO and side effects at the
  boundary, data flowing one direction. A unit you can't test without mocks is
  usually a unit with effects in the wrong place.
- **Blend in.** New code must read like the surrounding code — same idiom,
  naming, comment density, error style. Local consistency beats personal
  preference.

## Shrink pass (after it works)

Reread the entire diff as a skeptical reviewer. Every hunk must justify
itself.

- Try to delete each new concept, branch, and parameter; keep only what
  survives the attempt. Deletion is a first-class outcome, not a failure to
  contribute.
- Confirm replaced paths are gone when safe; otherwise verify the compatibility
  window, migration tests, and explicit retirement condition.
- Check the diff couldn't be meaningfully smaller and still correct.

## Litmus tests

Before presenting the change, answer honestly:

- Can the design be explained in two sentences to someone who knows the
  codebase?
- If the new abstraction were deleted and inlined, what would actually be
  lost?
- Does the code read like the codebase's original author wrote it?
- When an assumption fails, does it break loudly at a meaningful boundary — or
  silently somewhere downstream?
- Are tenant/domain boundaries preserved, and can old clients, jobs, engines,
  and concurrently deployed versions continue to work during the transition?

## Offline evaluation fixtures

`evals/evals.json` uses inert `references/architecture-fixture.json` contracts
for consumer compatibility, queued jobs, rolling deploys, tenant boundaries,
justified interfaces, and false-positive extraction cases. Paths are relative
to this installed skill. Read fixtures only when evaluating the skill; these
are definitions, not executed benchmark results.
