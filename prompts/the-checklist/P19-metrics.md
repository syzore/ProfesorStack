> Draft (basic) — pending Aviv's review.

# P19 · Metrics

Checklist: [the-checklist.md § Metrics](../the-checklist.md)

## What this step decides

Which numbers you track over time: request count, error rate, latency, traffic, database health, queue depth, job failures, external API failures, cost, authentication failures, one core business metric.

## How to think about it

- Start from the P3 observability requirements: what must be measurable per path. Each metric should be able to trigger a decision.
- Latency belongs as percentiles (p50, p99), matching the targets in P3 and the checks in P18.
- Cost is a metric. Track provider and LLM spend against the P3 monthly and per-user ceilings.
- Every production dependency needs a monitoring strategy (checklist rule). Database health, queue depth and external API failures are those hooks.
- Keep one core business metric visible, e.g. the activation event from P20, so you notice product failure that is not a technical error.

## Options and trade-offs

| Option | Good for | Cost |
|---|---|---|
| Host or platform metrics | Basic CPU, memory, requests | Limited custom metrics |
| Managed metrics/APM | Dashboards, percentiles, alerts | Per-host or per-series cost |
| Open-source (Prometheus style) | Control, low license cost | You operate it |

## How to choose: solo founder / pre-revenue defaults

- Use what the host gives free, plus a handful of app-level metrics.
- One dashboard with the listed items, readable in under a minute.
- Beware high-cardinality labels (user ID as a label) that blow up cost.

## Human in the loop: escalate when

- New paid monitoring vendor or tier.
- Metric collection that sends user-level or personal data to a third party.
- Cost metric shows spend above the P3 threshold that needs human approval.

## Done means

- Each listed metric exists or is `[N/A]` with reason.
- Dashboard values were checked against a known load or event.
- Each metric has an owner and a use (an alert or a review in P25).

## Depends on / feeds into

Phase depends on P3 · System architecture, P5 · Engineering foundation, P8 · Core product implementation. Feeds P19 · Alerts, P18 · Performance, P20 · Analytics and experimentation (business metric), P23 · Infrastructure / reliability (SLO and error budget).
