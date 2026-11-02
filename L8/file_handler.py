import json

from product import Product
from inventory import Inventory

class FileHandler:
    """Loads the inventory from a JSON file and turns it into Product objects."""

    def __init__(self, file_path):
        self.__file_path = file_path  # private attribute for the JSON file's path

    def load_inventory(self):
        """Read the JSON file and return an Inventory filled with Product objects."""
        inventory = Inventory()

        try:
            with open(self.__file_path, "r") as file:
                product_list = json.load(file)
        except FileNotFoundError:
            print(f"{self.__file_path} not found. Starting with an empty inventory.")
            return inventory
        except json.JSONDecodeError:
            print(f"{self.__file_path} is not valid JSON. Starting with an empty inventory.")
            return inventory

        for item in product_list:
            product = Product(item["ID"], item["Name"], item["Price"], item["Stock"])
            inventory.add_product(product)

        return inventory

    def save_inventory(self, inventory):
        """Save the Inventory object to the JSON file."""
        product_list = []
        for product in inventory.get_all_products():
            product_list.append({
                "ID": product.get_product_id(),
                "Name": product.get_name(),
                "Price": product.get_price(),
                "Stock": product.get_stock()
            })

        with open(self.__file_path, "w") as file:
            json.dump(product_list, file, indent=4)
