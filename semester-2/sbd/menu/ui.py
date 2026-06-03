from menu.query import fetch_all_menus, fetch_menu_by_id, insert_menu, update_menu
from tabulate import tabulate


def display_menus():
    menu = fetch_all_menus()
    if not menu:
        print("\nNo menu data found.")
        return
    print("\n=== MENU MAKANAN LIST ===\n")
    print(tabulate(menu, headers=["ID", "Name", "price", "stock"], tablefmt="grid"))


def form_add_menu():
    print("\n=== REGISTER NEW MENU MAKANAN ===")
    name = input("Menu Name : ").strip()
    price = input("Menu Price: ").strip()
    stock = input("Menu Stock: ").strip()

    if not name or not stock or not price:
        print("\n[Failed] All fields are required!")
        return

    if insert_menu(name, price, stock):
        print(f"\n[Success] menu makanan '{name}' successfully registered!")
    else:
        print("\n[Failed] Could not save menu makanan data.")


def form_update_menu():
    print("\n=== UPDATE MENU MAKANAN DATA ===")
    display_menus()

    menu_id = input("\nEnter Menu Makanan ID to update: ").strip()
    if not menu_id:
        return

    manu_makanan_data = fetch_menu_by_id(menu_id)
    if not manu_makanan_data:
        print(f"\n[Failed] Error: Menu Makanan ID {menu_id} not found!")
        return

    name = input("Menu Name : ").strip()
    price = input("Menu Price: ").strip()
    stock = input("Menu Stock: ").strip()

    if update_menu(name, price, stock):
        print(f"\n[Success] Menu Makanan ID {menu_id} successfully updated!")
    else:
        print(f"\n[Failed] Menu Makanan ID {menu_id} could not be updated.")
