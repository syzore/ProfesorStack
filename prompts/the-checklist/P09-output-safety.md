> Draft (basic) — pending Aviv's review.

# P9 · Output safety

Checklist: [the-checklist.md § Output safety](../the-checklist.md)

## What this step decides

What the app does with model output before showing it or acting on it: validation, sanitizing, link and code handling, tool arguments, refusals, hallucinations, and when a human must review.

## How to think about it

- Model output is untrusted input. Validate it the way you validate a form submission from a stranger.
- Split by use: shown as text (sanitize and encode), parsed as data (schema-validate and reject on failure), executed or passed to a tool (validate arguments against an allow-list, never run it directly).
- Generated links and markup are an attack and a trust problem: strip or allow-list them.
- Hallucination handling is a product decision: where wrong answers are costly, show sources, hedge or refuse, and give the user a way to report errors.
- Decide the human-review path by stakes: the more irreversible or the more personal the result, the earlier a person sees it.

## Options and trade-offs

| Decision | Boring default | Heavier option | Pick the heavier one when |
| --- | --- | --- | --- |
| Structured output | Schema validation, retry once, then fail clearly | Repair heuristics | Failure rate is costly and measured |
| Display | Render as plain text or sanitized markdown | Rich HTML | Never render raw model HTML |
| Review | Spot-check sample plus user report button | Review every output | High stakes content |
| Refusal | Fixed, honest message | Custom per-case flows | Frequent legitimate refusals |

## How to choose: solo founder / pre-revenue defaults

- Schema in, schema out. On failure, fail visibly instead of guessing.
- Never execute model-generated code or shell, and never put model text in a query or URL unescaped.
- Start with sampling: read a handful of real outputs weekly.

## Human in the loop: escalate when

- Output can trigger an irreversible, financial, or identity-related action.
- The product gives advice in a high-stakes domain (health, legal, money). Compliance scope and liability are Aviv's call.
- Enabling any executable-output feature, or removing a human-review step.
- Hallucination rate in a sample is above what Aviv accepted.

## Done means

- Every output path is classified (display, data, action) and has the matching validation, with a failing-input test for each.
- The refusal and hallucination behaviors are written down and visible in the UI, and the review path has a named reviewer.

## Depends on / feeds into

Depends on P2 · Users, Trust and Data Model, P3 · System Architecture, P6 · Security Foundation, P7 · Privacy and Data Governance. Follows P9 · Model layer and P9 · Prompting. Feeds P9 · Agents / tools, P9 · Evaluation, P6 · Application security (output encoding, XSS).
