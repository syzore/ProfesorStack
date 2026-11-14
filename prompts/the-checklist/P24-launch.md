> Draft (basic) — pending Aviv's review.

# P24 · Launch

Checklist: [the-checklist.md § Launch](../the-checklist.md)

## What this step decides

The final go/no-go: production smoke tests (general, analytics, critical API, critical flow), backup verification, sign-off, and a prepared rollback decision.

## How to think about it

- Smoke tests run on production, after deploy, and are short and read-only where possible.
- Sign-off is Aviv's decision, with the other P24 sections as evidence.
- Prepare the rollback decision before launch: who calls it, what triggers it, how long it takes.

## Options and trade-offs

No real fork here. Do the items, and record any `[N/A]` or `[DEFER]` with its reason or trigger.

## How to choose: solo founder / pre-revenue defaults

- Reuse P17 journeys as smoke tests.
- Launch on a quiet day with you available, not on a Friday evening.
- Soft launch to a few users first if risk is high.

## Human in the loop: escalate when

- The sign-off itself.
- A failing smoke test or an unverified backup, with pressure to ship anyway.
- Any launch step that sends real money or real emails to real users.

## Done means

- All smoke tests pass on production.
- Sign-off recorded with date.
- Rollback trigger and owner written down.

## Depends on / feeds into

Phase depends on all required prior gates. Launch checks verify earlier work; they do not replace it. Fed by every other P24 section. Feeds P25 · Post-launch operations.
