"""
Exercise 2 — Password Strength Checker (STUDENT STUB).

Write a function that RETURNS a verdict ("weak"/"medium"/"strong"),
with a tunable minimum length via a DEFAULT argument.

Run (asks for input):
    python password_checker.py
"""

# TODO 1: def check_password(pw, min_length=8):
#   - score = 0
#   - +1 if len(pw) >= min_length
#   - +1 if any character isdigit()
#   - +1 if any character isupper()
#   - +1 if any character is in a symbol set like "!@#$%^&*()-_"
#   - return "strong" if score >= 4, "medium" if score >= 2, else "weak"
#   IMPORTANT: return the verdict, don't print inside the function.

# TODO 2: input() a password, call check_password, print the verdict
# TODO 3: also try calling it with min_length=12 and compare
