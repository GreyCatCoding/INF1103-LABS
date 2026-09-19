#Smart Vending Machine
# • Rules:
# • Create a function called dispense_drink() that
# accepts a drink name and displays the correct message.
# • If the drink is "Coke" → Print "Dispensing Coke“
# • If the drink is "Water" → Print "Dispensing Water“
# • If the drink is "Juice" → Print "Dispensing Juice“
# • Otherwise → Print "Drink Not Available“
# • Challenge: Modify the function so that it also keeps track of the number of drinks
# dispensed


def dispense_drink(drink_name,drink_count):
    if drink_name == "Coke":
        print("Dispensing Coke")
    elif drink_name == "Water":
        print("Dispensing Water")
    elif drink_name == "Juice":
        print("Dispensing Juice")
    else:
        print("Drink Not Available")

    drink_count += 1
    return drink_count


drink_count = 0

while True:
    drink = input("Enter a drink name (Coke, Water, Juice) or type 'quit' to exit: ")
    if drink.lower() == "quit":
        break
    
    if drink.lower() not in ["coke", "water", "juice"]: #not in is used to check if the input is not in the list of valid drinks
        print("Invalid drink name. Please enter 'Coke', 'Water', or 'Juice'.")
        continue

    drink_count = dispense_drink(drink, drink_count)


print(f"Total drinks dispensed: {drink_count} drinks")