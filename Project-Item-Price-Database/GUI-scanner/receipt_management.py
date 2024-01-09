import tkinter as tk
from tkinter import simpledialog, messagebox
from file_management import update_inventory_in_file


class ScannerGUI:
    """Class that handles the scanning and receipt through a GUI"""

    def __init__(self, store, filename):
        """Initializes the GUI with window and the receipt"""
        self.window = tk.Tk()
        self.window.title("Scanner")
        self.window.geometry("800x600")

        # Supposed to store filename from prior file management to use in update inventory on closing
        self.filename = filename

        # Receipt that stores the scanned products and amount
        self.receipt = {}
        self.scan_actions = []

        # Frame to improve aesthetics
        input_frame = tk.Frame(self.window)
        input_frame.grid(row=0, column=0, columnspan=3)

        # Labels to display what the entries are supposed to be
        self.code_label = tk.Label(input_frame, text="Product Code:")
        self.code_label.grid(row=0, column=0)

        self.code = tk.Entry(input_frame)
        self.code.grid(row=0, column=1)

        self.amount_label = tk.Label(input_frame, text="Amount:")
        self.amount_label.grid(row=0, column=2)

        self.amount = tk.Entry(input_frame)
        self.amount.grid(row=0, column=3)

        # Buttons for actions
        self.scan_button = tk.Button(
            self.window,
            text="SCAN",
            command=lambda: self.scan_purchase(store),
            width=15,
        )
        self.scan_button.grid(row=1, column=0)

        self.finish_button = tk.Button(
            self.window,
            text="FINISH",
            command=lambda: self.finish_purchase(store),
            width=15,
        )
        self.finish_button.grid(row=1, column=1)

        self.undo_button = tk.Button(
            self.window,
            text="UNDO",
            command=lambda: self.undo_scan(store, self.receipt),
            width=15,
        )
        self.undo_button.grid(row=1, column=2)

        # Listbox to display the scanned actions
        self.scan_actions_listbox = tk.Listbox(self.window, height=10, width=80)
        self.scan_actions_listbox.grid(row=2, column=0, columnspan=3)

        # Text that will display the receipt as if it was in the terminal with the same formatting
        self.receipt_text = tk.Text(self.window, height=10, width=80, wrap=tk.WORD)
        self.receipt_text.grid(
            row=3, column=0, columnspan=3, sticky="nsew"
        )

        # Adjust the row and column weights to allow vertical growth of the text widget
        # Source https://www.pythontutorial.net/tkinter/tkinter-grid/
        for i in range(4):  
            self.window.grid_rowconfigure(i, weight=1)
        for i in range(3):  
            self.window.grid_columnconfigure(i, weight=1)

        # When the user closes the program, update the data file with current inventory
        self.window.protocol(
            "WM_DELETE_WINDOW", lambda: update_inventory_in_file(store, filename)
        )

        self.window.mainloop()


    def finish_purchase(self, store):
        """Handles the finish button to display the receipt"""

        # Display the receipt in the text widget
        receipt_text = self.format_receipt(store, self.receipt)
        self.receipt_text.insert(tk.END, receipt_text)

        # Clear the scan actions and update the Listbox
        self.scan_actions = []
        self.scan_actions_listbox.delete(0, tk.END)

        # Clear the receipt for the next purchase to start on scratch
        self.receipt = {}


    def scan_purchase(self, store):
        """Takes care of the scanning process, updating the listbox"""
        # The code from the entry box
        scanned_code = self.code.get()
        # The amount from the amount box
        scanned_amount = self.amount.get()
        amount = self.interpret_scanned_amount(scanned_amount)

        code = self.check_if_product_exists(scanned_code, store, self.receipt, 0)
        product = store.get_product(code)
        while True:
            if amount <= store.inventory[code]:
                store.remove_quantity(product, amount)
                # If product has not been registered earlier
                self.receipt.setdefault(code, 0)
                self.receipt[code] += amount

                # Update the scan actions listbox
                action = f"Scanned {amount} {product.name} (Code: {code})"
                self.scan_actions.append(action)
                self.scan_actions_listbox.delete(0, tk.END)
                for scan_action in self.scan_actions:
                    self.scan_actions_listbox.insert(tk.END, scan_action)

                # Clear the entry widgets
                self.code.delete(0, tk.END)
                self.amount.delete(0, tk.END)

                break
            else:
                messagebox.showwarning(
                    "Insufficient Inventory",
                    f"Only {store.inventory[code]} in inventory.",
                )
                amount = simpledialog.askinteger(
                    "Invalid Amount",
                    f"Enter a valid amount (less than {store.inventory[code]}):",
                )

                if amount is None:
                    # User clicked cancel
                    break


    def format_receipt(self, store, receipt):
        """Formats the receipt"""
        total_amount = 0
        total_sum = 0

        # Format inspiration from https://thepythonguru.com/python-string-formatting/
        receipt_text = "\nPurchase Accepted!\nReceipt:\n"
        receipt_text += "{:<20} {:<5} {:<10} {:<10}\n".format(
            "Product", "Amount", "Price", "Total"
        )
        receipt_text += "-" * 50 + "\n"

        for code in receipt.keys():
            product = store.get_product(code)
            row = f"{product.name} {receipt[code]} {product.price} {round(receipt[code]*product.price, 2)}"
            total_amount += receipt[code]
            total_sum += round(receipt[code] * product.price, 2)
            receipt_text += "{:<20} {:<5} {:<10} {:<10}\n".format(*row.split())

        receipt_text += "-" * 50 + "\n"
        receipt_text += "{:<20} {:<5} {:<10} {:<10}\n".format(
            "Total", f"{total_amount}", "", f"{total_sum}"
        )

        return receipt_text


    def interpret_scanned_amount(self, usr_input):
        """Chooses amount based on input, if no amount is written it is 1"""
        if len(usr_input) >= 1:
            amount = usr_input
            amount = self.amount_to_int(amount)
        else:
            amount = 1
        return amount


    def amount_to_int(self, amount):
        """Converts the amount to an integer"""
        while True:
            try:
                amount = int(amount)
                if amount < 0:
                    raise ValueError("Error: Integer must be non-negative.")
                break
            except ValueError:
                # Use simpledialog to get valid integer input
                amount = simpledialog.askinteger(
                    "Invalid Amount", "Enter a valid amount (positive integer): "
                )
        return amount


    def undo_scan(self, store, receipt):
        """Enables the user to undo a product input"""
        product_to_undo = simpledialog.askstring(
            "Undo Product",
            "Which product do you want to undo?\nEnter the product code:",
        )
        product_to_undo = self.check_if_product_exists(
            product_to_undo, store, receipt, 1
        )

        amount_to_undo = simpledialog.askinteger(
            "Undo Amount",
            f"How many to undo - {store.product_catalogue[product_to_undo].name}",
        )

        amount_to_undo = self.amount_to_int(amount_to_undo)

        if amount_to_undo is not None:  # User clicked Cancel
            while True:
                if amount_to_undo <= receipt[product_to_undo]:
                    receipt[product_to_undo] -= amount_to_undo
                    if receipt[product_to_undo] == 0:
                        # If all amount is gone, delete it from the receipt to avoid displaying a '0' amount
                        del receipt[product_to_undo]
                    break
                else:
                    amount_to_undo = simpledialog.askinteger(
                        "Undo Amount",
                        f"How many to undo - only {receipt[product_to_undo]} scanned",
                    )

        # Update the scan actions listbox
        unscanned_action = f"Unscanned {amount_to_undo} {store.product_catalogue[product_to_undo].name} (Code: {product_to_undo})"
        self.scan_actions.append(unscanned_action)
        self.scan_actions_listbox.delete(0, tk.END)
        for scan_action in self.scan_actions:
            self.scan_actions_listbox.insert(tk.END, scan_action)
        # Clear the entry widgets
        self.code.delete(0, tk.END)
        self.amount.delete(0, tk.END)


    def check_if_product_exists(self, code, store, receipt, check_receipt: bool):
        """Checks if the code is in the system or the receipt if check_receipt is true"""
        if check_receipt:
            while True:
                if code in receipt:
                    return code
                else:
                    code = simpledialog.askstring(
                        "Invalid Code",
                        "Invalid code, product does not match. Try again:",
                    )
                    if code is None:
                        # User cancelled
                        break
        else:
            while True:
                if code in store.product_catalogue:
                    return code
                else:
                    code = simpledialog.askstring(
                        "Invalid Code",
                        "Invalid code, product does not match. Try again:",
                    )
                    if code is None:
                        break
