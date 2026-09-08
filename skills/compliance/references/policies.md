# Policy pages — templates

Starting points, not legal advice. They are written to be *specific*, because a
policy that could describe any site describes nothing and is the kind regulators
single out.

Fill every `[bracket]`. A leftover bracket in production is worse than no page.

---

## The disclosure-only case

Most projects land here: everything stored is functional, nothing leaves the
device, no banner is needed. This is a short, honest page — and it makes a claim
most sites cannot.

```markdown
# Privacy

[App name] runs in your browser. [It has no accounts and no server-side
storage / Your account data is described below].

## What is stored on your device

| What | Where | Why | Kept for |
| --- | --- | --- | --- |
| [Best score] | `localStorage["best-thing"]` | [Remembers your record between visits] | [Until you clear site data] |
| [Theme] | `localStorage["theme"]` | [Keeps dark mode on] | [Until you clear site data] |
| [Sign-in session] | Cookie `[name]`, HttpOnly | [Keeps you signed in] | [30 days] |

None of this is sent anywhere. [It never leaves your browser / It is sent only
to our own server at [domain] to [purpose]].

We do not use analytics, advertising, or third-party trackers.

To erase it: clear site data for [domain] in your browser settings.
[Or use the Reset button on [page].]

## [Your API key]

[Delete this section if not applicable.]

[If you enter an API key it is stored in your browser's localStorage and sent
only to [provider], never to us. Any script running on this page could read it,
so use a key scoped to this purpose and revoke it if you stop using the app.]

## Contact

[email]

Last updated: [date]
```

Storage that never leaves the device is the strongest privacy claim a project
can make. Say it plainly and early.

---

## The consent case — cookie policy

Only for sites that actually set non-essential storage. It must match what the
banner offers, category for category; a policy listing categories the banner
cannot refuse is itself a finding.

```markdown
# Cookies

We use [cookies and similar storage] on [domain]. This page lists every one.

You can change your choices at any time — [link/button to reopen preferences].

## Strictly necessary

These make the site work and cannot be switched off. No consent is required for
them, and no consent is asked.

| Name | Provider | Purpose | Expires |
| --- | --- | --- | --- |
| `[session]` | [domain] (first party) | [Keeps you signed in] | [30 days] |
| `[csrf]` | [domain] (first party) | [Prevents forged requests] | [Session] |
| `[consent]` | [domain] (first party) | Remembers this choice | [6 months] |

## Analytics — off unless you accept

| Name | Provider | Purpose | Expires |
| --- | --- | --- | --- |
| `[_ga]` | [Google, USA] | [Counts visits, measures which pages are used] | [2 years] |

[Provider] is located in [country]. [Transfer mechanism, if outside the EEA.]

## [Advertising — off unless you accept]

[Same table shape. Delete the section if you run no ads.]

## Third-party embeds

[Delete if none. Name each one — embeds set their own storage and are the
usual source of the gap between the code inventory and the browser inventory.]

[YouTube videos on [pages] are loaded only after you accept, because YouTube
sets its own cookies.]

Last updated: [date]
```

---

## Banner copy

Short, no persuasion, no "we value your privacy" preamble. The two buttons carry
equal weight.

```
We use [analytics] to see which pages get used. It is off unless you turn it on.
Essential cookies keep you signed in and cannot be turned off.

[ Reject ]  [ Accept ]  [ Choose ]      Cookie policy →
```

Rules the copy has to respect:

- No "by continuing you agree". That is implied consent, invalid since
  *Planet49*.
- `Reject` and `Accept` on the same layer, same size, same contrast. `Choose`
  may be a third option; it may not be the only route to refusal.
- Never pre-tick a category in `Choose`.
- Do not describe advertising or analytics as "essential".

---

## Privacy policy, server-side

For anything with accounts, a database, or an API. GDPR Arts. 13–14 set the
required content; these are the headings that satisfy them.

```markdown
# Privacy policy

**Who we are.** [Name], [address], [email]. [DPO if appointed.]

**What we collect.** [Per category: account data, content you create, logs.
Say what is optional.]

**Why, and on what legal basis.**

| Data | Purpose | Basis |
| --- | --- | --- |
| [Email, password hash] | [Your account] | Contract |
| [Server logs, IP] | [Security, abuse] | Legitimate interest |
| [Analytics] | [Product decisions] | Consent |

**Who else sees it.** [Every processor: host, email, payments, error tracking.
Name them and their country.] [Transfer mechanism if outside the EEA.]

**How long we keep it.** [Per category. "As long as necessary" is not an answer.]

**Your rights.** Access, rectification, erasure, restriction, portability,
objection, and withdrawing consent at any time. Write to [email]; we answer
within one month. You may also complain to your national data protection
authority.

**Security.** [Encryption in transit, at rest, access control. Only claims that
are true.]

**Children.** [Minimum age and how it is enforced.]

**Changes.** [How you notify.]

Last updated: [date]
```

---

## Wiring it up

- Link privacy and cookie pages from the site footer, on every page.
- Give the consent UI a permanent reopen route — a footer link is the norm.
  Art. 7(3) needs withdrawal to be as easy as granting.
- Version the pages. Keep the previous text; a policy change is worthless as
  evidence if the old one is gone.
- Update the date when the content changes, not on every deploy.
- Keep the cookie policy generated from, or checked against, the same list the
  banner gates. Two hand-maintained lists diverge inside one sprint.
