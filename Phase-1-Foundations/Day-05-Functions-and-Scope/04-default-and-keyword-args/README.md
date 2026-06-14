# 04 — Default & Keyword Arguments

Two features that make function calls clearer and more flexible.

## Default values — make a parameter optional
Give a parameter a fallback in the `def`. Callers can omit it.
```python
def greet(name, greeting="Hi"):       # greeting defaults to "Hi"
    print(f"{greeting}, {name}!")

greet("Asha")                         # Hi, Asha!
greet("Ben", "Good morning")          # Good morning, Ben!
```
**Rule: defaulted parameters must come *after* required ones.** `def f(a=1, b)` is a `SyntaxError`.

## Keyword arguments — name the value at the call
Pass `param=value` so order stops mattering and the call self-documents:
```python
book_ticket(name="Asha", price=850, seat="12A")   # any order, crystal clear
```
This kills the "swapped arguments" bug from Module 02. Mixing is allowed, but **positional args must
come before keyword args**: `book_ticket("Asha", seat="12A", price=850)`.

## ⚠️ The mutable default trap (famous Python gotcha)
```python
def add_item(item, cart=[]):          # ❌ the list is created ONCE, shared by all calls
    cart.append(item)
    return cart

add_item("apple")                     # ['apple']
add_item("milk")                      # ['apple', 'milk']  <- leaked from last call!
```
The default `[]` is created **once**, at definition time, and reused — so it accumulates across calls.
**Fix:** default to `None` and build a fresh one inside:
```python
def add_item(item, cart=None):
    if cart is None:
        cart = []                     # fresh list every call
    cart.append(item)
    return cart
```

## 🎤 Talking points (what to say & focus on)
- **Defaults = sensible fallbacks.** `timeout=30`, `currency="INR"`, `retries=3`. Callers override
  only when they need to. Show how it shrinks call sites.
- **Keyword args = readable + safe.** Re-run Module 02's swapped-arguments bug, then fix it with
  `seat=..., price=...`. The names make the swap impossible and the call self-documenting.
- **Two ordering rules** — required-before-default in the `def`; positional-before-keyword in the
  call. Show the `SyntaxError`/`TypeError` for each once so they recognise it.
- **The mutable-default trap is a rite of passage.** Run the leaking-cart demo live — the second call
  showing `['apple','milk']` lands hard. Then show the `None` fix. They will hit this in real code.
- **AI tie-in:** every LLM SDK call is keyword args with defaults (`temperature=0.7`, `max_tokens=...`).
  You'll read and write these constantly in Phase 1 — this module is direct prep.

## ⚠️ Common mistakes to call out
- Default parameter before a required one → `SyntaxError`.
- Keyword argument before a positional one in a call → `SyntaxError`.
- Using a mutable default (`=[]`, `={}`) and being surprised by shared state.
- Typo in a keyword name → `TypeError: unexpected keyword argument`.

Run the examples:

```bash
python default_and_keyword_args.py
```

➡ Next: **[05-scope-legb](../05-scope-legb/)**
