> Draft (basic) — pending Aviv's review.

# P19 · Alerts

Checklist: [the-checklist.md § Alerts](../the-checklist.md)

## What this step decides

What wakes you or tells you something broke: service unavailable, error spike, latency spike, database failure, disk/storage exhaustion, queue failure, provider failure, security anomaly, cost anomaly, certificate/domain expiry, backup failure.

## How to think about it

- An alert is a request for a human to act. If nobody should act, it is a dashboard line, not an alert.
- Alert on symptoms users feel (errors, latency against the P3 SLO) more than on causes. Burn rate against the error budget is a good paging signal.
- Silent failures are the dangerous ones: backups, certificate expiry, queues that stop draining. Those are listed because no user complains first.
- Every alert needs an owner and a first step. Unowned alerts are drift (see P27 · Project maintenance / agent hygiene).
- Too many alerts means none get read. Tune on real incidents.

## Options and trade-offs

| Channel | Good for | Cost |
|---|---|---|
| Push or SMS to phone | Page-worthy only | Interrupts sleep |
| Email or chat | Warnings, daily review | Gets ignored |
| Dashboard only | Trends | Nobody sees it in time |

## How to choose: solo founder / pre-revenue defaults

- Few alerts, high signal. Page only for: service down, error spike, backup failure, security anomaly, cost spike.
- Warnings go to a daily digest.
- Use host or uptime-monitor built-ins first; one external uptime check is cheap.
- The founder must actually receive critical alerts, and it must be tested (P24 · Operations).

## Human in the loop: escalate when

- Adding a paid alerting or paging vendor.
- Defining what counts as a security anomaly if it needs account or session data shared with a vendor.
- Silencing or deleting an alert after an incident.

## Done means

- Each listed alert exists, or `[N/A]` with reason.
- A test alert reached Aviv's phone.
- Each alert names an owner and a first-response step.

## Depends on / feeds into

Phase depends on P3 · System architecture, P5 · Engineering foundation, P8 · Core product implementation. Fed by P19 · Metrics and P19 · Logging. Feeds P23 · Infrastructure / reliability (error-budget policy), P24 · Operations and P25 · Daily/continuous.
