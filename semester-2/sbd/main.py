import os

from db import close_connection
from kurir.ui import display_couriers, form_add_courier, form_update_courier
from pelanggan.ui import (
    display_customer_order_details,
    display_customers,
    form_add_customer,
    form_update_customer,
)


def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")


def pause():
    input("\nPress Enter to return...")


def main_menu():
    while True:
        clear_screen()

        print("==============================")
        print("    SIMPLE CASHIER SYSTEM     ")
        print("==============================")
        print("1. View Customers")
        print("2. View Customer Order Details")
        print("3. View Couriers")
        print("4. Add New Courier")
        print("5. Update Courier")
        print("6. Add New Customer")
        print("7. Update Customer")
        print("0. Exit")

        choice = input("\nSelect menu: ").strip()

        if choice == "1":
            clear_screen()
            display_customers()
            pause()

        elif choice == "2":
            clear_screen()
            display_customer_order_details()
            pause()

        elif choice == "3":
            clear_screen()
            display_couriers()
            pause()

        elif choice == "4":
            clear_screen()
            form_add_courier()
            pause()

        elif choice == "5":
            clear_screen()
            form_update_courier()
            pause()

        elif choice == "6":
            clear_screen()
            form_add_customer()
            pause()

        elif choice == "7":
            clear_screen()
            form_update_customer()
            pause()

        elif choice == "0":
            clear_screen()
            close_connection()
            print("Thank you for using the system!")
            break

        else:
            print("\nMenu not available.")
            pause()


if __name__ == "__main__":
    main_menu()
