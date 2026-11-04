from product import Product
from can_be_shipped import CanBeShipped

class PhysicalProduct(Product, CanBeShipped):

    BASE_SHIPPING_COST = 5.0  # base shipping cost for physical products
    RATE_PER_KG = 2.0  # shipping rate per kilogram

    def __init__(self, product_id, name, price, stock, weight):
        super().__init__(product_id, name, price, stock)# allows this subclass to initialize the attributes of the parent Product class
        self.__weight = weight  # private attribute for product weight

    def display_information(self):
        """display information about the physical product"""
        super().display_information() #inherits display from Product class
        print(f"Weight: {self.__weight} kg")

    def get_weight(self):
        """getter for product weight"""
        return self.__weight

    def get_fulfilment_info(self):
        return "This product requires physical shipping"

    def calculate_shipping_cost(self):
        return self.BASE_SHIPPING_COST + self.RATE_PER_KG * self.__weight
