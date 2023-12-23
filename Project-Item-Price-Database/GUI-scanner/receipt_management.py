def print_receipt(store, receipt):
    """Prints the final receipt"""
    total_amount = 0
    total_sum = 0

    # Display the receipt
    print("\nPurchase Accepted!\nReceipt:\n")

    # format inspiration from https://thepythonguru.com/python-string-formatting/
    print("{:<20} {:<10} {:<10} {:<10}".format("Product", "Amount", "Price", "Total"))
    print("-" * 50)
    for code in receipt.keys():
        product = store.get_product(code)
        row = f"{product.name} {receipt[code]} {product.price} {round(receipt[code]*product.price, 2)}"
        total_amount += receipt[code]
        total_sum += round(receipt[code] * product.price, 2)
        print(
            "{:<20} {:<10} {:<10} {:<10}".format(*row.split())
        )  # unpack the list as separate arguments
    print("-" * 50)
    print(
        "{:<20} {:<10} {:<10} {:<10}".format(
            "Total", f"{total_amount}", "", f"{total_sum}"
        )
    )

def scan_purchase(store):
    """Handles the whole scanning process, calling on functions that do calculations, undo etc"""
    receipt = {}
    scanning = True
    scan_count = 1
    print(
        "\nPress '%' to undo, '#' to finish, '&' to exit\nFor products-> enter 'CODE + 'space' + AMOUNT'"
    )
    while scanning:
        scanned_purchase = input(f"Scan {scan_count}: ")
        scan_count += 1
        scanned_items = scanned_purchase.split()
        amount = valid_amount(scanned_items)
        code = scanned_purchase.split()[0]

        if code == "#":
            scanning = False
        elif code == "%":
            undo_scan(store, receipt)
        elif code == "&":
            print("Signing off...")
            exit()
        else:
            code = check_if_product_exists(code, store, receipt, 0)
            product = store.get_product(code)
            while True:
                if amount <= store.inventory[code]:
                    store.remove_quantity(product, amount)
                    receipt.setdefault(code, 0)
                    receipt[code] += amount
                    break
                else:
                    print(f"Only {store.inventory[code]} in inventory:")
                    amount = amount_to_int(
                        ""
                    )  # empty string input since we want the exception to be called
    print_receipt(store, receipt)


def valid_amount(usr_input):
    """Chooses amount based on input, if no amount is written it is 1"""
    if len(usr_input) >= 2:
        amount = usr_input[1]
        amount = amount_to_int(amount)
    else:
        amount = 1
    return amount


def amount_to_int(amount):
    """Converts the amount to an integer"""
    while True:
        try:
            amount = int(amount)
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
        f"How many to undo - {store.product_catalogue[product_to_undo].name}"
    )
    amount_to_undo = amount_to_int(amount_to_undo)
    receipt[product_to_undo] -= amount_to_undo


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
