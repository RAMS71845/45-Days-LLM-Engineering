# 02 — Parameters & Arguments

A function gets useful when you can **feed it data**. The names in the `def` are **parameters**; the
values you pass when calling are **arguments**.

```python
def greet(name):              # `name` is a PARAMETER (a placeholder)
    print(f"Hello, {name}!")

greet("Asha")                 # "Asha" is an ARGUMENT (the real value)
greet("Ben")                  # same function, different argument
```

| Term | Where | Is | Example |
|------|-------|----|---------|
| **Parameter** | in the `def` | the placeholder name | `name` |
| **Argument** | at the call | the actual value | `"Asha"` |

(People use them interchangeably in conversation — but knowing the difference makes docs and error
messages click.)

## Multiple parameters — order matters (positional)
```python
def book_ticket(name, seat, price):
    print(f"{name} -> seat {seat} (Rs {price})")

book_ticket("Asha", "12A", 850)     # matched left-to-right by POSITION
```
The first argument fills the first parameter, and so on. Pass them in the wrong order and you'll book
seat `850` for `Rs 12A`. Keyword arguments (Module 04) fix this.

## 🎤 Talking points (what to say & focus on)
- **Parameter = empty box on the recipe; argument = the actual ingredient you pour in.** The box
  exists only while the function runs.
- **One function, many inputs = the real power.** Take Module 01's `confirm_order()` and give it an
  `order_id` parameter — now one definition handles every order. That's the upgrade.
- **Positional = matched by order.** Demonstrate the "swapped arguments" bug live (name/price
  reversed). It's silent and nasty — sets up *why* keyword args exist in Module 04.
- **Name parameters like variables** — `total_price`, not `tp`. The signature is documentation the
  caller reads first.
- **Arguments can be expressions**, not just literals: `greet(first.title())`, `area(r * 2)`. Python
  evaluates them, then passes the result.

## ⚠️ Common mistakes to call out
- Calling with the wrong **number** of arguments → `TypeError: missing 1 required positional argument`.
- Passing arguments in the **wrong order** (silent logic bug, no error).
- Confusing the parameter name (inside) with the variable name (outside) — they need not match.

Run the examples:

```bash
python parameters_and_arguments.py
```

➡ Next: **[03-return-values](../03-return-values/)**
