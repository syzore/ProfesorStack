---
name: user-path-recognition
description: Use when deciding which action to promote onto a screen, cutting the number of taps to a common action, instrumenting which routes people actually take through an app, or acting on funnel data where one branch dominates its parent. Covers recording paths, the threshold to act, where a shortcut can live, and how to tell whether it worked.
---

# User path recognition

Two jobs, strictly in that order. Record the routes people actually take, then
shorten the ones they take often. Do the second without the first and you are
guessing which button deserves promotion, and a wrong guess costs the most
valuable space on the screen for as long as it stays there.

## This runs on analytics you already have

Path recognition is a query over the event stream, not a second system. If the
app has no product analytics, that comes first. See `user-feedback` for the
choice of stack, offline queuing, the pseudonymous ID, and the declaration each
one costs.

## 1. Record the paths

A path is the ordered list of events in one session up to a terminal action
(signed in, purchased, level started, note saved).

- Name events after what the user pressed, not after the widget. `login_google`,
  never `btn_2`. A rename later cannot repair old rows.
- Log a session ID and a monotonic step index. Timestamps alone will not
  reconstruct order once events arrive out of a flush queue.
- **Log the entry point as a property.** `source: main_screen | login_sheet |
  deep_link`. Without it, a shortcut you add later is indistinguishable from the
  route it replaced, and you can never answer whether it is used.

## 2. Read them

Count sessions, not events. One stuck user tapping the same button nine times is
one vote, not nine, and rage taps look exactly like demand if you count rows.

Rank candidates by clicks saved, which is frequency times steps removed. A
two-step path taken by 60% of sessions beats a five-step path taken by 2%.

The signal worth hunting is a **sub-choice that dominates its parent**. When 71%
of people who open the login sheet pick Google, the sheet is asking a question
whose answer is already known. That is more precise than "this takes too many
taps", and it is the case where promotion clearly wins.

Two things that look similar and are not:

- A path everyone takes to reach one setting. Hoist the setting, leave the menu.
- Back and forth between two screens. That is a naming or layout problem. A
  shortcut papers over it and the confusion stays.

**Threshold to act:** roughly 100 sessions on the path, and a branch taking a
clear majority, over 60%. Below that you are promoting noise, and noise arrives
with confidence attached.

## 3. Add the shortcut

Cheapest first. The best shortcut removes the choice rather than moving it.

1. **Make it the default.** Pre-select the dominant option, or remember the last
   one. Zero taps, no new screen space.
2. **Promote it in place.** The button appears on the screen before the one it
   used to live on.
3. **Put it outside the app.** Android dynamic shortcuts and iOS Home Screen
   quick actions on long-press, a notification action, a deep link. These cost no
   in-app space at all and are consistently forgotten.

Rules:

- **Keep the long path.** A shortcut is an addition. People who learned the old
  route must still find it. The one exception is an intermediate screen that
  exists only to disambiguate and whose every option now has a shortcut. Then
  delete it outright.
- **Budget the surface.** Cap shortcuts per screen at about three and keep them
  as a ranked list, so adding a fourth means arguing which one drops. Without the
  cap every promotion is free and the screen fills up.
- **Never shortcut a destructive or paying action.** Delete account, purchase,
  send, publish. Frequency is not consent, and the step you would remove is the
  one doing the work.
- **Prefer one global change to per-user personalization.** A UI that rearranges
  itself defeats muscle memory and cannot be supported over a message, because
  "the third button" is no longer the same button for two people. If you
  personalize anything, personalize the order of a list that is already visible.

## 4. Check whether it worked

The metric is median steps to the terminal action, plus the completion rate of
that action. A shortcut with plenty of clicks and a flat completion rate moved a
click, it did not save one.

Then read the split:

- New route takes most of the traffic and the old one falls to near zero. The
  intermediate screen is now dead. Remove it.
- Both stay busy. They serve different intents. Keep both.
- The other options on the old screen lose absolute volume. The new button is
  catching mis-taps rather than intent. Back it out.

**The promoted option grows because it is visible.** Its post-promotion share is
not evidence the promotion was right, and quoting it as though it were is the
easiest mistake here to make. Judge on completion and steps, decided before you
look.

At low volume, ship it as a sequenced change and compare before and after rather
than running arms. `user-feedback` has the power arithmetic and why a per-attempt
metric settles in days where retention never will.

## Worked example

Login, then Login with Google.

| | |
| --- | --- |
| Observed | 71% of sessions opening the login sheet choose Google. Four options. Median three taps to signed in. |
| Change | Google button on the main screen, beside Log in. Sheet unchanged. |
| Expected | Two taps for those 71%. Everyone else is unaffected. |
| Confirms it | Sign-in completion up or flat, median steps down, Apple and email counts steady in absolute terms. |
| Backs it out | Sign-in completion down, or the other methods lose volume. |

## Common mistakes

| Mistake | What it costs |
| --- | --- |
| Shortcut before instrumentation | A permanent screen slot spent on a guess |
| Counting events instead of sessions | Rage taps read as demand |
| Replacing the old path | Breaks everyone who already learned it |
| A UI that rearranges per user | Nobody can be talked through it |
| Promoting a destructive action | The confirmation was the feature |
| Citing post-promotion share as proof | Circular. It grew because you promoted it |
| No `source` property on events | You can never tell whether the shortcut is used |
