# 05 — Scope (LEGB)

**Scope** is *where a variable is visible*. When Python sees a name, it searches four places, in this
exact order — remember it as **LEGB**:

| Letter | Scope | Where |
|--------|-------|-------|
| **L** | Local | inside the current function |
| **E** | Enclosing | a function that wraps this one (closures) |
| **G** | Global | the top level of the file/module |
| **B** | Built-in | Python's own names (`len`, `print`, `range`, …) |

First match wins. `len` resolves at the **B** level; a variable you set at the top of the file is
**G**; a variable assigned inside a function is **L**.

## Locals are born and die with the call
```python
def f():
    x = 10        # local — exists only while f() runs
    print(x)
f()
print(x)          # ❌ NameError: x is not defined out here
```
Each call gets its own fresh locals. They vanish when the function returns. That's a *feature* — it's
why two functions can both use `i` without colliding.

## Reading vs assigning a global
- **Reading** a global from inside a function: fine (no special keyword).
- **Assigning** a name inside a function makes it **local** — even if a global of the same name
  exists. To rebind the global you need `global` (Module 06). This surprises everyone:
```python
count = 0
def bump():
    count = count + 1     # ❌ UnboundLocalError: `count` is treated as local here
```

## Enclosing scope (a peek at closures)
A function defined inside another can *see* the outer function's locals (the **E** in LEGB):
```python
def make_multiplier(factor):
    def multiply(n):
        return n * factor     # `factor` comes from the ENCLOSING scope
    return multiply

triple = make_multiplier(3)
triple(10)                    # 30
```

## 🎤 Talking points (what to say & focus on)
- **Say "LEGB" out loud and write it big.** Local → Enclosing → Global → Built-in, first match wins.
  This one rule explains *every* scope question they'll ask.
- **Locals are private + temporary.** Demo the `NameError` when you print a local outside its
  function. Then frame it as a gift: isolation is *why* functions don't step on each other.
- **The UnboundLocalError is the money demo.** `count = count + 1` on a global looks innocent and
  blows up. Explain: assignment anywhere in the function marks the name local for the *whole*
  function. This is the bridge to Module 06's `global`.
- **You can shadow built-ins (don't!).** `list = [1,2,3]` then `list(...)` breaks. Name a variable
  `len`/`list`/`sum` and you've hidden the built-in. Common, frustrating, worth a warning.
- **Closures are a gentle "wow" to end on** — `make_multiplier` returns a function that remembers
  `factor`. Don't go deep; just plant that "E" is real and useful.

## ⚠️ Common mistakes to call out
- Expecting a local variable to exist after the function returns.
- `UnboundLocalError` from assigning to a name you also read as a global.
- Shadowing built-ins (`list`, `dict`, `sum`, `id`, `type`) with your own variables.
- Assuming an inner-function change to an enclosing variable "writes back" (it doesn't without `nonlocal`).

Run the examples:

```bash
python scope_legb.py
```

➡ Next: **[06-global-keyword](../06-global-keyword/)**
