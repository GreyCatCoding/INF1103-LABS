import json

from physical_product import PhysicalProduct
from digital_product import DigitalProduct
from subscription_product import SubscriptionProduct
from product import Product



class Inventory:
    """Inventory doesn't create products itself. It receives finished Product objects and manages them."""
    def __init__(self,file_path:str = "inventory.json") -> None:
        self.__products : list[Product] = []  # private attribute to store the list of products
        self.__file_path = file_path

    def add_product(self, new_product:Product):
        """Add a product if its ID is not already in the inventory. Returns True if added, False if duplicate."""
        for product in self.__products:
            if product.product_id == new_product.product_id:
                return False

        self.__products.append(new_product)
        return True

    def search_product(self, product_id:str):
        """Search for a product by its ID. Returns the Product object if found, None otherwise."""
        for product in self.__products:
            if product.product_id == product_id:
                return product
        return None

    def display_all(self):
        """Display information for all products in the inventory."""
        if not self.__products:
            print("Inventory is empty.")
            return

        for product in self.__products:
            product.display_information()

    def load_inventory(self):
        """Fill this inventory with products read from the JSON file."""
        try:
            with open(self.__file_path, "r") as file:
                product_list = json.load(file)
        except FileNotFoundError:
            print(f"{self.__file_path} not found. Starting with an empty inventory.")
            return
        except json.JSONDecodeError: 
            print(f"{self.__file_path} is not valid JSON. Starting with an empty inventory.")
            return

        

        for item in product_list:
            product_type = item.get("Type")

            if product_type == "p":
                product = PhysicalProduct(item["ID"], item["Name"], item["Price"], item["Stock"], item["Weight"])
            elif product_type == "d":
                product = DigitalProduct(item["ID"], item["Name"], item["Price"], item["Stock"], item["download_size"])
            elif product_type == "s":
                product = SubscriptionProduct(item["ID"], item["Name"], item["Price"], item["Stock"], item["duration"])
            else:
                print(f"Unknown product type: {product_type}")
                continue

            self.add_product(product)

    def save_inventory(self):
        """Write this inventory's products to the JSON file."""
        product_list = []
   
        for product in self.__products:
            product_data = {
                "ID": product.product_id,
                "Name": product.name,
                "Price": product.price,
                "Stock": product.stock,
                # retrieve supplier information from product's supplier attribute
                "SupplierID": product.supplier.supplier_id,
                "SupplierName": product.supplier.name,
                "SupplierEmail": product.supplier.email,
            }
            if isinstance(product, PhysicalProduct):
                product_data["Type"] = "p"
                product_data["Weight"] = product.weight
            elif isinstance(product, DigitalProduct):
                product_data["Type"] = "d"
                product_data["download_size"] = product.download_size
            elif isinstance(product, SubscriptionProduct):
                product_data["Type"] = "s"
                product_data["duration"] = product.duration
            else:
                print(f"Unknown product type for product ID: {product.product_id}")
                continue

            product_list.append(product_data)

        with open(self.__file_path, "w") as file:
            json.dump(product_list, file, indent=4)

    
    # def get_all_products(self):
    #     """Getter for all products in the inventory"""
    #     return self.__products
