"""
The `global` keyword — and why you should usually avoid it.

Run:
    python global_keyword.py
"""

# =====================================================================
# 1) global lets a function REBIND a module-level variable
# =====================================================================
score = 0

def add_point():
    global score        # "score" here means the module-level score
    score += 1          # this update sticks outside the function

add_point()
add_point()
add_point()
print("Score after 3 points:", score)   # 3
print()

# =====================================================================
# 2) Why it's a smell: ANY function can change it from ANYWHERE
# =====================================================================
# A second function also mutates the same global. Now if `score` is wrong,
# the bug could be in either function — hard to trace as code grows.
def reset_score():
    global score
    score = 0

reset_score()
print("Score after reset:", score)
print()

# =====================================================================
# 3) The cleaner pattern: take it in, return it out (explicit data flow)
# =====================================================================
def add_point_clean(current):
    """Pure: depends only on its input, returns a new value."""
    return current + 1

points = 0
points = add_point_clean(points)
points = add_point_clean(points)
print("Clean points:", points)   # 2 — no hidden state, trivially testable
print()

# =====================================================================
# 4) A LEGITIMATE use: a tiny app-wide config flag
# =====================================================================
DEBUG = False

def enable_debug():
    global DEBUG
    DEBUG = True

def log(message):
    # reads the global (no assignment -> no `global` needed just to read)
    if DEBUG:
        print(f"[debug] {message}")

log("you won't see this")        # DEBUG is False
enable_debug()
log("now logging is on")         # DEBUG is True
print()

# =====================================================================
# 5) nonlocal — the enclosing-scope cousin (rare, but here it is)
# =====================================================================
def make_counter():
    n = 0
    def increment():
        nonlocal n               # rebind n in the ENCLOSING function, not global
        n += 1
        return n
    return increment

tick = make_counter()
print("counter:", tick(), tick(), tick())   # 1 2 3
# Each make_counter() call gets its own independent n — cleaner than a global.
