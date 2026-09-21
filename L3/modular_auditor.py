inventory = 0
deliveries = 0
total_tax = 0
failed_attempts = 0
#declaring variables  

def get_valid_input():

    qty = input("Enter stock quantity or type 'quit' to quit: ").strip()

    if qty.lower() == "quit":
        return "quit"

    if qty.startswith("-"):
        print("Invalid input. Please enter a positive quantity or type 'quit' to exit.")
        return None

    elif qty.isdigit() and int(qty) > 0:
        print(f"Quantity recorded: {qty}")
        return int(qty)
    else:
        print("Invalid input. Please enter an integer or type 'quit' to exit.")
        return None

    
        
def process_delivery(current_total, new_value):
    processed = current_total + new_value
    return processed

def calculate_tax(amount):
    tax = amount * 0.10
    return tax

def generate_report(total_units, failed_attempts, total_tax): 
    print(f"Final Report:")
    print(f"Total inventory: {total_units}")
    print(f"Failed attempts: {failed_attempts}")
    print(f"Total tax collected: ${total_tax:.2f}")


while True:
    qty = get_valid_input()

    if qty == "quit":
        break

    if qty is None:
        failed_attempts += 1
        continue

    inventory = process_delivery(inventory, qty) # current_total is inventory, new_value is qty
    total_tax += calculate_tax(qty)
    deliveries += 1 #deliveries counter incremented for each successful delivery

generate_report(inventory, failed_attempts, total_tax)