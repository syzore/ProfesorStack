> Draft (basic) — pending Aviv's review.

# P04 · UX

Checklist: [the-checklist.md § UX](../the-checklist.md)

## What this step decides
How the product behaves from the user's side: the primary journey, onboarding, all states (empty, loading, success, failure, offline, slow network), destructive actions and undo, navigation, deep links, refresh, and mobile and responsive behavior.

## How to think about it
- Start with the primary user journey from P0 · Product. Every other item supports it. If it takes more than a few steps, cut steps first.
- Define the unhappy states with the same care as the happy path: empty, loading, failure, offline, slow. These cause most support requests.
- Destructive actions need confirmation or undo. Undo is better: it keeps flow and costs a retention window (P2 · Data lifecycle).
- Deep links, back and refresh are state questions: decide what a URL contains and what survives a reload.
- Platform and responsive behavior follow the platforms in P0 · Product.

## Options and trade-offs
| Decision | Option | Pick when | Cost |
| --- | --- | --- | --- |
| Destructive action | Confirm dialog / undo | Confirm for rare or irreversible; undo for frequent | Undo needs soft delete |
| Offline | Online only / read cache / full offline | Online only unless the job must work offline | Sync and conflict logic for full offline |
| Mobile | Responsive web / native | Responsive web first | Native adds stores and releases |

## How to choose: solo founder / pre-revenue defaults
- Default: one primary journey, minimal onboarding, honest error text, online only, responsive web.
- Use the platform's standard components before custom ones.
- Use the repo's design skills (`impeccable`, `ui-design`, `design:ux-copy`) for layout, states and copy.
- Test the primary journey on a phone-width screen and on a slow connection.

## Human in the loop: escalate when
- A destructive or money action without confirm or undo.
- UX that changes what is collected, consent text or terms acceptance (P1 impact).
- Dark patterns or retention tricks.
- Adding a platform or offline mode (architecture and cost change).
- Final copy for legal, error or billing messages: Aviv approves.

## Done means
- Each item answered; every state in the journey has a defined screen or message.
- Primary journey is walkable by someone new in a test.
- UX items from P1 · Compliance deliverable are covered.

## Depends on / feeds into
Depends on: P0 · Product, P2 · Users and P2 · Identity (sign-in states), P3 · Architecture (platform). Feeds: P4 · Accessibility, P4 · Internationalization, frontend implementation, end-to-end tests.
