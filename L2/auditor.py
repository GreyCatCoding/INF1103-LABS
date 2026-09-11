inventory = 0

while True:
    qty = input("Enter stock quantity or type 'quit' to quit: ")
    if qty.lower() == "quit":
        break

    if qty.startswith("-"):
        print("Invalid input. Please enter a positive quantity or type 'quit' to exit.")
        continue

    if qty.isdigit():
        inventory += int(qty)
        print(f"Quantity recorded: {int(qty)}")
    else:
        print("Invalid input. Please enter an integer or type 'quit' to exit.")

    if inventory > 500:
        print("Inventory has exceeded 500 units")
        break

print(f"Total inventory: {inventory}")


