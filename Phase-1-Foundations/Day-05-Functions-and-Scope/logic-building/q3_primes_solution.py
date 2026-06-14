"""
Problem 3 - Prime checker + list primes up to N (SOLUTION).

Run:
    python q3_primes_solution.py

Logic-building note:
  "Is n prime?" = "does ANY number from 2..n-1 divide n?" The moment we find
  ONE divisor, the answer is settled, so we `break` (Day 4) instead of wasting
  time. Don't forget the edge case: 0, 1, and negatives are not prime.
  Speed-up: a divisor never exceeds sqrt(n), so we only test up to n ** 0.5.
"""

def is_prime(n):
    """Return True if n is prime. Tests divisors only up to sqrt(n)."""
    if n < 2:                       # edge case: 0, 1, negatives are not prime
        return False
    i = 2
    while i * i <= n:               # i*i <= n is the same as i <= sqrt(n), no floats
        if n % i == 0:             # found a divisor -> definitely not prime
            return False           # early return = the search-with-break idea
        i += 1
    return True                     # no divisor found -> prime


def primes_up_to(n):
    """Collect every prime from 2 to n using the accumulator pattern."""
    result = []
    for candidate in range(2, n + 1):
        if is_prime(candidate):    # reuse the boolean function (decompose!)
            result.append(candidate)
    return result


if __name__ == "__main__":
    print("is_prime checks:")
    for x in (1, 2, 7, 9, 13, 100):
        print(f"  {x:>4} -> {is_prime(x)}")

    print("\nPrimes up to 50:")
    print(" ", primes_up_to(50))
    print(f"\nThere are {len(primes_up_to(100))} primes up to 100.")
