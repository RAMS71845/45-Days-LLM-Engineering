"""
Problem 1 - FizzBuzz (STUB - fill in the TODOs).

Print 1..N, but:
  - multiples of 3       -> "Fizz"
  - multiples of 5       -> "Buzz"
  - multiples of 3 and 5 -> "FizzBuzz"

Run:
    python q1_fizzbuzz.py
"""

def fizzbuzz(n):
    """Print the FizzBuzz sequence from 1 to n (inclusive)."""
    for i in range(1, n + 1):
        # TODO: check "divisible by BOTH 3 and 5" FIRST (it's the most specific case)
        # TODO: then divisible by 3 -> "Fizz"
        # TODO: then divisible by 5 -> "Buzz"
        # TODO: else just print the number
        pass


if __name__ == "__main__":
    fizzbuzz(15)
