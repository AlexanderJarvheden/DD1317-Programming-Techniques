import file_management
from product_catalogue import Product_Catalogue

def main():
    catalogue = Product_Catalogue()
    file_management.read_file(catalogue)
