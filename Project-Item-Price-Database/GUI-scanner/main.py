import file_management
from store import Store
import receipt_management

def main():
    store = Store()
    file_management.read_file(store)
    while True:
        receipt_management.scan_purchase(store)

main()