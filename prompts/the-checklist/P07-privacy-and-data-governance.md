> Draft (basic) — pending Aviv's review.

# P7 · Privacy and Data Governance

Checklist: [the-checklist.md § Privacy and Data Governance](../the-checklist.md)

## What this step decides

The legal and operational layer around personal data: published documents (privacy policy, terms), consent, user rights processes (access, export, deletion), retention, vendors and transfers, and breach response. This is a phase with no sub-sections, so the guide covers all of it.

## How to think about it

- Everything here is driven by P1 (which laws apply) and P2 (what data exists). If P1 said a regime does not apply, say so per item with an `[N/A]` reason instead of skipping.
- Think in processes, not documents. A privacy policy is a claim. Each claim (we delete on request, we keep X for Y days) must be backed by something that runs: a deletion process, retention enforcement, a vendor inventory that matches reality.
- Group the items: public documents, consent (flows, storage, withdrawal), user rights (access, export, deletion, account deletion), retention and backups, vendors (processor inventory, agreements, transfers, subprocessors), internal controls (analytics, log scrubbing, support and staff access), and breach response.
- Deadlines for user requests are set by law and vary by regime. Do not hard-code a number from memory; take the period from the P1 compliance notes and confirm with counsel or Aviv.
- Backups are the awkward case: decide what deletion means there (expiry window, restore-and-reapply) and state it honestly in the policy.

## Options and trade-offs

| Decision | Boring default | Heavier option | Pick the heavier one when |
| --- | --- | --- | --- |
| Policies | Reviewed template, tailored to real data flows | Bespoke legal drafting | Regulated data or enterprise customers |
| Consent | Only what the law needs, via a maintained consent tool | Custom consent platform | Ad or tracking module (P11) is on |
| Rights requests | Manual runbook with a ticket and a checklist | Self-service automation | Request volume makes manual slow |
| Analytics | Privacy-safe, cookieless where possible | Full tracking with consent | Growth work needs per-user data |

## How to choose: solo founder / pre-revenue defaults

- Collect less. Each field you never store removes a deletion, export and breach-notification item.
- Start manual: a runbook that deletes a user across every store in the inventory, tested once. Automate when requests actually arrive.
- Keep a vendor table (vendor, data sent, region, agreement status) and keep it in the repo.
- Policies describe what the product actually does today, never what you plan to do.

## Human in the loop: escalate when

- Publishing or changing a privacy policy or terms. Legal text is for Aviv, with counsel where stakes warrant it.
- Any irreversible deletion of user data, and any change to a retention period.
- A new vendor receiving personal data, or data crossing to a new region.
- Changing consent behavior, or collecting a new category of personal data (compliance scope change).
- Responding to a user rights request that is unusual, disputed, or from a regulator.
- Any suspected breach. Notification decisions are Aviv's and counsel's.

## Done means

- Each published claim maps to a mechanism, and the deletion runbook has been executed end to end on a test account across all stores and vendors.
- The vendor and subprocessor inventory matches the code (checked by searching for outbound calls), and the breach response procedure has a named owner.

## Depends on / feeds into

Depends on P1 · Applicability / Compliance Discovery, P2 · Users, Trust and Data Model, P3 · System Architecture, P6 · Security Foundation. Feeds P8 · Core Product Implementation, P10 · Payments, P11 · Ads / Monetization, P12 · Email / Notifications, P20 · Analytics and Experimentation, P24 · Launch Readiness (Legal/business).
