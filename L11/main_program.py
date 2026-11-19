from inventory import Inventory
from product_factory import ProductFactory
from supplier import Supplier



class MainProgram:

    def __init__(self, inventory: Inventory) -> None:
        self.__inventory: Inventory = inventory 

    def display_menu(self) -> None:
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

    def get_user_input(self, prompt: str) -> str:
        return input(prompt).strip()

    def get_positive_float(self, prompt: str) -> float:
        while True:
            try:
                value = float(self.get_user_input(prompt))
                if value <= 0:
                    print("Please enter a value greater than zero.")
                    continue
                return value
            except ValueError:
                print(f"Invalid input. Please enter a valid number.")

    def get_non_negative_int(self, prompt: str) -> int:
        while True:
            try:
                value = int(self.get_user_input(prompt))
                if value < 0:
                    print("Please enter a whole number of 0 or more.")
                    continue
                return value
            except ValueError:
                print(f"Invalid input. Please enter a valid number.")

    def handle_option(self, option: str) -> str | None:
        if option == "1":
            print("Current Inventory")
            self.__inventory.display_all()


        elif option == "2":

            product_id = self.get_user_input("Enter product ID: ")
            name = self.get_user_input("Enter product name: ")
           
            price = self.get_positive_float("Enter product price: ")
            stock = self.get_non_negative_int("Enter product stock: ")
            
            product_type = self.get_user_input("Enter product type (p for physical, d for digital , s for subscription-based): ").lower()

            supplier_id = self.get_user_input("Enter supplier ID: ")
            supplier_name = self.get_user_input("Enter supplier name: ")
            supplier_email = self.get_user_input("Enter supplier email: ")

            
            supplier = Supplier(supplier_id, supplier_name, supplier_email)

            if product_type == "p":
                try:
                   extra_attribute = float(self.get_user_input("Enter Weight of product: "))
                except ValueError:
                    print("Invalid weight")
                    return
                
                

            elif product_type == "d":
                try:
                    extra_attribute = float(self.get_user_input("Enter downloadable size : "))
                except ValueError:
                    print("Invalid downloadable size")
                    return

               
            elif product_type == "s":
                try:
                    extra_attribute = int(self.get_user_input("Enter duration of subscription: "))
                except ValueError:
                    print("Invalid duration")
                    return

              
            else:
                print("Invalid product type.")
                return

            product = ProductFactory.create(product_type, product_id, name, price, stock, supplier, extra_attribute)

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

            print(f"Name: {product.name}")
            print(f"Current Stock: {product.stock}")

            try:
                new_stock = int(self.get_user_input("Enter new stock: "))
            except ValueError:
                print("Please enter a whole number.")
                return None

            try:
                product.update_stock(new_stock) # value error is raised if new stock is negative
            except ValueError as error: # handle the case when new stock is negative
                print(error)
            else:
                print("Stock updated successfully.")


        elif option == "4":
            product_id = self.get_user_input("Enter product ID to search: ")
            product = self.__inventory.search_product(product_id)
            if product:
                product.display_information()
            else:
                print("Product not found.")

            remove_option = self.get_user_input("Do you want to remove this product? (y/n): ").lower()
            
            try:
                if remove_option == "y":
                    if self.__inventory.remove_product(product_id):
                        print("Product removed successfully.")
                else:
                    print("selection cancelled.")

            except Exception as e:
                print(f"An error occurred: {e}")

        elif option == "5":
            self.__inventory.save_inventory()
            print("Inventory saved successfully.")

        elif option == "6":
            self.__inventory.save_inventory()
            print("Inventory saved successfully. Exiting the program.")
            return "quit"

        else:
            print("Invalid option.")
