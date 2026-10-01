---
name: experiment
description: Use when adding, changing or concluding an experiment (A/B test) - UI layouts, copy, LLM prompts, models, generation params - or when a new feature has a dimension that may need multiple versions. PostHog is the control plane. Covers architecture, the experiment contract, exposure, fallbacks, lifecycle and anti-patterns.
---

# Experiments

**PostHog decides which experience a user gets. Git defines what each experience is. Analytics records what happened. The experiment definition says what we're trying to learn.**

PostHog is the only assumed tool. For anything else (LLM stack, evaluators, other analytics), use what the project already has; don't install tools because a reference mentions them.

References, load when relevant:
- `references/posthog.md` - SDK calls, exposure config, overrides, MCP skills
- `references/llm.md` - prompt/model/generation experiments and their telemetry

## 1. Pick the right primitive

| Primitive | Question | Example |
| --- | --- | --- |
| Feature flag | Should this exist for this user? | `new_editor` |
| Remote config | Which value should this use? | `max_cards = 5` |
| Experiment | Which variant, and what happened? | `generation_prompt`, `landing_copy`, `landing_layout` |

Only an experiment needs a hypothesis and a metric. Don't make an experiment out of a config value nobody is measuring. Don't experiment for the sake of it.

## 2. Architecture

- **One wrapper module** (`experiments.ts` / `experiments.py` / `experiments.dart`). App code asks `experiments.variant("key")` / `experiments.config("key")`; nothing else imports the flag SDK.
- **Ownership split.** PostHog owns assignment, allocation and rollout. Code owns the implementation of each variant and validates which values it supports. An unsupported value from PostHog is treated as missing.
- **PostHog picks WHICH version, git holds WHAT it is.** `generation_prompt = prompt_v7` -> `PROMPTS["prompt_v7"]`; `landing_layout = cards_v2` -> `layouts/cards_v2`; `homepage_copy = copy_v4` -> `copy/copy_v4`. No prompt text, long copy or secrets in PostHog.
- **Shipped versions are immutable.** A substantial change is a new version id, so any past event can be traced to experiment, variant, version, model/params and code version.
- **Assignment is sticky.** Same stable user id on client and server; no re-randomizing per request; anonymous -> identified keeps the same assignment.

## 3. Experiment contract

Every experiment has a definition, kept next to the wrapper (YAML or typed constant) and mirrored in the PostHog description:

```yaml
key: generation_prompt
hypothesis: "prompt_v3 increases accepted ideas"
surface: idea_generation
eligibility: users who click Generate     # who can enter
allocation: equal                         # how eligible users split
exposure: generation_started              # when they count as in
variants: { control: prompt_v1, a: prompt_v2, b: prompt_v3 }
payload_schema: none                      # or typed fields + defaults
primary_metric: idea_accepted / exposed
guardrails: [generation_cost, generation_latency, generation_error]
decision: ship best variant if PostHog shows a meaningful lift and no guardrail regresses
review_after: 2026-10-15
```

- **Eligibility is separate from allocation.** Decide who can enter (reaches the screen, new users, locale, platform), then how they split.
- **Payloads are typed.** Required fields, allowed values, defaults. Unknown or malformed -> the safe default, never a crash. Adding fields stays backward compatible with the code's defaults.
- **Decision rule written before launch.** With enough traffic, state the expected effect and stopping criterion. With low traffic, results are directional, not proof; say so when reporting.

## 4. Exposure

A user enters the experiment when they actually meet the changed experience, not when some code happened to read the flag.

- UI: surface becomes visible -> exposure -> interaction.
- Generation: user clicks Generate -> resolve variant -> generation starts (exposure) -> result.
- Reading the flag at app boot for a surface most users never reach pollutes both arms. Resolve at the exposure point, or configure a custom exposure event in PostHog.
- Don't block first paint on flags, and don't swap a layout after paint.

## 5. Measurement

- Same event name for all variants; experiment and variant ride as properties.
- Primary metric close to the change (prompt -> accepted/completed; copy -> click/signup), plus guardrails (latency, cost, errors, discard rate).
- Filter internal, bot and synthetic traffic before reading results.
- Let PostHog do the statistics. Inconclusive -> say so, ship the simpler/cheaper variant, don't extend until something looks significant.

## 6. Multiple experiments

- **Default: one experiment per independent hypothesis.** Combine dimensions deliberately only when their interaction is the hypothesis.
- **Before creating one, check active experiments on the same surface/journey.** If variants could interact (copy and layout on the same hero), reuse the existing experiment, make them mutually exclusive, or run them in sequence.
- "Test another version" = add a variant to the existing experiment, not a new mechanism.

## 7. Fallbacks, dev, testing

- PostHog unavailable, slow, malformed or missing -> control. Never block the user. Short timeouts on server calls.
- Dev override to force any variant without traffic (env var / URL param in dev builds); ignored in production.
- Tests cover control and each variant through the override, plus the fallback path.

## 8. Lifecycle

`draft -> development -> running -> paused -> concluded -> cleaned_up`

- **Allocation changes** (10% -> 25% -> 50%) are allowed for risky variants, but each change starts a new phase; before/after results aren't directly comparable. Same for adding/removing variants. Default to equal allocation unless risk or cost argues otherwise.
- **Pause** rather than delete when something breaks.
- **Conclude**: record the decision and result in the definition.
- **Clean up**: keep the winner, delete losing variants and branching, remove the definition and config, archive the flag. Don't let dead experiments accumulate.

## Anti-patterns

- `Math.random()`, DB assignment tables, home-rolled cookie bucketing (unless PostHog provably can't do it, documented).
- Flag SDK calls scattered through components.
- Prompt text or big blobs in flag payloads.
- Per-variant event names (`signup_variant_b`).
- Exposure at app boot for a deep surface.
- Cartesian products by accident (prompt x model x layout x copy).
- Editing a shipped version in place.
- Duplicating whole pages when only config differs.
- Output-schema-changing LLM variants with no downstream handling.
