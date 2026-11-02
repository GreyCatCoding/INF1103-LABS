from product import Product

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
