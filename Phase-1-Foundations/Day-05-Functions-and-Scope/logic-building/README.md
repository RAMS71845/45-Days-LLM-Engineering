# Day 05 — Logic Building Challenge (Days 1–5 recap)

Five problems that make you **think**, not just recall syntax. Everything you need was covered in
**Days 1–5**: variables & operators, strings & f-strings, booleans & conditionals, loops
(`while`/`for`/`range`/`break`/`continue`/nested), and functions (`def`/`return`/scope).

> 🧠 **Watch the deck first:** open [`index.html`](index.html) — *The Logic Building Approach for
> Programming*. It teaches the **5-step method** (Understand → Example by hand → Plan → Code → Test)
> that every solution below uses. Then come back and try the problems.

## How to use this

1. **Read a problem** and try it *before* looking at anything else. Struggle is the point.
2. Stuck? Read the **Approach hint** — it nudges, it doesn't solve.
3. Write your answer in the **stub file** (`qN_*.py`, has `# TODO`s).
4. Compare with the worked **solution** (`qN_*_solution.py`) and the deep write-up in
   [`SOLUTIONS.md`](SOLUTIONS.md).

Every solution is runnable on its own:

```bash
python q1_fizzbuzz_solution.py
```

---

## The 5-step method (use it on every problem)

| Step | Ask yourself | Output |
|--:|---|---|
| 1. **Understand** | What are the **inputs**? The **output**? Any rules/edge cases? | A one-line restatement |
| 2. **Example by hand** | Solve one case on paper. *How* did your brain do it? | A traced example |
| 3. **Plan** | Write the steps in plain English (pseudocode). Pick a **pattern**. | Pseudocode |
| 4. **Code** | Translate each pseudocode line to Python. | A function |
| 5. **Test** | Try normal, boundary, and weird inputs. | Confidence |

**The pattern toolbox** (you've already met all of these): *accumulator* (running total/string),
*counter*, *boolean flag*, *search-with-`break`*, *nested loops*, and *break a problem into functions*.

---

## Problem 1 — FizzBuzz (the classic warm-up) 🥁

Print the numbers from **1 to N**. But:
- multiples of **3** → print `Fizz` instead
- multiples of **5** → print `Buzz` instead
- multiples of **both 3 and 5** → print `FizzBuzz`

**Skills:** `for`/`range`, the modulo operator `%`, `if/elif/else`, a function with a parameter.

> **Approach hint:** Test the **most specific** condition first. "Divisible by both" is more specific
> than "divisible by 3", so check `n % 3 == 0 and n % 5 == 0` *before* the single checks — or build
> the word up with two separate `if`s.

➡ Stub: [`q1_fizzbuzz.py`](q1_fizzbuzz.py) · Solution: [`q1_fizzbuzz_solution.py`](q1_fizzbuzz_solution.py)

---

## Problem 2 — Reverse a number & check palindrome (no strings!) 🔁

Given a positive integer like `12321`, **reverse its digits** using only **maths** (no converting to a
string and slicing). Then say whether the number is a **palindrome** (reads the same both ways).

**Skills:** `while` loop, integer division `//`, modulo `%`, the accumulator pattern, returning a
value, a boolean check.

> **Approach hint:** The last digit of `n` is `n % 10`. Remove it with `n // 10`. Build the reversed
> number with `reversed = reversed * 10 + last_digit`. Trace `123` by hand: 3 → 32 → 321.

➡ Stub: [`q2_reverse_number.py`](q2_reverse_number.py) · Solution: [`q2_reverse_number_solution.py`](q2_reverse_number_solution.py)

---

## Problem 3 — Prime numbers up to N 🔢

Write `is_prime(n)` that returns `True`/`False`, then **list every prime from 2 to N**. A prime has
exactly two divisors: 1 and itself.

**Skills:** function returning a **boolean**, nested loops, `break` (stop early once you find a
divisor), the accumulator pattern to collect results.

> **Approach hint:** `n` is prime if **no** number from 2 up to `n-1` divides it. The moment you find
> one divisor, you can `break` — it's settled. Numbers below 2 are not prime (edge case!). Bonus: you
> only need to test up to `n ** 0.5`.

➡ Stub: [`q3_primes.py`](q3_primes.py) · Solution: [`q3_primes_solution.py`](q3_primes_solution.py)

---

## Problem 4 — Word & character statistics 📊

Given a sentence, return its stats in **one** function call: number of **words**, number of
**vowels**, and the **longest word**. (Return all three at once — Python packs them into a tuple.)

**Skills:** string methods (`.split()`, `.lower()`), looping over characters, the counter pattern,
tracking a "best so far", and **returning multiple values**.

> **Approach hint:** `.split()` gives you the words list. Count vowels by looping each character and
> checking `ch in "aeiou"`. For the longest word, keep a `longest = ""` and update it whenever you see
> a longer one — the "best so far" pattern.

➡ Stub: [`q4_word_stats.py`](q4_word_stats.py) · Solution: [`q4_word_stats_solution.py`](q4_word_stats_solution.py)

---

## Problem 5 — Number pyramid pattern 🔺

Print a pyramid of `N` rows. For `N = 4`:

```
   1
  2 2
 3 3 3
4 4 4 4
```

Row `r` is centred, and prints the digit `r`, exactly `r` times.

**Skills:** **nested loops** (one for rows, one for spaces, one for the numbers), building a string,
turning a visual shape into loop bounds.

> **Approach hint:** For row `r` (from 1 to N): print `N - r` leading spaces, then `r` copies of the
> digit. You can do the inner part with loops *or* with string multiplication (`" " * (N - r)`).
> Figure out the bounds by writing the spaces and digits counts for each row in a small table first.

➡ Stub: [`q5_pyramid.py`](q5_pyramid.py) · Solution: [`q5_pyramid_solution.py`](q5_pyramid_solution.py)

---

### Stretch goals (if you finish early)
- **FizzBuzz:** make the words/divisors configurable via a dict (forward ref to Day 6).
- **Reverse:** handle trailing zeros and negative numbers; print whether the *sum of digits* is even.
- **Primes:** optimise to loop only to `int(n ** 0.5) + 1` and time it on N = 100000.
- **Word stats:** also return the count of each vowel; ignore punctuation.
- **Pyramid:** print it upside-down, then mirror it into a full diamond.

➡ Full worked walk-throughs: **[`SOLUTIONS.md`](SOLUTIONS.md)**
</content>
</invoke>
