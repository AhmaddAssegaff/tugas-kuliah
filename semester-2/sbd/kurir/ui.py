from kurir.query import (
    fetch_all_couriers,
    fetch_courier_by_id,
    insert_courier,
    update_courier,
)
from tabulate import tabulate


def display_couriers():
    couriers = fetch_all_couriers()
    if not couriers:
        print("\nNo courier data found.")
        return
    print("\n=== COURIER LIST ===\n")
    print(
        tabulate(couriers, headers=["ID", "Name", "Status", "Vehicle"], tablefmt="grid")
    )


def form_add_courier():
    print("\n=== REGISTER NEW COURIER ===")
    name = input("Courier Name : ").strip()
    vehicle = input("Vehicle Type : ").strip()

    if not name or not vehicle:
        print("\n[Failed] All fields are required!")
        return

    if insert_courier(name, vehicle):
        print(f"\n[Success] Courier '{name}' successfully registered!")
    else:
        print("\n[Failed] Could not save courier data.")


def form_update_courier():
    print("\n=== UPDATE COURIER DATA ===")
    display_couriers()

    courier_id = input("\nEnter Courier ID to update: ").strip()
    if not courier_id:
        return

    courier_data = fetch_courier_by_id(courier_id)
    if not courier_data:
        print(f"\n[Failed] Error: Courier ID {courier_id} not found!")
        return

    new_name = input("New Name: ").strip()
    new_vehicle = input("New vehicle: ").strip()

    if update_courier(courier_id, new_name, new_vehicle):
        print(f"\n[Success] Courier ID {courier_id} successfully updated!")
    else:
        print(f"\n[Failed] Courier ID {courier_id} could not be updated.")
