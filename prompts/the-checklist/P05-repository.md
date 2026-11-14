> Draft (basic) — pending Aviv's review.

# P05 · Repository

Checklist: [the-checklist.md § Repository](../the-checklist.md)

## What this step decides
How the code lives and runs on a machine: repository, branches, commits, directory structure, environments, configuration and secrets strategy, development setup, local database and seed data.

## How to think about it
- Keep it simple. One repository unless there is a hard reason to split.
- Branches: with one developer, trunk-based (commit to `main` in short steps) is the lighter default. The project's CLAUDE.md states the phase: pre-revenue personal repos commit to `main`; paying-customer phase uses PRs.
- The directory structure should mirror the module boundaries chosen in P3 · Architecture decisions.
- The environment strategy defines which environments exist (e.g. local, production, maybe staging) and what differs between them.
- Secrets never enter the repo. Decide where they live and how they are injected before the first one exists.
- A new machine should reach a running app in a few commands: document the setup and seed data.

## Options and trade-offs
| Decision | Smallest option | Cost of going bigger |
| --- | --- | --- |
| Repo layout | One repo, one app | Multi-repo coordination |
| Branching | Trunk-based on `main` | PR flow overhead, needed once customers pay |
| Environments | Local + production | Staging costs money and upkeep |
| Local database | Containerized or managed dev instance | Drift from production |
| Seed data | Script that generates fake data | Maintaining fixtures |

## How to choose: solo founder / pre-revenue defaults
- Default: one repo, `main` only pre-revenue, local and production environments, a seed script with synthetic data only, secrets in the host's secret store.
- Never seed with real user data.
- Add staging only when a change cannot be tested locally.

## Human in the loop: escalate when
- Moving to PR-only flow or changing the branch policy (follows phase change to paying customers).
- Any secret stored somewhere new or committed by accident: rotate and tell Aviv.
- Production data copied into local or staging (privacy).
- A new paid environment or tool.

## Done means
- Every item addressed; a fresh checkout reaches a running app by documented steps.
- Secrets strategy is written and no secret is in history.
- Seed data contains no real personal data.

## Depends on / feeds into
Depends on: P3 (architecture, escalations, boundaries). Feeds: P5 · Code quality, P5 · Configuration, P6 · Application security (secrets), P22 · Deployment / CI/CD.
