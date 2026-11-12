from abc import ABC, abstractmethod
from supplier import Supplier

class Product(ABC):
    @abstractmethod
    def get_fulfilment_info(self) -> str:
        """Return information necessary for fulfilling the product (e.g., shipping details or download link)"""
        pass

    def __init__(self, product_id:str, name:str, price:float, stock:int, supplier:Supplier) -> None:
        self.__product_id = product_id # private attribute for product ID
        self.__name = name # private attribute for product name
        self.__price = price # private attribute for product price
        self.__stock = stock # private attribute for product stock
        self.__supplier = supplier # private attribute for product supplier

    def update_stock(self, new_stock:int) -> int | None:
        if new_stock < 0:
            return None

        self.__stock = new_stock

        return self.__stock

    def display_information(self) -> None:
        """display information about the product"""
        print(f"ID: {self.__product_id} | Name: {self.__name} | Price: ${self.__price:.2f} | Stock: {self.__stock}")

    @property
    def product_id(self) -> str:
        """property for product ID"""
        return self.__product_id
    @property
    def name(self) -> str:
        """property for product name"""
        return self.__name
    @property
    def price(self) -> float:
        """property for product price"""
        return self.__price
    @property
    def stock(self) -> int:
        """property for product stock"""
        return self.__stock
    @property
    def supplier(self) -> Supplier:
        """property for product supplier"""
        return self.__supplier

