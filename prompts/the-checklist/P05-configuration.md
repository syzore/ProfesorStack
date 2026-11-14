> Draft (basic) — pending Aviv's review.

# P05 · Configuration

Checklist: [the-checklist.md § Configuration](../the-checklist.md)

## What this step decides
How the app is configured per environment (development, test, staging, production): where values live, how secrets are injected, how config is validated, what happens when it is missing, and how it is documented.

## How to think about it
- Separate config (varies per environment) from code. Secrets are config of the most sensitive kind.
- Validate configuration at startup. A missing or malformed value should fail fast and loudly, not fall back silently to a wrong default.
- Decide the missing-config behavior per value: fail at boot, use a safe default, or disable one feature. Silent fallbacks hide production mistakes.
- Inject secrets from the host's secret store or an environment variable, not files in the repo. Keep an example file with names and no values.
- Document every variable: purpose, where it is set, safe example, and who can change it.

## Options and trade-offs
| Mechanism | Pick when | Cost |
| --- | --- | --- |
| Environment variables | Default | Needs validation and docs |
| Host secret store | Secrets in production | Vendor feature; access setup |
| Dedicated secrets manager | Many secrets, rotation needs | New paid vendor and complexity |
| Config files in repo | Non-secret defaults only | Risk of committing secrets |

## How to choose: solo founder / pre-revenue defaults
- Default: environment variables validated by a typed settings object at boot, a committed example file without values, production secrets in the host's store, separate values per environment.
- Test config never points at production.
- Missing required config stops the app with a clear message.

## Human in the loop: escalate when
- Adding a secrets manager or any new paid configuration vendor.
- Production config or secrets changed in a way that can affect users or money.
- Test or staging pointed at production data.
- A secret was exposed: rotate and report to Aviv.
- Disabling a safety flag in production.

## Done means
- All four environments are described, or `[N/A]` with reason.
- Startup validation exists and a missing value fails with a clear error (tested).
- Every variable is documented and no secret is in version control.

## Depends on / feeds into
Depends on: P3 · Architecture, P5 · Repository (environment and secrets strategy). Feeds: P6 · Application security, P22 · Deployment / CI/CD, P19 · Metrics (per-environment settings).
