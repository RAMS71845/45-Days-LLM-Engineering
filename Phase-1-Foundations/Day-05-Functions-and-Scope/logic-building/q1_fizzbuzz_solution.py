"""
Problem 1 - FizzBuzz (SOLUTION).

Run:
    python q1_fizzbuzz_solution.py

Logic-building note:
  The whole problem is one decision per number. The ONLY trap is ordering the
  checks: "divisible by both 3 and 5" must be tested BEFORE the single checks,
  otherwise a number like 15 would match `% 3 == 0` first and print "Fizz".
"""

def label(i):
    """Return the FizzBuzz label for a single number i (as a string)."""
    if i % 3 == 0 and i % 5 == 0:   # most specific case first (i.e. % 15 == 0)
        return "FizzBuzz"
    elif i % 3 == 0:
        return "Fizz"
    elif i % 5 == 0:
        return "Buzz"
    else:
        return str(i)               # plain number -> string, so the type is consistent


def fizzbuzz(n):
    """Print the FizzBuzz sequence from 1 to n (inclusive)."""
    for i in range(1, n + 1):
        print(label(i))


# --- An alternative "build the word" approach (no special both-case needed) ---
def label_build(i):
    """Same result, built up piece by piece. Notice: no 'FizzBuzz' literal needed."""
    word = ""
    if i % 3 == 0:
        word += "Fizz"
    if i % 5 == 0:
        word += "Buzz"
    return word or str(i)           # empty string is falsy -> fall back to the number


if __name__ == "__main__":
    print("--- if/elif version ---")
    fizzbuzz(15)

    print("\n--- build-the-word version (same output) ---")
    for i in range(1, 16):
        print(label_build(i))
