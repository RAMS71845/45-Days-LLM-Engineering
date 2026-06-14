"""
Problem 5 - Number pyramid pattern (STUB).

For N = 4 print:
   1
  2 2
 3 3 3
4 4 4 4

Run:
    python q5_pyramid.py
"""

def pyramid(n):
    """Print a centred number pyramid of n rows."""
    for r in range(1, n + 1):
        # TODO: leading spaces  -> (n - r) of them
        # TODO: the digit r, printed r times, separated by spaces
        # TODO: build one line as a string, then print it once
        pass


if __name__ == "__main__":
    pyramid(4)
