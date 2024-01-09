import file_management
from store import Store
import receipt_management

def main():
    store = Store()
    filename = file_management.read_file(store)
    receipt_management.scan_purchase(store)

    file_management.update_inventory_in_file(store, filename)

main()