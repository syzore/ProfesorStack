> Draft (basic) — pending Aviv's review.

# P04 · Accessibility

Checklist: [the-checklist.md § Accessibility](../the-checklist.md)

## What this step decides
The standard of access the product meets: keyboard, focus, screen-reader support, names and labels, contrast, text and zoom, motion, touch targets, and accessible dialogs, notifications, charts and media, plus how it is tested.

## How to think about it
- Pick a target level first, commonly WCAG 2.2 AA, and say so. Everything below is a way to meet it.
- Build it in from the first component. Retrofits cost far more than doing it right once, and semantic HTML gives most of it free.
- Cover the keyboard-only critical journeys end to end: if the primary journey needs a mouse, it fails.
- Color is never the only signal; errors are tied to their fields; focus is visible and in a sensible order.
- Automated tools catch a fraction of issues. Manual checks (keyboard, a screen reader, zoom to 200%) are required for the critical journey.
- The `compliance` skill audits against WCAG 2.2 AA for web projects.

## Options and trade-offs
| Check | Automated | Manual |
| --- | --- | --- |
| Contrast, labels, names | Yes | Spot check |
| Focus order, keyboard traps | Partly | Required |
| Screen-reader flow | No | Required for critical journey |
| Zoom and text resize | No | Required |
| Reduced motion | Partly | Check once |

## How to choose: solo founder / pre-revenue defaults
- Default: target WCAG 2.2 AA; use native elements and a component library with accessibility built in; add an automated checker in CI; do a manual keyboard and screen-reader pass of the primary journey before launch.
- `[N/A]` is rarely right here; items like accessible media apply only if media exists, and then say so.
- Charts: give a text or table alternative.

## Human in the loop: escalate when
- Any shipped exception to the target level or a known failing item.
- Accessibility is a legal or contractual duty (P1 · Industry-specific): confirm scope with counsel.
- Accessibility overlay or paid third-party tools (new vendor).
- Conformance claims on the site or in contracts: Aviv approves wording.

## Done means
- Target level stated; each item addressed or `[N/A]` with reason.
- Automated checks run; a manual pass of the primary journey is recorded with date.
- Known gaps are listed with owners.

## Depends on / feeds into
Depends on: P4 · UX, P1 · Industry-specific (legal duty), P3 · Architecture (frontend). Feeds: frontend implementation, accessibility tests in P17 · End-to-end, P24 · Launch.
