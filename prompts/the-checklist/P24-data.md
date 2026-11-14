> Draft (basic) — pending Aviv's review.

# P24 · Data

Checklist: [the-checklist.md § Data](../the-checklist.md)

## What this step decides

Whether data is safe and controllable: backups running, restore tested, deletion tested, export tested if required, privacy controls tested.

## How to think about it

- A restore test is the only proof of a backup. Use the timed result from P23 against RTO and RPO.
- Deletion must actually remove data, including from backups on their rotation and from third parties. Test it with a real account.
- Export applies where a law or promise requires it (P1, P7). Confirm which with counsel or Aviv.

## Options and trade-offs

No real fork here. Do the items, and record any `[N/A]` or `[DEFER]` with its reason or trigger.

## How to choose: solo founder / pre-revenue defaults

- Run restore and deletion on a copy or test account, never on real users.
- Verify privacy controls (consent, opt-out) behave as P7 specifies.

## Human in the loop: escalate when

- Any test that would touch real user data.
- Doubt about which privacy or deletion duty applies (compliance scope; confirm with counsel).
- Backups found not to be running.

## Done means

- Restore time and data age recorded.
- Deletion and export tests pass end to end.
- Privacy controls tested against the P7 spec.

## Depends on / feeds into

Phase depends on all required prior gates. Launch checks verify earlier work; they do not replace it. Fed by P2 · Data lifecycle, P7 · Privacy and data governance, P23 · Infrastructure / reliability.
