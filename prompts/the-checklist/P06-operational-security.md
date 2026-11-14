> Draft (basic) — pending Aviv's review.

# P6 · Operational security

Checklist: [the-checklist.md § Operational security](../the-checklist.md)

## What this step decides

Who can do what in production, how access is granted in an emergency and taken away, how you notice an attack, and what you do when one lands.

## How to think about it

- Operations are where solo-founder security usually fails: one person holds every key. The aim is to shrink what a single stolen account can do, not to build a security team.
- Treat admin accounts, production access, SSH or console access and least privilege as one access model. Write it as a table: person or service, system, level, reason.
- Emergency access (break-glass) and revocation are the two items people skip. Test them: can you cut a contractor or a leaked token in minutes?
- Audit logging and security alerts exist so someone finds out. An alert with no owner and no response step is not a control.
- Incident response and vulnerability reporting are procedures, short ones. One page of who to call, what to preserve, what to tell users.

## Options and trade-offs

| Decision | Boring default | Heavier option | Pick the heavier one when |
| --- | --- | --- | --- |
| Admin login | MFA, ideally phishing-resistant keys | SSO for everything | More than a handful of people |
| Prod access | Platform console with audited roles | Bastion host, SSH keys | You run your own servers |
| Audit log | Platform audit logs plus app-level log of privileged actions | SIEM | Compliance or a team |
| Vuln reporting | `security.txt` and a mailbox | Bug bounty | Real user base and budget |

## How to choose: solo founder / pre-revenue defaults

- MFA on every admin and vendor account, no shared logins, a break-glass credential stored offline.
- Use platform roles instead of SSH where you can.
- Log privileged actions in the app database or log stream with actor, action and target.
- Write the one-page incident procedure now and run it once as a dry run before launch.

## Human in the loop: escalate when

- Adding anyone, human or agent, to production with write or data-read access.
- Using or rotating the break-glass credential.
- Any suspected incident or breach. Possible notification duties (users, regulators) are a legal call for Aviv and counsel, not an engineering decision.
- Turning off or narrowing audit logging or an alert.
- Agent-run operations that touch production: the agent's own access is part of this model and needs Aviv's sign-off.

## Done means

- Access table exists and matches reality, checked against the actual console and repository settings.
- A revocation drill was done, a security alert has fired in a test and reached a human, and the incident procedure and reporting contact are published.

## Depends on / feeds into

Depends on P2 · Users, Trust and Data Model, P3 · System Architecture, P5 · Engineering Foundation. Feeds P7 · Privacy and Data Governance (breach response), P19 · Observability (Alerts), P22 · Deployment / CI/CD, P23 · Infrastructure / Reliability, P25 · Post-Launch Operations.
