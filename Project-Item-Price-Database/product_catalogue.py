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