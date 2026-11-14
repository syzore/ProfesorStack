> Draft (basic) — pending Aviv's review.

# P17 · End-to-end

Checklist: [the-checklist.md § End-to-end](../the-checklist.md)

## What this step decides

The few full-journey tests through the real UI: new user, returning user, core product journey, account recovery, account deletion, payment journey if applicable, error journey, mobile journey, critical accessibility journey.

## How to think about it

- E2E is slow and brittle, so keep it to the journeys whose failure would end the business or break a legal duty.
- Account recovery and account deletion are easy to forget and legally relevant (P2 identity, P7 privacy). Test them.
- Mobile and accessibility journeys are listed because they fail silently in desktop-only testing.
- A failing E2E test should be quick to localize. If it is not, push the check down to API or unit tests.

## Options and trade-offs

| Tool | Good for | Cost |
|---|---|---|
| Browser automation (e.g. Playwright) | Web UI, multiple browsers | Maintenance, flake |
| Device/emulator automation | Native mobile | Slow, heavy setup |
| Manual checklist | Rare or visual journeys | Does not scale, easy to skip |

## How to choose: solo founder / pre-revenue defaults

- Fewer than 10 journeys. Run on merge to main, not every commit, if too slow.
- Manual checklist for anything not yet automated, recorded in the launch gate.
- Fix or delete flaky tests quickly; a test that is ignored is worse than none.

## Human in the loop: escalate when

- Payment journey tests need live mode or real money.
- Account deletion test would run against real accounts.
- Adding a paid device-farm or testing vendor.

## Done means

- Each listed journey is automated or `[N/A]` / `[DEFER]` with reason or trigger.
- Critical journeys pass on the production-like environment.
- Flaky tests are tracked and fixed (see P27 · Project maintenance / agent hygiene).

## Depends on / feeds into

Phase depends on P8 · Core product implementation and every relevant conditional module (P9 to P16). Feeds P24 · Product and P24 · Launch (smoke tests reuse these journeys).
