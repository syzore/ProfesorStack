> Draft (basic) — pending Aviv's review.

# P19 · Logging

Checklist: [the-checklist.md § Logging](../the-checklist.md)

## What this step decides

What gets written down about what happened: structured logs, request/correlation IDs, user/session correlation, error classes, security and admin events, redaction, retention, access.

## How to think about it

- Logs are for answering "what happened to this request" after the fact. Design them around that question.
- One structured (JSON) line per event with a request ID that follows the request through every service and job.
- Security events (login failures, permission denials) and admin actions are the audit trail. Keep them separate or tagged so they are easy to retain longer.
- Redact before writing. Passwords, tokens, payment data and unnecessary PII never enter a log (every user-data field needs a reason to exist).
- Retention and access are policy: a log with personal data is personal data (P7 · Privacy and data governance).

## Options and trade-offs

| Option | Good for | Cost |
|---|---|---|
| Platform logs (host built-in) | Zero setup, small apps | Short retention, weak search |
| Managed log service | Search, retention, alerts | Per-GB cost, data sharing |
| Self-hosted stack | Control | Operations burden, rarely worth it solo |

## How to choose: solo founder / pre-revenue defaults

- Use the host's built-in logs until retention or search hurts. Add a managed service only then.
- Short retention for app logs, e.g. 14 to 30 days; longer only for security and admin events if a rule requires it.
- Log levels used honestly; no debug logging in production by default.

## Human in the loop: escalate when

- Adding a managed logging vendor (cost, data sharing, personal data leaves your host).
- Choosing retention that conflicts with a P1 or P7 obligation.
- Any log found containing secrets or sensitive data (treat as incident, rotate the secret).

## Done means

- A sample request can be followed end to end by ID.
- A redaction test proves secrets and PII do not appear.
- Retention and access rules are written and enforced.

## Depends on / feeds into

Phase depends on P3 · System architecture, P5 · Engineering foundation, P8 · Core product implementation. Feeds P19 · Alerts, P25 · Daily/continuous (error health) and P24 · Operations (logs work).
