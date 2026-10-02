# PostHog implementation notes

PostHog's SDKs and experiments product change often. Treat this as a starting point and confirm against current docs or the PostHog skills below before relying on a method name.

## SDK calls (as of 2026-10)

- Web (`posthog-js`): `getFeatureFlag(key)`, `getFeatureFlagPayload(key)`, `onFeatureFlags(cb)`, `featureFlags.overrideFeatureFlags({...})` for local overrides, `init({ bootstrap: { distinctID, featureFlags } })` to avoid flicker when the server already evaluated flags.
- Server (`posthog-python` / `posthog-node`): `get_feature_flag(key, distinct_id)`, `get_feature_flag_payload(...)`. Each call is a network round trip unless **local evaluation** is enabled (personal API key, flag definitions polled). Turn it on for hot paths like generation.
- Flutter (`posthog_flutter`): flags load async; cache last-known variants, fall back to control on first launch, don't flip mid-session.

## Exposure

- Experiments resolve exposure to `$experiment_exposure` by default (the experiment's `resolved_exposure_event`, verified 2026-10-01); SDK flag reads still send `$feature_flag_called`. Either way *where you read the flag* is the exposure point unless a custom exposure event is configured.
- Experiments can instead use a custom exposure event (e.g. `generation_started`). Prefer that when the flag must be read earlier than the real exposure.
- Server-side reads send `$feature_flag_called` too (unless disabled); make sure the same `distinct_id` as the client is used.

## Tagging events

- Web SDK adds `$feature/<key>` to captured events automatically.
- Server events: add `$feature/<key>: <variant>` yourself so they can be broken down by variant.

## Identity

- Pass the browser/app `distinct_id` to the backend (header or request field) for server flag evaluation and capture.
- On login call `identify`; enable "persist flag across authentication steps" for flags whose funnel crosses login.

## Experiment vs plain flag

- Experiment: you want results against a primary metric, with PostHog's statistics (confidence thresholds, MDE, CUPED are configured there).
- Multivariate flag alone: rollouts, kill switches, remote config.

## Agent tooling

PostHog MCP (`exec`) can create/update flags and experiments and query results. Load the matching PostHog skill instead of re-researching:

`posthog:creating-experiments`, `configuring-experiment-rollout`, `configuring-experiment-analytics`, `debugging-experiments`, `diagnosing-experiment-results`, `managing-experiment-lifecycle`, `cleaning-up-stale-feature-flags`, `instrument-feature-flags`, `instrument-llm-analytics`, `analyzing-experiment-session-replays`, `filtering-bot-traffic`, `auditing-experiments-flags`.

## Other analytics

If the project also has a web-analytics/attribution tool (e.g. Datafast), use it for outer-funnel signal on landing experiments only; PostHog remains the source of truth for results. Check that tool's docs for how to attach a variant; don't assume.
