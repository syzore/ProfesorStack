> Draft (basic) — pending Aviv's review.

# P02 · Users

Checklist: [the-checklist.md § Users](../the-checklist.md)

## What this step decides
Whether and how people have identities in the product: login or not, guest mode, account lifecycle, sessions, roles, admin and support access.

## How to think about it
- Ask first whether login must exist. Each account feature (recovery, verification, deletion, multi-device) is a permanent cost.
- Anonymous and guest behavior need a rule for what happens to their data when they sign up later.
- Roles and permissions: list privileged actions, then who may do each. Every privileged action needs an authorization rule (checklist rule).
- Support impersonation is the most dangerous access: decide whether it exists, who can use it, and how it is logged.

## Options and trade-offs
| Choice | Pick when | Cost |
| --- | --- | --- |
| No accounts | Tool works without saved state | No cross-device state |
| Guest then upgrade | Want low friction first | Data merge rules |
| Accounts from start | State or payment per user | Recovery, deletion, support load |
| One role + admin | Solo or small | Simple; admin is a powerful secret |

## How to choose: solo founder / pre-revenue defaults
- Default: the fewest roles (user, admin). Admin is you.
- Account deletion and recovery exist if accounts exist; plan them now, build the simplest version.
- No support impersonation pre-revenue; use read-only admin views.

## Human in the loop: escalate when
- Introducing support impersonation or any admin power over user data.
- Adding a role that can read other users' data.
- Account deletion semantics that affect other users' data or money.
- Multi-organization or tenant models (one-way door for the data model).
- Anything that changes who can reach identity or money data.

## Done means
- Every item answered or `[N/A]` with reason.
- Roles table lists each role, its permissions and the privileged actions it can take.
- Account lifecycle (create, verify, recover, delete) is described end to end.

## Depends on / feeds into
Depends on: P0, P1 · Privacy and P1 · Industry-specific (age, deletion rules). Feeds: P2 · Identity, P2 · Data inventory, P3 · Architecture (auth provider), P4 · UX (onboarding, empty states), P6 · Application security.
