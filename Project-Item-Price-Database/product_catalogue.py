class Product_Catalogue:
    """Catalogue of all products"""

    def __init__(self):
        """Creates an instance of the product catalogue"""
        self.inventory = {}
        self.product_info = {}

    def add_product(self, product, quantity):
        """Adds a product from database to catalogue"""
        self.inventory[product.code] = int(quantity)
        self.product_info[product.code] = product
    
    def remove_quantity(self, product, purchased_quantity):
        self.inventory[product.code] -= purchased_quantity

    def get_product(self, code):
        return self.product_info.get(code)

    # def print_receipt(self, receipt):
    #     total_amount = 0
    #     total_sum = 0

    #     # Display the receipt
    #     print("\nPurchase Accepted!\nReceipt:")
    #     print("{:<10} {:<5} {:<10} {:<10}".format("Product", "Amount", "Price", "Total"))
    #     print("-" * 40)

    #     for code in receipt.keys():
    #         product = self.get_product(code)
    #         row = f"{product.name}    {receipt[code]}     {product.price}     {round(receipt[code]*product.price, 2)}"
    #         total_amount += receipt[code]
    #         total_sum += round(receipt[code]*product.price, 2)
    #         print("{:<10} {:<5} {:<10} {:<10}".format(*row.split()))

    #     print("-" * 40)
    #     print("{:<10} {:<5} {:<10} {:<10}".format("Total", f"{total_amount}", "", f"{total_sum}"))

    # def scan_purchase(self):
    #     receipt = {}

    #     scanning = True
    #     scan_count = 1
    #     print("\nPress '%' to undo, '#' to finish\nEnter 'code+space+amount'")
    #     while scanning:
    #         scanned_purchase = input(f"Scan {scan_count}: ")
    #         scan_count += 1
    #         scanned_items = scanned_purchase.split()

    #         if len(scanned_items) >= 2:
    #             amount = scanned_items[1]
    #         else:
    #             amount = 1

    #         code = scanned_purchase.split()[0]

    #         if code == "#":
    #             scanning = False
    #         elif code in self.product_info:
    #             product = self.get_product(code)
    #             while True:
    #                 if int(amount) <= self.inventory[code]:
    #                     self.remove_quantity(product, int(amount))
    #                     receipt.setdefault(code, 0)
    #                     receipt[code] += int(amount)
    #                     break
    #                 else: 
    #                     print(f"Only {self.inventory[code]} in inventory:")
    #                     amount = input(f"Enter a valid amount: ")

    #     self.print_receipt(receipt)