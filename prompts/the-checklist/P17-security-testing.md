> Draft (basic) — pending Aviv's review.

# P17 · Security testing

Checklist: [the-checklist.md § Security testing](../the-checklist.md)

## What this step decides

Which attack classes get tested and scanned: authentication, authorization, injection, XSS, CSRF, SSRF, file upload, rate limit, abuse, secret-leak scanning, dependency scanning, security regression tests.

## How to think about it

- Test against the requirements from P6, not a generic list. Each security requirement needs an acceptance criterion (checklist rule); the test is that criterion.
- Automated scanners find known classes. Authorization bugs (wrong user reads another user's data) usually need written tests.
- Skip classes with no surface. No file upload means file-upload testing is `[N/A]` with that reason.
- Every fixed vulnerability gets a regression test so it cannot return.

## Options and trade-offs

| Method | Finds | Cost |
|---|---|---|
| Dependency and secret scanners | Known CVEs, committed keys | Noise, needs triage |
| Written authz/injection tests | Logic flaws in your own code | Authoring time |
| External pen test | Unknown unknowns | Money, scheduling |

## How to choose: solo founder / pre-revenue defaults

- Run secret and dependency scanning in CI from day one. They are cheap.
- Write cross-user access tests for every resource type.
- Defer external pen testing until real user data or payments exist.
- Run abuse and rate-limit tests against staging, never production.

## Human in the loop: escalate when

- Hiring an external tester or buying a scanner (new paid vendor, data sharing).
- Any proposal to disable, loosen or suppress a security test or control.
- A critical finding in production data.

## Done means

- Every applicable class has a test or a scan with a pass result.
- Findings are triaged with owner and date; criticals are fixed before launch.
- Regression test exists for each fixed vulnerability.

## Depends on / feeds into

Phase depends on P8 · Core product implementation and every relevant conditional module (P9 to P16). Fed by P6 · Security foundation and P7. Feeds P24 · Security.
