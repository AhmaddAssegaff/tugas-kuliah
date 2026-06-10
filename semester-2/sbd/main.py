import os

from db import close_connection
from kurir.ui import display_couriers, form_add_courier, form_update_courier
from menu.ui import display_menus, form_add_menu, form_update_menu
from pelanggan.ui import (
    display_customer_order_details,
    display_customers,
    form_add_customer,
    form_update_customer,
)
from pesanan.ui import form_create_order, form_delete_order
from ulasan.ui import form_add_review


def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")


def pause():
    input("\nPress Enter to return...")


def customer_menu():
    while True:
        clear_screen()
        print("==============================")
        print("    CUSTOMER MANAGEMENT       ")
        print("==============================")
        print("1. View All Customers")
        print("2. View Customer Order Details")
        print("3. Add New Customer")
        print("4. Update Customer Data")
        print("0. Back to Main Menu")

        choice = input("\nSelect action: ").strip()

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
            form_add_customer()
            pause()
        elif choice == "4":
            clear_screen()
            form_update_customer()
            pause()
        elif choice == "0":
            break
        else:
            print("\nAction not available.")
            pause()


def courier_menu():
    while True:
        clear_screen()
        print("==============================")
        print("     COURIER MANAGEMENT       ")
        print("==============================")
        print("1. View All Couriers")
        print("2. Add New Courier")
        print("3. Update Courier Data")
        print("0. Back to Main Menu")

        choice = input("\nSelect action: ").strip()

        if choice == "1":
            clear_screen()
            display_couriers()
            pause()
        elif choice == "2":
            clear_screen()
            form_add_courier()
            pause()
        elif choice == "3":
            clear_screen()
            form_update_courier()
            pause()
        elif choice == "0":
            break
        else:
            print("\nAction not available.")
            pause()


def food_menu():
    while True:
        clear_screen()
        print("==============================")
        print("     FOOD MENU MANAGEMENT     ")
        print("==============================")
        print("1. View All Food Menu")
        print("2. Add New Food Menu")
        print("3. Update Food Menu Data")
        print("0. Back to Main Menu")

        choice = input("\nSelect action: ").strip()

        if choice == "1":
            clear_screen()
            display_menus()
            pause()
        elif choice == "2":
            clear_screen()
            form_add_menu()
            pause()
        elif choice == "3":
            clear_screen()
            form_update_menu()
            pause()
        elif choice == "0":
            break
        else:
            print("\nAction not available.")
            pause()


def order_menu():
    while True:
        clear_screen()
        print("==============================")
        print("      ORDER MANAGEMENT        ")
        print("==============================")
        print("1. Create New Order & Details")
        print("2. Delete Order user")
        print("0. Back to Main Menu")

        choice = input("\nSelect action: ").strip()

        if choice == "1":
            clear_screen()
            form_create_order()
            pause()
        if choice == "2":
            clear_screen()
            form_delete_order()
            pause()
        elif choice == "0":
            break
        else:
            print("\nAction not available.")
            pause()


def review_menu():
    while True:
        clear_screen()
        print("===============================")
        print("      REVIEW MANAGEMENT        ")
        print("===============================")
        print("1. Create New Review")
        print("0. Back to Main Menu")

        choice = input("\nSelect action: ").strip()

        if choice == "1":
            clear_screen()
            form_add_review()
            pause()
        elif choice == "0":
            break
        else:
            print("\nAction not available.")
            pause()


def main_menu():
    while True:
        clear_screen()
        print("==============================")
        print("    SIMPLE CASHIER SYSTEM     ")
        print("==============================")
        print("1. Customer Management")
        print("2. Courier Management")
        print("3. Food Menu Management")
        print("4. Order Management")
        print("5. Review Management")
        print("0. Exit")

        choice = input("\nSelect menu: ").strip()

        if choice == "1":
            customer_menu()
        elif choice == "2":
            courier_menu()
        elif choice == "3":
            food_menu()
        elif choice == "4":
            order_menu()
        elif choice == "5":
            review_menu()
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
