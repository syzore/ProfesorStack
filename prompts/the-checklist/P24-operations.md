> Draft (basic) — pending Aviv's review.

# P24 · Operations

Checklist: [the-checklist.md § Operations](../the-checklist.md)

## What this step decides

Whether you can run it once it is live: monitoring, alerts, logs, founder receiving critical alerts, rollback, incident procedure, provider outage procedures.

## How to think about it

- Do not just check that alerts exist. Fire a test and confirm it reaches Aviv.
- Rollback tested means actually rolling back once, on a real deploy.
- Incident procedure can be one page: who, what to check first, how to communicate.
- Provider outage procedures cover each production dependency's failure mode (checklist rule).

## Options and trade-offs

No real fork here. Do the items, and record any `[N/A]` or `[DEFER]` with its reason or trigger.

## How to choose: solo founder / pre-revenue defaults

- One-page incident runbook and one outage note per critical provider.
- Test a rollback and an alert end to end before launch.

## Human in the loop: escalate when

- Adding a paid on-call or status-page vendor.
- An incident that involves data exposure, which has legal notification duties.

## Done means

- Each item has evidence of a test run.
- Runbooks are written and findable.

## Depends on / feeds into

Phase depends on all required prior gates. Launch checks verify earlier work; they do not replace it. Fed by P19 · Observability, P22 · Deployment / CI/CD, P23 · Infrastructure / reliability.
