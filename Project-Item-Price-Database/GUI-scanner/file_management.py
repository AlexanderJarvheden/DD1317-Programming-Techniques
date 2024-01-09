import os
from product import Product
import tkinter as tk
from tkinter import messagebox


class File_input_GUI:
    """GUI handling the filename input"""

    def __init__(self, store):
        """Initializes the window for file input"""
        self.window = tk.Tk()
        self.window.title("Load products data")

        self.filename_label = tk.Label(self.window, text="Enter data file with product info:")
        self.filename_label.grid(row=0, column=0)

        self.filename = tk.Entry(self.window)
        self.filename.grid(row=0, column=1)

        self.ok_button = tk.Button(
            self.window, text="OK", command=lambda: self.read_file(store)
        )
        self.ok_button.grid(row=0, column=2)

        self.window.mainloop()


    def read_file(self, store):
        """Reads the data from the file and loads it into the store"""
        filename = self.get_valid_file()

        with open(filename, "r") as file:
            lines = file.readlines()
            self.load_into_store(store, lines)
        self.filename = self.filename.get()

        # When loaded into store destroy file input window
        self.window.destroy()
        return


    def get_valid_file(self):
        """Validates the filename input and returns the valid filename"""
        filename = self.filename.get()

        if not filename:
            messagebox.showinfo("Error", "Please enter a filename.")
            return ""

        if not os.path.exists(filename):
            messagebox.showinfo("Error", "File does not exist. Try again.")
            return ""

        return filename


    def load_into_store(self, store, lines):
        """Loads the products and available quantity into Store data structure"""
        # Increment by 3 since the format consists of 3 lines
        for i in range(0, len(lines), 3):
            code = lines[i].strip()
            name = lines[i + 1]
            price, quantity = self.input_validate_from_data_file(lines, i)
            product = Product(code, name, price)
            store.add_product(product, quantity)
        messagebox.showinfo("Success", f"Product data successfully loaded")


    def input_validate_from_data_file(self, lines, line_number):
        """Return price and quantity as number datatypes if valid in data file"""
        try:
            # line_number + 2 because of the format order in the data file
            price = float(lines[line_number + 2].split(";")[0])
            quantity = int(lines[line_number + 2].split(";")[1])
            return price, quantity
        except ValueError:
            messagebox.showinfo(
                "Error", f"Error format in file: line '{line_number+2}'"
            )
            exit()


# Not part of the class object
def update_inventory_in_file(store, filename):
        """Updates the inventory in the data file and exits the program"""

        with open(filename, 'r') as file:
            lines = file.readlines()

        for code in store.product_catalogue:
            # Find the line that corresponds to the product in the data file
            for i, line in enumerate(lines):
                if line.strip() == code:
                    # Update the inventory in the line
                    lines[i+2] = f"{store.product_catalogue[code].price};{store.inventory[code]}\n"

        with open(filename, 'w') as file:
            file.writelines(lines)

        exit()