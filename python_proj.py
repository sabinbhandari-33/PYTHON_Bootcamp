"""
ELECTRICAL CIRCUIT ANALYSIS TOOLKIT
------------------------------------
A menu-driven Python program for basic electrical engineering calculations:
  1. Ohm's Law Calculator (solve for V, I, or R)
  2. Series & Parallel Resistance Calculator
  3. Electrical Power Calculator
  4. Voltage Divider Calculator
  5. Plot V-I Characteristic Curve for a resistor
  6. Exit

Author: <Your Name>
"""

import matplotlib.pyplot as plt


# ---------------------- OHM'S LAW ----------------------
def ohms_law():
    print("\n--- Ohm's Law Calculator (V = I x R) ---")
    print("Which value do you want to find?")
    print("1. Voltage (V)\n2. Current (I)\n3. Resistance (R)")
    choice = input("Enter choice (1/2/3): ")

    if choice == "1":
        I = float(input("Enter Current (A): "))
        R = float(input("Enter Resistance (ohm): "))
        print(f"Voltage = {I * R:.3f} V")
    elif choice == "2":
        V = float(input("Enter Voltage (V): "))
        R = float(input("Enter Resistance (ohm): "))
        print(f"Current = {V / R:.3f} A")
    elif choice == "3":
        V = float(input("Enter Voltage (V): "))
        I = float(input("Enter Current (A): "))
        print(f"Resistance = {V / I:.3f} ohm")
    else:
        print("Invalid choice.")


# ---------------------- RESISTANCE ----------------------
def resistance_calculator():
    print("\n--- Series & Parallel Resistance Calculator ---")
    n = int(input("How many resistors? "))
    resistors = []
    for i in range(n):
        r = float(input(f"Enter value of R{i+1} (ohm): "))
        resistors.append(r)

    series_total = sum(resistors)
    parallel_total = 1 / sum(1 / r for r in resistors)

    print(f"\nTotal Resistance (Series)   = {series_total:.3f} ohm")
    print(f"Total Resistance (Parallel) = {parallel_total:.3f} ohm")


# ---------------------- POWER ----------------------
def power_calculator():
    print("\n--- Power Calculator (P = V x I) ---")
    V = float(input("Enter Voltage (V): "))
    I = float(input("Enter Current (A): "))
    P = V * I
    print(f"Power = {P:.3f} W")

    if P < 10:
        print("Category: Low Power Device")
    elif P < 1000:
        print("Category: Medium Power Device")
    else:
        print("Category: High Power Device")


# ---------------------- VOLTAGE DIVIDER ----------------------
def voltage_divider():
    print("\n--- Voltage Divider Calculator ---")
    Vin = float(input("Enter Input Voltage (V): "))
    R1 = float(input("Enter R1 (ohm): "))
    R2 = float(input("Enter R2 (ohm): "))

    Vout = Vin * (R2 / (R1 + R2))
    print(f"Output Voltage across R2 = {Vout:.3f} V")


# ---------------------- V-I GRAPH ----------------------
def plot_vi_curve():
    print("\n--- V-I Characteristic Curve ---")
    R = float(input("Enter Resistance value (ohm): "))
    voltages = list(range(0, 21))  # 0V to 20V
    currents = [V / R for V in voltages]

    plt.figure(figsize=(6, 4))
    plt.plot(voltages, currents, marker='o', color='blue')
    plt.title(f"V-I Characteristic Curve (R = {R} ohm)")
    plt.xlabel("Voltage (V)")
    plt.ylabel("Current (A)")
    plt.grid(True)
    plt.tight_layout()
    plt.savefig("vi_curve.png")
    print("Graph saved as 'vi_curve.png' in the current folder.")
    plt.show()


# ---------------------- MAIN MENU ----------------------
def main():
    while True:
        print("\n===== ELECTRICAL CIRCUIT ANALYSIS TOOLKIT =====")
        print("1. Ohm's Law Calculator")
        print("2. Series & Parallel Resistance Calculator")
        print("3. Power Calculator")
        print("4. Voltage Divider Calculator")
        print("5. Plot V-I Characteristic Curve")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")

        if choice == "1":
            ohms_law()
        elif choice == "2":
            resistance_calculator()
        elif choice == "3":
            power_calculator()
        elif choice == "4":
            voltage_divider()
        elif choice == "5":
            plot_vi_curve()
        elif choice == "6":
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice, please try again.")


if __name__ == "__main__":
    main()