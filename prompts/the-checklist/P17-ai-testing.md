> Draft (basic) — pending Aviv's review.

# P17 · AI testing

Checklist: [the-checklist.md § AI testing](../the-checklist.md)

## What this step decides

How the AI features are tested: prompt-injection, output validation, data leakage, tool abuse, cost abuse, hallucination/quality, regression suite, model replacement.

## How to think about it

- Only applies if P9 · AI / LLM is in scope. Otherwise `[N/A]`.
- Every AI capability needs cost, abuse, privacy, reliability and evaluation behavior (checklist rule). These tests are the evidence.
- LLM output is nondeterministic, so test properties (valid schema, no leaked secret, refusal on abuse) more than exact strings.
- A fixed eval set of real and adversarial inputs is the regression suite. Rerun it on every prompt or model change; model replacement is just that rerun on the new model.
- Cost abuse means a user or loop that burns tokens. Test the cap, not just the happy path.

## Options and trade-offs

| Check | Method | Cost |
|---|---|---|
| Schema and policy validation | Deterministic code | Cheap, run always |
| Quality scoring | Eval set, rubric or LLM judge | Token spend, judge bias |
| Human spot check | Sample reviewed by Aviv | Time, but catches what judges miss |

## How to choose: solo founder / pre-revenue defaults

- Start with 20 to 50 eval cases, e.g. a mix of normal, edge and hostile. Grow it from real failures.
- Run the suite on demand and before changing a model or prompt, not on every commit, to limit token cost.
- Hard per-user and per-day token caps tested before launch.

## Human in the loop: escalate when

- Switching to a more expensive model or adding a paid eval/judge vendor.
- A leakage test shows personal or secret data in output.
- Changing the quality threshold that gates a release.

## Done means

- Each listed test has a result recorded against a named eval set.
- Injection, leakage and tool-abuse failures are fixed or explicitly accepted by Aviv.
- Model replacement can be run as a single command.

## Depends on / feeds into

Phase depends on P8 and relevant modules; this step depends on P9 · AI / LLM (especially Evaluation, Output safety, Agents/tools). Feeds P24 · Security and P19 · Metrics (cost).
