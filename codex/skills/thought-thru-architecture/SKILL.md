---
name: thought-thru-architecture
description: Design-first coding discipline. Use BEFORE writing or changing product code whenever implementing a feature, refactoring, restructuring, or making any change that adds a new file, class, module, abstraction, or dependency. Skip for one-line fixes, doc edits, and mechanical renames.
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
5. For anything touching 3+ files or adding a layer, write the sketch down
   first: files touched, each new concept and why it earns its place, what old
   code dies. Then read `references/vignettes.md` for the failure modes to
   avoid.

## While coding — prohibitions

- **No defensive wrapping.** Don't blanket code in try/catch or invent fallback
  values that mask errors. Let failure surface loudly at the boundary where it
  means something.
- **No backwards-compat shims** — aliases, re-exports, deprecation paths, dual
  code paths — unless something in this repo actually depends on the old path.
  Migrating means deleting the old code in the same diff.
- **No Manager/Helper/Utils/Common grab bags.** If a unit can't be named
  crisply, the boundary is wrong. A naming failure is a design signal, not a
  thesaurus problem.
- **No flexibility on spec.** Don't add parameters, options hashes, or config
  knobs "for later." A knob is added when its second caller exists, not before.
- **No interface or base class with one implementation.**
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
- Confirm the old path is actually gone if this change replaces one.
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
