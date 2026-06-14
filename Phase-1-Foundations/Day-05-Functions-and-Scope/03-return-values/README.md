# 03 — Return Values

`return` sends a value **back to the caller** so you can store it, reuse it, or feed it into the next
step. This is the single most important idea about functions.

```python
def add(a, b):
    return a + b              # hand the result back

total = add(2, 3)            # total is now 5 — we can USE it
print(total * 10)            # 50
```

## ⚠️ `return` is NOT `print`
This is the #1 confusion of the whole day:

| | `print(x)` | `return x` |
|--|-----------|-----------|
| What it does | shows `x` on screen | hands `x` back to the caller |
| Can you reuse the value? | **No** — it's gone | **Yes** — store it in a variable |
| Function's result | `None` | `x` |

```python
def add_print(a, b):
    print(a + b)             # shows 5, but...
x = add_print(2, 3)          # x is None! nothing was returned
```
A function with no `return` returns `None` automatically.

## Return ends the function immediately
The moment `return` runs, the function stops — lines after it don't execute. This enables **early
return** ("guard clauses"): handle the bad/edge case and bail, keeping the main logic un-nested.

## Returning multiple values
`return a, b, c` packs them into a **tuple**; the caller can **unpack** them:
```python
def min_max(nums):
    return min(nums), max(nums)

low, high = min_max([4, 9, 1])   # low=1, high=9
```

## 🎤 Talking points (what to say & focus on)
- **Drill return vs print until it's reflexive.** Write `add_print` and `add_return`, then try to do
  `total = fn(2,3) * 10` with each. Only the `return` version works; the `print` one explodes on
  `None * 10`. That failure *is* the lesson.
- **"A function's job is to give you something back."** `print` is a side effect for humans; `return`
  is for the rest of the program. Pure data functions should `return`.
- **Early return flattens code.** Show a validate-then-compute function: `if invalid: return error`
  up top, happy path below, no nesting. Reviewers love this.
- **Multiple return values are just a tuple.** `return lo, hi` then `lo, hi = ...`. Tie back to Day-4
  patterns and forward to Day-6 tuples.
- **No return = None.** Show it explicitly (`print(fn())` -> `None`). Explains a *lot* of "why is my
  variable None?" bugs.

## ⚠️ Common mistakes to call out
- Using `print` where you meant `return` (then trying to reuse the "result").
- Putting code after `return` and wondering why it never runs.
- Forgetting to *capture* the return value (`add(2,3)` on its own line throws the result away).
- `return` outside a function → `SyntaxError`.

Run the examples:

```bash
python return_values.py
```

➡ Next: **[04-default-and-keyword-args](../04-default-and-keyword-args/)**
