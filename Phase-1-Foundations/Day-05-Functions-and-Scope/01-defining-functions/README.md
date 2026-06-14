# 01 — Defining Functions

A **function** is a named, reusable block of code. You **define** it once with `def`, then **call** it
as many times as you like.

```python
def greet():                 # define: `def` name() then a colon
    """Say hello."""         # docstring: one line describing what it does
    print("Hello!")          # the body (indented, like a loop/if)

greet()                      # call: the () actually runs it
greet()                      # call again — reuse, no copy-paste
```

## Why functions exist: DRY
**D**on't **R**epeat **Y**ourself. The moment you copy-paste code and tweak one value, you want a
function with that value as a *parameter* (Module 02). Benefits:
- **Reuse** — write once, call anywhere.
- **Naming** — `calculate_gst(amount)` documents intent better than five raw lines.
- **Isolation** — a bug lives in one place; fix it once.
- **Testing** — small named pieces are easy to test (and to hand to an AI agent as a "tool").

## Define vs call — the timing
Defining a function **does not run it**. Python just remembers it. Only the `()` call runs the body.
So you must define a function *before* the line that calls it.

## Docstrings
The `"""triple-quoted"""` string right under `def` is the **docstring** — it shows up in `help(fn)`
and in your editor's tooltips. One clear sentence is enough on Day 5.

## 🎤 Talking points (what to say & focus on)
- **"A function is a recipe; calling is cooking it."** Defining writes the recipe down; the `()` cooks
  it. You can write a recipe and never cook it — defining alone prints nothing.
- **Sell DRY with a real before/after.** Show three near-identical blocks, then collapse them into one
  function. The "ohhh" is the lesson.
- **The `()` is not optional.** `greet` (no parens) is the function *object*; `greet()` *runs* it.
  Show what bare `greet` prints (`<function ...>`) — a very common beginner confusion.
- **Define before call.** Reordering to call-then-define raises `NameError`. Demonstrate it once.
- **Docstrings are free documentation** — `help(greet)` reads them back. Build the habit now; in the
  AI track, an agent literally reads your tool's docstring to decide when to call it.

## ⚠️ Common mistakes to call out
- Forgetting the `()` when calling — nothing happens, no error.
- Forgetting the colon `:` or not indenting the body.
- Calling a function on a line *above* its `def`.
- Expecting `def` alone to produce output.

Run the examples:

```bash
python defining_functions.py
```

➡ Next: **[02-parameters-and-arguments](../02-parameters-and-arguments/)**
