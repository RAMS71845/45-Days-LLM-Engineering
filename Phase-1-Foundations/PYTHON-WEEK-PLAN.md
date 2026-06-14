# 🐍 Python Power-Up Week — Detailed Plan (Days 1–7)

The prerequisite week of **SSAI-101**. Goal: take students with *only* Python basics and lock in
every skill the LLM track (Day 8+) assumes. Source outline: [`../dump/python.txt`](../dump/python.txt);
day ranges fixed by [`../COURSE-PLAN.md`](../COURSE-PLAN.md).

> **Audience:** complete beginners (pre-final/final-year B.Tech, BCA/MCA). One concept per module,
> heavily-commented runnable `.py`, India-context examples, free-tier only.

## Status at a glance
| Day | Topic | Build status |
|----:|-------|--------------|
| 1 | Setup, data types, operators & variables | ✅ Built & verified |
| 2 | Strings, f-strings & string methods | ✅ Built & verified (+ trainer's guide) |
| 3 | Booleans, conditionals & logic | ✅ Built & verified (+ trainer's guide) |
| 4 | Loops | ✅ Built & verified |
| 5 | Functions & scope | ✅ Built & verified |
| 6 | Data structures | ✅ Built & verified |
| 7 | Errors, modules & OOP | ✅ Built & verified |

## 🐙 GitHub Basics mini-track (Days 4–6)
A beginner-friendly **3-part GitHub intro** runs alongside the code on Days 4–6 — one visual deck per
day in that day's `github-basics/` folder (`index.html` + speaker-notes `README.md`, same Softpro deck
template as the career talks, with inline-SVG diagrams). Goal: students *understand why* version
control matters and *start using* GitHub for their course work.

| Day | Deck | Visuals |
|----:|------|---------|
| 4 | **Why GitHub?** — Git vs GitHub, commit=snapshot, repo, local vs remote, make an account | commit-timeline SVG, local↔remote SVG |
| 5 | **The Everyday Workflow** — `status → add → commit → push`, the 3 areas, `.gitignore`, `pull` | staging-pipeline SVG, terminal blocks |
| 6 | **Branching & Collaboration** — branches, merge, conflicts, pull requests, forks, repo-as-portfolio | branch-and-merge graph SVG, PR-flow strip |

Each deck ends with a ≤15-min **GitHub Action** (create account → push Day-4 folder → open first PR),
so by Day 6 every student has a live repo. `.env`/secrets hygiene is taught in Part 2 ahead of the AI track.

## Per-day shape (every day is identical in structure)
Each day = a `Day-NN-Topic/` folder following the repo convention:
`README.md` (objectives + module table + how-to-run + exercise) · numbered `NN-concept/` modules
(teaching `README.md` + runnable `snake_case.py`) · `exercises/` (stub `# TODO` + `_solution.py`) ·
`career-talk/` (the 30-min deck) · optionally `TRAINERS-GUIDE.md`.

**Standard 3.5-hour session timing** (per [`../COURSE-PLAN.md`](../COURSE-PLAN.md)):

| Block | Time | Use |
|-------|:----:|-----|
| Career talk | 30 min | The day's `career-talk/` deck |
| Concept + live coding | 75 min | Trainer-led walk through the modules (REPL-first) |
| Guided code-along | 45 min | Students type along; TA floats |
| Independent work | 45 min | The day's exercises |
| Standup + wrap | 15 min | Recap + preview next day |

## The dependency chain (why this order)
`variables/types (D1)` → `strings (D2)` → `booleans→conditionals (D3)` → `loops (D4)` →
`functions/scope (D5)` → `data structures (D6)` → `errors/modules/OOP (D7)` → **ready for the AI track (D8)**.
Each day only forward-references the next minimally (e.g. f-strings appeared D2 before functions; flag and move on).

---

## ✅ Day 1 — Setup, Data Types, Operators & Variables
*Built. 8 modules + 3 exercises + opening Software-Engineering presentation.*

| # | Module | Covers |
|--:|--------|--------|
| 00 | presentation-software-engineering-basics | Big-picture map (frontend/backend/API/DB/Git/cloud/AI) |
| 01 | running-python | REPL vs script files; first program |
| 02 | numbers | int, float, numeric notations |
| 03 | operators | arithmetic + `//`, `%`, `**` |
| 04 | comments | single/inline/block |
| 05 | variables | storing values, reassignment, dynamic typing |
| 06 | variable-naming | rules, conventions, keywords |
| 07 | assignment-operators | `+=`, `-=`, `*=`, … |
| 08 | print-function | `sep`, `end`, multiple values |

**Exercises:** Magic Trick · Seconds-in-a-day · Split the Bill.

---

## ✅ Day 2 — Strings, f-strings & String Methods
*Built. 8 modules + 3 exercises + trainer's guide.*

| # | Module | Covers |
|--:|--------|--------|
| 01 | strings | quotes, `+` concat, `*` repeat |
| 02 | string-indexing | indexing, negative, immutability, `None` |
| 03 | string-slices | `[start:stop:step]`, `[::-1]` |
| 04 | escape-and-triple-quotes | `\n \t \" \\`, multi-line (→ LLM prompts) |
| 05 | len-input-typecasting | `len()`, `input()`, `int()/float()/str()` |
| 06 | f-strings | embedded expr, `:.2f` / `:,` / `:.0%` |
| 07 | string-methods | upper/lower/title/strip/replace/find, `help()` |
| 08 | method-chaining | back-to-back calls, `split`/`join` taster |

**Exercises:** Age Calculator · Shopping Cart · Press Release.

---

## 📋 Day 3 — Booleans, Conditionals & Logic
**Folder:** `Day-03-Booleans-and-Conditionals` · **Objective:** make programs *decide*.

| # | Module | Covers | `python.txt` source |
|--:|--------|--------|---------------------|
| 01 | booleans | `True`/`False`, `bool` type | Introducing Booleans |
| 02 | comparison-operators | `< > <= >= == !=`, comparing across types | Comparison/Equality Operators |
| 03 | truthiness-and-in | truthy/falsey values, the `in` operator | Truthiness & Falseyness, "in" Operator |
| 04 | if-elif-else | conditionals + indentation rules | If/Elif/Else keywords, Indentation |
| 05 | nesting-conditionals | conditionals inside conditionals | Nesting Conditionals |
| 06 | logical-operators | `and` / `or` / `not` + precedence | Logical AND/OR/NOT, Precedence |
| 07 | random-numbers | `random.randint()` (for the games) | Generating Random Numbers |

**Exercises:** `tweet_checker` (length check, booleans) · `bmi_calculator` (if/elif/else) ·
`rock_paper_scissors` (logic + random) — RPS is the headline.
**Learning checks:** explain truthiness of `0`/`""`/`[]`; trace an `and`/`or` precedence expression.
**Gotchas to stage:** `=` vs `==`; indentation errors; `if x = 5` SyntaxError.

---

## ✅ Day 4 — Loops
**Folder:** `Day-04-Loops` · **Objective:** repeat work without repeating code. *Built. 6 modules + 3 exercises.*

| # | Module | Covers | `python.txt` source |
|--:|--------|--------|---------------------|
| 01 | while-loops | `while`, conditions, **avoiding infinite loops**, `while True`+`break` | While Loops, Avoiding Infinite Loops |
| 02 | for-loops | iterating strings/lists, `enumerate`, `for` vs `while` | For Loops, Loops & Indentation |
| 03 | range | `range(stop/start,stop/step)`, countdowns, pagination | The range() function |
| 04 | break-and-continue | early exit + skip, loop-`else`, retry/validation | Break and Continue |
| 05 | nested-loops | loops inside loops (grids, tables, pairs) | Working With Nested Loops |
| 06 | loop-patterns | accumulate / count / search-flag / build / **retry-backoff** | Loops In The Wild |

**Exercises:** `guessing_game` (while + input + random — ties D3 in) · `fizzbuzz`
(for + range + `%`, the classic screen) · `multiplication_table` (nested loops + f-string alignment).
**Gotchas staged:** off-by-one in `range`; the infinite `while True` without `break`; forgetting to
update the loop variable; one `break` only escaping the inner loop.

---

## ✅ Day 5 — Functions & Scope
**Folder:** `Day-05-Functions-and-Scope` · **Objective:** package logic into reusable, named blocks. *Built. 7 modules + 3 exercises.*

| # | Module | Covers | `python.txt` source |
|--:|--------|--------|---------------------|
| 01 | defining-functions | `def`, calling, docstrings, DRY | Introducing/First Function |
| 02 | parameters-and-arguments | one & multiple inputs, positional order | Functions With Input(s) |
| 03 | return-values | `return` vs `print`; early return; multiple returns | Introducing/Using Return |
| 04 | default-and-keyword-args | defaults, ordering, named args, **mutable-default trap** | Default Params, Keyword Arguments, Mutable Default Args |
| 05 | scope-legb | local/enclosing/global/built-in, closures | Global/Local/Enclosing Scope, Precedence |
| 06 | global-keyword | `global`, why it's a smell, `nonlocal` | The 'Global' Keyword |
| 07 | args-kwargs | `*args`, `**kwargs`, unpacking calls | *args, **kwargs |

**Exercises:** `temperature_converter` (params + return, composing) · `password_checker`
(default args, returns a verdict) · `receipt_builder` (`*args` + `**kwargs`).
**Learning checks:** difference between `return` and `print`; predict a LEGB scope puzzle.
**Gotchas staged:** function that prints but returns `None`; the mutable default arg `def f(x=[])`;
the `UnboundLocalError` from assigning to a global.

---

## ✅ Day 6 — Data Structures
**Folder:** `Day-06-Data-Structures` · **Objective:** store and organise collections of data.
*(Densest pre-OOP day.) Built. 7 modules + 3 exercises.*

| # | Module | Covers | `python.txt` source |
|--:|--------|--------|---------------------|
| 01 | lists | create, index, slice, `append`/`insert`/`extend`/`pop`/`remove` | Creating/Accessing/Updating Lists, List Methods |
| 02 | list-patterns-and-nested | iterate, `sort`/`sorted`, comprehensions, nested lists, **copy vs reference** | List Slices, Iterating, Nested Lists, Copying |
| 03 | dictionaries | create, `get`/`in`, add/update, `pop`/`del` | Dictionaries (intro/access/update) |
| 04 | dict-iteration-and-merging | `keys`/`values`/`items`, merging, **list-of-dicts** | Iterating Dicts, Merging, Lists+Dicts |
| 05 | tuples | immutability, unpacking, why/when to use | Tuples |
| 06 | sets | uniqueness, union/intersection/difference, when to use | Sets |
| 07 | choosing-the-right-structure | the decision flow + real scenarios + nesting (JSON) | (synthesis) |

**Exercises:** `todo_list` (list CRUD via menu) · `word_frequency` (dict count pattern) ·
`common_skills` (set algebra `&` / `|` / `-` / `^`).
**Gotchas staged:** list aliasing (`b = a` shares the same list) vs `a.copy()`; `KeyError` vs `.get()`;
`{}` is a dict not a set; mutating a method's return value of `None`.

---

## ✅ Day 7 — Errors, Modules & OOP
**Folder:** `Day-07-Errors-Modules-and-OOP` · **Objective:** handle failure, reuse code, model with classes.
*(The most packed day — three sub-topics.) Built. 7 modules + 3 exercises.*

| # | Module | Covers | `python.txt` source |
|--:|--------|--------|---------------------|
| 01 | error-types | common exceptions; reading tracebacks bottom-up | Common Error Types |
| 02 | try-except | `try`/`except`/`else`/`finally`, `raise`, custom exceptions, LBYL vs EAFP | Try/Except, Raising, LBYL/EAFP |
| 03 | modules-and-imports | built-in modules (`math`/`random`/`datetime`/`json`), import styles, `__name__` | Built-In Modules, Import Syntax, Custom Modules |
| 04 | pip-and-third-party | PyPI, `pip`, `requirements.txt`, venv, **safe `ImportError` fallback** | Pip & PyPI, First Pip Package |
| 05 | classes-and-objects | `class`, instances, `__init__`, `self`, attributes | Class Syntax, Instance Methods |
| 06 | instance-methods | methods, class vs instance attributes, `__str__` | Class Attributes/Methods |
| 07 | inheritance-and-super | inheritance ("is-a"), overriding, `super()` | Inheritance Basics, super() |

**Exercises:** `safe_calculator` (try/except + custom exception) · `bank_account` (a class with guarded
methods + statement log) · `shapes` (base `Shape` + `Rectangle`/`Circle`/`Square` via `super()`).
**Note:** the pip module runs offline — it demonstrates a graceful `try/except ImportError` so it works
even when the package isn't installed.
**Gotchas staged:** bare `except:` swallowing everything; `self` forgotten in methods; forgetting
`super().__init__()`; `ValueError` vs `TypeError`.

---

## What students can do after Day 7 (entry check for Day 8)
- [ ] Read input, branch with `if/elif/else`, and loop with `for`/`while`.
- [ ] Write functions with parameters, defaults, and return values.
- [ ] Use lists & dicts fluently (the shape of all JSON / API data).
- [ ] `try/except` around risky code; `pip install` a package and import it.
- [ ] Read and write a basic class (needed for Pydantic models on Day 8/11).

## Production checklist (when building each planned day)
1. Read the day's row above + the matching `python.txt` lessons.
2. Create modules in order; one concept each; runnable `.py` + teaching `README.md`.
3. Add `exercises/` (stub `# TODO` + `_solution.py`).
4. **Run every script** with the real CPython (`…\Python312\python.exe`) before marking done.
   ⚠️ Avoid printing `₹` (Windows console can't encode it — use `Rs`; see Day 2 Module 06).
5. Update this file's status table + the phase/root READMEs + CLAUDE.md status.
6. Career deck already exists in each `career-talk/`; add a `TRAINERS-GUIDE.md` if desired.
