> Draft (basic) — pending Aviv's review.

# P01 · Compliance deliverable

Checklist: [the-checklist.md § Compliance deliverable](../the-checklist.md)

## What this step decides
The written output of P1: matrices and lists that later phases read. P1 produces these artifacts; it implements nothing.

## How to think about it
- The jurisdiction matrix: rows are places, columns are the roles those places play (users, hosting, payments, staff, stores).
- The compliance applicability matrix: rows are regimes or obligations, columns are applies, why, owner and the phase that implements it. Every N/A gets its reason here.
- The impact lists say where a requirement bites: architecture, UX, data storage, logging, marketing, launch. This is how P1 reaches P3, P4 and the P24 · Launch.
- The professional-review list is short: only questions counsel must answer, each phrased as a question with the facts.
- This guide is practical orientation, not legal advice. Where a legal point matters, confirm with counsel or Aviv.

## Options and trade-offs
| Artifact | Reader | Failure if missing |
| --- | --- | --- |
| Jurisdiction matrix | Later phases, counsel | Scope guessed again each phase |
| Applicability matrix | Everyone | N/A decisions lost |
| Counsel questions | Aviv, counsel | Legal risk discovered at launch |
| Impact lists | P3, P4, launch | Requirements found after build |

## How to choose: solo founder / pre-revenue defaults
- Keep it one document, tables over prose, so an agent can scan it.
- Date every entry; laws and your facts change.
- Each impact list item names the phase that must act, using the `P<N> · <Heading>` form.

## Human in the loop: escalate when
- Anything on the counsel list: Aviv decides whether and when to engage.
- A requirement that would force a major architecture or product change.
- Marketing or launch constraints with legal weight.
- Changing a recorded N/A to applicable later (compliance scope change).

## Done means
- Both matrices exist with no blank cells.
- Every N/A has a reason; every impact item has an owning phase.
- Counsel questions are listed with facts, even if not yet sent.

## Depends on / feeds into
Depends on: P1 · Jurisdiction, P1 · Privacy, P1 · Commercial/legal, P1 · Industry-specific. Feeds: P2 · Data inventory, P3 · Non-functional requirements, P3 · Architecture decisions, P4 · UX, P19 · Logging, P24 · Launch.
