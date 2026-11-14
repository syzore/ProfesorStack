> Draft (basic) — pending Aviv's review.

# P17 · Unit

Checklist: [the-checklist.md § Unit](../the-checklist.md)

## What this step decides

Which pure logic gets fast tests that run on every change: domain logic, validation, state transitions, permission logic, utility functions.

## How to think about it

- Unit tests cover code with no I/O. If a test needs a database or network, it belongs in P17 · Integration.
- Test behavior through the public function, not private helpers. A refactor should not break the suite.
- Permission logic and state transitions are the highest value. They are small, pure and costly when wrong (see the rule that every privileged action needs an authorization rule).
- Write the regression test first when a bug is found and the test is cheap.

## Options and trade-offs

| Style | Good for | Cost |
|---|---|---|
| Example-based | Known edge cases, readable failures | Misses cases you did not think of |
| Property-based | Validation, parsers, state machines | Harder to read, slower to write |
| Mocks of collaborators | Isolating one unit | Brittle, can pass while reality fails |

## How to choose: solo founder / pre-revenue defaults

- Example-based tests first. Add property tests only for parsers and state machines.
- Prefer real in-memory objects over mocks. Mock only the clock, randomness and the network edge.
- Coverage is a hint, not a target. Cover every branch of permission and money logic, skip getters.
- Suite should run in seconds so agents run it after every edit.

## Human in the loop: escalate when

- A coverage or test-strategy change that lowers the bar on permission, payment or deletion logic.
- A flaky unit test is about to be deleted or skipped rather than fixed.

## Done means

- Every listed area has tests, or `[N/A]` with reason.
- Tests are VERIFIED by running them, not just present.
- Each permission rule from P2 and P6 has at least one allow and one deny case.

## Depends on / feeds into

Phase depends on P8 · Core product implementation and every relevant conditional module (P9 to P16). Feeds P22 · Deployment / CI/CD (the Test gate) and P24 · Launch readiness.
