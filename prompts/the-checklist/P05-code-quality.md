> Draft (basic) — pending Aviv's review.

# P05 · Code quality

Checklist: [the-checklist.md § Code quality](../the-checklist.md)

## What this step decides
The tooling and conventions that keep the code consistent: pinned toolchains, dependency manager and versions, formatter, linter, type checking, static analysis, pre-commit checks, dead-code policy, and conventions for errors, logging, naming, API, database, migrations and tests.

## How to think about it
- Automate what a tool can check; write conventions only for what it cannot. Fewer written rules get followed more.
- Pin language and toolchain versions and control dependency versions, so a build today is a build next month.
- Pick one formatter and linter and let them settle style arguments. Strict typing catches bugs before tests do.
- Dead-code strategy: delete rather than comment out; the history has it.
- Migration conventions matter most: migrations should be repeatable, ordered and, where possible, reversible. An irreversible one is an escalation (P3 · Escalations).
- Error handling and logging conventions should say what is logged and what must never be (personal data, secrets).

## Options and trade-offs
| Tool | Pick when | Cost |
| --- | --- | --- |
| Formatter and linter in CI | Always | Initial fix-up |
| Strict type checking | Typed language available | Annotation effort |
| Pre-commit checks | Fast checks only | Slow hooks get bypassed |
| Static analysis | Security or complexity risk | Noise; tune rules |

## How to choose: solo founder / pre-revenue defaults
- Default: the ecosystem's standard formatter, linter and type checker; lockfile committed; versions pinned; the same checks locally and in CI; a short conventions file. Add only what the project's own CLAUDE.md requires, e.g. explicit Dart types in Flutter code.
- Keep pre-commit fast; run the full suite in CI.
- Prefer boring, widely used tools.

## Human in the loop: escalate when
- Adding a paid code-quality or analysis service (new vendor).
- Disabling a security-relevant lint or check.
- Migration conventions that allow an irreversible production change.
- Upgrading a major dependency or runtime that affects data or auth.
- Changing a project rule from CLAUDE.md: Aviv decides.

## Done means
- Each tool is configured and runs locally and in CI, or has an `[N/A]` reason.
- Conventions are written once, briefly, and linked from the repo's contributor notes.
- A clean checkout passes all checks.

## Depends on / feeds into
Depends on: P3, P5 · Repository. Feeds: P5 · Configuration, P6 · Supply chain, P17 · Unit, P22 · Deployment / CI/CD, all implementation.
