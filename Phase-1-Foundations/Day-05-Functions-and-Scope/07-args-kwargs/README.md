# 07 — `*args` and `**kwargs`

Sometimes you don't know *how many* arguments a function will get. These two let a function accept
**any number** of them.

| Syntax | Collects | Into a | Example call |
|--------|----------|--------|--------------|
| `*args` | extra **positional** args | **tuple** | `total(10, 20, 30)` |
| `**kwargs` | extra **keyword** args | **dict** | `make_user(name="Asha", age=21)` |

```python
def total(*args):                 # args is a tuple of everything passed
    return sum(args)

total(10, 20, 30)                 # args == (10, 20, 30) -> 60
total(5)                          # args == (5,) -> 5

def make_user(**kwargs):          # kwargs is a dict of name=value pairs
    return kwargs

make_user(name="Asha", age=21)    # {'name': 'Asha', 'age': 21}
```
The names `args`/`kwargs` are **convention**, not required — but everyone uses them; the `*`/`**` is
what matters.

## Parameter ordering (the full picture)
When you combine everything, the order in the `def` is fixed:
```
def f(positional, *args, keyword_only, **kwargs):
```
i.e. **normal params → `*args` → keyword params → `**kwargs`**.

## Unpacking — the mirror image at the *call* site
`*` and `**` also *spread* a collection into arguments:
```python
nums = [10, 20, 30]
total(*nums)                      # same as total(10, 20, 30)

info = {"name": "Asha", "age": 21}
make_user(**info)                 # same as make_user(name="Asha", age=21)
```
You'll see this constantly: `function(*list)` and `function(**dict)`.

## 🎤 Talking points (what to say & focus on)
- **`*` = "pack the rest into a tuple," `**` = "pack the rest into a dict."** One sentence each. Show
  `args`/`kwargs` printed so they SEE the tuple and the dict.
- **Motivate with a real variadic API:** `print(*values)` already does this; so does a `sum_all(*n)`
  or a logger `log(msg, **context)`. They've been *using* `*args` (in `print`) all week.
- **Unpacking is the same star, mirrored.** In a `def`, `*` collects; at a call, `*` spreads. The
  `total(*nums)` / `make_user(**info)` demo makes it click — and it's how you forward arguments.
- **`**kwargs` + a real config dict is the AI tie-in:** `client.generate(**settings)` where `settings`
  is a dict of model options. They'll do exactly this in Phase 1.
- **Don't overload it.** If you always pass the same 3 things, name them as real parameters. `*args`
  is for genuine variability, not laziness.

## ⚠️ Common mistakes to call out
- Wrong order in the `def` (e.g. `*args` before a normal positional param).
- Forgetting `args` is a **tuple** and `kwargs` is a **dict** (then calling list/dict methods wrongly).
- Mixing up collecting (`def f(*args)`) with spreading (`f(*mylist)`) — same symbol, opposite sides.
- Passing a positional after `**kwargs` at the call site.

Run the examples:

```bash
python args_kwargs.py
```

➡ Next: **[exercises/](../exercises/)** — Temperature Converter, Password Checker & Receipt Builder
