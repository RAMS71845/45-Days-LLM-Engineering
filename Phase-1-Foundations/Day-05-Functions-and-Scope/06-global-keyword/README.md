# 06 — The `global` Keyword

By default, **assigning** to a name inside a function creates a *local*. The `global` keyword tells
Python "no — use the module-level variable" so your assignment sticks outside the function.

```python
score = 0

def add_point():
    global score          # "score refers to the GLOBAL one"
    score += 1            # now this actually updates the outer score

add_point()
add_point()
print(score)              # 2
```

Without `global`, that `score += 1` raises `UnboundLocalError` (Module 05's trap).

## ⚠️ Use it sparingly — it's usually a smell
Globals that functions quietly mutate make code hard to follow and test: any function might change
`score` from anywhere, so a bug could live anywhere. The cleaner pattern is **take it in, return it
out**:
```python
def add_point(score):
    return score + 1

score = add_point(score)      # the data flow is explicit and testable
```
Reach for `global` only for genuinely app-wide state (a config flag, a cache, a counter in a small
script) — and even then, prefer passing values or (Day 7) wrapping state in a class.

## `nonlocal` (one-line cousin)
`global` jumps to the module level; `nonlocal` rebinds a variable in the *enclosing function* (for
closures). Same idea, one level in. You'll rarely need it on Day 5 — just know it exists.

## 🎤 Talking points (what to say & focus on)
- **`global` = "edit the outer variable, not a new local."** It fixes the UnboundLocalError from
  Module 05 — show that fix to make the link concrete.
- **Then immediately argue against overusing it.** Functions that mutate globals are "spooky action
  at a distance" — show the same counter done by passing/returning, and ask which they'd rather debug
  at 2am. The lesson is judgment, not the keyword.
- **Legit uses exist:** a single config flag, a memoization cache, a quick script counter. Don't
  forbid it — frame it as "rare and deliberate."
- **Forward-hook to OOP (Day 7):** "when you have a bundle of state several functions share, that's a
  *class* waiting to happen." Plants the seed without teaching it yet.
- **`nonlocal` in one breath** — same idea for the enclosing scope; note it and move on.

## ⚠️ Common mistakes to call out
- Sprinkling `global` everywhere to "make errors go away" instead of passing arguments.
- Declaring `global x` *after* you've already used `x` in the function → `SyntaxError`.
- Confusing `global` (module level) with `nonlocal` (enclosing function).
- Reaching for `global` when a plain return would be clearer.

Run the examples:

```bash
python global_keyword.py
```

➡ Next: **[07-args-kwargs](../07-args-kwargs/)**
