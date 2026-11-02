class Inventory:
    """Inventory doesn't create products itself. It receives finished Product objects and manages them."""
    def __init__(self):
        self.__products = []  # private attribute to store the list of products

    def add_product(self, new_product):
        """Add a product if its ID is not already in the inventory. Returns True if added, False if duplicate."""
        for product in self.__products:
            if product.get_product_id() == new_product.get_product_id():
                return False

        self.__products.append(new_product)
        return True

    def search_product(self, product_id):
        """Search for a product by its ID. Returns the Product object if found, None otherwise."""
        for product in self.__products:
            if product.get_product_id() == product_id:
                return product
        return None

    def display_all(self):
        """Display information for all products in the inventory."""
        if not self.__products:
            print("Inventory is empty.")
            return

        for product in self.__products:
            product.display_information()

    def get_all_products(self):
        """Getter for all products in the inventory"""
        return self.__products
