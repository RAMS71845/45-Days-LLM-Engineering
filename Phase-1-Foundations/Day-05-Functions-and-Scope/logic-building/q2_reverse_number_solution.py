"""
Problem 2 - Reverse a number & check palindrome, using MATHS only (SOLUTION).

Run:
    python q2_reverse_number_solution.py

Logic-building note - trace 123 by hand to see WHY this works:
    start: n=123  reversed=0
    step1: last=3  reversed=0*10+3=3     n=12
    step2: last=2  reversed=3*10+2=32    n=1
    step3: last=1  reversed=32*10+1=321  n=0  -> loop stops
  The two key tools: `n % 10` reads the last digit, `n // 10` chops it off.
"""

def reverse_number(n):
    """Return n with its digits reversed (123 -> 321). Uses only integer maths."""
    reversed_n = 0
    while n > 0:
        last = n % 10                    # last digit
        reversed_n = reversed_n * 10 + last   # accumulator: make room, drop it in
        n = n // 10                      # remove the last digit
    return reversed_n


def is_palindrome(n):
    """True if n reads the same both ways. We reuse reverse_number (DRY)."""
    return n == reverse_number(n)        # decompose: build on the function we already have


def digit_sum(n):
    """Bonus helper: sum of the digits, same loop shape."""
    total = 0
    while n > 0:
        total += n % 10
        n //= 10
    return total


if __name__ == "__main__":
    for value in (123, 12345, 12321, 1000, 7):
        rev = reverse_number(value)
        print(f"{value:>6} -> reversed {rev:<6} palindrome={is_palindrome(value)}  digit_sum={digit_sum(value)}")
