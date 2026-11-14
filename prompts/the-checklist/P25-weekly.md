> Draft (basic) — pending Aviv's review.

# P25 · Weekly

Checklist: [the-checklist.md § Weekly](../the-checklist.md)

## What this step decides

The weekly review: dependency updates, security, product analytics, cost, errors, dead code, backup verification, performance, user feedback.

## How to think about it

- Weekly is where trends show: slowly growing cost, latency drift, repeated errors.
- Dependency updates should be small and frequent so none becomes a big-bang upgrade.
- Backup verification is a periodic restore or integrity check, not just "job succeeded".
- Compare performance with the P3 targets and the P18 baseline.

## Options and trade-offs

| Mode | Good for | Cost |
|---|---|---|
| Manual review | Judgment, product sense | Time |
| Automated bot PRs plus agent summary | Dependencies, dead code, cost | Setup, review noise |

## How to choose: solo founder / pre-revenue defaults

- One 30 to 60 minute slot. Automate dependency PRs and let an agent prepare the numbers.
- Keep a one-line log of what was changed each week.

## Human in the loop: escalate when

- A major version upgrade or dependency with a security fix that changes behavior.
- Cost review shows spend above the P3 ceiling.
- Deleting data or code whose purpose is unclear.

## Done means

- Each item has a dated note: looked, nothing, or acted.
- Findings are filed as tracked items.

## Depends on / feeds into

Phase depends on P24 · Launch readiness. Fed by P19, P20 · Analytics and experimentation, P23. Feeds P25 · Monthly/periodic and P27.
