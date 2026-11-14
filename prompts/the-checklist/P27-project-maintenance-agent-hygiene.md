> Draft (basic) — pending Aviv's review.

# P27 · Project maintenance / agent hygiene

Checklist: [the-checklist.md § Project maintenance / agent hygiene](../the-checklist.md)

## What this step decides

The continuous detection of rot: dead code and dependencies, unused config and env vars, stale flags/migrations/docs/tests, duplicated logic, drift, orphaned fields/endpoints/jobs, flaky tests, monitoring gaps, unowned alerts, excess complexity.

## How to think about it

- Continuous, so make it cheap: scheduled agent sweeps that report, not auto-delete.
- Detection is the step. Removal is a separate change with its own review, because dead-looking code is sometimes used dynamically.
- Orphaned database fields tie back to the rule that every user-data field needs a reason to exist (P2, P7).
- Monitoring gaps and unowned alerts feed back into P19 · Alerts.

## Options and trade-offs

| Method | Good for | Cost |
|---|---|---|
| Static tools (unused code, deps, env) | Dead code, dependencies | False positives |
| Scheduled agent audit | Drift, stale docs, orphans | Token cost, needs review |
| Manual spot check | Judgment | Time |

## How to choose: solo founder / pre-revenue defaults

- Weekly or monthly agent sweep, output a short list into the backlog.
- Delete in small PRs with tests passing.
- Track flaky tests and fix them first; they erode trust in CI.

## Human in the loop: escalate when

- Dropping a column, table, endpoint or job (irreversible data change or breaking client).
- Removing an alert, scan or security control found as unused.
- Removing a dependency that changes licensing or behavior.

## Done means

- Each detect item has a method and a schedule, or `[DEFER]` with trigger.
- Findings land as tracked items with owners.
- No unowned alerts remain.

## Depends on / feeds into

Continuous. Fed by P5, P19, P22. Overlaps with P25 · Weekly and P25 · Monthly/periodic. Feeds P28 · Retirement / exit (clean inventory).
