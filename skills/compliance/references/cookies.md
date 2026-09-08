# Storage and consent — the sources

## The text that actually governs

**ePrivacy Directive 2002/58/EC Art. 5(3)**, as amended by 2009/136/EC:

> Member States shall ensure that the storing of information, or the gaining of
> access to information already stored, in the terminal equipment of a subscriber
> or user is only allowed on condition that the subscriber or user concerned has
> given his or her consent, having been provided with clear and comprehensive
> information [...] This shall not prevent any technical storage or access for
> the sole purpose of carrying out the transmission of a communication over an
> electronic communications network, or as strictly necessary in order for the
> provider of an information society service explicitly requested by the
> subscriber or user to provide the service.

Three things follow, and they are the ones most often missed.

**It is not a cookie law.** "Storing information, or gaining access to
information already stored" covers localStorage, sessionStorage, IndexedDB,
Cache API, service worker storage, ETag and HSTS abuse, canvas and font
fingerprinting, and reading a device identifier. Migrating a tracker from a
cookie to localStorage changes nothing.

**It applies whether or not the data is personal.** GDPR governs personal data;
Art. 5(3) governs the device. Confirmed in *Planet49* — the court held the
consent requirement applies "regardless of whether or not the information
[...] is personal data".

**The exemption is defined by the user's request, not the operator's need.** Two
narrow gates: transmission of a communication, or strictly necessary for a
service *explicitly requested by the user*. Analytics is requested by the
operator, so it does not pass.

Consent itself borrows GDPR's definition — Art. 4(11), freely given, specific,
informed and unambiguous, by a statement or clear affirmative action — plus
Art. 7 on demonstrability and withdrawal.

## Case law and regulator positions

**CJEU C-673/17 *Planet49*** (1 Oct 2019) — a pre-ticked checkbox is not valid
consent; consent must be an active behaviour. Also settled the personal-data
point above, and that storage duration and third-party recipients are part of
the "clear and comprehensive information".

**CJEU C-61/19 *Orange România*** (11 Nov 2020) — a pre-filled box in a contract
where the customer must actively strike it out does not show valid consent. The
controller carries the burden of proving consent was freely given.

**EDPB Guidelines 05/2020 on consent** — scrolling or continuing to browse is
not a clear affirmative action. Cookie walls that make access conditional on
consent do not produce freely given consent.

**EDPB Cookie Banner Taskforce report** (adopted 17 Jan 2023), after 700+
complaints filed by noyb. Its findings are the practical checklist most EU DPAs
now apply:

- no reject option on the first layer is an infringement
- pre-ticked boxes are invalid
- deceptive design — contrast, colour, size favouring Accept — invalidates
  consent
- "legitimate interest" is not available for Art. 5(3) storage
- classifying advertising cookies as "essential" is an infringement
- consent must be as easy to withdraw as to give, via a persistent control
- a banner-level "reject" must actually stop the storage

**CNIL v. Google and Facebook** (Dec 2021, €150M and €60M) — the finding was
specifically that accepting took one click and refusing took several. This is
the enforcement precedent for the "same layer, same weight" rule.

**Audience measurement.** There is no EU-wide exemption. CNIL operates a narrow
carve-out for first-party audience measurement strictly limited to the site,
aggregated, with no cross-site tracking and no data sharing — some
self-hosted-and-configured Matomo and Plausible setups qualify. Google Analytics
does not, in any configuration. Treat the carve-out as a French-regulator
position, not a general rule.

## United States

A different model: opt-out, not opt-in.

**CCPA as amended by CPRA** — a "Do Not Sell or Share My Personal Information"
link, a right to limit use of sensitive personal information, and — the part
usually missed — **Global Privacy Control must be honoured** as a valid opt-out
signal in California. GPC is a browser header (`Sec-GPC: 1`); ignoring it while
publishing an opt-out link has been the subject of enforcement, including the
Sephora settlement (Aug 2022, $1.2M).

Other state laws (Virginia, Colorado, Connecticut, Utah, Texas and the rest)
broadly follow the opt-out shape, with Colorado and Connecticut also requiring
universal opt-out signal recognition.

**Practical consequence:** the EU model satisfies both. If you build one system,
build that one, and add the "Do Not Sell or Share" link for US visitors.

## Classifying the common cases

| Item | Bucket | Note |
| --- | --- | --- |
| Auth / session cookie | Disclosure | Explicitly requested — the user asked to log in |
| CSRF token | Disclosure | Strictly necessary |
| Load balancer / sticky routing | Disclosure | Transmission |
| Shopping cart | Disclosure | Explicitly requested |
| Theme, language, dismissed-notice flag | Disclosure | User preference, first-party, never leaves device |
| Game high score in localStorage | Disclosure | Functional, first-party |
| The user's own API key in localStorage | Disclosure | Say where it lives — an XSS reads it |
| Consent record itself | Disclosure | Necessary to honour the choice |
| Google Analytics / GA4 | **Consent** | No exemption in any configuration |
| Plausible / Matomo self-hosted, aggregated | **Consent** (CNIL carve-out possible) | Do not assume; verify the config |
| A/B testing, feature-flag targeting by user | **Consent** | Not requested by the user |
| Heatmaps, session replay | **Consent** | Also a data-minimisation problem |
| Ad pixels, retargeting, conversion tags | **Consent** | Never "essential" |
| Embedded YouTube (default domain) | **Consent** | Sets cookies on load; `youtube-nocookie.com` still stores on play |
| Google Fonts loaded from Google | **Consent** or self-host | Discloses IP to a third country; self-hosting removes the question |
| Embedded Maps, Recaptcha, Intercom, Hotjar | **Consent** | Third-party, loads on render |
| Sentry / error tracking | **Consent** unless strictly scoped | Depends on what the payload carries |

## Implementation notes

**Gate the load, not the fire.** The tag must not be in the DOM before consent.
Loading a script and asking it not to track is not compliance — the request to
the third party already happened, carrying an IP and a referrer.

**Default deny before the answer exists.** First render, no stored decision:
nothing non-essential loads. A "default on, opt out" implementation inverts the
law.

**Store the decision granularly, and version it.** Record per purpose, plus a
timestamp and the version of the banner text. Art. 7(1) requires demonstrating
consent; "the user accepted, some time, to something" does not.

**Rebuild the banner when purposes change.** Adding a new tracker to a category
someone consented to a year ago is not covered by that consent.

**Withdrawal has to be reachable.** A persistent footer link is the usual
answer. A one-time banner with no route back fails Art. 7(3).

**Do not rename the consent cookie to force a re-prompt.** It silently discards
every recorded decision, which destroys the Art. 7(1) evidence and re-interrupts
users who already answered.
