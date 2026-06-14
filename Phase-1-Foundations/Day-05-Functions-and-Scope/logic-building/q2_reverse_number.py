"""
Problem 2 - Reverse a number & check palindrome, using MATHS only (STUB).

No str(n)[::-1] allowed - the point is to practise // and %.

Run:
    python q2_reverse_number.py
"""

def reverse_number(n):
    """Return n with its digits reversed (e.g. 123 -> 321)."""
    reversed_n = 0
    # TODO: while n is greater than 0:
    #   1. grab the last digit: last = n % 10
    #   2. shift reversed_n left and add it: reversed_n = reversed_n * 10 + last
    #   3. drop the last digit from n: n = n // 10
    return reversed_n


def is_palindrome(n):
    """Return True if n reads the same forwards and backwards."""
    # TODO: a number is a palindrome if it equals its own reverse
    return False


if __name__ == "__main__":
    print(reverse_number(12345))   # expect 54321
    print(is_palindrome(12321))    # expect True
    print(is_palindrome(12345))    # expect False
