---
name: crap
description: Use for /crap, or when judging whether a function is too risky to change - runs a deterministic sweep that scores every function by CRAP (Change Risk Anti-patterns, cc^2 * (1-cov)^3 + cc), then decides per offender whether the fix is tests or a refactor.
---

# CRAP score

`CRAP(m) = CC(m)² × (1 − Cov(m))³ + CC(m)`

`CC` is cyclomatic complexity, `Cov` is coverage from 0.0 to 1.0. **Strictly
above 30 is crappy**; 30 exactly passes. Coined by Alberto Savoia and Bob Evans
at Google ("This code is crap", Google Testing Blog, 2011) and implemented in
Crap4J.

## Division of labour

**The script measures. You fix.** `sweep.py` finds functions, counts branches,
parses the coverage report and computes scores — deterministic, exact, free.
Reading source to count `if` statements yourself burns tokens to produce a worse
answer that drifts between runs.

Run the sweep, then open only what it flags.

```bash
python3 ~/.claude/skills/crap/sweep.py            # files changed vs default branch
python3 ~/.claude/skills/crap/sweep.py src/       # a path
python3 ~/.claude/skills/crap/sweep.py --json     # for piping
```

Stdlib only, no install. Exits 1 when anything is over threshold, so it drops
into CI unchanged.

| Flag | |
| --- | --- |
| `--cov PATH` | coverage report; auto-detected otherwise |
| `--threshold N` | default 30 |
| `--limit N` | offenders shown, default 20 |
| `--all` | include passing functions |
| `--include-tests` | score test files too |
| `--no-exclude` | do not skip deps, build output, vendored dirs |
| `--no-bool` | stop counting `&&` / `\|\|` |
| `--ternary` | count `?:` as well |

Coverage auto-detects `coverage/lcov.info`, `coverage-final.json` (istanbul),
`coverage.xml` (cobertura), `coverage.out` (Go). Branch coverage is used when
the report has it, line coverage otherwise, and the header says which. If a
report is found but covers none of the scanned files, the sweep warns instead of
reporting a confident `cov = 0`.

**Prefer a native reporter where one exists** — `phpunit --coverage-crap4j`,
phpmetrics, the Crap4J Java plugin, `jest-crap-reporter`, NDepend. They work
from a real compiler front end. `sweep.py` earns its place on everything else,
GDScript and Dart included.

## Three consequences, before you measure anything

**Below cc 6, nothing is ever crappy.** With no tests a function scores
`cc² + cc`, and cc 5 lands on exactly 30 — which passes. The sixth branch is
where an untested function first fails, at 42.

**At cc 31 and above, tests cannot save it.** The trailing `+ cc` is a floor, so
a 31-branch function scores 31 even at perfect coverage. Writing tests for it is
wasted work before you start. Split it. (cc 30 is the knife edge: it needs
exactly 100%.)

**With no coverage report, this is branch counting.** cov is 0 everywhere and
the threshold collapses to "cc ≥ 6". The sweep says so in its header. Do not
wire up a coverage tool to learn something arithmetic already told you.

## Which lever

For anything over 30, `cc` decides what to do — not the score.

**cc ≥ 31** — refactor. Tests are provably pointless here.

**cc ≤ 30** — either lever works, so pick by cost. Coverage needed to get back
to 30:

| cc | Coverage needed |
| --- | --- |
| ≤ 5 | none, cannot be crappy |
| 6 | 13% |
| 8 | 30% |
| 10 | 42% |
| 12 | 50% |
| 15 | 59% |
| 18 | 67% |
| 20 | 71% |
| 25 | 80% |
| 29 | 89% |
| 30 | 100% |
| ≥ 31 | impossible |

The sweep prints this per function as `cover 42%`. Read it as a cost estimate.
At cc 10 two tests clear it; at cc 25 you must cover four fifths of a tangled
function, and splitting is usually cheaper.

**Splitting wins twice**, which the table understates. The `cc²` term means
halving complexity quarters that part of the score, and the pieces are far
easier to cover. A cc-14 function at zero coverage scores 210; split evenly it
is 56 and 72 before a single test exists.

Between 15 and 30 the sweep counts a warning band. Worth a look when you are
already in the file; not worth a special trip.

## Then fix, in this order

1. **Read the top offender only.** The list is ranked, and the tail is usually
   the same problem in smaller form.
2. **Name the branches.** Guard clauses and early returns delete decision points
   rather than moving them.
3. **Extract the densest block** into a named function. Complexity leaves the
   parent, and the extracted piece is testable alone.
4. **Re-run the sweep.** The number moved or it did not. Never claim an
   improvement you have not measured.

Refactor before writing tests when both are needed, or the tests pin the shape
you are about to change.

## How counting works

Base 1, then +1 per branching construct: `if` / `elif`, `while`, `for`, each
`case`, each `catch` / `except`, and each `&&` / `||`. Nothing for `else`,
`default`, `finally`, `try`, or `switch` itself — they add no new path.

**Python is exact**, walked with the stdlib `ast`: nested functions are scored
as themselves rather than folded into the parent, and comprehensions and
`match` cases are counted properly. Every other language uses a regex scanner
over source with comments and string literals blanked out first.

Two deliberate choices in the scanner:

- **`&&` and `||` count**, matching Crap4J and the definition most tools use.
  `--no-bool` drops to McCabe's narrower one. Either is defensible; switching
  between runs is not, because the numbers are not comparable.
- **`?:` does not count by default.** Dart and TypeScript nullable types
  (`String?`) are indistinguishable from a ternary by regex and would inflate
  every count. `--ternary` turns it on for languages without them. Python
  ternaries are counted regardless, because the AST leaves no ambiguity.

Outside Python it is a regex parser, not a compiler. Treat a surprising number
as a question, not a verdict — closures and callbacks may be attributed to the
enclosing function.

Dependencies, build output, vendored and test directories are skipped on a
directory walk. A path named explicitly is always scored, since some repos keep
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
| Treating 30 as broken and 29 as safe | A smell with an arbitrary line, not a gate |

The last one matters most. A cc-4 function holding a payment calculation
deserves tests at a score of 20; a cc-9 match over an enum may be fine forever
at 90. The threshold starts the conversation, it does not end it.
