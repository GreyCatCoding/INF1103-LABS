from physical_product import PhysicalProduct
from digital_product import DigitalProduct
from subscription_product import SubscriptionProduct
from supplier import Supplier



class MainProgram:

    def __init__(self, inventory: object):
        self.__inventory = inventory 

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

    def get_user_input(self, prompt: str):
        return input(prompt).strip()

    def handle_option(self, option: str):
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
            product_type = self.get_user_input("Enter product type (p for physical, d for digital , s for subscription-based): ").lower()

            
            supplier_id = self.get_user_input("Enter supplier ID: ")
            supplier_name = self.get_user_input("Enter supplier name: ")
            supplier_email = self.get_user_input("Enter supplier email: ")
            supplier = Supplier(supplier_id, supplier_name, supplier_email)


            if product_type == "p":
                try:
                    weight = float(self.get_user_input("Enter Weight of product: "))
                except ValueError:
                    print("Invalid weight")
                    return
                
                product = PhysicalProduct(product_id, name, price, stock, supplier, weight)

            elif product_type == "d":
                try:
                    download_size = float(self.get_user_input("Enter downloadable size : "))
                except ValueError:
                    print("Invalid downloadable size")
                    return

                product = DigitalProduct(product_id, name, price, stock, supplier, download_size)
            elif product_type == "s":
                try:
                    duration = int(self.get_user_input("Enter duration of subscription: "))
                except ValueError:
                    print("Invalid duration")
                    return

                product = SubscriptionProduct(product_id, name, price, stock, supplier, duration)
            else:
                print("Invalid product type.")
                return

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
            self.__inventory.save_inventory()
            print("Inventory saved successfully.")

        elif option == "6":
            self.__inventory.save_inventory()
            print("Inventory saved successfully. Exiting the program.")
            return "quit"

        else:
            print("Invalid option.")
