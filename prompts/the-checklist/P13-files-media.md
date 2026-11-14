> Draft (basic) — pending Aviv's review.

# P13 · Files / Media

Checklist: [the-checklist.md § Files / Media](../the-checklist.md)

## What this step decides

How user files are accepted, checked, stored, served, transformed and removed. Phase-level guide.

## How to think about it

- Uploads are untrusted input that is also large and stored forever. Think in a pipeline: limit, validate, store in isolation, serve under access control, transform safely, delete completely.
- Validate type by content, not just extension or declared content type, and sanitize file names. Never use a user-supplied name as a path.
- Storage isolation means uploaded files cannot execute and are not served from your app origin. Serve through signed, expiring URLs with access-control checks.
- Processing is an attack surface: image-processing limits and archive-bomb protection bound CPU, memory and disk.
- Deletion and backup handling connect to P7: when the user or file is deleted, derived files (thumbnails, CDN copies) go too, and backups expire on the stated schedule.
- Metadata stripping matters when files carry location or device data.

## Options and trade-offs

| Decision | Boring default | Heavier option | Pick the heavier one when |
| --- | --- | --- | --- |
| Storage | Managed object storage, private buckets | Own file server | Never |
| Access | Short-lived signed URLs | Proxy through app | Per-request logic needed |
| Malware scan | Defer unless files are shared between users | Scan on upload | Users download each other's files |
| Processing | Provider or sandboxed worker with limits | In-process | Never for untrusted input |

## How to choose: solo founder / pre-revenue defaults

- Smallest possible upload surface: allow-list a few types, a small size limit, private bucket, signed URLs.
- Run processing in a background job with time and memory limits.
- Rate-limit uploads per user.

## Human in the loop: escalate when

- Opening uploads to anonymous users, or allowing user-to-user sharing.
- Allowing file types that can execute or contain active content (HTML, SVG, archives, office macros).
- Hosting content that may be illegal or contain minors' data. Legal exposure is Aviv's call.
- Choosing a CDN or scanning vendor (new paid vendor, new data recipient).
- Bulk deletion of stored files.

## Done means

- Each limit and validation has a test with a hostile sample (oversized, mislabeled, traversal name, archive bomb).
- Another user's file cannot be fetched by guessing a URL, expired links fail, and deleting a file removes derived copies.

## Depends on / feeds into

Depends on P2 · Users, Trust and Data Model, P3 · System Architecture, P6 · Security Foundation, P8 · Core Product Implementation. Feeds P6 · Application security (file-upload security), P7 · Privacy and Data Governance (deletion), P16 · Background Jobs, P18 · Performance, P23 · Infrastructure / Reliability.
