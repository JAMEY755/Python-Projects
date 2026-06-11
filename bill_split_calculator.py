def get_tip_percentage():
    """Prompt user to select or enter a tip percentage."""
    print("\nSelect tip percentage:")
    print("  1. 10%")
    print("  2. 15%")
    print("  3. 20%")
    print("  4. Custom")

    while True:
        choice = input("Enter choice (1-4): ").strip()
        if choice == "1":
            return 10.0
        elif choice == "2":
            return 15.0
        elif choice == "3":
            return 20.0
        elif choice == "4":
            while True:
                try:
                    custom = float(input("Enter custom tip percentage: ").strip())
                    if custom < 0:
                        print("Tip percentage cannot be negative.")
                    else:
                        return custom
                except ValueError:
                    print("Please enter a valid number.")
        else:
            print("Invalid choice. Please enter 1, 2, 3, or 4.")


def get_positive_float(prompt):
    """Prompt user for a positive float value with validation."""
    while True:
        try:
            value = float(input(prompt).strip())
            if value <= 0:
                print("Value must be greater than zero.")
            else:
                return value
        except ValueError:
            print("Please enter a valid number.")


def get_positive_int(prompt):
    """Prompt user for a positive integer value with validation."""
    while True:
        try:
            value = int(input(prompt).strip())
            if value <= 0:
                print("Number of people must be at least 1.")
            else:
                return value
        except ValueError:
            print("Please enter a whole number (e.g. 3).")


def print_receipt(bill_amount, num_people, tip_pct, tip_amount, total_bill, per_person):
    """Print a formatted receipt showing all calculations."""
    width = 44
    divider = "=" * width
    thin = "-" * width

    print(f"\n{divider}")
    print(f"{'BILL SPLIT RECEIPT':^{width}}")
    print(divider)
    print(f"  {'Original Bill:':<28} UGX {bill_amount:>8,.2f}")
    print(f"  {'Tip Percentage:':<28} {tip_pct:>8.1f}%")
    print(f"  {'Tip Amount:':<28} UGX {tip_amount:>8,.2f}")
    print(thin)
    print(f"  {'Total Bill (Bill + Tip):':<28} UGX {total_bill:>8,.2f}")
    print(thin)
    print(f"  {'Number of People:':<28} {num_people:>9}")
    print(f"  {'Each Person Pays:':<28} UGX {per_person:>8,.2f}")
    print(divider)
    print(f"{'Split equally among all guests':^{width}}")
    print(f"{divider}\n")


def main():
    print("=" * 44)
    print(f"{'BILL SPLIT CALCULATOR':^44}")
    print("=" * 44)

    # --- Inputs with validation ---
    bill_amount = get_positive_float("\nEnter total bill amount (UGX): ")
    num_people  = get_positive_int("Enter number of people: ")
    tip_pct     = get_tip_percentage()

    # --- Calculations ---
    tip_amount = bill_amount * (tip_pct / 100)
    total_bill = bill_amount + tip_amount
    per_person = total_bill / num_people

    # --- Output ---
    print_receipt(bill_amount, num_people, tip_pct, tip_amount, total_bill, per_person)


if __name__ == "__main__":
    main()
