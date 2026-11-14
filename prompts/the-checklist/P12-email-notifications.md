> Draft (basic) — pending Aviv's review.

# P12 · Email / Notifications

Checklist: [the-checklist.md § Email / Notifications](../the-checklist.md)

## What this step decides

How the product contacts people: provider, sender-domain authentication, transactional versus marketing messages, preferences and unsubscribe, bounce and complaint handling, limits, retries, templates, and monitoring. Phase-level guide.

## How to think about it

- Email reaches a person, so mistakes are visible and sometimes irreversible. Sender reputation is a shared asset: one bad send can land everything in spam.
- Keep two streams apart: transactional (receipts, password resets, security notices) and marketing. Different legal rules, different providers or domains, different failure tolerance.
- Domain authentication (SPF, DKIM, DMARC) is a one-time setup that gates deliverability. Do it before any real send.
- Bounces and complaints must feed back into suppression, otherwise you keep mailing dead or angry addresses.
- Retries and deduplication prevent two failure modes: a message lost, and a message sent five times. Pair each send with an idempotency key.
- Marketing consent and unsubscribe rules differ by jurisdiction. Take the rules from P1 and confirm with counsel or Aviv.

## Options and trade-offs

| Decision | Boring default | Heavier option | Pick the heavier one when |
| --- | --- | --- | --- |
| Provider | One transactional email provider | Own mail server | Never at this stage |
| Marketing | Defer, or a separate tool | Same provider | Volume and need are real |
| Templates | Versioned in the repo | Provider template UI | Non-engineers edit them |
| Push or SMS | Skip | Add channel | A user need email cannot meet |

## How to choose: solo founder / pre-revenue defaults

- Transactional only at launch, from a subdomain, with SPF, DKIM and a DMARC policy starting at monitoring.
- Process bounce and complaint webhooks into a suppression list from day one.
- Per-user and global send limits, and a send log with delivery status.

## Human in the loop: escalate when

- First sending to real users, or any bulk or marketing send to existing users.
- Choosing or changing the provider or sending domain (reputation reset).
- DMARC enforcement changes that could block legitimate mail.
- A complaint spike, blocklisting, or provider warning.
- New message types that carry personal data, or any change to consent or unsubscribe behavior.

## Done means

- Authentication records verified with a real send test to a major mailbox, and each message type is classified with its preference and unsubscribe rules.
- Bounces, complaints and retries are tested, duplicates are suppressed, and delivery is monitored with an alert.

## Depends on / feeds into

Depends on P2 · Users, Trust and Data Model, P7 · Privacy and Data Governance, P8 · Core Product Implementation. Feeds P10 · Payments (receipts), P16 · Background Jobs (sending queue), P19 · Observability, P4 · UX, UI, Accessibility and Internationalization (localization).
