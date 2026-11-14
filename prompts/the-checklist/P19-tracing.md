> Draft (basic) — pending Aviv's review.

# P19 · Tracing

Checklist: [the-checklist.md § Tracing](../the-checklist.md)

## What this step decides

Whether you can see a single request's path across components: critical requests, background jobs, external calls, database where useful.

## How to think about it

- Tracing answers "where did the time go" across more than one component. In a single-process app, structured logs with timings often do the job.
- Trace the critical paths named in P3 first. Background jobs and external calls are where hidden latency and failures live.
- Propagate the correlation ID from P19 · Logging into jobs so a trace can continue past the queue.
- Sampling controls cost. Trace all errors and a small slice of successes.

## Options and trade-offs

| Option | Good for | Cost |
|---|---|---|
| Request ID plus timing logs | Monolith, solo | Manual correlation |
| OpenTelemetry to a backend | Multi-service, async flows | Setup, vendor or hosting cost |
| Managed APM tracing | Fast start | Per-host cost, data sharing |

## How to choose: solo founder / pre-revenue defaults

- Monolith: skip full tracing. Log durations of external calls and queries instead, and mark the item `[DEFER]` with trigger "second service or async hop appears".
- If adopted, use OpenTelemetry so the backend can be swapped.
- Sample, e.g. 5 to 10 percent of successes, all errors.

## Human in the loop: escalate when

- Adding a paid tracing vendor.
- Traces would carry personal data or payload bodies to a third party.

## Done means

- Either traces cover the listed paths, or the item is `[DEFER]` with a trigger.
- A slow request can be diagnosed to the component that caused it.
- No sensitive data in span attributes.

## Depends on / feeds into

Phase depends on P3 · System architecture, P5 · Engineering foundation, P8 · Core product implementation. Feeds P18 · Performance (diagnosis) and P25 · Weekly (performance review).
