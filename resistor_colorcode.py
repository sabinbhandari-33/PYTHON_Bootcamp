# Resistor Color Code Decoder
# EE Second Semester Python Project

COLOR_BANDS = {
    "black":  {"digit": 0, "multiplier": 1,          "tolerance": None},
    "brown":  {"digit": 1, "multiplier": 10,          "tolerance": 1},
    "red":    {"digit": 2, "multiplier": 100,         "tolerance": 2},
    "orange": {"digit": 3, "multiplier": 1_000,       "tolerance": None},
    "yellow": {"digit": 4, "multiplier": 10_000,      "tolerance": None},
    "green":  {"digit": 5, "multiplier": 100_000,     "tolerance": 0.5},
    "blue":   {"digit": 6, "multiplier": 1_000_000,   "tolerance": 0.25},
    "violet": {"digit": 7, "multiplier": 10_000_000,  "tolerance": 0.1},
    "grey":   {"digit": 8, "multiplier": 100_000_000, "tolerance": 0.05},
    "white":  {"digit": 9, "multiplier": None,        "tolerance": None},
    "gold":   {"digit": None,"multiplier": 0.1,       "tolerance": 5},
    "silver": {"digit": None,"multiplier": 0.01,      "tolerance": 10},
}

DIGIT_COLORS = [c for c, v in COLOR_BANDS.items() if v["digit"] is not None]
MULT_COLORS  = [c for c, v in COLOR_BANDS.items() if v["multiplier"] is not None]
TOL_COLORS   = [c for c, v in COLOR_BANDS.items() if v["tolerance"] is not None]


def format_ohms(value):
    """Format a resistance value into a readable string."""
    if value >= 1_000_000:
        return f"{value / 1_000_000:.4g} MΩ"
    elif value >= 1_000:
        return f"{value / 1_000:.4g} kΩ"
    else:
        return f"{value:.4g} Ω"


def colors_to_value(bands):
    """
    Convert a list of color band names to a resistance value and tolerance.

    Supports 4-band and 5-band resistors.
    Returns (resistance_in_ohms, tolerance_percent) or raises ValueError.
    """
    bands = [b.strip().lower() for b in bands]

    if len(bands) == 4:
        d1_color, d2_color, mult_color, tol_color = bands

        if COLOR_BANDS[d1_color]["digit"] is None:
            raise ValueError(f"'{d1_color}' is not a valid digit color for Band 1.")
        if COLOR_BANDS[d2_color]["digit"] is None:
            raise ValueError(f"'{d2_color}' is not a valid digit color for Band 2.")
        if COLOR_BANDS[mult_color]["multiplier"] is None:
            raise ValueError(f"'{mult_color}' is not a valid multiplier color.")
        if COLOR_BANDS[tol_color]["tolerance"] is None:
            raise ValueError(f"'{tol_color}' is not a valid tolerance color.")

        d1   = COLOR_BANDS[d1_color]["digit"]
        d2   = COLOR_BANDS[d2_color]["digit"]
        mult = COLOR_BANDS[mult_color]["multiplier"]
        tol  = COLOR_BANDS[tol_color]["tolerance"]

        resistance = (d1 * 10 + d2) * mult

    elif len(bands) == 5:
        d1_color, d2_color, d3_color, mult_color, tol_color = bands

        if COLOR_BANDS[d1_color]["digit"] is None:
            raise ValueError(f"'{d1_color}' is not a valid digit color for Band 1.")
        if COLOR_BANDS[d2_color]["digit"] is None:
            raise ValueError(f"'{d2_color}' is not a valid digit color for Band 2.")
        if COLOR_BANDS[d3_color]["digit"] is None:
            raise ValueError(f"'{d3_color}' is not a valid digit color for Band 3.")
        if COLOR_BANDS[mult_color]["multiplier"] is None:
            raise ValueError(f"'{mult_color}' is not a valid multiplier color.")
        if COLOR_BANDS[tol_color]["tolerance"] is None:
            raise ValueError(f"'{tol_color}' is not a valid tolerance color.")

        d1   = COLOR_BANDS[d1_color]["digit"]
        d2   = COLOR_BANDS[d2_color]["digit"]
        d3   = COLOR_BANDS[d3_color]["digit"]
        mult = COLOR_BANDS[mult_color]["multiplier"]
        tol  = COLOR_BANDS[tol_color]["tolerance"]

        resistance = (d1 * 100 + d2 * 10 + d3) * mult

    else:
        raise ValueError("Only 4-band and 5-band resistors are supported.")

    return resistance, tol


def value_to_colors(ohms, bands=4):
    """
    Convert a resistance value (in ohms) to color band names.

    Supports 4-band and 5-band output.
    Returns a list of color names, or raises ValueError if no mapping found.
    """
    if ohms <= 0:
        raise ValueError("Resistance must be a positive value.")

    for mult_color in MULT_COLORS:
        mult = COLOR_BANDS[mult_color]["multiplier"]
        base = ohms / mult

        if bands == 4:
            if 10 <= base < 100 and base == round(base):
                d1 = int(base) // 10
                d2 = int(base) % 10
                c1 = [c for c in DIGIT_COLORS if COLOR_BANDS[c]["digit"] == d1][0]
                c2 = [c for c in DIGIT_COLORS if COLOR_BANDS[c]["digit"] == d2][0]
                return [c1, c2, mult_color, "gold"]  # gold = ±5% default

        elif bands == 5:
            if 100 <= base < 1000 and base == round(base):
                base = int(round(base))
                d1 = base // 100
                d2 = (base % 100) // 10
                d3 = base % 10
                c1 = [c for c in DIGIT_COLORS if COLOR_BANDS[c]["digit"] == d1][0]
                c2 = [c for c in DIGIT_COLORS if COLOR_BANDS[c]["digit"] == d2][0]
                c3 = [c for c in DIGIT_COLORS if COLOR_BANDS[c]["digit"] == d3][0]
                return [c1, c2, c3, mult_color, "brown"]  # brown = ±1% default

    raise ValueError(
        f"Cannot map {format_ohms(ohms)} to a standard {bands}-band code. "
        "Try a rounder value like 470, 4700, or 47000."
    )


def print_color_table():
    """Print a reference table of all color codes."""
    print("\n--- Color Code Reference Table ---")
    print(f"{'Color':<10} {'Digit':<8} {'Multiplier':<15} {'Tolerance'}")
    print("-" * 45)
    for color, props in COLOR_BANDS.items():
        digit = str(props["digit"]) if props["digit"] is not None else "-"
        mult  = str(props["multiplier"]) if props["multiplier"] is not None else "-"
        tol   = f"±{props['tolerance']}%" if props["tolerance"] is not None else "-"
        print(f"{color.capitalize():<10} {digit:<8} {mult:<15} {tol}")
    print()


def menu_colors_to_value():
    """Interactive prompt for colors → value."""
    print("\n--- Colors to Resistance Value ---")
    n = input("How many bands? (4 or 5): ").strip()
    if n not in ("4", "5"):
        print("Invalid choice. Please enter 4 or 5.")
        return

    n = int(n)
    labels = (
        ["Band 1 (digit)", "Band 2 (digit)", "Multiplier", "Tolerance"]
        if n == 4
        else ["Band 1 (digit)", "Band 2 (digit)", "Band 3 (digit)", "Multiplier", "Tolerance"]
    )

    bands = []
    for label in labels:
        color = input(f"  Enter color for {label}: ").strip().lower()
        if color not in COLOR_BANDS:
            print(f"  Unknown color '{color}'. Valid colors: {', '.join(COLOR_BANDS)}")
            return
        bands.append(color)

    try:
        resistance, tol = colors_to_value(bands)
        print(f"\n  Resistance  : {format_ohms(resistance)}")
        print(f"  Tolerance   : ±{tol}%")
        min_r = resistance * (1 - tol / 100)
        max_r = resistance * (1 + tol / 100)
        print(f"  Actual range: {format_ohms(min_r)} – {format_ohms(max_r)}")
    except (ValueError, KeyError, IndexError) as e:
        print(f"  Error: {e}")


def menu_value_to_colors():
    """Interactive prompt for value → colors."""
    print("\n--- Resistance Value to Color Bands ---")
    try:
        val  = float(input("Enter resistance value: "))
        unit = input("Unit? (1=Ω, 2=kΩ, 3=MΩ): ").strip()
        multipliers = {"1": 1, "2": 1_000, "3": 1_000_000}
        if unit not in multipliers:
            print("Invalid unit selection.")
            return
        ohms = val * multipliers[unit]
        n = input("How many bands? (4 or 5): ").strip()
        if n not in ("4", "5"):
            print("Invalid choice.")
            return
        bands = value_to_colors(ohms, bands=int(n))
        print(f"\n  Value  : {format_ohms(ohms)}")
        print(f"  Bands  : {' | '.join(b.capitalize() for b in bands)}")
    except ValueError as e:
        print(f"  Error: {e}")


def main():
    print("=" * 45)
    print("   Resistor Color Code Decoder")
    print("   EE Project — Python")
    print("=" * 45)

    while True:
        print("\nWhat would you like to do?")
        print("  1. Colors → Resistance value")
        print("  2. Resistance value → Colors")
        print("  3. Show color code reference table")
        print("  4. Quit")

        choice = input("\nEnter choice (1-4): ").strip()

        if choice == "1":
            menu_colors_to_value()
        elif choice == "2":
            menu_value_to_colors()
        elif choice == "3":
            print_color_table()
        elif choice == "4":
            print("\nGoodbye!")
            break
        else:
            print("Invalid choice. Please enter 1, 2, 3, or 4.")


if __name__ == "__main__":
    main()