class Product_Catalogue:
    """Catalogue of all products"""

    def __init__(self):
        """Creates an instance of the product catalogue"""
        self.inventory = {}
        self.product_info = {}

    def add_product(self, product, quantity):
        """Adds a product to catalogue"""
        self.inventory[product.code] = quantity
        self.product_info[product.code] = product

    def remove_quantity(self, product, purchased_quantity):
        inventory_quantity = self.inventory[product.code]
        while True:
            if inventory_quantity >= purchased_quantity:
                inventory_quantity -= purchased_quantity
                return
            else:
                print(f"Invalid amount of {product.name}s, only {inventory_quantity} in inventory, try again.")

    def get_product(self, code):
        for product in self.product_info:
            if product.code == code:
                return product

    def scan_purchase(self):
        receipt = {}
        total_amount = 0
        total_sum = 0

        while True:
            scanned_purchase = input()
            code = scanned_purchase.split()[0]
            amount = scanned_purchase.split()[1]

            if scanned_purchase == "#":
                return
            
            elif isinstance(code, int) and isinstance(amount, int):
                self.remove_quantity(self.get_product(code), amount)
                receipt[code] += amount

            elif isinstance(code, int):
                self.remove_quantity(self.get_product(code), 1)
                receipt[code] += 1
            break

        header = "Product    Amount    Price    Total"
        print("{:<10} {:<5} {:<10} {:<10}".format("Product", "Amount", "Price", "Total"))
        print("-" * 40)
        print("{:<10} {:<5} {:<10} {:<10}".format(*header.split()))

        for code in receipt:
            product = self.get_product(code)
            row = f"{product.name}    {receipt[code]}     {product.price}     {receipt[code]*product.price}"
            total_amount += receipt[code]
            total_sum += receipt[code]*product.price
            print("{:<10} {:<5} {:<10} {:<10}".format(*row.split()))

        print("-" * 40)
        print("{:<10} {:<5} {:<10} {:<10}".format("Total", f"{total_amount}", "", f"{total_sum}"))
