> Draft (basic) — pending Aviv's review.

# P03 · Escalations

Checklist: [the-checklist.md § Escalations](../the-checklist.md)

## What this step decides
The architecture choices an agent must not make alone. Each one is a trigger: stop, bring the human the options and a recommendation, and wait. This step also records the cost threshold above which an estimate needs approval.

## How to think about it
- These triggers share a shape: money, identity, irreversible data, new recurring cost or dependency, weaker security, wider legal scope, or a choice that is expensive to undo. When a choice has none of these, decide it and record it in an ADR.
- Escalating is not asking "what do you think". It is a decision packet: options, cost, reversibility, risk, and a recommendation with a reason.
- Reversibility is the sorting question. A two-way door (easy to undo) is decided and logged. A one-way door (hard or costly to undo) goes to a human.
- When a trigger is unclear, treat it as hit. Cheap to ask, expensive to unwind.
- Do not split a risky change into small pieces to avoid a trigger.

## Options and trade-offs
| Trigger | Why it needs a human | What to bring |
| --- | --- | --- |
| AP over CP for money or identity data | Stale or divergent reads could cost money or grant wrong access; the business tolerance is Aviv's call | The domain, the failure scenario, what users see, CP option with its availability cost, recommendation |
| RPO above zero for customer data | Accepting possible data loss is a promise to customers | RPO number, backup and replication method, cost of lower RPO, what data could be lost |
| Irreversible data migration | No tested way back; a mistake is permanent | Migration plan, backup and restore test result, dry-run output, rollback or why none exists |
| New paid or managed vendor | New recurring cost, dependency and data sharing | Vendor, monthly cost, data shared, lock-in, exit path, free or self-run alternative |
| Cross-region deployment or data residency | Legal and cost impact | Regions, regimes involved (confirm with counsel), cost, latency gain, one-region alternative |
| Cost estimate above the threshold | Money beyond what Aviv agreed | Estimate with inputs, worst case, cheaper options, cap that would apply |
| Weakening a security control | Reduces protection for users and the business | The control, why, residual risk, compensating control, expiry date |
| Compliance scope change (SOC 2, GDPR, HIPAA, CCPA) | New legal duties and cost | Regime, trigger event, what it adds to architecture, counsel questions |
| One-way-door architecture choice | Hard or costly to reverse | Options, cost to reverse each, evidence, smallest reversible alternative |

## How to choose: solo founder / pre-revenue defaults
- Record the cost threshold first, with Aviv: one monthly number and one per-user number, e.g. a figure you would not mind losing. Until set, treat any new recurring cost as over threshold.
- Default to the reversible option and ship it; escalate only when the reversible option cannot meet an NFR.
- Keep an "escalated and decided" log in the ADRs, so the same question does not come back.
- Pre-revenue, most triggers will be "no, not yet". Say so in the checklist with the date.

## Human in the loop: escalate when
- Every item in the table above: this guide is the list.
- Also: money or identity data touched in any way not already approved.
- Also: a promise to a user or customer that you cannot undo (data retention, availability, refunds).
- Treat any ambiguity about whether a trigger applies as a hit.
- Format: send the "What to bring" column filled in, plus a recommendation. Do not proceed on silence.

## Done means
- The cost threshold is recorded as numbers.
- Each trigger has an answer for the project: not applicable, hit-and-approved (with the approver and date), or deferred with a trigger.
- No architecture choice in P3 that matches a trigger lacks an approval.

## Depends on / feeds into
Depends on: P3 · Non-functional requirements, P3 · Architecture, P3 · Trade-offs and options, P3 · Scale. Feeds: P3 · Architecture documentation (ADRs record approvals), P5 · Configuration, and every later phase that touches money, identity, data migration, vendors or compliance scope.
