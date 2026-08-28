---
name: crap
description: Use for /crap, or when judging whether a function is too risky to change - runs a deterministic sweep that scores every function by CRAP (Change Risk Anti-patterns, cc^2 * (1-cov)^3 + cc), then decides per offender whether the fix is tests or a refactor.
---

# CRAP score

`CRAP = cc² × (1 − cov)³ + cc` — `cc` is cyclomatic complexity, `cov` is test
coverage from 0 to 1. At 30 or above the function is too risky to change safely.
From Crap4J, by Alberto Savoia and Bob Evans.

## Division of labour

**The script measures. You fix.** `sweep.py` finds functions, counts branches,
parses the coverage report and computes scores — all deterministic, all exact,
all free. Reading source to count `if` statements yourself burns tokens to
produce a worse answer that drifts between runs.

Run the sweep, then open only the functions it flags.

```bash
python3 ~/.claude/skills/crap/sweep.py            # files changed vs default branch
python3 ~/.claude/skills/crap/sweep.py src/       # a path
python3 ~/.claude/skills/crap/sweep.py --json     # for piping
```

Stdlib only, no install. Exits 1 when anything scores at or above the
threshold, so it drops into CI unchanged.

| Flag | |
| --- | --- |
| `--cov PATH` | coverage report; auto-detected otherwise |
| `--threshold N` | default 30 |
| `--limit N` | offenders shown, default 20 |
| `--all` | include passing functions |
| `--include-tests` | score test files too |
| `--no-exclude` | do not skip deps, build output, vendored dirs |
| `--ternary` / `--bool` | count `?:` / `&&`, both off by default |

Coverage is auto-detected from `coverage/lcov.info`, `coverage-final.json`
(istanbul), `coverage.xml` (cobertura), or `coverage.out` (Go). Branch coverage
is used when the report has it, line coverage otherwise, and the output says
which.

## Three consequences, before you measure anything

**Below cc 5, nothing is ever crappy.** With no tests a function scores
`cc² + cc`, which is 20 at cc 4. Complexity alone cannot reach 30 until the
fifth branch.

**At cc 30 and above, tests cannot save it.** The trailing `+ cc` is a floor, so
a 30-branch function scores exactly 30 at *perfect* coverage and stays crappy.
Writing tests for it is wasted work before you start. Split it.

**With no coverage report, this is branch counting.** cov is 0 everywhere and
the threshold collapses to "cc ≥ 5". The sweep says so in its header. Do not
spend twenty minutes wiring up a coverage tool to learn something arithmetic
already told you — if the repo has no tests, the number is what it is.

## Which lever

For anything at or above 30, `cc` decides what to do — not the score.

**cc ≥ 30** — refactor. Tests are provably pointless here.

**cc < 30** — either lever works, so pick by cost. Coverage needed to drop
under 30:

| cc | Coverage needed |
| --- | --- |
| ≤ 4 | none, cannot be crappy |
| 5 | any at all |
| 6 | 13% |
| 8 | 30% |
| 10 | 42% |
| 12 | 50% |
| 15 | 59% |
| 18 | 67% |
| 20 | 71% |
| 25 | 80% |
| 29 | 89% |
| ≥ 30 | impossible |

The sweep prints this per function as `cover 42%`. Read it as a cost estimate.
At cc 10 two tests clear it; at cc 25 you must cover four fifths of a tangled
function and splitting is usually cheaper.

**Splitting wins twice**, which the table understates. The `cc²` term means
halving complexity quarters that part of the score, and the smaller pieces are
far easier to cover. A cc-14 function at zero coverage scores 210; split evenly
it is 56 and 72 before a single test exists.

## Then fix, in this order

1. **Read the top offender only.** The list is ranked; the tail is usually the
   same problem in smaller form.
2. **Name the branches.** Guard clauses and early returns delete decision points
   outright rather than moving them.
3. **Extract the densest block** into a named function. Complexity leaves the
   parent, and the extracted piece is testable in isolation.
4. **Re-run the sweep.** The number moved or it did not. Do not claim an
   improvement you have not measured.

Refactor before writing tests when both are needed, or the tests pin the shape
you are about to change.

## What the sweep will not tell you

It is a regex parser, not a compiler. Treat a surprising result as a question.

- Nested closures and callbacks may be attributed to the enclosing function.
- `--ternary` is off because Dart and TypeScript nullable types (`String?`) look
  identical to `?:` and would inflate every count. Turn it on for languages
  without them.
- `&&` and `||` are off, matching McCabe's original definition. Extended
  complexity counts them. Either is defensible; switching between runs is not,
  because the two numbers are not comparable.
- Dependencies, build output, vendored and test directories are skipped on a
  directory walk. A path you name explicitly is always scored — some repos keep
  real source under `.claude` or similar.

## Common mistakes

| Mistake | What it costs |
| --- | --- |
| Reading source to count branches yourself | Tokens spent on a worse, drifting answer |
| Line coverage reported as branch coverage | The cube turns a small error into a wrong verdict |
| Writing tests for a cc-40 function | Cannot reach 30. Wasted before it starts |
| Scoring a whole repo unasked | A wall of numbers about code nobody is touching |
| Counting `&&` in one run and not the next | Two incomparable numbers, no trend |
| Chasing the score with tests that assert nothing | Coverage rises, risk does not move |
| Treating 29 as safe and 30 as broken | A smell with an arbitrary line, not a gate |

The last one matters most. A cc-4 function holding a payment calculation
deserves tests at a score of 20; a cc-9 match over an enum may be fine forever
at 90. The threshold starts the conversation, it does not end it.
