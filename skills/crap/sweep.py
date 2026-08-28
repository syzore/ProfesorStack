#!/usr/bin/env python3
"""CRAP score sweep. CRAP = cc^2 * (1-cov)^3 + cc.

Measures deterministically so a model does not have to read source and count
branches. Prints only offenders. No dependencies beyond the stdlib.
"""
import argparse, ast, json, os, re, subprocess, sys, xml.etree.ElementTree as ET
from pathlib import Path

THRESHOLD = 30.0

INDENT_LANGS = {".py", ".gd"}
EXTS = {".py", ".gd", ".ts", ".tsx", ".js", ".jsx", ".mjs", ".dart", ".go",
        ".java", ".kt", ".cs", ".rb", ".php", ".c", ".cc", ".cpp", ".h", ".swift"}

# Decision keywords. Deliberately excludes else/default/finally/try/switch --
# they introduce no new branch. Ternary and boolean operators are opt-in.
KEYWORDS = r"\b(if|elif|while|for|foreach|case|catch|except|rescue|when)\b"


# ---------------------------------------------------------------- scrubbing
def scrub(src, ext):
    """Blank out comments and string literals, preserving line structure.

    Without this, the word 'if' inside a message string or a commented-out
    block inflates every count.
    """
    line_c = {"#"} if ext in (".py", ".gd", ".rb") else {"//", "#"}
    out, i, n = [], 0, len(src)
    triple = ext in (".py", ".gd")
    while i < n:
        ch = src[i]
        two = src[i:i + 2]
        if triple and src[i:i + 3] in ('"""', "'''"):
            q = src[i:i + 3]
            j = src.find(q, i + 3)
            j = n if j == -1 else j + 3
            out.append(re.sub(r"[^\n]", " ", src[i:j])); i = j; continue
        if ch in "\"'`":
            j = i + 1
            while j < n and src[j] != ch:
                j += 2 if src[j] == "\\" else 1
            j = min(j + 1, n)
            out.append(re.sub(r"[^\n]", " ", src[i:j])); i = j; continue
        if two == "/*" and ext not in (".py", ".gd"):
            j = src.find("*/", i + 2)
            j = n if j == -1 else j + 2
            out.append(re.sub(r"[^\n]", " ", src[i:j])); i = j; continue
        if two in line_c or ch in line_c:
            j = src.find("\n", i)
            j = n if j == -1 else j
            out.append(" " * (j - i)); i = j; continue
        out.append(ch); i += 1
    return "".join(out)


# ------------------------------------------------------------ function scan
SIGS = {
    "indent": [re.compile(r"^([ \t]*)(?:static\s+)?(?:async\s+)?(?:def|func)\s+(\w+)\s*\(")],
    "brace": [
        re.compile(r"^\s*(?:export\s+)?(?:public|private|protected|internal|static|final|override|async|virtual|abstract|\s)*"
                   r"(?:func|function|fun|def|sub)\s*\*?\s*(\w+)\s*[\(<]"),
        re.compile(r"^\s*(?:export\s+)?(?:const|let|var|final)\s+(\w+)\s*(?::[^=]+)?=\s*(?:async\s*)?(?:function\b|\([^;]*?\)\s*(?::[^=]*?)?=>)"),
        re.compile(r"^\s*(?:@\w+\s*)*(?:export\s+)?(?:public|private|protected|internal|static|final|override|async|virtual|abstract|get|set|\s)*"
                   r"(?:[\w<>\[\],.?]+\s+)?(\w+)\s*\([^;{]*\)\s*(?:const\s*)?(?:->\s*[\w<>\[\].,? ]+)?(?::\s*[\w<>\[\].,? ]+)?(?:async\s*)?\{"),
    ],
}
NOT_FN = {"if", "for", "while", "switch", "catch", "return", "case", "with",
          "do", "else", "foreach", "using", "lock", "when", "match"}


def functions(path, text, ext):
    lines = text.split("\n")
    found = []
    if ext in INDENT_LANGS:
        for i, ln in enumerate(lines):
            m = SIGS["indent"][0].match(ln)
            if not m:
                continue
            indent = len(m.group(1).expandtabs(4))
            end = i
            for j in range(i + 1, len(lines)):
                s = lines[j]
                if not s.strip():
                    continue
                cur = len(s[:len(s) - len(s.lstrip())].expandtabs(4))
                if cur <= indent:
                    break
                end = j
            found.append((m.group(2), i + 1, end + 1))
    else:
        for i, ln in enumerate(lines):
            name = None
            for rx in SIGS["brace"]:
                m = rx.match(ln)
                if m and m.group(1) not in NOT_FN:
                    name = m.group(1); break
            if not name:
                continue
            depth, started, end = 0, False, None
            for j in range(i, min(len(lines), i + 4000)):
                for ch in lines[j]:
                    if ch == "{":
                        depth += 1; started = True
                    elif ch == "}":
                        depth -= 1
                        if started and depth == 0:
                            end = j; break
                if end is not None:
                    break
                if started and depth <= 0 and j > i:
                    break
            if end is None:
                continue
            if any(s <= i + 1 <= e for _, s, e in found):   # nested/inner fn
                continue
            found.append((name, i + 1, end + 1))
    return found


def _own_nodes(fn):
    """Every node belonging to this function, not descending into nested
    functions or classes -- those are scored as themselves."""
    stack = list(ast.iter_child_nodes(fn))
    while stack:
        n = stack.pop()
        if isinstance(n, (ast.FunctionDef, ast.AsyncFunctionDef, ast.Lambda,
                          ast.ClassDef)):
            continue
        yield n
        stack.extend(ast.iter_child_nodes(n))


def py_functions(text, boolops=True):
    """Exact complexity for Python via the stdlib AST.

    Real CRAP tools walk an AST rather than pattern-match, and for Python that
    costs nothing extra. Returns None on a syntax error so the caller falls
    back to the regex scanner.
    """
    try:
        tree = ast.parse(text)
    except (SyntaxError, ValueError):
        return None
    out = []
    for fn in ast.walk(tree):
        if not isinstance(fn, (ast.FunctionDef, ast.AsyncFunctionDef)):
            continue
        cc = 1
        for n in _own_nodes(fn):
            if isinstance(n, (ast.If, ast.While, ast.For, ast.AsyncFor,
                              ast.IfExp, ast.ExceptHandler)):
                cc += 1
            elif isinstance(n, ast.comprehension):
                cc += 1 + len(n.ifs)
            elif boolops and isinstance(n, ast.BoolOp):
                cc += len(n.values) - 1
            elif n.__class__.__name__ == "match_case":
                cc += 1
        out.append((fn.name, fn.lineno, getattr(fn, "end_lineno", fn.lineno), cc))
    return out


def complexity(body, ext, ternary=False, boolops=True):
    cc = 1 + len(re.findall(KEYWORDS, body))
    if ternary:
        # ?. ?? ?: and Dart/TS nullable types are not branches.
        cc += len(re.findall(r"\?(?![.?:)\]>=,;])", body)) if ext not in (".py", ".gd") else 0
    if boolops:
        cc += len(re.findall(r"&&|\|\||\band\b|\bor\b", body))
    return cc


# -------------------------------------------------------------- coverage
class Cov:
    """line/branch hit maps keyed by absolute file path."""

    def __init__(self):
        self.files, self.kind = {}, "none"

    def ratio(self, path, lo, hi):
        rec = self.files.get(os.path.abspath(path))
        if not rec:
            return None
        br = [(l, t) for l, t in rec.get("branch", []) if lo <= l <= hi]
        if br:
            return sum(t for _, t in br) / len(br), "branch"
        ln = [(l, h) for l, h in rec.get("line", []) if lo <= l <= hi]
        if not ln:
            return None
        return sum(1 for _, h in ln if h > 0) / len(ln), "line"


def load_lcov(p, cov):
    cur = None
    for raw in Path(p).read_text(errors="ignore").splitlines():
        if raw.startswith("SF:"):
            cur = os.path.abspath(raw[3:].strip())
            cov.files.setdefault(cur, {"line": [], "branch": []})
        elif raw.startswith("DA:") and cur:
            a, _, b = raw[3:].partition(",")
            try: cov.files[cur]["line"].append((int(a), int(b.split(",")[0])))
            except ValueError: pass
        elif raw.startswith("BRDA:") and cur:
            parts = raw[5:].split(",")
            if len(parts) >= 4:
                try: cov.files[cur]["branch"].append(
                    (int(parts[0]), 0 if parts[3] == "-" else (1 if int(parts[3]) > 0 else 0)))
                except ValueError: pass
    cov.kind = "lcov"


def load_cobertura(p, cov):
    root = ET.parse(p).getroot()
    roots = [s.text for s in root.iter("source") if s.text] or ["."]
    for cls in root.iter("class"):
        fn = cls.get("filename") or ""
        abspath = next((os.path.abspath(os.path.join(r, fn))
                        for r in roots if os.path.exists(os.path.join(r, fn))),
                       os.path.abspath(fn))
        rec = cov.files.setdefault(abspath, {"line": [], "branch": []})
        for ln in cls.iter("line"):
            try: num, hits = int(ln.get("number")), int(ln.get("hits") or 0)
            except (TypeError, ValueError): continue
            rec["line"].append((num, hits))
            cc = ln.get("condition-coverage") or ""
            m = re.search(r"\((\d+)/(\d+)\)", cc)
            if m and int(m.group(2)):
                for k in range(int(m.group(2))):
                    rec["branch"].append((num, 1 if k < int(m.group(1)) else 0))
    cov.kind = "cobertura"


def load_istanbul(p, cov):
    data = json.loads(Path(p).read_text())
    for fn, d in data.items():
        if not isinstance(d, dict) or "statementMap" not in d:
            continue
        rec = cov.files.setdefault(os.path.abspath(fn), {"line": [], "branch": []})
        for k, st in d.get("statementMap", {}).items():
            rec["line"].append((st["start"]["line"], d.get("s", {}).get(k, 0)))
        for k, br in d.get("branchMap", {}).items():
            line = br.get("loc", {}).get("start", {}).get("line") or br.get("line")
            for hit in d.get("b", {}).get(k, []):
                if line: rec["branch"].append((line, 1 if hit > 0 else 0))
    cov.kind = "istanbul"


def load_goprofile(p, cov):
    for raw in Path(p).read_text().splitlines()[1:]:
        m = re.match(r"(.+):(\d+)\.\d+,(\d+)\.\d+ \d+ (\d+)$", raw)
        if not m: continue
        f = os.path.abspath(m.group(1).split("/", 1)[-1] if not os.path.exists(m.group(1)) else m.group(1))
        rec = cov.files.setdefault(f, {"line": [], "branch": []})
        for ln in range(int(m.group(2)), int(m.group(3)) + 1):
            rec["line"].append((ln, int(m.group(4))))
    cov.kind = "go"


CANDIDATES = [
    ("coverage/lcov.info", load_lcov), ("lcov.info", load_lcov),
    ("coverage/coverage-final.json", load_istanbul),
    ("coverage.xml", load_cobertura), ("coverage/coverage.xml", load_cobertura),
    ("coverage.out", load_goprofile),
]


def find_coverage(explicit):
    cov = Cov()
    if explicit:
        for name, fn in CANDIDATES:
            if explicit.endswith(Path(name).name):
                fn(explicit, cov); return cov
        for fn in (load_lcov, load_istanbul, load_cobertura, load_goprofile):
            try: fn(explicit, cov); return cov
            except Exception: pass
        sys.exit(f"cannot parse coverage file: {explicit}")
    for name, fn in CANDIDATES:
        if os.path.exists(name):
            try: fn(name, cov); return cov
            except Exception: continue
    return cov


# ------------------------------------------------------------------ scope
def changed_files():
    def sh(*a):
        return subprocess.run(a, capture_output=True, text=True).stdout.split()
    base = None
    for ref in ("origin/HEAD", "origin/main", "origin/master", "main", "master"):
        r = subprocess.run(["git", "merge-base", "HEAD", ref], capture_output=True, text=True)
        if r.returncode == 0:
            base = r.stdout.strip(); break
    files = sh("git", "diff", "--name-only", base) if base else []
    files += sh("git", "diff", "--name-only", "HEAD")
    files += sh("git", "ls-files", "--others", "--exclude-standard")
    return sorted({f for f in files if os.path.exists(f)})


DENY_DIRS = {"node_modules", ".venv", "venv", ".git", "build", "dist", ".next",
             "out", "vendor", "site-packages", "__pycache__", ".dart_tool",
             "target", "obj", "coverage", ".agents", ".claude", "third_party",
             "external", "generated", ".godot", ".gradle", "Pods", ".tox",
             "bower_components", ".mypy_cache", ".pytest_cache", ".idea"}
DENY_FILE = re.compile(r"(\.min\.|\.g\.dart$|\.freezed\.dart$|\.pb\.go$|_pb2\.py$"
                       r"|\.generated\.|\.d\.ts$|-lock\.|\.bundle\.)")
TEST_DIRS = {"test", "tests", "spec", "specs", "__tests__", "testing", "e2e"}
TEST_FILE = re.compile(r"(^test_|_test\.|\.test\.|\.spec\.|_spec\.)")


def excluded(path, include_tests):
    parts = Path(path).parts
    if any(p in DENY_DIRS for p in parts):
        return True
    if DENY_FILE.search(Path(path).name):
        return True
    if not include_tests:
        if any(p.lower() in TEST_DIRS for p in parts):
            return True
        if TEST_FILE.search(Path(path).name):
            return True
    return False


def expand(paths, include_tests=False, no_exclude=False):
    """Dependencies, build output and vendored code are not yours to refactor.
    Left in, they bury the finding under thousands of functions nobody owns.

    Exclusions apply to directory walks only. A file named explicitly is always
    scored -- some repos keep their real source under .claude or a dir this list
    would otherwise skip, and naming it is an unambiguous request.

    Returns (kept, n_excluded) so an empty result can explain itself.
    """
    kept, named, n_walked = [], [], 0
    for p in paths:
        pp = Path(p)
        if pp.is_dir():
            for f in pp.rglob("*"):
                if f.suffix not in EXTS:
                    continue
                n_walked += 1
                # Judge exclusions relative to the root asked for. Naming
                # .venv/lib/foo or .claude/skills/x means "yes, scan it".
                if no_exclude or not excluded(f.relative_to(pp), include_tests):
                    kept.append(str(f))
        elif pp.exists() and pp.suffix in EXTS:
            named.append(str(pp))
    return sorted(set(kept) | set(named)), n_walked - len(kept)


# ------------------------------------------------------------------- main
def main():
    ap = argparse.ArgumentParser(description="CRAP score sweep")
    ap.add_argument("paths", nargs="*", help="files or dirs (default: files changed vs default branch)")
    ap.add_argument("--cov", help="coverage report; auto-detected if omitted")
    ap.add_argument("--threshold", type=float, default=THRESHOLD)
    ap.add_argument("--limit", type=int, default=20)
    ap.add_argument("--all", action="store_true", help="list passing functions too")
    ap.add_argument("--ternary", action="store_true", help="count ?: (off: Dart/TS nullable types false-positive)")
    ap.add_argument("--no-bool", dest="boolops", action="store_false", default=True,
                    help="do not count && and || (McCabe's narrower definition)")
    ap.add_argument("--include-tests", action="store_true", help="score test files too")
    ap.add_argument("--no-exclude", action="store_true", help="do not skip deps, build output, vendored dirs")
    ap.add_argument("--json", action="store_true")
    a = ap.parse_args()

    files, skipped = expand(a.paths or changed_files(), a.include_tests, a.no_exclude)
    if not files:
        if skipped:
            print(f"no source files in scope - {skipped} were excluded as "
                  f"dependencies, build output, vendored or test code.\n"
                  f"If this repo keeps its real source there, name the path "
                  f"directly or pass --no-exclude.")
        else:
            print("no source files in scope")
        return 0
    cov = find_coverage(a.cov)

    rows, kinds = [], set()
    for f in files:
        try:
            text = Path(f).read_text(errors="ignore")
        except OSError:
            continue
        ext = Path(f).suffix
        clean = scrub(text, ext)
        cl = clean.split("\n")
        found = py_functions(text, a.boolops) if ext == ".py" else None
        if found is None:
            found = [(n, lo, hi,
                      complexity("\n".join(cl[lo - 1:hi]), ext, a.ternary, a.boolops))
                     for n, lo, hi in functions(f, clean, ext)]
        for name, lo, hi, cc in found:
            got = cov.ratio(f, lo, hi)
            c, kind = got if got else (0.0, "none")
            kinds.add(kind)
            score = cc ** 2 * (1 - c) ** 3 + cc
            # Crappy is strictly ABOVE the threshold: cc 5 with no tests scores
            # exactly 30 and passes; cc 31 exceeds it even at perfect coverage.
            unfixable = cc > a.threshold
            need = None if unfixable else max(
                0.0, 1 - ((a.threshold - cc) / cc ** 2) ** (1 / 3))
            rows.append({"file": f, "line": lo, "function": name, "cc": cc,
                         "cov": round(c, 3), "cov_kind": kind,
                         "crap": round(score, 1),
                         "status": ("crappy" if score > a.threshold
                                    else "warn" if score > 15 else "clean"),
                         "fix": ("split - tests cannot fix" if unfixable
                                 else f"cover {need:.0%}" if score > a.threshold else "")})
    rows.sort(key=lambda r: -r["crap"])
    bad = [r for r in rows if r["status"] == "crappy"]
    warn = [r for r in rows if r["status"] == "warn"]

    if a.json:
        print(json.dumps({"scored": len(rows), "offenders": len(bad),
                          "warnings": len(warn), "threshold": a.threshold,
                          "coverage": cov.kind,
                          "rows": rows if a.all else bad}, indent=1))
        return 1 if bad else 0

    src = f"{cov.kind} ({'/'.join(sorted(k for k in kinds if k != 'none')) or 'no data'})"
    print(f"{len(bad)} of {len(rows)} functions over {a.threshold:g}"
          f" ({len(warn)} more in the 15-{a.threshold:g} warning band).  coverage: {src}")
    if cov.kind == "none":
        print("NO COVERAGE REPORT FOUND - every cov=0, so this is branch counting only.")
    elif kinds == {"none"}:
        # A report was loaded but matched nothing. Usually the wrong file, or
        # paths recorded relative to a different root. Scoring every function
        # at cov=0 here would look measured and be fiction.
        print(f"WARNING: {cov.kind} report loaded but it covers none of these "
              f"files - paths may not match. Scores below assume cov=0.")
    show = (rows if a.all else bad)[:a.limit]
    if show:
        print(f"\n{'CRAP':>7}  {'cc':>3}  {'cov':>4}  {'location':<46}  fix")
        for r in show:
            loc = f"{r['file']}:{r['line']} {r['function']}"
            loc = loc if len(loc) <= 46 else "\u2026" + loc[-45:]
            print(f"{r['crap']:7.1f}  {r['cc']:3d}  {r['cov']:4.0%}  {loc:<46}  {r['fix']}")
    if len(bad) > a.limit and not a.all:
        print(f"... {len(bad) - a.limit} more")
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main())
