from file_handler import FileHandler
from main_program import MainProgram

if __name__ == "__main__":
    file_handler = FileHandler("inventory.json")
    inventory = file_handler.load_inventory()
    main_program = MainProgram(inventory, file_handler)

    while True:
        main_program.display_menu()
        option = main_program.get_user_input("Enter option (1-6): ")
        if main_program.handle_option(option) == "quit":
            break
