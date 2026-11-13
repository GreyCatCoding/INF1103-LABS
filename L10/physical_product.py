from product import Product
from can_be_shipped import CanBeShipped
from supplier import Supplier

class PhysicalProduct(Product, CanBeShipped):

    BASE_SHIPPING_COST = 5.0  # base shipping cost for physical products
    RATE_PER_KG = 2.0  # shipping rate per kilogram

    def __init__(self, product_id:str, name:str, price:float, stock:int, supplier: Supplier ,weight:float) -> None:
        super().__init__(product_id, name, price, stock, supplier)# allows this subclass to initialize the attributes of the parent Product class
        self.__weight: float = weight  # private attribute for product weight

    def display_information(self) -> None:
        """display information about the physical product"""
        super().display_information() #inherits display from Product class
        print(f"Weight: {self.__weight} kg")

    @property  
    def weight(self) -> float:
        """getter for product weight"""
        return self.__weight

    def get_fulfilment_info(self) -> str:
        return "This product requires physical shipping"

    def calculate_shipping_cost(self) -> float:
        return self.BASE_SHIPPING_COST + self.RATE_PER_KG * self.__weight
