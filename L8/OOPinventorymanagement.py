import json
from pathlib import Path

class Product:

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

    def init(self, inventory, file_handler):
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
    
def add_product():
    print(f"Add new product") 
    product_id = input("Enter product ID: ").strip() # input

    # if input matches an existing product ID in the inventory
    # for each product in the inventory, check if the product ID matches the input
    if any(product_id == product["ID"] 
           for product in load_inventory()):
        print("Product ID already exists.") 
        return
    
    # if the product ID does not exist in the inventory, proceed to add the new product
    product_name = input("Enter product name: ").strip()

    # guardrail: ensure that the product price is a valid float and the stock quantity is a valid integer
    try:
        product_price = float(input("Enter product price: ").strip())
    except ValueError:
        print("Invalid product price.")
        return None
    #guardrail: ensure that the product price is a valid float and the stock quantity is a valid integer
    try:
        product_quantity = int(input("Enter stock quantity: ").strip())
    except ValueError:
        print("Invalid stock quantity.")
        return None
    
    inventory = load_inventory()

    # append the new product as a dictionary to the inventory list
    inventory.append(
        {
            "ID": product_id,
            "Name": product_name,
            "Price": product_price,
            "Stock": product_quantity,
        }
    )
    save_inventory(inventory)
    print("Product added successfully!")



def search_product():
    print("Search for a product")
    product_id = input("Enter product ID: ").strip()
    inventory = load_inventory()

    # REPLACED NEXT(): Loop through inventory to find the matching ID
    product = None
    for item in inventory:
        if item["ID"] == product_id:
            product = item
            break  # Stops scanning immediately once a match is found

    if product is None:
        print("Product not found.")
        return

    print("Product Found:")
    print(f"ID: {product['ID']}")
    print(f"Name: {product['Name']}")
    print(f"Price: ${product['Price']:.2f}")
    print(f"Stock: {product['Stock']}")

def display_all():
  
    print("Current Inventory:")
    print("--------------------")
    inventory = load_inventory()  # This returns a list of dictionaries

    # Loop through the list of product dictionaries
    if not inventory:
        print("Inventory is empty.")
        return
    else:
        for product in inventory:
            print(
                f"ID: {product['ID']} | "
                f"Name: {product['Name']} | "
                f"Price: ${product['Price']:.2f} | "
                f"Stock: {product['Stock']}"
            )

    print("--------------------")

def get_valid_input():
    

    try:
        option = int(input("\nEnter option (1-6): ").strip())
    except ValueError:
        print("Please enter a number from 1 to 6.")
        return None

    if option == 1:
        inventory.display_all()
        if not inventory.display_all():
            print("Inventory is empty.")
            return None
        for product in inventory.display_all():
            product.display_information()
            
    elif option == 2:
        print(f"Add new product") 
        product_id = input("Enter product ID: ").strip()
        product_name = input("Enter product name: ").strip()
        product_price = float(input("Enter product price: ").strip())
        product_stock = int(input("Enter product stock: ").strip())
        new_product = Product(product_id, product_name, product_price, product_stock)
        inventory.add_product(new_product)

    elif option == 3:
        print(f"Update product stock")
        product_id = input("Enter product ID: ").strip()

        product = inventory.search_product(product_id)

        if product is None:
            print("Product not found.")
            return None
        
        print(f"Name: {product.get_name()}")
        print(f"Current Stock: {product.get_stock()}")

        try:
            new_stock = int(input("Enter new stock: ").strip())
        except ValueError:
            print("Please enter a whole number.")
            return None

        result = product.update_stock(new_stock)
        if result is None:
            print("Stock updated successfully.")
        else:
            print("Product not found.")

    elif option == 4:
        print(f"Search product")
        search_id = input("Enter product ID to search: ").strip()
        product = inventory.search_product(search_id)
        if product:
            product.display_information()
        else:
            print("Product not found.")
    elif option == 5:
        print("Exiting the program.")
        return "quit"
    else:
        print("Invalid option. Please try again.")
        return None
    
while True:
    option = get_valid_input()
    if option == "quit":
        break

    if option is None:
        continue 
    elif option == 5:
        save_inventory(load_inventory())
        if inventory.add_product(product):
            print("Product added successfully!")
        else:
            print("Product ID already exists.")
    elif option == 6:
        save_inventory(load_inventory())
        print("Saving inventory before exit")
        print("Inventory saved successfully.")
        return "quit"


def load_inventory():
    try:
        with open(INVENTORY_FILE, "r") as file:
            inventory = json.load(file)
    except FileNotFoundError:
        print(f"{INVENTORY_FILE} not found. Starting with the default inventory.")
        return [product.copy() for product in DEFAULT_INVENTORY.values()]

    existing_ids = {product["ID"] for product in inventory}

    inventory.extend(
        product.copy()
        for product_id, product in DEFAULT_INVENTORY.items()
        if product_id not in existing_ids
    )
    return inventory

def save_inventory(products):
    # ✅ Fix: Skip the loop entirely and dump the incoming dictionary list directly
    with open(INVENTORY_FILE, "w") as file:
        json.dump(products, file, indent=4)
        #json dump is used to write the list of dictionaries to the file in JSON format
        # the format is (variable to write, file object, indent level)
        
    return products



