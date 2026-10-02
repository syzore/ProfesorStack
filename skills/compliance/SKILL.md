---
name: compliance
description: Use for /compliance, or when a web project gains a cookie banner, an analytics snippet, a login session, or any client-side storage - decides per item whether the law wants consent, a disclosure line, or nothing at all, then audits the result for accessibility. Covers ePrivacy 5(3), GDPR consent validity, CCPA opt-out and WCAG 2.2 AA.
---

# Compliance

Most cookie banners are theatre. They interrupt the visitor, cost conversion,
and buy no protection — because the thing they ask permission for needed no
permission, or because the banner asks in a way that is invalid anyway.

The job is to sort each stored item into one of three buckets and then do only
what its bucket requires.

## The tree

```
Does the app store or read anything on the device?
(cookies, localStorage, sessionStorage, IndexedDB, cache probes,
 fingerprinting, any third-party pixel or embed)
│
├─ No ─────────────────────────────► nothing to do
│
└─ Yes: take each item separately.
   │
   │  Is this item strictly necessary to deliver
   │  what the user explicitly asked for?
   │
   ├─ Yes ──────────────────────────► DISCLOSURE ONLY
   │   auth session, CSRF token, cart, load balancing,
   │   theme, language, high score, the user's own API key
   │
   └─ No ───────────────────────────► CONSENT REQUIRED
       analytics, ads, A/B testing, heatmaps, session replay,
       embedded YouTube/Maps/fonts that phone home,
       anything a third party can read across sites
```

The exemption is the user's purpose, not yours. "We need analytics to run the
business" is your necessity, not theirs — that item needs consent. The test in
ePrivacy Art. 5(3) is *strictly necessary for a service explicitly requested by
the user*, and regulators read "strictly" strictly.

**The law is about storage, not about cookies.** Art. 5(3) says "storing
information, or gaining access to information already stored, in the terminal
equipment" — technology-neutral since the 2009 amendment. localStorage counts.
So does an ETag used as a tracker. Swapping cookies for localStorage to dodge a
banner is a well-known move and it does not work.

## Disclosure only

Do not add a banner. A banner here trains people to dismiss banners and costs
you the one place a real consent request would have landed.

Write the storage into a privacy or cookie page: what is stored, under what key,
why, how long, and whether it ever leaves the device. Storage that never leaves
the device is worth saying out loud — it is the strongest privacy claim most
projects have and almost nobody makes it.

If the item holds a user secret (an API key, a token), say where it lives and
what that implies. `localStorage` is readable by any script on the origin,
so an XSS becomes key theft. That belongs in the disclosure and probably in
the backlog.

Template: `references/policies.md`.

## Consent required

Consent that does not meet all of these is not consent, and the fallback is not
"partial credit" — it is processing without a legal basis.

| Requirement | Source | Fails as |
| --- | --- | --- |
| Asked **before** the item is stored | ePrivacy 5(3) | Script fires on load, banner asks after |
| A clear affirmative act | GDPR 4(11) | "By continuing to browse you agree", scrolling, pre-ticked boxes |
| Reject as easy as accept — same layer, same weight | EDPB Cookie Banner Taskforce, Jan 2023 | Accept on layer 1, reject two clicks deep in "Manage" |
| Granular by purpose | GDPR 4(11) "specific" | One switch for analytics + ads together |
| Withdrawable, as easily as given | GDPR 7(3) | No way back once accepted |
| Refusal leaves the site usable | EDPB Guidelines 05/2020 | Cookie wall |
| **The answer actually gates the script** | — | Both buttons do the same thing |

That last row is the one that gets skipped, and it is the only one a visitor
could ever detect. A banner whose Decline does nothing is worse than no banner:
it is a documented, dated, per-user record of a promise the code does not keep.

Do not use "legitimate interest" for advertising or analytics storage. Art. 5(3)
consent has no legitimate-interest route, and the Taskforce called this out
directly.

Detail and the CJEU/EDPB citations: `references/cookies.md`.

## Not everyone is in the EU

The EU model is opt-in before storage. California's is the opposite: collection
is allowed, and the user gets a way out — a "Do Not Sell or Share My Personal
Information" link, and Global Privacy Control honoured as a valid opt-out
signal. Building only the CCPA model for an EU audience is a straightforward
violation; building only the GDPR model for a US audience usually just costs
conversion.

A site with EU visitors and no geo-detection should build the EU model, because
it is the stricter one and it satisfies both. Geo-gating consent is legitimate
but is a second system to keep correct, so it earns its place only at real
traffic.

## Then check it is usable

Every consent UI is a modal that appears before anything else on the page. That
makes it the single highest-traffic accessibility surface a site has, and it is
routinely the worst.

Run `references/a11y.md` against the banner first, then the app. Non-negotiable
for the banner specifically:

- reachable and operable by keyboard alone, in a sensible focus order
- `Esc` dismisses it, and focus returns where it came from
- it does not obscure the element that has focus (WCAG 2.2 SC 2.4.11)
- targets at least 24×24 CSS px (SC 2.5.8)
- 4.5:1 text contrast, 3:1 for the buttons and the focus ring
- Accept and Reject are the same visual weight — a greyed-out Reject is both a
  contrast failure and a consent-validity failure, which is a useful reminder
  that these two audits are one audit

In the EU the accessibility question is no longer only reputational: the
European Accessibility Act has applied since **28 June 2025** to consumer-facing
e-commerce, banking, transport and e-books, with EN 301 549 (which wraps WCAG AA)
as the conformance route.

## Working a project

1. **Inventory first, judgment second.** Grep for `document.cookie`, `Set-Cookie`,
   `cookies()`, `localStorage`, `sessionStorage`, `indexedDB`, and every
   third-party `<script>`, `<iframe>` and font/CDN origin. Then load the site and
   read the actual Application tab — the inventory in the code is always shorter
   than the inventory in the browser, because embeds set their own.
2. **Sort every item through the tree.** Write the verdict per item. An item you
   cannot classify is usually one nobody can name an owner for, which is its own
   finding.
3. **Do the smallest thing each bucket requires.** Resist upgrading a disclosure
   into a banner because a banner feels more diligent.
4. **Audit the result for a11y** before calling it done. Unplug the mouse
   **before** counting contrast ratios. The primary interaction has to exist
   without a pointer: fractal-chat's reply-click ran off `clientX/clientY`,
   the idea-machine builder's ports resolve via `elementFromPoint`, puzzle-game
   #330's shader cards had no focus. Three codebases, same class of defect.
   Contrast can pass while the product does not exist for a keyboard.
5. **Record it.** Flip the project's cells in `~/.claude/global-rollouts.md` for
   `Cookie/storage compliance` and `Accessibility (WCAG AA)`, in the same commit
   as the work. `n/a` is a real and common answer for the first one.

## Red flags

| Thought | Reality |
| --- | --- |
| "Add a cookie banner to be safe" | A banner for exempt storage is not safety, it is a conversion cost and a dismissal habit. |
| "It's localStorage, not cookies" | Art. 5(3) is about storage on the device. Same rule. |
| "We'll gate the scripts later" | Until then the banner is a written record of a promise the code breaks. |
| "Analytics is essential for us" | Strictly necessary means necessary *to the user*, for what they asked for. |
| "Legitimate interest covers it" | Not for Art. 5(3) storage. There is no such route. |
| "No EU users" | Check. A `.io` domain and an English site collect EU visitors by default. |
| "The banner is temporary" | Consent UIs outlive the sprint that added them. This one is on the critical path of every first visit. |
