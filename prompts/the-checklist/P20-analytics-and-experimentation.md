> Draft (basic) — pending Aviv's review.

# P20 · Analytics & Experimentation

Checklist: [the-checklist.md § Analytics & Experimentation](../the-checklist.md)

## What this step decides

How product behavior is measured and how changes are tested: events, identities, funnel, KPIs, retention, then experiments, flags, metrics, sample size, ramp and kill criteria.

## How to think about it

- Start from the questions a founder will actually ask: do people activate, do they come back, where do they drop off.
- Define a small, named event set with one naming convention. Events without a decision attached are noise.
- Identity has two states (anonymous, authenticated) and a join between them. Decide it with P2 and P7 in mind, and avoid unnecessary PII.
- Keep product events separate from error events so neither pollutes the other.
- Experiments need a primary metric, guardrail metrics, a sample-size plan and kill criteria before launch, not after.
- At small traffic, most A/B tests cannot reach significance. Be honest about power; use qualitative feedback instead.
- Feature flags need an expiry. A stale flag is code debt (P27).

## Options and trade-offs

| Option | Good for | Cost |
|---|---|---|
| Hosted product analytics | Fast funnels, flags, experiments | Vendor, privacy, per-event cost |
| Self-built events in own database | Control, no third party | Build and query effort |
| No experiments yet | Pre-traffic stage | Slower learning, zero cost |

## How to choose: solo founder / pre-revenue defaults

- Pick one hosted tool or your own database, not both. Fewer than 15 events at first.
- Define the activation event and one funnel before anything else.
- Defer the experiment framework until there is enough traffic to reach a result in a reasonable time, e.g. weeks. Record that as `[DEFER]` with the trigger.
- Verify accuracy by performing a journey and checking the events arrive once with correct properties.

## Human in the loop: escalate when

- Adding a paid analytics or experimentation vendor.
- Collecting new personal data or enabling cross-site tracking (consent and compliance scope, P1 and P7).
- Changing identity linking between anonymous and authenticated users.
- Running an experiment that affects pricing or billing.

## Done means

- Event schema, naming convention and identity rules are written down.
- Analytics accuracy is VERIFIED against a real journey.
- Experiment items each have a decision or an explicit `[DEFER]` trigger.

## Depends on / feeds into

Depends on P2 · Users, trust and data model, P4 · UX, P7 · Privacy and data governance, P8 · Core product implementation. Feeds P24 · Product (analytics verified), P26 · Growth (funnels, experiment pipeline) and P27 (flag cleanup).
