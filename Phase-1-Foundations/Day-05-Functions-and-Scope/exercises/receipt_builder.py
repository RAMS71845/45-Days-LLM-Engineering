"""
Exercise 3 — Receipt Builder (STUDENT STUB).

A real variadic API: any number of line items (*items) + optional
settings (**kwargs). Does NOT use input() — call it with different shapes.

Run:
    python receipt_builder.py
"""

# TODO: def build_receipt(*items, gst_percent=18, currency="Rs", **extra):
#   - *items is any number of (name, price) tuples
#   - loop them: print each "<name> ... <price>" and add price to a subtotal
#   - gst = subtotal * gst_percent / 100; print the grand total
#   - print any **extra fields (e.g. customer="Asha") as a footer
#
# Then call it a few ways, e.g.:
#   build_receipt(("Coffee", 120), ("Sandwich", 180))
#   build_receipt(("Book", 499), gst_percent=5, customer="Asha", store="MG Road")
