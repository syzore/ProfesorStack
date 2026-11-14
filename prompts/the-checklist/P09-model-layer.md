> Draft (basic) — pending Aviv's review.

# P9 · Model layer

Checklist: [the-checklist.md § Model layer](../the-checklist.md)

## What this step decides

How the app talks to models: which calls exist, which provider and model each uses, the limits (time, tokens, cost, per user, global), caching, streaming, structured output, and PII censoring before text leaves the process.

## How to think about it

- Start with an inventory: every place text goes to a model, what is in it, and what the app does with the answer. Anything unlisted cannot be limited or evaluated.
- Every call needs the five behaviors the rules demand: cost, abuse, privacy, reliability, evaluation. Here that means cost limits (per user and global), timeouts and retries, the PII censor, and a fallback.
- Limits must fail closed: when a budget is exhausted or the censor errors, the call is blocked and the user gets a clear message. A silent unlimited path is the main way these bills run away.
- The PII censor items are a chain: catch the types you define, keep the token map in memory only, restore after the response, and keep the map out of logs, storage and the outbound request. Pick a tool or build it, then record owner, failure mode and replacement path.
- Abstraction is useful only where you may switch providers; a thin wrapper around your few calls is usually enough.

## Options and trade-offs

| Decision | Boring default | Heavier option | Pick the heavier one when |
| --- | --- | --- | --- |
| Provider | One provider, one thin wrapper | Multi-provider router | Outages or price shifts hurt, proven by incident |
| Model choice | Smaller model by default, larger where a test shows need | Always the largest | Quality tests fail on the smaller one |
| Output | Structured output with schema validation | Free text parsing | Output is only shown to a human |
| Caching | Cache identical requests | Semantic cache | High repeat volume and acceptable staleness |
| Censor | Maintained library | In-house build | Library does not cover required PII types |

## How to choose: solo founder / pre-revenue defaults

- Set a hard global monthly cap and a per-user daily cap before the first public call. Choose the numbers from the expected margin per user, treating them as examples to revisit.
- Timeout and a bounded retry with backoff. One fallback (smaller model or a graceful no-AI path).
- Censor by default for any user-supplied text. Skipping it needs a recorded reason.

## Human in the loop: escalate when

- Adding or switching a provider or paid plan (new vendor, new data recipient, P7 vendor inventory).
- Raising any cost cap, or removing a per-user or global limit.
- Sending a new category of personal data to a model, or disabling the censor.
- A censor failure mode that would let text through (never auto-resolve; the call must block).
- Choosing a model that changes unit economics noticeably.

## Done means

- Inventory complete. Every call has timeout, retry, token and cost limits, with a test showing the limit fires.
- The censor blocks on failure (tested by forcing a failure) and its map never appears in logs or storage, and spend is visible per user and in total.

## Depends on / feeds into

Depends on P2 · Users, Trust and Data Model, P3 · System Architecture, P6 · Security Foundation, P7 · Privacy and Data Governance. Feeds P9 · Prompting, P9 · Output safety, P9 · Evaluation, P8 · API (per-user limits), P19 · Observability (cost metrics), P18 · Performance.
