---
name: aviv
description: >-
  Rewrites prose into Aviv Profesorsky's voice. Use when the user says
  /aviv, "in my language", "in aviv", "sound like me", "make this mine",
  "rewrite this like I write", or wants text in his style. Also use when
  adding a sample, phrase, or correction to his voice collection.
---

# Aviv

Rewrite the given text so it sounds like Aviv wrote it. Meaning stays.
Voice changes. Unslop first (cut AI tells), then match him — not generic
"human", him.

Always read the collection before rewriting:

`~/.aviv/collection.md`

Then read [voice.md](voice.md) if the collection alone is not enough to
hear the rhythm.

If the collection file is missing, create it from the template at the
bottom of this file and rewrite from [voice.md](voice.md) only.

## Register

Pick one. Destination decides.

- **chat** — messages, comments, slack, talking to an agent. lowercase
  `i`, fragments, missing apostrophes, numbered thoughts. Default.
- **shipped** — UI, landing, public posts, anything a stranger reads.
  Same bones, spelled and punctuated. Capital `I`. No typos.

If he names the register, that wins.

## Rewrite

1. Read the collection. Steal rhythm, not sentences. Do not collage
   quotes unless he asked to reuse a line.
2. Lead with the thing. Reason after. Example last.
3. One thought per sentence. Stack them. "also" starts a new one.
4. Concrete nouns. Photosynthesis, not "the learning journey".
5. Return only the rewrite, unless he asked to see the diff or the
   rules you used.

Done when a paragraph from the collection could sit next to it and not
look like a different person.

## Grow the collection

The collection is how this skill gets better. It lives at
`~/.aviv/collection.md` (home dir, not the public repo).

Append, verbatim, when he:

- pastes a line and says add this / remember this / this is how I say it
- corrects a rewrite ("no, like this") — store **his** version
- says "that's more like it" about a rewrite — store that rewrite

Write under the right heading (`Paragraphs`, `Phrases`, `Sentences`,
`Corrections`). Keep his typos in the sample. Date it if you know the
date. Do not polish a sample as you store it. Do not invent samples.

If a correction is a new rule (not just a one-off wording), add one
line to [voice.md](voice.md).

## Collection template

Use this when `~/.aviv/collection.md` does not exist yet:

```markdown
# Aviv collection

Append only. Verbatim. Never invent. Never clean up a sample.

## Paragraphs

## Phrases

## Sentences

## Corrections
```
