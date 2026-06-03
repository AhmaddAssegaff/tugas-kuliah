import os

from db import close_connection
from kurir.ui import display_couriers
from pelanggan.ui import (
    display_customer_order_details,
    display_customers,
    form_add_customer,
    form_update_customer,
)


def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")


def main_menu():
    while True:
        clear_screen()
        print("==============================")
        print("    SIMPLE CASHIER SYSTEM     ")
        print("==============================")
        print("1. View Customers")
        print("2. View Customer Order Details")
        print("3. View Couriers")
        print("4. Add New Customer")
        print("5. Update Customer")
        print("0. Exit")

        choice = input("\nSelect menu: ").strip()

        if choice == "1":
            clear_screen()
            display_customers()
            input("\nPress Enter to return...")
        elif choice == "2":
            clear_screen()
            display_customer_order_details()
            input("\nPress Enter to return...")
        elif choice == "3":
            clear_screen()
            display_couriers()
            input("\nPress Enter to return...")
        elif choice == "4":
            clear_screen()
            form_add_customer()
            input("\nPress Enter to return...")
        elif choice == "5":
            clear_screen()
            form_update_customer()
            input("\nPress Enter to return...")
        elif choice == "0":
            clear_screen()
            close_connection()
            print("Thank you for using the system!")
            break
        else:
            print("\nMenu not available.")
            input("\nPress Enter to continue...")


if __name__ == "__main__":
    main_menu()
