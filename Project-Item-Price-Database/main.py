import file_management
from product_catalogue import Product_Catalogue
import receipt_management

def main():
    catalogue = Product_Catalogue()
    file_management.read_file(catalogue)
    
    receipt_management.scan_purchase(catalogue)

main()