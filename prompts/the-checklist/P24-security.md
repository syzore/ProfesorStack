> Draft (basic) — pending Aviv's review.

# P24 · Security

Checklist: [the-checklist.md § Security](../the-checklist.md)

## What this step decides

Whether security is acceptable to launch: critical vulnerabilities resolved, authentication and authorization verified, secrets checked, production access checked, dependency vulnerabilities reviewed.

## How to think about it

- Evidence beats assertion. Use the P17 · Security testing results and scan output.
- Production access check means list who and what can touch production and remove extras.
- Every security requirement needs an acceptance criterion; this is where they are ticked off as VERIFIED.

## Options and trade-offs

No real fork here. Do the items, and record any `[N/A]` or `[DEFER]` with its reason or trigger.

## How to choose: solo founder / pre-revenue defaults

- No critical or high findings open. Mediums need an owner and date.
- Confirm no secrets in the repo history or logs; rotate any that were exposed.

## Human in the loop: escalate when

- Launching with an open critical or high finding.
- Accepting any weakened security control to hit a date.
- Granting wider production access.

## Done means

- Scan and test output attached for each item.
- Access list for production is reviewed and minimal.

## Depends on / feeds into

Phase depends on all required prior gates. Launch checks verify earlier work; they do not replace it. Fed by P6 · Security foundation and P17 · Security testing.
