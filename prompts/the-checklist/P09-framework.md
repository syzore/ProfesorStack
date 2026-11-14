> Draft (basic) — pending Aviv's review.

# P9 · Framework

Checklist: [the-checklist.md § Framework](../the-checklist.md)

## What this step decides

Whether to adopt an orchestration framework at all, and if you do, how to keep it contained.

## How to think about it

- The default answer is no. A single call, or a short fixed sequence, needs an SDK and a function, not a framework.
- Ask what the framework gives you that twenty lines would not: durable state, branching graphs, built-in tracing, tool loops. If you cannot name it, you do not need it.
- If you adopt one, its types must not leak into the domain. Keep all framework code behind your own small interface, so replacing it is a contained change.
- Frameworks move fast. Upgrades are recurring work, so decide the cadence and who owns it.

## Options and trade-offs

| Option | Good for | Cost |
| --- | --- | --- |
| Direct SDK calls | One to a few calls, fixed flows | You write retries and logging yourself |
| Small helper library | Structured output, retries | Another dependency to track |
| Orchestration framework | Multi-step agent graphs with state | Upgrade churn, indirection, harder debugging |

## How to choose: solo founder / pre-revenue defaults

- Use the provider SDK directly with your own thin wrapper.
- Revisit only when a flow needs durable multi-step state or the wrapper is turning into a framework itself.
- Record the decision, including what would change it, so it is not reopened by novelty.

## Human in the loop: escalate when

- Adopting a framework (new dependency that shapes the architecture, hard to remove).
- A framework that requires a paid hosted service or sends data to a new vendor.
- A major-version upgrade that changes behavior of production flows.

## Done means

- The decision is recorded (chosen or rejected, with reason).
- If chosen, framework imports are confined to one module, and an upgrade procedure and owner are named.

## Depends on / feeds into

Depends on P2 · Users, Trust and Data Model, P3 · System Architecture, P6 · Security Foundation, P7 · Privacy and Data Governance. Follows P9 · Model layer. Feeds P9 · Agents / tools, P5 · Engineering Foundation (dependency policy), P6 · Supply chain.
