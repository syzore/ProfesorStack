> Draft (basic) — pending Aviv's review.

# P04 · Internationalization

Checklist: [the-checklist.md § Internationalization](../the-checklist.md)

## What this step decides
Which languages and locales the product supports and what it takes to support them: string extraction, plurals, date, time, number and currency formats, timezone, right-to-left, text expansion, translated errors, locale validation and the translation workflow.

## How to think about it
- Start with the supported languages from P0 · Product and P1 · Jurisdiction. One language is a valid answer.
- Externalizing strings is cheap now and expensive later. Do it even for one language if a second is plausible.
- Locale touches more than words: plurals, dates, numbers, currency, timezones, name and address forms, validation rules (phone, postal).
- RTL changes layout; decide before building the UI if it may be needed.
- Translated error messages need keys and tested fallbacks, not concatenated sentences.

## Options and trade-offs
| Choice | Pick when | Cost |
| --- | --- | --- |
| One language, strings externalized | Default | Small upfront work |
| One language, strings inline | Throwaway experiment | Costly retrofit |
| Several languages | Real demand per market | Translation, QA, layout work |
| RTL support | Target market uses it | Layout and testing work |

## How to choose: solo founder / pre-revenue defaults
- Default: single language, all user-facing strings in a resource file, locale-aware formatting through the platform's standard library, UTC in storage and local time in display.
- Use machine translation only with human review for anything legal, billing or safety.
- Add a language only when a named user group needs it.

## Human in the loop: escalate when
- Adding a market or language (scope, support and legal effects).
- Translation vendor or a paid localization service (new vendor).
- Legal or billing text in another language: confirm with counsel.
- Currency or tax display for a new region.

## Done means
- Languages and locales listed; each item addressed or `[N/A]` with reason.
- No user-facing string is hardcoded outside the resource file.
- Translation workflow and owner are named if more than one language.

## Depends on / feeds into
Depends on: P0 · Product (geography), P1 · Jurisdiction, P4 · UX. Feeds: frontend implementation, P12 · Email / notifications content, P25 · Daily/continuous (support), P24 · Launch.
