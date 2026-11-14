> Draft (basic) — pending Aviv's review.

# P17 · Integration

Checklist: [the-checklist.md § Integration](../the-checklist.md)

## What this step decides

Which real dependencies get exercised together: database, authentication, external APIs, payments, email, storage, queue/jobs, AI provider, search/vector infrastructure.

## How to think about it

- Integration tests prove the seams work: schema matches code, the queue delivers, the provider contract is honored.
- Only test integrations that exist in the architecture chosen in P3. Others are `[N/A]`.
- Every external dependency needs a failure mode (checklist rule). Integration tests are where you force that failure and watch the behavior.
- Use the real database engine in tests, same version as production. SQLite standing in for Postgres hides real bugs.

## Options and trade-offs

| Approach | Good for | Cost |
|---|---|---|
| Real service in a container | Database, queue, storage | Slower, needs setup |
| Provider sandbox | Payments, email | Rate limits, flaky network |
| Recorded or stubbed responses | AI provider, third-party APIs | Drifts from the real contract |

## How to choose: solo founder / pre-revenue defaults

- Real database in a container for every run. Stub paid or rate-limited providers, with one scheduled contract check against the real sandbox.
- AI provider calls are stubbed in CI and cost nothing. A small live smoke test runs on demand only.
- Keep fixtures small and reset per test.

## Human in the loop: escalate when

- A test would call a paid API on every CI run (new recurring cost).
- A test needs production data or real user data.
- Payment integration tests would touch live mode.

## Done means

- Each applicable integration has a passing test for success and one named failure (timeout, 5xx, auth error).
- Test data is isolated and cleaned up.
- Stubs are checked against the real contract on a schedule or documented as a known gap.

## Depends on / feeds into

Phase depends on P8 · Core product implementation and every relevant conditional module (P9 to P16). Feeds P22 · Deployment / CI/CD. Conditional modules P10 to P16 each add integrations to cover here.
