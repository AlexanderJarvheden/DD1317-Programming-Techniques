class Store:
    """The store with inventory and products"""

    def __init__(self):
        """Creates an instance of the product store"""
        self.inventory = {}
        self.product_catalogue = {}

    def add_product(self, product, quantity):
        """Adds a product from database to store"""
        self.inventory[product.code] = int(quantity)
        self.product_catalogue[product.code] = product
    
    def remove_quantity(self, product, purchased_quantity):
        """Removes purchased amount from inventory"""
        self.inventory[product.code] -= purchased_quantity

    def get_product(self, code):
        """Gets the product item from the product catalogue"""
        return self.product_catalogue.get(code)