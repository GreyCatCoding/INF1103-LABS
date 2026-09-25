
# 1 Persistence: At the start of the program, read the information previously saved in the inventory file.
#  If the inventory file does not exist, start with an empty inventory and continue running without producing an error.
# 2. History Tracking: Use a Python list (array) to store every valid transaction amount entered.
# 3. Write-Back: When the user types quit, save the final total and the transaction history list to inventory.txt.
# 4. Modularity: Maintain your functional design. Create a load_inventory() and save_inventory() function.
def load_inventory():
    orders = []  
    transaction_history = []
    total_inventory = 0
    next_order_id = 1001
    print("Current Orders:")

    try: 
        with open("inventory.txt","r") as file:
            for line in file:

                order_id , product_name, qty = line.strip().split(",") #stirp no spaces then split by comma

                order_id = int(order_id.strip()) 
                product_name = product_name.strip()
                qty = int(qty.strip())

                orders.append((order_id, product_name, qty))

                transaction_history.append(qty) 

                total_inventory += qty
                
                print(f"{order_id},{product_name},{qty}")

                next_order_id = order_id + 1 #find the first available ID after previous runs

               
    except FileNotFoundError:
        print("No previous inventory found. Starting with an empty inventory.")

    return orders, transaction_history, total_inventory, next_order_id

def save_inventory(orders):
    with open("inventory.txt", "w") as file:
        for order_id,product_name,quantity in orders:
            file.write(f"{order_id},{product_name},{quantity}\n")
        


def get_valid_input():

    product_name = input("\nEnter Product Name or type 'quit' to exit: ").strip()

    # Let the user quit before being asked for a quantity.
    if product_name.lower() == "quit":
        print("\nOrder successfully saved to orders.txt.")
        return "quit"

    if product_name.isdigit() == "":
        print("Invalid product name.")
        return None

    quantity_input = input("Enter Quantity: ").strip()

    if quantity_input.lower() == "quit":
        return "quit"

    if not quantity_input.isdigit() or int(quantity_input) <= 0:
        print("Invalid quantity. Enter a positive whole number.")
        return None

    quantity = int(quantity_input)

    return product_name, quantity


orders, transaction_history, inventory, next_order_id = load_inventory() 

while True:
    

    user_input = get_valid_input() # stores product name and quantity

    if user_input == "quit":
        save_inventory(orders)
        break

    if user_input is None:
        continue # txt file will not be saved if the user quits before entering a valid order.

    # Only runs for valid input.
    product_name, quantity = user_input 

    orders.append((next_order_id, product_name, quantity))
    transaction_history.append(quantity)

    print("\nNew Order Added:")
    print(f"{next_order_id},{product_name},{quantity}\n")

    next_order_id += 1 
    #main loop:move to the next ID after each newly entered order