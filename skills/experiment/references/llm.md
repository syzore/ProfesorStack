# LLM / generation experiments

Applies to prompt, model, temperature, generation strategy, curriculum/question generation. Use the project's existing LLM stack, evaluator and tracing; the examples name tools only where a project already has them.

## Versioning

- `PROMPTS = { "prompt_v1": ..., "prompt_v2": ... }` in git; the flag value is the key. Same for strategy/graph versions.
- Model and params can be a typed payload: `{ "model": "...", "temperature": 0.7 }`, validated against an allowlist; fallback = control config.
- Shipped versions never change; a new idea is a new id.

## Resolve once per run

Resolve the variant at the start of a run (after the user asked for generation = exposure), then pass it down. Don't re-resolve per step; a run must use one variant throughout.

With LangChain/LangGraph, put it in run metadata so traces carry it:

```python
config = {"metadata": {"experiment": "generation_prompt", "variant": v, "prompt_version": v}}
```

## Telemetry per generation

Record enough to compare quality and cost, and to reproduce any output later:

experiment, variant, prompt version, model, params, code version (git sha), latency, tokens, cost, automatic quality score, accepted/discarded, downstream action.

In PostHog, send these on the `$ai_generation` event (LLM analytics) plus `$feature/<key>` so results break down by variant.

## Automatic quality scores

If the project has an evaluator (e.g. Trellar confidence score, an LLM judge, PostHog evaluations), compare score distributions per variant. It works offline or on low traffic, before user metrics mean anything. It's a proxy: confirm the winner with a product metric (accepted, completed, retained).

If the evaluator isn't configured, the experiment still runs; just without that metric.

## Caching

Any cache of generated content keys on prompt version + model + params, or variants contaminate each other.

## Offline comparison

For batch/script generation (curriculum, question banks) where there's no live user, you can run variants side by side on the same inputs and compare scores, without a PostHog experiment. Still use versioned prompts and record the version on the stored output.

## Guardrails

Cost per generation, latency, error/retry rate, discard rate, output-schema validity.
