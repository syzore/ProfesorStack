---
name: jev
description: Use when code needs a typed judgment from a model instead of generated text - scoring, classifying, a true/false check, ranking by score, or LLM-as-judge on a free-form answer - or when the user mentions Jev, TypeSafe or System One. Covers the request, picking Choice/Score/Noul, confidence gating, caching, cost logging and failure fallback.
---

# Jev

Jev is TypeSafe's System One model: you send a **state** (text, object or array) and named, typed **questions**; it returns typed answers with probabilities. No text, no parsing. Docs: https://docs.typesafe.ai (index for agents: `/llms.txt`; append `.md` to any page path for raw markdown).

## Jev or a generative LLM

Reach for Jev when your code branches, sorts or routes on the answer: a label, a level, a yes/no probability. Reach for a generative LLM when a human reads the output, or the answer is open-ended text (an explanation, a rewrite, a new question).

Ask **atomic** questions: each one a judgment an expert makes in a few seconds. A judgment that weighs several factors becomes one question per factor, combined in code with your own weights. All questions in one call run in parallel and in isolation, so fan-out barely moves latency; extra questions still cost tokens.

## Pick the primitive per question

| Primitive | Use for | `criteria` | Answer fields |
| --- | --- | --- | --- |
| `choice` | one label from a set | `{label: description or null}`, max 255 | `choice`, `probabilities`, `confidence` |
| `score` | a position on an ordered rubric | list of levels, low → high, 2-10 | `score` (float, can sit between levels), `legend`, `probabilities`, `confidence` |
| `noul` | is this statement true? | optional `{true: ..., false: ...}` | `noul` (0..1), no `confidence` |

Score levels are judged one by one, blind to their number and neighbours: describe each as a concrete situation ("broken, workaround exists"), never as a degree or digit. One dimension per Score. To combine Scores, normalise each by `score / (len(criteria) - 1)` first.

## Request

`pip install typesafe-sdk` (Python >= 3.10). The client reads `TYPESAFE_API_KEY`.

```python
from typesafe_sdk import Choice, Noul, Score, TypeSafeClient, TypeSafeError

with TypeSafeClient() as client:  # AsyncTypeSafeClient for async code
    response = client.system_one(
        state=text,
        questions={
            "team": Choice(instructions="Which team should handle this",
                           criteria={"billing": "Payment issues", "technical": "Bugs"}),
            "frustration": Score(instructions="How frustrated the customer is",
                                 criteria=["Calm, stating facts", "Frustrated but civil", "Angry, strong language"]),
            "urgent": Noul(instructions="The message conveys time pressure"),
        },
    )
response.answers["team"].choice, response.answers["team"].confidence
response.usage.input_tokens, response.usage.output_tokens
```

```bash
curl -X POST https://api.typesafe.ai/v1/systemone \
  -H "Authorization: Bearer $TYPESAFE_API_KEY" -H "Content-Type: application/json" \
  -d '{"state": "...", "model": "jev-latest",
       "questions": {"urgent": {"type": "noul", "instructions": "The message conveys time pressure"}}}'
```

## Wiring it into an app

Every Jev call site has all five:

1. **Key from the environment.** Read `TYPESAFE_API_KEY` only; add the name with an empty value to `.env.example`. The key value never appears in code, tests, logs, docs or commits.
2. **Confidence gate.** Choice/Score: act on high confidence, confirm or degrade on medium, take the fallback on low. Noul: threshold the probability in code, with a middle band (`|2p - 1|` gives a comparable confidence). Start the floor near 0.5, raise it for destructive or costly actions, tune on real data.
3. **Fallback.** Define what happens with no answer: a default, a generative-LLM path, or skipping the feature. Catch `TypeSafeError` (base of API, timeout and connection errors); the SDK's default `RetryPolicy` already retries 408, 429 and 5xx, timeouts and connection errors (2 retries, 30 s timeout), so pass a tighter `RetryPolicy(max_retries=..., timeout=...)` on user-facing paths. Without the SDK, retry 429/529 with exponential backoff yourself. Rate limits and quotas are undocumented: treat 429 after retries as the fallback case.
4. **Cache.** A judgment on static content (a topic, a question, a pair of topics) is computed once and stored, keyed by state + questions + model. In graph-knowledge-game, a backend script that writes judgments onto graph nodes follows `caching-llm-data-scripts`.
5. **Log cost and latency.** Log `usage.input_tokens`, `usage.output_tokens`, the returned `model` version and wall time per call, so spend and drift are visible.

Done when the call site has all five, and the questions were tried on a handful of real examples with the answers checked by eye.

## First uses in graph-knowledge-game

- **Interest of a topic at a level**: Score with levels described as learner reactions.
- **Prerequisite direction between two topics**: state holds both topics; Choice `{a_before_b, b_before_a, independent}`, gated on confidence.
- **Judging a free-form quiz answer**: state holds question, reference answer and learner answer; Noul "the learner's answer means the same as the reference", or a Score for partial credit.
