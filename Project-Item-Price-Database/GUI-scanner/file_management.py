import os
from product import Product

def read_file(store):
        """Reads the data from the file and loads it into the store"""
        filename = valid_file()

        with open(filename, 'r') as file:
            lines = file.readlines()
            load_into_store(store, lines)
        return

def valid_file():
    """Validates the filename input and returns the valid filename"""
    while True:
        filename = input("What is the name of the product data file?\n")
        
        if not filename:
            print("Please enter a filename.")
            continue
        elif not os.path.exists(filename):
            print("File does not exist. Try again.")
            continue
        else:
            return filename
        
def load_into_store(store, lines):
    """Loads the products and available quantity into Store data structure"""
    for i in range(0, len(lines), 3):
        code = lines[i].strip()  # Remove leading and trailing whitespace
        name = lines[i+1]
        price, quantity = input_validate_from_data_file(lines, i)
        product = Product(code, name, price)
        store.add_product(product, quantity)

def input_validate_from_data_file(lines, line_number):
    """Return price and quantity as number datatypes if valid in data file"""
    try:
        price = float(lines[line_number+2].split(';')[0])
        quantity = int(lines[line_number+2].split(';')[1])
        return price, quantity
    except ValueError:
        print(f"Error format in file: line '{line_number+2}'")
        exit()