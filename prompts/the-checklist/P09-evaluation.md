> Draft (basic) — pending Aviv's review.

# P9 · Evaluation

Checklist: [the-checklist.md § Evaluation](../the-checklist.md)

## What this step decides

How you know the AI feature works and keeps working: golden sets, regression, quality, safety, cost and latency tests, and re-testing whenever the model, prompt or fallback changes.

## How to think about it

- Evaluation is how a prompt or model change becomes a decision instead of a hunch. Without it you cannot change anything safely.
- Start small: a golden set of real or realistic inputs with expected properties (not exact strings). Grow it from every production failure.
- Separate dimensions: quality, safety (injection, leakage, refusals), cost per request, latency. A change can win on one and lose another.
- Model-change, prompt-change and fallback evaluation are the same harness run at different triggers. The fallback path must be tested, since it is the path nobody sees.

## Options and trade-offs

| Decision | Boring default | Heavier option | Pick the heavier one when |
| --- | --- | --- | --- |
| Scoring | Programmatic checks and rubric | LLM judge | Subjective quality at volume (validate the judge against human labels) |
| Cadence | Run before each prompt or model change | Continuous in CI | Change frequency is high |
| Dataset | Dozens of curated cases | Large synthetic sets | Coverage gaps measured |

## How to choose: solo founder / pre-revenue defaults

- Twenty to fifty real cases beats a framework. Store them in the repo and run with one command.
- Record a baseline score and a cost and latency figure, treating them as examples to be re-measured.
- Use a stronger model as judge only after checking agreement with your own labels.

## Human in the loop: escalate when

- Defining what good means for a product-critical feature (a taste and risk call).
- Accepting a regression in quality or safety to save cost.
- Adding paid evaluation tooling or sending real user data into an evaluation vendor.
- A safety test failing for any reason, since launch decisions are Aviv's.

## Done means

- A golden set and a one-command run exist, with a recorded baseline for quality, safety, cost and latency.
- Any model, prompt or fallback change is gated by the run, and failures from production become new cases.

## Depends on / feeds into

Depends on P2 · Users, Trust and Data Model, P3 · System Architecture, P6 · Security Foundation, P7 · Privacy and Data Governance. Follows all other P9 sections. Feeds P17 · Testing (AI testing), P18 · Performance, P24 · Launch Readiness.
