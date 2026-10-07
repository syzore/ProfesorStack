---
name: de-entropy
description: Use for /de-entropy, or when the user no longer trusts a codebase's structure - recovers the conceptual model the project was meant to be, removes structure that exists only from historical accumulation, and rewrites the implementation around the recovered model. Not for local refactors.
---

# De-Entropy

Refactoring keeps the system conceptually the same and improves the code.
De-Entropy changes the system: **recover the simplest coherent system this
project was supposed to be, then make the code conform to it.**

**Entropy** is structure that exists because of history, not because of the
problem: a second abstraction beside the first, a workaround for a bug since
fixed, six names for one concept. **Essence** is what remains when every piece
of entropy is gone. Every decision in this skill sorts code into one or the
other.

## Scope

Pick one **subsystem** per run: a slice with a nameable purpose (`feed`,
`auth`, `billing pipeline`). A whole repo is in scope only if it is small enough
to hold in one model. Ask the user when the scope is unclear; it decides how
much gets rewritten.

## The ledger

Everything lives in one file, `docs/de-entropy/<subsystem>.md` (or the repo's
existing docs folder). It is written before any code changes, it is the
artifact the user approves, and it is updated as passes complete. Sections, in
order:

```markdown
# De-Entropy: <subsystem>

## Essence            3-10 sentences: what this subsystem actually is
## Concepts           each core concept, one line, one canonical name
## Invariants         rules that must hold, numbered
## Canonical order    layers/modules and the allowed dependency direction
## Entropy map        every finding, classified (table below)
## Plan               deletions, consolidations, rewrites, in commit order
## Uncertain          candidates not proven safe, with what would prove them
## Measure            before/after table
```

If the repo has a `CONTEXT.md` or glossary, the Concepts section reuses its
terms and the run ends by updating it (the `domain-modeling` skill owns that
file).

## Passes

Each pass ends on its completion criterion. Passes 0-4 change no code.

### 0. Observe

Map what exists: entry points, modules, domain concepts, data flow, state,
config, external dependencies, APIs, tests, hacks, and every name that refers
to a domain concept.

**Done when** every file in scope is listed in the ledger draft with a
one-line role, and every entry point is traced to where its data ends up.

### 1. Distill

Set the implementation aside and answer: **what is the irreducible idea?**
Write the Essence as the story the domain tells (`User creates Task → Task
enters Queue → Worker claims Task → Result stored`), then the Concepts and
Invariants it needs. Derive them from behaviour users and callers depend on:
UI, API contracts, persisted data, tests. Class names are evidence, not truth.

**Done when** every behaviour found in Observe is explained by the Essence,
Concepts and Invariants, or is listed as entropy.

### 2. Model

Write the Canonical order: the modules the Concepts imply and the one
direction dependencies flow (e.g. `interface → application → domain`,
`infrastructure → application`, `domain → nothing`). Match the size of the
order to the subsystem; a 300-line feature needs two modules, not four layers.
Use `codebase-design` for module depth and seams.

**Done when** each Concept has exactly one home and the dependency rule is
stated as arrows.

### 3. Entropy map

Classify every significant piece of the subsystem:

| Class | Meaning | Action |
| --- | --- | --- |
| core | the product needs it | keep |
| support | machinery the core needs | keep, move to its home |
| duplicate | one concept, many representations | consolidate |
| accidental | exists because of a past decision | rewrite or delete |
| dead | proven unreachable | delete |
| legacy | live, but the model has no place for it | migrate callers, then delete |
| boundary violation | right code, wrong layer | move |
| uncertain | cannot prove whether it matters | keep, list in Uncertain |

**Dead requires proof**: no static reference (grep every spelling, including
string-built names, reflection, routes, config, scripts, other repos in the
org), and no runtime use where telemetry exists. Anything short of proof is
**uncertain**, with the check that would settle it. Uncertainty is preserved,
never cleaned away.

**Done when** every file in scope carries a class and every duplicate names
the one representation that survives.

### 4. Approve

Fill in the Plan and the before column of Measure, then show the user the
ledger and stop. The Plan orders work so each step lands green on its own:
consolidate, then move, then rewrite, then delete. Rewriting starts only after
the user accepts the Canonical order; editing before that only rearranges the
mess.

**Done when** the user has approved the ledger, with their edits applied.

### 5. Collapse

Branch first. Consolidate duplicates onto the surviving representation, move
boundary violations home, delete what is proven dead. Before touching
behaviour that tests do not cover, write **characterization tests** that pin
what it does today; they are the contract the rewrite must keep.

**Done when** every consolidate/move/delete item in the Plan is done or moved
to Uncertain with a reason, and the suite is green.

### 6. Rewrite

When a module's model has changed substantially, **replace it**: write the new
implementation of the recovered model and move callers onto it in the same
change. A 1,400-line module that becomes 350 lines is the expected shape.

The rewrite ends **clean**: callers use the new code directly, and the old
code is deleted in the same pass. Every adapter, compatibility shim, wrapper or
migration helper left behind is new entropy and goes into the map. The one
exception is a boundary the repo does not control (a public API, a stored data
format, a mobile client already shipped): there, keep the old contract at the
edge and convert once, and record it as an invariant.

**Done when** every rewrite in the Plan is merged into the branch, old code
deleted, suite and characterization tests green.

### 7. Verify

Run the full test suite, type checks and linters, then launch the app and
drive each entry point traced in Observe. Every Invariant in the ledger has a
test or a stated reason it cannot.

**Done when** all checks are green and every entry point has been exercised
end to end.

### 8. Re-distill

Read the result as a newcomer would and fill the after column of Measure. Ask:
**is the code as simple as the model?** Anywhere the code still has more
concepts, names or layers than the ledger, run passes 3-7 again on that part.

**Done when** the after column matches the model: one representation per
concept, no live entries in the entropy map except Uncertain.

## Measure

Count, don't score. Before and after, for the subsystem:

| Metric | Before | After |
| --- | --- | --- |
| files / lines | | |
| concepts in the model | | |
| representations (types, classes, names) per concept, max and total | | |
| dependency edges against the canonical direction | | |
| entropy map items: accidental, duplicate, legacy, dead | | |
| uncertain items | | |

The goal is fewer concepts and representations, not prettier code. Lines going
down is a consequence, not the target.

## Commits

One commit per Plan item, each green, so any step reverts alone. The ledger
updates in the same commit as the work it records. The final commit message
summarizes the Measure table.
