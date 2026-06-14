"""
Exercise 1 — Temperature Converter (solution).

Run (asks for input):
    python temperature_converter_solution.py
"""

def c_to_f(c):
    """Celsius -> Fahrenheit."""
    return c * 9 / 5 + 32

def f_to_c(f):
    """Fahrenheit -> Celsius."""
    return (f - 32) * 5 / 9

celsius = float(input("Temperature in Celsius: "))   # cast text -> number

fahrenheit = c_to_f(celsius)                         # USE the returned value
print(f"{celsius:.1f}C = {fahrenheit:.1f}F")

# Round-trip check: convert back and confirm we recover the original.
back = f_to_c(fahrenheit)
print(f"...and back again: {back:.1f}C  (matches input: {abs(back - celsius) < 1e-9})")
