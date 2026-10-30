import json
from abc import ABC, abstractmethod

class Product(ABC):
    @abstractmethod
    def get_fulfilment_info(self):
        """Return information necessary for fulfilling the product (e.g., shipping details or download link)"""
        pass
    
    def __init__(self, product_id, name, price, stock):
        self.__product_id = product_id # private attribute for product ID
        self.__name = name # private attribute for product name
        self.__price = price # private attribute for product price
        self.__stock = stock # private attribute for product stock

    def update_stock(self, new_stock):
        if new_stock < 0:
            return None
        
        self.__stock = new_stock

        return self.__stock
   
    def display_information(self):
        """display information about the product"""
        print(f"ID: {self.__product_id} | Name: {self.__name} | Price: ${self.__price:.2f} | Stock: {self.__stock}")
   
    def get_product_id(self):
        """getter for product ID"""
        return self.__product_id

    def get_name(self):
        """getter for product name"""
        return self.__name

    def get_price(self):
        """getter for product price"""
        return self.__price

    def get_stock(self):
        """getter for product stock"""
        return self.__stock

class PhysicalProduct(Product):
    def __init__(self, product_id, name, price, stock, weight):
        super().__init__(product_id, name, price, stock)# allows this subclass to initialize the attributes of the parent Product class
        self.__weight = weight  # private attribute for product weight

    def get_weight(self):
        """getter for product weight"""
        return self.__weight

    def display_information(self):
        """display information about the physical product"""
        super().display_information() #inherits display from Product class
        print(f"Weight: {self.__weight} kg")

    def get_fulfilment_info(self):
        return "This product requires physical shipping"
 
class DigitalProduct(Product):
    def __init__(self,product_id, name, price, stock , download_size):
        super().__init__(product_id, name, price, stock)
        self.__download_size = download_size

    def get_download_size(self):
        """getter for download size"""
        return self.__download_size

    def display_information(self):
        """display information about the digital product"""
        super().display_information() # inherits display from Product class
        print(f"Download Size: {self.__download_size} MB")

    def get_fulfilment_info(self):
        return "This product is available for is delivered digitally"



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

class MainProgram:

    def __init__(self, inventory, file_handler):
        self.__inventory = inventory
        self.__file_handler = file_handler

    def display_menu(self):
        print("--------------")
        print("Inventory Management System")
        print("--------------")
        print(f"MENU")
        print("1. Display All Products")
        print("2. Add Product")
        print("3. Update Stock")
        print("4. Search Product")
        print("5. Save inventory")
        print("6. Exit")
        print("--------------") 

    def get_user_input(self, prompt):
        return input(prompt).strip()
    
    def handle_option(self, option):
        if option == "1":
            print("Current Inventory")
            self.__inventory.display_all()

        elif option == "2":
            product_id = self.get_user_input("Enter product ID: ")
            name = self.get_user_input("Enter product name: ")
            try:
                price = float(self.get_user_input("Enter product price: "))
                stock = int(self.get_user_input("Enter product stock: "))
            except ValueError:
                print("Invalid price or stock.")
                return
            product = Product(product_id, name, price, stock)
            if self.__inventory.add_product(product):
                print("Product added successfully.")
            else:
                print("Product ID already exists.")

        elif option == "3":
            print("Update product stock")
            product_id = self.get_user_input("Enter product ID: ")

            product = self.__inventory.search_product(product_id)

            if product is None:
                print("Product not found.")
                return None

            print(f"Name: {product.get_name()}")
            print(f"Current Stock: {product.get_stock()}")

            try:
                new_stock = int(self.get_user_input("Enter new stock: "))
            except ValueError:
                print("Please enter a whole number.")
                return None

            result = product.update_stock(new_stock)
            if result is None:
                print("Stock quantity cannot be negative.")
            else:
                print("Stock updated successfully.")

        elif option == "4":
            product_id = self.get_user_input("Enter product ID to search: ")
            product = self.__inventory.search_product(product_id)
            if product:
                product.display_information()
            else:
                print("Product not found.")

        elif option == "5":
            self.__file_handler.save_inventory(self.__inventory)
            print("Inventory saved successfully.")

        elif option == "6":
            self.__file_handler.save_inventory(self.__inventory)
            print("Inventory saved successfully. Exiting the program.")
            return "quit"
        
        else:
            print("Invalid option.")

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

file_handler = FileHandler("inventory.json")
inventory = file_handler.load_inventory()
main_program = MainProgram(inventory, file_handler)

while True:
    main_program.display_menu()
    option = main_program.get_user_input("Enter option (1-6): ")
    if main_program.handle_option(option) == "quit":
        break
    



