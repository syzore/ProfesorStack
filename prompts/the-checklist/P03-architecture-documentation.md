> Draft (basic) — pending Aviv's review.

# P03 · Architecture documentation

Checklist: [the-checklist.md § Architecture documentation](../the-checklist.md)

## What this step decides
The written and drawn record of the architecture: diagram, data flows, sequences for critical flows, dependency map, ADRs and rejected alternatives. These let a later agent or Aviv understand and change the system safely.

## How to think about it
- Diagrams serve a reader. Make the fewest that answer: what are the parts, where does data go, what happens in the critical flow, what do we depend on.
- Data-flow diagrams should mark where personal data and secrets move and where trust boundaries are (from P3 · Architecture decisions and P2 · Data inventory).
- Sequence diagrams only for critical flows: sign-in, payment, data deletion, the primary user action.
- The dependency map lists each external service with owner, failure mode and replacement path.
- An ADR is short: context, decision, alternatives, consequences, date. Write one per meaningful decision, including each escalated one with its approver.
- Text-based diagrams (Mermaid or similar) live in the repo and diff in review.

## Options and trade-offs
| Artifact | Pick when | Cost |
| --- | --- | --- |
| Architecture diagram | Always | Needs updating with the system |
| Data-flow diagram | Personal data or third parties exist | A few hours; high audit value |
| Sequence diagram | Critical or tricky flow | Only for those flows |
| Dependency map | Any external dependency | Short table |
| ADR | Meaningful or hard-to-reverse choice | A paragraph each |

## How to choose: solo founder / pre-revenue defaults
- Default: Mermaid in markdown inside the repo, one page for architecture and data flow, a table for dependencies, one ADR file per decision.
- Skip diagrams of trivial parts. Mark `[N/A]` with a reason.
- Record rejected alternatives in each ADR; this is where future you finds the reason.

## Human in the loop: escalate when
- Documenting an exception to a security control or a compliance requirement.
- An ADR for an escalated decision needs the approver's name and date; Aviv signs off.
- Publishing diagrams outside the team: they reveal infrastructure.

## Done means
- The listed artifacts exist, or each has an `[N/A]` reason.
- Diagrams match the code and the NFRs; each meaningful decision has an ADR.
- Escalated decisions are recorded with approvals.

## Depends on / feeds into
Depends on: P3 · Architecture, P3 · Architecture decisions, P3 · Trade-offs and options, P3 · Escalations. Feeds: P5 · Repository (docs location), P6 security foundation (threat models use these), operations and onboarding documents.
