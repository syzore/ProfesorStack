> Draft (basic) — pending Aviv's review.

# P02 · Identity

Checklist: [the-checklist.md § Identity](../the-checklist.md)

## What this step decides
How users prove who they are and how that proof lasts and fails: mechanism, sessions, tokens, logout, compromise handling, MFA, provider and email failures.

## How to think about it
- Choose the mechanism before the vendor: passwordless email link, password, social login. Passwords add storage and reset risk; social login adds provider dependency.
- Decide failure behavior now: what users see if the OAuth provider or the email service is down.
- Session expiration and refresh are security trade-offs: short is safer, long is smoother. Define logout so it really ends the session on the server.
- Compromised-account behavior: how you detect it, force sign-out and let the user recover.
- Do not write your own crypto or auth if a managed provider fits.

## Options and trade-offs
| Mechanism | Pick when | Cost |
| --- | --- | --- |
| Managed auth provider | Default for small teams | Vendor dependency, per-user price at scale |
| Email magic link | Low-frequency use | Depends on email delivery |
| Social login | Users expect it | Provider outages, data sharing |
| Self-built password auth | Almost never | Security burden on you |

## How to choose: solo founder / pre-revenue defaults
- Default: a managed provider with email link or social login. Boring beats custom.
- Require MFA for admin accounts at least; users optional unless money is involved.
- Pick session lengths from risk, e.g. long for a low-risk app, short for anything touching money. Write the number.

## Human in the loop: escalate when
- Choosing or changing the authentication provider (new vendor, data sharing, lock-in).
- Weakening session, MFA or password rules, or skipping MFA for admin.
- Any account-recovery path that bypasses the normal proof.
- Money or identity data tied to login (this is the CP-over-AP rule in P3 · Escalations).
- A compromise: incident handling needs Aviv.

## Done means
- Mechanism, expiry, refresh, logout, compromise, MFA, provider and email failure behaviors are written.
- Each has an acceptance criterion a test can check (security rule).

## Depends on / feeds into
Depends on: P2 · Users, P1 · Privacy. Feeds: P3 · Architecture (auth provider choice), P3 · Non-functional requirements (security), P4 · UX (sign-in and error states), P6 security foundation.
