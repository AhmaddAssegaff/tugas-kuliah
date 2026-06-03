from kurir.query import fetch_all_couriers
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
