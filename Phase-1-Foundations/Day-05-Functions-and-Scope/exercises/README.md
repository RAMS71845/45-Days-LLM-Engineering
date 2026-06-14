# Day 05 — Exercises

Put today's tools to work: `def`, parameters, `return`, default/keyword args, scope, and
`*args`/`**kwargs`. Try each in the stub file first, then check the matching `*_solution.py`.

---

## Exercise 1 — Temperature Converter 🌡️
Write two small functions and use their **return values** together.

**Your task:** in `temperature_converter.py`
1. `def c_to_f(c):` → `return c * 9 / 5 + 32`.
2. `def f_to_c(f):` → `return (f - 32) * 5 / 9`.
3. `input()` a Celsius value, `float()`-cast it, call `c_to_f`, and print the result to 1 decimal.
4. **Round-trip check:** feed the result back into `f_to_c` and confirm you get the original.

*Skills:* `def`, one parameter, `return`, composing functions, f-string formatting.
*Focus:* using a returned value (not printing inside the function) — `return`, not `print`.

➡ Solution: [`temperature_converter_solution.py`](temperature_converter_solution.py)

---

## Exercise 2 — Password Strength Checker 🔐
Write a function that **returns** a strength verdict, with a tunable minimum length via a default arg.

**Your task:** in `password_checker.py`
1. `def check_password(pw, min_length=8):` — return a string verdict, don't print inside.
2. Score points for: length ≥ `min_length`, has a digit, has an uppercase, has a symbol.
   (Hint: `any(ch.isdigit() for ch in pw)`, `ch.isupper()`, and a set of symbols.)
3. Map score → `"weak"` / `"medium"` / `"strong"` and `return` it.
4. `input()` a password and print the verdict. Try calling with `min_length=12` too.

*Skills:* `def`, `return`, default arguments, booleans, `any()`, string methods.
*Focus:* the function returns data; the caller decides what to do with it.

➡ Solution: [`password_checker_solution.py`](password_checker_solution.py)

---

## Exercise 3 — Receipt Builder 🧾
A real variadic API: any number of **line items** (`*args`) plus optional **settings** (`**kwargs`).

**Your task:** in `receipt_builder.py`
1. `def build_receipt(*items, gst_percent=18, currency="Rs", **extra):`
   - `*items` = any number of `(name, price)` tuples.
   - `gst_percent`, `currency` = defaults the caller can override.
   - `**extra` = anything else (e.g. `customer="Asha"`), printed as a footer.
2. Loop the items, print each line, accumulate the subtotal.
3. Add GST, print the grand total, then print any `**extra` footer fields.

*Skills:* `*args`, `**kwargs`, default args, the accumulate pattern (Day 4), tuple unpacking.
*Focus:* how `*args`/`**kwargs` make one function handle calls of any shape.

➡ Solution: [`receipt_builder_solution.py`](receipt_builder_solution.py)

---

### Stretch goals (if you finish early)
- **Converter:** add Kelvin (`c_to_k`, `k_to_c`) and a tiny menu (`while True` from Day 4) to pick a direction.
- **Password:** return a `(verdict, score, tips)` tuple and print actionable tips for missing criteria.
- **Receipt:** accept a `discount_percent=0` default and apply it before GST; right-align the prices.
