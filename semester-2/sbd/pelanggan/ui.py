from pelanggan.query import (
    fetch_all_customers,
    fetch_customer_by_id,
    fetch_customer_order_details,
    insert_customer,
    update_customer,
)
from tabulate import tabulate


def display_customers():
    customers = fetch_all_customers()
    if not customers:
        print("\nNo customer data found.")
        return
    print("\n=== CUSTOMER LIST ===\n")
    print(
        tabulate(
            customers,
            headers=["ID", "Name", "Address", "Phone Number"],
            tablefmt="grid",
        )
    )


def display_customer_order_details():
    display_customers()
    customer_id = input("\nEnter Customer ID: ").strip()
    if not customer_id:
        return

    orders = fetch_customer_order_details(customer_id)
    if not orders:
        print("\nNo orders found for this customer.")
        return

    print("\n=== ORDER DETAILS ===\n")
    headers = [
        "Cust ID",
        "Name",
        "Order ID",
        "Status",
        "Order Date",
        "Payment",
        "Total",
        "Delivery Done",
        "Courier",
        "Vehicle",
        "Rating",
        "Comment",
    ]
    print(tabulate(orders, headers=headers, tablefmt="grid"))


def form_add_customer():
    print("\n=== REGISTER NEW CUSTOMER ===")
    name = input("Name: ").strip()
    address = input("Address: ").strip()
    phone = input("Phone Number: ").strip()

    if not name or not address or not phone:
        print("\n[Failed] All fields are required!")
        return

    if insert_customer(name, address, phone):
        print(f"\n[Success] Customer '{name}' successfully registered!")
    else:
        print("\n[Failed] Could not save customer data.")


def form_update_customer():
    print("\n=== UPDATE CUSTOMER DATA ===")
    display_customers()

    customer_id = input("\nEnter Customer ID to update: ").strip()
    if not customer_id:
        return

    if not fetch_customer_by_id(customer_id):
        print(f"\n[Failed] Error: Customer ID {customer_id} not found!")
        return

    print("\n--- Enter New Data ---")
    new_name = input("New Name: ").strip()
    new_address = input("New Address: ").strip()
    new_phone = input("New Phone Number: ").strip()

    if not new_name or not new_address or not new_phone:
        print("\n[Failed] All fields are required for update!")
        return

    success = update_customer(customer_id, new_name, new_address, new_phone)

    if success:
        print(f"\n[Success] Customer ID {customer_id} successfully updated!")
    else:
        print(f"\n[Failed] Customer ID {customer_id} could not be updated.")
