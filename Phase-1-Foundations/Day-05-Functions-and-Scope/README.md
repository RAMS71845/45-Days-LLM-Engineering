# Day 05 — Functions & Scope

So far your programs run top-to-bottom, once. **Functions** let you *name* a chunk of logic, reuse it
anywhere, and stop copy-pasting. They're the unit every real codebase is built from — a Django view,
a data-cleaning step, an API client method, and (Phase 1) every tool you'll hand to an AI agent is a
function. Today you learn to write them well: clear inputs, a single clear output, sensible defaults,
and an understanding of **where variables live** (scope).

We go from "define and call" up to `*args`/`**kwargs` and the **LEGB** scope rule that explains every
"why can't I see that variable?" bug you'll ever hit.

> 🐙 **GitHub mini-track (Part 2 of 3).** Today's deck — *The Everyday Workflow: `status → add →
> commit → push`* (with `.gitignore` for your future API keys) — lives in
> [`github-basics/`](github-basics/). Open `github-basics/index.html`. Part 1 was Day 4; Part 3 is Day 6.

## Learning objectives
By the end of today you can:
- **Define** and **call** functions with `def`, and write a one-line **docstring**
- Pass **parameters** and read **arguments**; tell a *parameter* (the name) from an *argument* (the value)
- Use **`return`** to send a value back — and explain why `return` ≠ `print`
- Return **multiple values** at once (Python packs them into a tuple)
- Give parameters **default values** and call with **keyword arguments** — and dodge the **mutable
  default** gotcha
- Explain **scope** with **LEGB** (Local → Enclosing → Global → Built-in) and use **`global`** sparingly
- Accept any number of arguments with **`*args`** / **`**kwargs`** and **unpack** with `*` / `**`

## Modules (work through them in order)

| # | Module | What it covers |
|--:|--------|----------------|
| 01 | [defining-functions](01-defining-functions/) | `def`, calling, docstrings, why functions (DRY) |
| 02 | [parameters-and-arguments](02-parameters-and-arguments/) | positional args, multiple params, parameter vs argument |
| 03 | [return-values](03-return-values/) | `return` vs `print`, returning multiple values, early return |
| 04 | [default-and-keyword-args](04-default-and-keyword-args/) | default values, keyword args, ordering, the mutable-default trap |
| 05 | [scope-legb](05-scope-legb/) | local/enclosing/global/built-in, why locals vanish, closures |
| 06 | [global-keyword](06-global-keyword/) | `global`, why it's usually a smell, return-instead pattern |
| 07 | [args-kwargs](07-args-kwargs/) | `*args`, `**kwargs`, parameter ordering, unpacking calls |

Then test yourself in **[exercises/](exercises/)**.

## The 5 things to really nail today
1. **`return` sends a value back; `print` just shows it.** A function that only `print`s gives you
   `None` to work with. This is the #1 confusion of the day.
2. **Define once, call many.** If you've copy-pasted code with one value changed, that's a function
   begging to exist (DRY — Don't Repeat Yourself).
3. **Defaults go last.** `def greet(name, greeting="Hi")` — required params before defaulted ones.
4. **Never use a mutable default** (`def f(items=[])`). It's shared across calls and silently grows.
   Use `None` and create it inside.
5. **LEGB:** a name is looked up Local → Enclosing → Global → Built-in. Assigning inside a function
   makes it local unless you say `global`.

## How to run
From this folder, run any file directly:

```bash
python 01-defining-functions/defining_functions.py
```

The exercises use `input()` and will pause for you. Or import a function in the REPL:

```bash
python
>>> from importlib import import_module
>>> 1 + 1
2
```

## Today's exercises
Three of them — see [`exercises/`](exercises/):
1. **Temperature Converter** — functions with parameters + `return` (and round-tripping the result)
2. **Password Strength Checker** — a function that returns a verdict, using default arguments
3. **Receipt Builder** — `*args` for line items + `**kwargs` for options (a real variadic API)

## 🧠 Logic Building Challenge (Days 1–5 recap)
A separate set of **5 think-first problems** plus a deck on *how to build logic when you code* —
the 5-step method (Understand → Example by hand → Plan → Code → Test). See
[`logic-building/`](logic-building/): open `index.html` for the deck, `README.md` for the problems,
and `SOLUTIONS.md` for the detailed worked walk-throughs.

➡ Next: **[Day 06 — Data Structures](../Day-06-Data-Structures/)**
