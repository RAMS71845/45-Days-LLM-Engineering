"""
Exercise 3 — Receipt Builder (solution).

One function handles calls of any shape, thanks to *args and **kwargs.

Run:
    python receipt_builder_solution.py
"""

def build_receipt(*items, gst_percent=18, currency="Rs", **extra):
    """
    Print a receipt.
      *items      : any number of (name, price) tuples
      gst_percent : GST rate (default 18%)
      currency    : currency label (default "Rs")
      **extra     : any extra footer fields (customer=..., store=..., etc.)
    """
    print("=" * 32)
    subtotal = 0
    for name, price in items:                 # tuple-unpack each line item
        subtotal += price                     # accumulate (Day 4 pattern)
        print(f"{name:<20}{currency} {price:>7.2f}")
    gst = subtotal * gst_percent / 100
    print("-" * 32)
    print(f"{'Subtotal':<20}{currency} {subtotal:>7.2f}")
    print(f"{'GST @ ' + str(gst_percent) + '%':<20}{currency} {gst:>7.2f}")
    print(f"{'TOTAL':<20}{currency} {subtotal + gst:>7.2f}")
    if extra:                                 # **extra is a dict
        print("-" * 32)
        for key, value in extra.items():
            print(f"{key}: {value}")
    print("=" * 32)
    print()


# Call it three different ways — same function, different shapes:
build_receipt(("Coffee", 120), ("Sandwich", 180))

build_receipt(("Book", 499), ("Pen", 25), ("Notebook", 60),
              gst_percent=5, customer="Asha", store="MG Road")

build_receipt(("Annual Plan", 4999), currency="USD", gst_percent=0,
              invoice="INV-2026-001")
