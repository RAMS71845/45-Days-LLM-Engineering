"""
Problem 5 - Number pyramid pattern (SOLUTION).

Run:
    python q5_pyramid_solution.py

Logic-building note - turn the SHAPE into a small table first, then code it:
    row r | leading spaces (n-r) | digits printed (r)
      1   |        3             |   1
      2   |        2             |   2 2
      3   |        1             |   3 3 3
      4   |        0             |   4 4 4 4
  Once the counts are in a table, the loop bounds write themselves.
"""

def pyramid(n):
    """Print a centred number pyramid using string building."""
    for r in range(1, n + 1):
        spaces = " " * (n - r)              # leading spaces shrink each row
        digits = " ".join([str(r)] * r)     # a list of r copies of the digit, space-joined
        print(spaces + digits)


def pyramid_with_loops(n):
    """Same output, but using explicit nested loops (no string tricks)."""
    for r in range(1, n + 1):
        line = ""
        for _ in range(n - r):              # inner loop 1: the spaces
            line += " "
        for c in range(r):                  # inner loop 2: the digits
            line += str(r)
            if c < r - 1:                   # space between digits, not after the last
                line += " "
        print(line)


if __name__ == "__main__":
    print("--- string-building version ---")
    pyramid(4)

    print("\n--- nested-loop version (identical output) ---")
    pyramid_with_loops(4)

    print("\n--- scales to any size ---")
    pyramid(6)
