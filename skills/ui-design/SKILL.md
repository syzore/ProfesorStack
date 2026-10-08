---
name: ui-design
description: The method for any UI or UX work, from references to critique. Use when designing, redesigning or critiquing a screen, flow, component or page.
---

# UI design

Run the steps in order. The designer runs 1–5; `design-critic` runs 6, routed by the design-manager.

1. **References.** The brief carries Aviv's references (inspiration images, screenshots, layout sketches, mocks) or his explicit "none". The co-founder collects them, since agents cannot ask Aviv. A brief with neither: stop and hand back asking for them.
2. **Real-world patterns.** `mobbin:search` (Cursor: `search`) for real app screens and flows that match the task; collect a few, with links. Reworking an existing screen: `mobbin:redesign-screen` (Cursor: `redesign-screen`).
3. **Options.** `prototype` builds 2–3 throwaway variants, compared side by side, per `principle-exhaust-the-design-space`. Pick one.
4. **Craft.** `impeccable` sets the direction and polishes the chosen variant.
5. **Interface text.** Every label, button, empty state and error goes through `unslop` and `design:ux-copy` (Claude Code only).
6. **Critique.** `design-critic` reviews with `impeccable` in critique/audit mode, plus `compliance` for accessibility. The designer resolves each finding: fixed, or kept with a reason.

## Report

Write the report the designer hands up through `mobbin:plain-writing` (Cursor: `plain-writing`).

Done when the report carries every step's output:

- the references used, and what each one decided
- the Mobbin links
- the prototype variants, the chosen one and why
- each critique finding and how it was resolved
