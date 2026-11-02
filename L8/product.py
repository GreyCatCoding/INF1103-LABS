class Product:

    def __init__(self, product_id, name, price, stock):
        self.__product_id = product_id # private attribute for product ID
        self.__name = name # private attribute for product name
        self.__price = price # private attribute for product price
        self.__stock = stock # private attribute for product stock

    def update_stock(self, new_stock):
        if new_stock < 0:
            return None

        self.__stock = new_stock

        return self.__stock

    def display_information(self):
        """display information about the product"""
        print(f"ID: {self.__product_id} | Name: {self.__name} | Price: ${self.__price:.2f} | Stock: {self.__stock}")

    def get_product_id(self):
        """getter for product ID"""
        return self.__product_id

    def get_name(self):
        """getter for product name"""
        return self.__name

    def get_price(self):
        """getter for product price"""
        return self.__price

    def get_stock(self):
        """getter for product stock"""
        return self.__stock
