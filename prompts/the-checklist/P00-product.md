> Draft (basic) — pending Aviv's review.

# P00 · Product

Checklist: [the-checklist.md § Product](../the-checklist.md)

## What this step decides
What the product is, for whom, and when to stop. Every later phase reads from these answers: scale, platforms and launch date feed P3, target user and geography feed P1 and P2.

## How to think about it
- Write the one-sentence description so a stranger can say who it is for and what they do with it. If it needs "and", it is two products.
- Primary user problem, primary action and primary value are one chain. If you cannot trace problem to action to value, the MVP is not defined yet.
- Non-goals matter as much as goals. They are what the agent may refuse to build.
- Success, failure and kill criteria need numbers and a date, e.g. "20 weekly active users by week 8; below 5 at week 12 means stop". An adjective is not a criterion.
- Expected scale, frequency, geography and platforms are estimates. Write the guess and the reason; P3 and P1 test them.

## Options and trade-offs
| Decision | Options | Pick when |
| --- | --- | --- |
| Product type | prototype / MVP / production / internal tool / experiment | Prototype or experiment if the goal is learning; production only once users pay or depend on it |
| Platforms | web only / web + mobile / native | Web only unless the primary action needs a device capability |
| MVP cut | one core loop / several features | One core loop: the smallest thing that delivers the primary value |

## How to choose: solo founder / pre-revenue defaults
- Default type is MVP or experiment. Say so in the checklist; it licenses skipping heavy items with a reason.
- One platform, one geography, one language at first.
- Kill criteria are not optional: a solo founder has no one else to call time.
- Launch date: only a hard external constraint counts (event, partner). Otherwise write "none" and a target.

## Human in the loop: escalate when
- Target user or primary problem cannot be named in one sentence: stop and ask Aviv. Guessing here poisons every later phase.
- The MVP scope grows past one core loop.
- Success, failure or kill criteria are missing or set without Aviv.
- A non-goal is being reversed (scope change).
- Geography widens, which changes P1 scope.

## Done means
- Every Product item is `[x]`, `[N/A]` with a reason, or `[DEFER]` with a trigger.
- A reader can state who, what problem, what MVP, what non-goals, and when it is killed.
- Criteria carry numbers and a review date.

## Depends on / feeds into
Depends on: nothing. Feeds: P0 · Business (price must fit the user), P0 · Product risks (assumptions come from here), P1 · Jurisdiction (geographic scope), P3 · Non-functional requirements (scale, platforms), P4 · UX (platforms, primary journey).
