def print_receipt(catalogue, receipt):
    total_amount = 0
    total_sum = 0
    # Display the receipt
    print("\nPurchase Accepted!\nReceipt:")
    print("{:<10} {:<5} {:<10} {:<10}".format("Product", "Amount", "Price", "Total"))
    print("-" * 40)
    for code in receipt.keys():
        product = catalogue.get_product(code)
        row = f"{product.name}    {receipt[code]}     {product.price}     {round(receipt[code]*product.price, 2)}"
        total_amount += receipt[code]
        total_sum += round(receipt[code]*product.price, 2)
        print("{:<10} {:<5} {:<10} {:<10}".format(*row.split()))
    print("-" * 40)
    print("{:<10} {:<5} {:<10} {:<10}".format("Total", f"{total_amount}", "", f"{total_sum}"))
    
def scan_purchase(catalogue):
    receipt = {}
    scanning = True
    scan_count = 1
    print("\nPress '%' to undo, '#' to finish\nFor products enter 'CODE + 'space' + AMOUNT'")
    while scanning:
        scanned_purchase = input(f"Scan {scan_count}: ")
        scan_count += 1
        scanned_items = scanned_purchase.split()
        if len(scanned_items) >= 2:
            amount = scanned_items[1]
        else:
            amount = 1
        code = scanned_purchase.split()[0]
        if code == "#":
            scanning = False
        elif code == "%":
            undo_scan(catalogue, receipt)
        elif code in catalogue.product_info:
            product = catalogue.get_product(code)
            while True:
                if int(amount) <= catalogue.inventory[code]:
                    catalogue.remove_quantity(product, int(amount))
                    receipt.setdefault(code, 0)
                    receipt[code] += int(amount)
                    break
                else: 
                    print(f"Only {catalogue.inventory[code]} in inventory:")
                    amount = input(f"Enter a valid amount: ")
    print_receipt(catalogue, receipt)

def undo_scan(catalogue, receipt):
    product_to_undo = input("Which product do you want to undo?\nEnter the product code: ")
    amount_to_undo = input(f"How many to undo - {catalogue.product_info[product_to_undo].name}")
    receipt[product_to_undo] -= int(amount_to_undo)