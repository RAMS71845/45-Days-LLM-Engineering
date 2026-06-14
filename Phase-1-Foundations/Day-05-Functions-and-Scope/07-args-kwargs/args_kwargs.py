"""
*args (extra positionals -> tuple) and **kwargs (extra keywords -> dict),
plus unpacking with * and ** at the call site.

Run:
    python args_kwargs.py
"""

# =====================================================================
# 1) *args -> accept ANY number of positional arguments (as a tuple)
# =====================================================================
def total(*args):
    print("  args is a tuple:", args)
    return sum(args)

print("total(10, 20, 30) =", total(10, 20, 30))   # args == (10, 20, 30)
print("total(5)          =", total(5))             # args == (5,)
print("total()           =", total())              # args == () -> 0
print()

# =====================================================================
# 2) **kwargs -> accept ANY number of keyword arguments (as a dict)
# =====================================================================
def make_user(**kwargs):
    print("  kwargs is a dict:", kwargs)
    return kwargs

make_user(name="Asha", age=21, city="Pune")
make_user(name="Ben")
print()

# =====================================================================
# 3) Combine them — fixed param, then *args, then **kwargs
# =====================================================================
# A logger: a required message, optional extra values, optional context.
def log(message, *values, **context):
    line = message
    if values:
        line += " " + " ".join(str(v) for v in values)
    if context:
        extras = ", ".join(f"{k}={v}" for k, v in context.items())
        line += f"  [{extras}]"
    print(line)

log("Server started")
log("Processed items:", 1, 2, 3)
log("Request done", user="asha", status=200, ms=42)
print()

# =====================================================================
# 4) UNPACKING — the same * and ** spread a collection INTO arguments
# =====================================================================
nums = [10, 20, 30]
print("total(*nums)   =", total(*nums))   # spreads list -> total(10, 20, 30)

info = {"name": "Asha", "age": 21}
make_user(**info)                          # spreads dict -> make_user(name=..., age=...)
print()

# =====================================================================
# 5) REAL USE: forward keyword settings to an "LLM client" (Phase 1 preview)
# =====================================================================
def generate(prompt, model="gemini-1.5-flash", **options):
    """Pretend LLM call that accepts arbitrary extra options."""
    print(f"[{model}] {prompt!r}")
    for key, value in options.items():
        print(f"    {key} = {value}")

# You keep your settings in a dict and spread them — extremely common pattern:
settings = {"temperature": 0.2, "max_tokens": 256, "top_p": 0.9}
generate("Summarise the meeting notes", **settings)
