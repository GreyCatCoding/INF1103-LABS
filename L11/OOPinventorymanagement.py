from inventory import Inventory
from main_program import MainProgram

if __name__ == "__main__":

    inventory = Inventory("inventory.json")
    inventory.load_inventory()
    main_program = MainProgram(inventory)

    while True:
        main_program.display_menu()
        option = main_program.get_user_input("Enter option (1-6): ")
        if main_program.handle_option(option) == "quit":
            break
