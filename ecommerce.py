# E-commerce Application

# USER DATABASE

users = {
    "admin": {"password": "admin111", "role": "Admin"},
    "jamey": {"password": "jamey111", "role": "Customer"},
    "helen": {"password": "helen111", "role": "Customer"},
    "peter": {"password": "peter111", "role": "Cashier"},
}

# Valid coupon codes and their discount percentages
valid_coupons = {
    "SAVE10": 10,
    "SAVE20": 20,
    "HALFOFF": 50,
}


# LOGIN SYSTEM

def login():
    print("\n WELCOME TO SHOPRITE ")
    print("Please log in to continue.\n")

    username = input("Username: ").strip()
    password = input("Password: ").strip()

    if username in users:
        if users[username]["password"] == password:
            role = users[username]["role"]
            print(f"\nLogin successful! Welcome, {username}. You are logged in as: {role}")
            return username, role
        else:
            print("Incorrect password. Access denied.")
            return None, None
    else:
        print("Username not found. Access denied.")
        return None, None


# PRICE CALCULATOR

def calculate_price():
    print("\n========== PRICE CALCULATOR ==========")

    # Get subtotal
    subtotal = float(input("Enter product subtotal (UGX): "))

    # Discount based on subtotal amount
    if subtotal >= 500000:
        auto_discount = 15
        print(f"You qualify for a 15% loyalty discount (subtotal >= 500,000).")
    elif subtotal >= 200000:
        auto_discount = 10
        print(f"You qualify for a 10% discount (subtotal >= 200,000).")
    elif subtotal >= 100000:
        auto_discount = 5
        print(f"You qualify for a 5% discount (subtotal >= 100,000).")
    else:
        auto_discount = 0
        print("No automatic discount applied.")

    # Coupon code
    coupon_code = input("Enter coupon code (or press Enter to skip): ").strip().upper()

    if coupon_code == "":
        coupon_discount = 0
        print("No coupon applied.")
    elif coupon_code in valid_coupons:
        coupon_discount = valid_coupons[coupon_code]
        print(f"Valid coupon! Extra {coupon_discount}% discount applied.")
    else:
        coupon_discount = 0
        print("Invalid coupon code. No coupon discount applied.")

    # Total discount (cap at 50% so the store doesn't go bankrupt)
    total_discount_percent = auto_discount + coupon_discount
    if total_discount_percent > 50:
        total_discount_percent = 50
        print("Discount capped at 50%.")

    discount_amount = (total_discount_percent / 100) * subtotal
    price_after_discount = subtotal - discount_amount

    # Tax based on location
    print("\nSelect your location:")
    print("1. Kampala (VAT 18%)")
    print("2. Other Uganda cities (VAT 16%)")
    print("3. Outside Uganda (No tax)")

    location = input("Enter choice (1/2/3): ").strip()

    if location == "1":
        tax_rate = 18
        location_name = "Kampala"
    elif location == "2":
        tax_rate = 16
        location_name = "Other Uganda"
    elif location == "3":
        tax_rate = 0
        location_name = "Outside Uganda"
    else:
        print("Invalid location choice. Defaulting to 18% VAT.")
        tax_rate = 18
        location_name = "Kampala (default)"

    tax_amount = (tax_rate / 100) * price_after_discount
    final_price = price_after_discount + tax_amount

    # Summary
    print("\n ORDER SUMMARY ")
    print(f"Subtotal:              UGX {subtotal:,.0f}")
    print(f"Auto Discount ({auto_discount}%):    UGX -{(auto_discount/100)*subtotal:,.0f}")
    print(f"Coupon Discount ({coupon_discount}%): UGX -{(coupon_discount/100)*subtotal:,.0f}")
    print(f"Price after discount:  UGX {price_after_discount:,.0f}")
    print(f"Tax ({tax_rate}% - {location_name}): UGX {tax_amount:,.0f}")
    print(f"FINAL PRICE:           UGX {final_price:,.0f}")
    print("-----------------------------------")


# MENUS PER ROLE

def admin_menu():
    print("\n ADMIN MENU ")
    print("1. Calculate product price")
    print("2. View all users")
    print("3. Logout")

    choice = input("Choose an option: ").strip()

    if choice == "1":
        calculate_price()
    elif choice == "2":
        print("\n--- Registered Users ---")
        for uname, info in users.items():
            print(f"  {uname} | Role: {info['role']}")
    elif choice == "3":
        print("Logging out...")
    else:
        print("Invalid option.")


def customer_menu():
    print("\n======== CUSTOMER MENU =========")
    print("1. Calculate product price")
    print("2. Logout")

    choice = input("Choose an option: ").strip()

    if choice == "1":
        calculate_price()
    elif choice == "2":
        print("Logging out...")
    else:
        print("Invalid option.")


def cashier_menu():
    print("\n========== CASHIER MENU ==========")
    print("1. Process a sale (calculate final price)")
    print("2. Logout")

    choice = input("Choose an option: ").strip()

    if choice == "1":
        calculate_price()
    elif choice == "2":
        print("Logging out...")
    else:
        print("Invalid option.")


# MAIN PROGRAM

def main():
    username, role = login()

    if username is None:
        print("Exiting program.")
        return

    # Direct user to the right menu based on their role
    if role == "Admin":
        admin_menu()
    elif role == "Customer":
        customer_menu()
    elif role == "Cashier":
        cashier_menu()
    else:
        print("Unknown role. Access denied.")


main()
