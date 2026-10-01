---
name: experiment
description: Use when adding or running an experiment (A/B test) on UI layout, copy, LLM prompts, models, generation params, curriculum or question generation - or when a feature has a dimension that might need multiple versions. PostHog is the control plane; Trellar scores LLM output; LangChain runs the generation. Covers the architecture, todos, todon'ts, and PostHog tricks.
---

# Experiments

Stack in every project: **PostHog** (flags + experiments + analysis), **Datafast** (acquisition / revenue attribution), **Trellar** (automatic LLM confidence score), **LangChain/LangGraph** (generation).

Roles, do not blur them:

| Tool | Role in an experiment |
| --- | --- |
| PostHog | assigns variants, records exposure, computes results |
| Trellar | quality metric for generation variants, no user traffic needed |
| Datafast | did the variant move traffic/revenue (outer funnel) |
| LangChain | consumes the variant config |

## Mental model

Not "A/B test the website". An **Experiment** is a named dimension with explicit variants and a safe control:

```
experiment key -> assignment (PostHog) -> variant/config -> app behavior -> events (tagged) -> PostHog analysis
```

Dimensions: generation (prompt, model, temperature, strategy), UI (layout, component, copy, CTA, order), behavior (item count, onboarding, refresh).

## Todos

1. **Wrap PostHog in one small module** (`experiments.ts` / `experiments.py`). App code calls `experiments.variant("key")` / `experiments.payload("key")`, never PostHog directly. One place to add overrides, fallbacks, tagging.
2. **One experiment per hypothesis.** `generation_prompt`, `generation_model`, `landing_layout`, `landing_copy` run independently. Combine only if the combined experience is the thing under test.
3. **Every experiment has:** unique key, explicit variants, safe control, exposure event, primary metric, optional secondary metrics, written hypothesis. Put the hypothesis in the PostHog flag/experiment description and in a code comment at the registry.
4. **Registry in code**: a typed map `key -> {control, variants[]}`. Unknown variant from PostHog -> control. Gives agents and reviewers one place to see what is live.
5. **Prompts live in git, flag picks the version.** Flag value = `prompt_v3`, code maps `PROMPTS["prompt_v3"]`. Never put prompt text in PostHog. Prompt versions are immutable once shipped; substantial change = new version.
6. **Copy**: use a JSON payload (`headline`, `subtitle`, `cta`) so one variant swaps several strings. Default copy lives in code as the fallback.
7. **Layout**: variant string -> render branch. Don't fork whole pages when only config differs.
8. **Fail open to control**: PostHog down / slow / malformed / missing -> control, never block render or generation. Short timeout on server flag calls.
9. **Dev override**: force any variant locally without traffic (env var `EXPERIMENT_OVERRIDES=landing_layout=cards,generation_prompt=prompt_v3`, or `posthog.featureFlags.overrideFeatureFlags({...})` on web, plus a `?exp_landing_layout=cards` URL param in dev builds only). Overrides must be ignored in production.
10. **Tag events, don't rename them.** Same event name for all variants; carry experiment + variant as properties. Web SDK auto-adds `$feature/<key>` to captured events; on the server add it yourself (`properties={"$feature/generation_prompt": v}`).
11. **Generation experiments record**: experiment, variant, prompt version, model, temperature, latency, tokens, cost, **Trellar score**, accepted/discarded, downstream action. Send as PostHog LLM analytics `$ai_generation` (set `$ai_model`, tokens, latency) plus the `$feature/...` tag so results are sliceable by variant.
12. **Use Trellar as the fast metric** for prompt/model/curriculum/question experiments: compare score distributions per variant before real users weigh in. It is a proxy; confirm winners with a product metric (accepted, completed, retained).
13. **Same identity across the stack.** Pass the web `distinct_id` to the backend (header or request field) and use it for server flag eval + event capture, otherwise assignment differs between client and server and the variant is not sticky. Anonymous -> logged-in: call `identify` (PostHog merges); don't mint a new id.
14. **Clean up.** Finished experiment = ship the winner, delete losing variants and branching, remove registry entry and env config, archive the flag. Put a review date in the hypothesis. Dead experiments are debt.
15. **New feature?** Ask once whether a meaningful dimension deserves a variant. "Test another version" = add a variant to the existing experiment, not a new mechanism.

## Todon'ts

- No `Math.random()`, no DB assignment tables, no cookie-based home-rolled bucketing.
- No direct `posthog.getFeatureFlag` scattered across components.
- No prompt text, long copy, or secrets in flag payloads.
- No Cartesian products (prompt x model x layout x copy) unless that combination is the hypothesis.
- No per-variant event names (`signup_variant_b`). Same event, variant property.
- No re-randomizing per request. Don't evaluate flags without a stable `distinct_id`.
- No editing a live prompt version in place; no changing variants/rollout mid-experiment (restarts validity, biases results).
- No peeking-and-stopping on first significant blip. Decide sample size / duration up front.
- No experimenting on tiny traffic with small effects (see power below). Don't experiment merely for the sake of it.
- No blocking first paint on flag load.
- No LLM variant that changes the output schema without handling it downstream.

## Tools and tech stack

- **posthog-js** (web): `getFeatureFlag`, `getFeatureFlagPayload`, `onFeatureFlags`, `overrideFeatureFlags`. **posthog-node / posthog-python** (server): `get_feature_flag`, `get_feature_flag_payload`. Server flags cost a network call per eval unless **local evaluation** is on (needs a personal API key + polling); enable it on hot paths like generation.
- **PostHog MCP** (`mcp__plugin_posthog_posthog__exec`): agents can create/update flags, create experiments, query results, find stale flags. Skills: `posthog:creating-experiments`, `configuring-experiment-rollout`, `configuring-experiment-analytics`, `debugging-experiments`, `diagnosing-experiment-results`, `managing-experiment-lifecycle`, `cleaning-up-stale-feature-flags`, `instrument-feature-flags`, `instrument-llm-analytics`. Load those instead of re-researching.
- **Experiments product vs plain flag**: use an Experiment when you want significance/Bayesian results and a defined primary metric; plain multivariate flag for rollouts, kill-switches, or when you only watch an insight.
- **LangChain**: resolve the variant once per run, then pass it in the run config / metadata (`config={"metadata": {"experiment": ..., "variant": ..., "prompt_version": ...}}`) so LangSmith/Trellar traces carry it. Build the prompt template from the registry, not inline.
- **Trellar**: score each generation run; store score on the `$ai_generation` / result event. Missing key = scoring off, experiment still runs.
- **Datafast**: outer-funnel signal (landing copy/layout -> visits -> signups -> revenue). Attach the landing variant as a custom property/goal parameter if its API supports it (verify in its docs, not verified here); otherwise join through PostHog.

## Tricks and tips

- **Exposure = `$feature_flag_called`.** Fires when the flag is read, so read the flag at the point the user *sees* the thing, not at app boot, or the control/variant populations include people who never saw it. For server-only experiments the server read is the exposure.
- **Avoid flicker**: bootstrap flags (server-render with the evaluated flags and pass to `posthog.init({bootstrap})`), or render control skeleton / reserve space until flags load. Never swap layout after paint.
- **Sample size first.** At 1-3 users nothing reaches significance. Use experiments only when traffic can detect the effect; before that, use Trellar scores and qualitative review, or ship by judgment. Rough: detecting a 10% relative lift on a 10% base rate needs thousands per arm.
- **Pick the metric near the change.** Prompt change -> accepted/completed, not revenue. Landing copy -> signup, not retention. Far metrics are noise.
- **Guardrail metrics**: also watch latency, cost per generation, error rate, discard rate so a "winner" isn't just slower/pricier.
- **Rollout %**: start 50/50 for clean results; for risky variants start small with a kill-switch flag, then widen (changes the experiment, so restart).
- **Holdouts and mutual exclusion**: independent experiments overlap by default, fine for orthogonal ones. If two touch the same screen, use mutually exclusive groups or run sequentially.
- **Persistence**: a flag keyed on person property, not session, keeps the variant across devices post-login. Use "persist flag across authentication steps" for funnels that cross login.
- **Bot / internal traffic**: filter before reading results (`posthog:filtering-bot-traffic`). Exclude your own team and the synthetic-user swarm via a person property.
- **Offline / mobile (Flutter)**: cache last-known variants locally, evaluate on launch, fall back to control. Variant must not flip mid-session.
- **Cache keys include variant**: any cache of generated content (see `caching-llm-data-scripts`) must key on prompt version + model, or variants contaminate each other.
- **Naming**: flag key `snake_case` = dimension (`generation_prompt`), variants = value (`prompt_v3`, `cards`). `control` is always the default key. Avoid dates/people in keys.
- **Reading results**: if inconclusive, say so and ship the cheaper/simpler variant. Don't extend the test until something turns significant.
- **Replays**: `posthog:analyzing-experiment-session-replays` for the "why" behind a UI result.

## Minimal shape

```ts
// experiments.ts - only file that imports posthog for flags
const REGISTRY = {
  generation_prompt: { control: "prompt_v1", variants: ["prompt_v1", "prompt_v2", "prompt_v3"] },
  landing_layout:    { control: "grid",      variants: ["grid", "cards", "minimal"] },
} as const;

export function variant<K extends keyof typeof REGISTRY>(key: K): string {
  const { control, variants } = REGISTRY[key];
  const forced = devOverride(key);                  // ignored in prod
  const v = forced ?? safeGetFlag(key);             // try/catch + timeout, undefined on failure
  return (variants as readonly string[]).includes(v ?? "") ? v! : control;
}
```

```python
# experiments.py
def variant(key: str, distinct_id: str) -> str:
    reg = REGISTRY[key]
    try:
        v = override(key) or posthog.get_feature_flag(key, distinct_id)
    except Exception:
        v = None
    return v if v in reg.variants else reg.control
```

## Checklist before shipping an experiment

- [ ] Hypothesis + primary metric + guardrails written
- [ ] Registry entry with control; unknown/failed flag -> control
- [ ] Flag read at exposure point; no flicker
- [ ] Events carry experiment/variant; generation events carry prompt/model/Trellar/cost
- [ ] Dev override works for every variant
- [ ] Same `distinct_id` client + server
- [ ] Sample size / duration decided; review date set
- [ ] Cleanup plan: what gets deleted when it ends
