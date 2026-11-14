> Draft (basic) — pending Aviv's review.

# P25 · Daily/continuous

Checklist: [the-checklist.md § Daily/continuous](../the-checklist.md)

## What this step decides

What gets watched every day or continuously: service health, errors, security alerts, cost, infrastructure capacity, user-reported issues, failed jobs, payment failures, provider failures.

## How to think about it

- Most of this should be automated and alert-driven (P19 · Alerts). The daily habit is a short look, not a ritual.
- Failed background jobs and payment failures lose money or data quietly. Check them.
- Every user-reported issue gets a reply and a tracked item.

## Options and trade-offs

| Mode | Good for | Cost |
|---|---|---|
| Alert-driven | Outages, spikes | Needs good alerts |
| Daily digest | Trends, cost, failed jobs | Five minutes a day |

## How to choose: solo founder / pre-revenue defaults

- Digest plus paging for critical only. Time-box to 10 minutes.
- Let an agent summarize overnight logs, metrics and failures into one note for Aviv.

## Human in the loop: escalate when

- A security alert suggesting real compromise or data exposure.
- Cost spike above the P3 threshold.
- Any payment dispute or money-impacting fix.

## Done means

- Alerts and the digest run without manual work.
- Every item is either acted on or marked as noise and tuned.

## Depends on / feeds into

Phase depends on P24 · Launch readiness. Fed by P19 · Observability. Feeds P25 · Weekly and P27 · Project maintenance / agent hygiene.
