> Draft (basic) — pending Aviv's review.

# P01 · Industry-specific

Checklist: [the-checklist.md § Industry-specific](../the-checklist.md)

## What this step decides
Whether the product enters a regulated area: health, finance, education and minors, employment, security/surveillance, gambling, regulated products, biometrics, accessibility law, AI-specific regulation.

## How to think about it
- This is a screening list. Most items are "no, because X". Write X in one line; that line is the `[N/A]` reason.
- A "maybe" is a stop sign, not a to-do: it can add licensing or heavy duties that change the product.
- Accessibility can be a legal obligation by market or customer type. Record it here; P4 · Accessibility does the work.
- AI-specific rules are moving. Note current exposure and the date you checked.
- This guide is practical orientation, not legal advice. Where a legal point matters, confirm with counsel or Aviv.

## Options and trade-offs
| Answer | Meaning | Next |
| --- | --- | --- |
| No, with reason | Out of scope | Record `[N/A]` |
| Maybe | Unclear exposure | Counsel review before design |
| Yes | Regulated | Major scope change; decide go, narrow, or drop |

## How to choose: solo founder / pre-revenue defaults
- Default: design the product to stay out of regulated areas (no health claims, no minors, no payments you hold, no biometrics) unless that is the product.
- If a feature would enter a regulated area, cut or defer the feature before taking on the regime.

## Human in the loop: escalate when
- Any "maybe" or "yes" on health, finance, minors, employment, gambling, biometrics or surveillance.
- Regulated-product or AI-regulation exposure.
- Accessibility becomes a contractual or legal duty.
- This is always a compliance scope change; Aviv decides, with counsel.

## Done means
- Every industry item has yes, no-with-reason, or an open question assigned to counsel.
- Yeses and maybes are in the compliance applicability matrix.

## Depends on / feeds into
Depends on: P0 · Product, P1 · Jurisdiction. Feeds: P1 · Compliance deliverable, P2 · Users (age, roles), P4 · Accessibility, P3 · Non-functional requirements (privacy and compliance), P3 · Escalations.
