def print_receipt(store, receipt):
    """Prints and formats the final receipt"""
    total_amount = 0
    total_sum = 0

    # Display the receipt
    print("\nPurchase Accepted!\nReceipt:\n")

    # Format inspiration from https://thepythonguru.com/python-string-formatting/
    print("{:<10} {:<5} {:<10} {:<10}".format("Product", "Amount", "Price", "Total"))
    print("-" * 40)
    
    # Iterate over all registered products in the receipt and update amount and sum
    for code in receipt.keys():
        product = store.get_product(code)
        receipt_row = f"{product.name} {receipt[code]} {product.price} {round(receipt[code]*product.price, 2)}"
        total_amount += receipt[code]
        total_sum += round(receipt[code] * product.price, 2)
        print(
            "{:<10} {:<5} {:<10} {:<10}".format(*receipt_row.split()) # Unpack the list as separate arguments
        )  
    print("-" * 40)
    print(
        "{:<10} {:<5} {:<10} {:<10}".format(
            "Total", f"{total_amount}", "", f"{total_sum}"
        )
    )


def scan_purchase(store):
    """Handles the whole scanning process, calling on functions that do calculations, undo etc"""
    # Receipt that stores the scanned products and amount
    receipt = {}

    # Keeps count of amount of scans to display it during scanning process
    scan_count = 1

    # Save original inventory in case scanner exits whilst scanning a purchase
    original_inventory = dict(
        store.inventory
    ) 
    print(
        "\nPress '%' to undo, '#' to finish, '&' to exit\nFor products-> enter 'CODE + 'space' + AMOUNT'"
    )
    scanning = True
    while scanning:
        scanned_purchase = input(f"Scan {scan_count}: ")
        scan_count += 1
        scanned_items = scanned_purchase.split()
        amount = interpret_scanned_amount(scanned_items)
        code = scanned_purchase.split()[0]

        # User wants to finish the receipt
        if code == "#":
            scanning = False

        # User wants to undo a product amount
        elif code == "%":
            undo_scan(store, receipt)
        
        # User wants to turn off the scanner
        elif code == "&":
            print("Signing off...")
            store.inventory = original_inventory
            return
        else:
            code = check_if_product_exists(code, store, receipt, 0)
            product = store.get_product(code)
            while True:
                if amount <= store.inventory[code]:
                    store.remove_quantity(product, amount)
                    # If product has not been registered earlier
                    receipt.setdefault(code, 0)
                    receipt[code] += amount
                    print(f"Scanned {amount} {product.name} (Code: {code})")
                    break
                else:
                    print(f"Only {store.inventory[code]} in inventory:")
                    amount = amount_to_int(
                        ""
                    )  # empty string input since we want the exception to be called
    print_receipt(store, receipt)


def interpret_scanned_amount(usr_input):
    """Chooses scanned amount based on input, if no amount is written it is 1"""
    if len(usr_input) >= 2:
        amount = usr_input[1]
        amount = amount_to_int(amount)
    else:
        amount = 1
    return amount


def amount_to_int(amount):
    """Converts the amount to a fit integer for the program (non negative)"""
    while True:
        try:
            amount = int(amount)
            if amount < 0:
                print("Error: Integer must be non-negative.")
                raise ValueError('Error: Integer must be non-negative.')
            break
        except ValueError:
            amount = input("Enter a valid amount (integer): ")
    return amount


def undo_scan(store, receipt):
    """Enables the user to undo a product input"""
    product_to_undo = input(
        "Which product do you want to undo?\nEnter the product code: "
    )
    product_to_undo = check_if_product_exists(product_to_undo, store, receipt, 1)

    amount_to_undo = input(
        f"How many to undo - {store.product_catalogue[product_to_undo].name}: "
    )
    amount_to_undo = amount_to_int(amount_to_undo)
    receipt[product_to_undo] -= amount_to_undo

    if receipt[product_to_undo] == 0:
        # If all amount is gone, delete it from the receipt to avoid displaying a '0' amount
        del receipt[product_to_undo]
    print(f"Unscanned {amount_to_undo} {store.product_catalogue[product_to_undo].name} (Code: {product_to_undo})")
    


def check_if_product_exists(code, store, receipt, check_receipt: bool):
    """Checks if the code is in the system or the receipt if check_receipt is true"""
    if check_receipt:
        while True:
            if code in receipt:
                return code
            else:
                code = input("Invalid code, product does not match try again: ")
    else:
        while True:
            if code in store.product_catalogue:
                return code
            else:
                code = input("Invalid code, product does not match try again: ")
