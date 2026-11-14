> Draft (basic) — pending Aviv's review.

# P22 · Deployment / CI/CD

Checklist: [the-checklist.md § Deployment / CI/CD](../the-checklist.md)

## What this step decides

How code reaches production safely: CI gates, artifacts, environments, secrets, deploy and migration strategy, release-step work, rollback, health checks, locking, post-deploy verification.

## How to think about it

- CI is the gate that runs P17 tests, lint, type check, and security and dependency scans. A deploy that skips the gate is a bypass.
- Build once, promote the same artifact. Do not rebuild per environment.
- One-off startup work (schema, migrations, seed, recompute) runs once per deploy in a release step, not in every app process. With more than one process (P23), per-process migrations race.
- Rollback must be real. Code rollback is easy; data migrations are not. Prefer backward-compatible migrations (add, then migrate, then remove).
- Health, readiness and liveness are different. Readiness gates traffic; liveness restarts a stuck process.
- Post-deploy verification is a smoke check that runs automatically, not a hope.

## Options and trade-offs

| Strategy | Good for | Cost |
|---|---|---|
| Replace in place | Solo, tiny | Short blip, rollback is a redeploy |
| Rolling | Multiple processes | Old and new run together; migrations must be compatible |
| Blue/green or canary | Large or risky changes | Extra infrastructure, money |

## How to choose: solo founder / pre-revenue defaults

- Host-managed deploys from main with CI as a required check.
- Rolling or replace-in-place, with a release step for migrations.
- Environment separation: at least local, production; staging only if justified (P23).
- One deploy at a time (lock). Smoke check after each deploy.

## Human in the loop: escalate when

- Any irreversible migration (dropping or rewriting data without a tested way back).
- Adding a paid CI or deploy vendor.
- Granting CI production secrets or access, or weakening a CI security gate.
- Deploying without a passing gate, even for an emergency.

## Done means

- A deploy from clean main works end to end and a rollback was exercised once.
- Migrations run once per deploy.
- Post-deploy check fails the release when it should.

## Depends on / feeds into

Depends on P5 · Engineering foundation, P6 · Security foundation, P17 · Testing. Feeds P23 · Infrastructure / reliability, P24 · Operations (rollback tested) and P25.
