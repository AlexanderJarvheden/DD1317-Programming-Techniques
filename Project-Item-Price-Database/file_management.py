import os
from product import Product

def read_file(catalogue):
    while True:
        filename = input("What is the name of the product catalogue file?\n")
        if os.path.exists(filename):
            with open(filename, 'r') as file:
                lines = file.readlines()
                for i in range(0, len(lines), 3):
                    code = lines[i].strip()  # Remove leading and trailing whitespace
                    name = lines[i+1]
                    price = lines[i+2].split(';')[0]
                    quantity = lines[i+2].split(';')[1]
                    product = Product(code, name, float(price))
                    catalogue.add_product(product, quantity)
            return
        else: 
            print("The suggested filename does not exist, please try again")