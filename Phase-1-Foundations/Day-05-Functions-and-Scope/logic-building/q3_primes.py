"""
Problem 3 - Prime checker + list primes up to N (STUB).

A prime number > 1 has exactly two divisors: 1 and itself.

Run:
    python q3_primes.py
"""

def is_prime(n):
    """Return True if n is a prime number."""
    # TODO: numbers below 2 are NOT prime -> return False early (edge case!)
    # TODO: loop i from 2 up to n-1; if n % i == 0, n has a divisor -> not prime
    # TODO: if the loop finds no divisor, n is prime
    return False


def primes_up_to(n):
    """Return a list of all primes from 2 to n (inclusive)."""
    result = []
    # TODO: loop the numbers and keep the ones where is_prime(...) is True
    return result


if __name__ == "__main__":
    print(is_prime(7))          # expect True
    print(is_prime(9))          # expect False
    print(primes_up_to(30))     # expect [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
