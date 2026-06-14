# Day 05 — Logic Building: Detailed Solutions

Each problem is worked through the **5-step method** from the deck:
**Understand → Example by hand → Plan (pseudocode) → Code → Test.**
Read these *after* you've tried the problem yourself.

---

## Problem 1 — FizzBuzz

### 1. Understand
- **Input:** an integer `N`.
- **Output:** the numbers `1..N` printed, but some replaced by words.
- **Rules:** mult. of 3 → `Fizz`, mult. of 5 → `Buzz`, mult. of **both** → `FizzBuzz`.
- **Key tool:** "divisible by k" means `n % k == 0`.

### 2. Example by hand (N = 15)
`1, 2, Fizz, 4, Buzz, Fizz, 7, 8, Fizz, Buzz, 11, Fizz, 13, 14, FizzBuzz`.
Notice `15` is divisible by *both* 3 and 5 — it must print `FizzBuzz`, not just `Fizz`.

### 3. Plan
```
for i from 1 to N:
    if i divisible by 3 AND by 5 -> print "FizzBuzz"   # most specific FIRST
    else if divisible by 3       -> print "Fizz"
    else if divisible by 5       -> print "Buzz"
    else                         -> print i
```

### 4. Code
See [`q1_fizzbuzz_solution.py`](q1_fizzbuzz_solution.py). The crucial idea is **ordering**: test the
combined condition before the single ones, or you'll never reach `FizzBuzz`.

### 5. Test
| i | Expected |
|--:|---|
| 3 | Fizz |
| 5 | Buzz |
| 15 | FizzBuzz |
| 7 | 7 |

**Two valid designs:** the `if/elif` chain, *or* "build the word" (`""` → add `Fizz`/`Buzz` → fall
back to the number with `word or str(i)`). The second needs **no** special both-case — a nice
example of how a different mental model removes a branch.

---

## Problem 2 — Reverse a number & palindrome (maths only)

### 1. Understand
- **Input:** a positive integer like `123`.
- **Output:** the digits reversed (`321`) **without** strings, then a True/False palindrome check.
- **Key tools:** `n % 10` = last digit, `n // 10` = drop the last digit.

### 2. Example by hand (123)
```
n=123 reversed=0
  last=3  reversed = 0*10 + 3 = 3    n=12
  last=2  reversed = 3*10 + 2 = 32   n=1
  last=1  reversed = 32*10 + 1 = 321 n=0  -> stop
```
The `reversed * 10` shifts existing digits left to "make room" for the new one.

### 3. Plan
```
reversed = 0
while n > 0:
    last = n % 10
    reversed = reversed*10 + last
    n = n // 10
return reversed

is_palindrome(n) = (n == reverse_number(n))
```

### 4. Code
See [`q2_reverse_number_solution.py`](q2_reverse_number_solution.py). `is_palindrome` **reuses**
`reverse_number` — don't re-derive the loop (DRY, Day 5).

### 5. Test
| n | reversed | palindrome |
|--:|--:|---|
| 123 | 321 | False |
| 12321 | 12321 | True |
| 7 | 7 | True |
| 1000 | 1 | False (trailing zeros vanish — a real edge case) |

**Why no strings?** This is the same digit-extraction loop you'll use for checksums, digital roots,
and base conversion. The pattern is worth more than the shortcut `str(n)[::-1]`.

---

## Problem 3 — Primes up to N

### 1. Understand
- **Input:** integer `N`.
- **Output:** `is_prime(n)` → bool, and the list of primes `2..N`.
- **Definition:** prime = exactly two divisors (1 and itself). `0`, `1`, negatives are **not** prime.

### 2. Example by hand (is 9 prime?)
Test divisors: `9 % 2 = 1` (no), `9 % 3 = 0` → **yes, 3 divides it** → not prime. Stop immediately —
once you've found one divisor, the verdict is final.

### 3. Plan
```
is_prime(n):
    if n < 2: return False          # edge case
    i = 2
    while i*i <= n:                 # only test up to sqrt(n)
        if n % i == 0: return False # found a divisor -> done early
        i += 1
    return True

primes_up_to(N): collect every k in 2..N where is_prime(k)
```

### 4. Code
See [`q3_primes_solution.py`](q3_primes_solution.py). Two ideas to notice:
- **Search-with-early-exit:** `return False` the instant a divisor appears (the `break` idea from Day 4).
- **`i*i <= n` instead of `i <= sqrt(n)`:** avoids floats and is faster. A factor larger than √n always
  pairs with one smaller than √n, so testing past √n is wasted work.

### 5. Test
| n | is_prime |
|--:|---|
| 1 | False |
| 2 | True (smallest prime) |
| 9 | False |
| 13 | True |
`primes_up_to(30)` → `[2, 3, 5, 7, 11, 13, 17, 19, 23, 29]`. There are **25** primes ≤ 100.

---

## Problem 4 — Word & character statistics

### 1. Understand
- **Input:** a sentence (string).
- **Output:** three values at once — word count, vowel count, longest word.

### 2. Example by hand ("Softpro School of AI")
- Words: `["Softpro", "School", "of", "AI"]` → **4**.
- Vowels: o,o,o,o,a,i… count each → **7**.
- Longest: compare lengths, `"Softpro"` (7) wins → **"Softpro"**.

### 3. Plan — three mini-problems, three known patterns
```
words = sentence.split()                 # word count = len(words)

vowel_count = 0                           # COUNTER pattern
for ch in sentence.lower():
    if ch in "aeiou": vowel_count += 1

longest = ""                             # BEST-SO-FAR pattern
for w in words:
    if len(w) > len(longest): longest = w

return len(words), vowel_count, longest  # tuple
```

### 4. Code
See [`q4_word_stats_solution.py`](q4_word_stats_solution.py). One function returns **three** values;
the caller unpacks them: `wc, vc, longest = word_stats(s)`. That's the multiple-return-values idea
from Day 5 (Python packs them into a tuple automatically).

### 5. Test
| sentence | words | vowels | longest |
|---|--:|--:|---|
| "Softpro School of AI" | 4 | 7 | "Softpro" |
| "Python" | 1 | 1 | "Python" |
| "" (empty) | 0 | 0 | "" |

**Decomposition lesson:** a scary-sounding task is often 2–3 familiar patterns stacked together. Name
the sub-problems first, then each one is something you've already done.

---

## Problem 5 — Number pyramid

### 1. Understand
- **Input:** number of rows `N`.
- **Output:** a centred pyramid; row `r` shows the digit `r`, `r` times.

### 2. Example by hand → a counts table (this IS the trick)
```
row r | leading spaces (n-r) | digits printed (r)
  1   |        3             |   1
  2   |        2             |   2 2
  3   |        1             |   3 3 3
  4   |        0             |   4 4 4 4
```
Spaces **decrease** by 1 each row; the digit and its repeat-count both equal `r`.

### 3. Plan
```
for r in 1..N:
    print( (N-r) spaces  +  r copies of str(r) joined by " " )
```

### 4. Code
See [`q5_pyramid_solution.py`](q5_pyramid_solution.py). Two equivalent versions:
- **String building:** `" " * (n-r)` and `" ".join([str(r)] * r)` — concise.
- **Nested loops:** one inner loop for spaces, one for digits — shows the mechanics explicitly.

Both produce the same output; pick whichever you can read more easily.

### 5. Test
`pyramid(1)` → single `1`. `pyramid(4)` → the 4-row pyramid above. `pyramid(6)` still aligns because
the leading-space formula scales with `N`.

**Pattern-printing lesson:** never code a shape by guessing. Write the per-row counts in a table, find
the relationship to `r` and `N`, and the loop bounds fall out for free.

---

## The one habit that ties all five together

Every solution started **away from the keyboard** — restating the problem, tracing one example by
hand, and writing the steps in plain English. The Python was the *last* and *easiest* step. That is
logic building: **think first, type second.**
</content>
