"""
Exercise 2 — Password Strength Checker (solution).

Run (asks for input):
    python password_checker_solution.py
"""

SYMBOLS = set("!@#$%^&*()-_=+[]{};:,.<>?/")

def check_password(pw, min_length=8):
    """Return a strength verdict for `pw`. Default minimum length is 8."""
    score = 0
    if len(pw) >= min_length:
        score += 1
    if any(ch.isdigit() for ch in pw):          # any() = the search pattern (Day 4)
        score += 1
    if any(ch.isupper() for ch in pw):
        score += 1
    if any(ch in SYMBOLS for ch in pw):
        score += 1

    if score >= 4:
        return "strong"
    elif score >= 2:
        return "medium"
    return "weak"

# The function RETURNS data; the caller decides what to do with it.
pw = input("Choose a password: ")
print(f"Default rules (>=8) : {check_password(pw)}")
print(f"Strict rules (>=12) : {check_password(pw, min_length=12)}")   # override the default
