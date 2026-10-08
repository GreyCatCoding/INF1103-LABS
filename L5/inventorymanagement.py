import json
from pathlib import Path

INVENTORY_FILE = Path(__file__).with_name("inventory.json")

DEFAULT_INVENTORY = {
    "P001": {"ID": "P001", "Name": "Laptop", "Price": 1200.00, "Stock": 15},
    "P002": {"ID": "P002", "Name": "Mouse", "Price": 25.50, "Stock": 40},
    "P003": {"ID": "P003", "Name": "Keyboard", "Price": 45.00, "Stock": 25},
}

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


    

def update_stock():
    print("Update stock for a product")
    inventory = load_inventory()
    product_id = input("Enter product ID: ").strip()

    product = None
    for item in inventory:
        if item["ID"] == product_id:
            product = item
            break

    if product is None:
        print("Product not found.")
        return

    print("Product Found:")
    print(f"Name: {product['Name']}")
    print(f"Current Stock: {product['Stock']}")

    try:
        new_quantity = int(input("Enter new stock quantity: ").strip())
    except ValueError:
        print("Please enter a whole number.")
        return

    if new_quantity < 0:
        print("Stock quantity cannot be negative.")
        return

    product["Stock"] = new_quantity

    save_inventory(inventory)
    print("Stock updated successfully!")
    


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
    
    print("--------------")
    print("Inventory Management System")
    print("--------------")
    print(f"MENU")
    print("1. Display All Products")
    print("2. Add Product")
    print("3. Update Stock")
    print("4. Search Product")
    print("5. Save Inventory")
    print("6. Exit")
    print("--------------") 

    try:
        option = int(input("\nEnter option (1-6): ").strip())
    except ValueError:
        print("Please enter a number from 1 to 6.")
        return None

    if option == 1:
        display_all()
    elif option == 2:
        add_product()
    elif option == 3:
        update_stock()
    elif option == 4:
        search_product()
    elif option == 5:
        save_inventory(load_inventory())
        print("Inventory saved successfully.")
    elif option == 6:
        save_inventory(load_inventory())
        print("Saving inventory before exit")
        print("Inventory saved successfully.")
        return "quit"
    else:
        print("Invalid option. Please try again.")
        return None

    return option


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


while True:
    option = get_valid_input()
    if option == "quit":
        break

    if option is None:
        continue 

