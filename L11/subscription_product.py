from product import Product
from supplier import Supplier

class SubscriptionProduct(Product):
    def __init__(self,product_id:str, name:str, price:float, stock:int,supplier:Supplier, duration:int) -> None:
        super().__init__(product_id,name,price,stock,supplier)
        self.__duration: int = duration

    def display_information(self) -> None:
        super().display_information()
        print(f"Duration: {self.__duration} months")
        
    @property
    def duration(self) -> int:
        """property for subscription duration"""
        return self.__duration

    def get_fulfilment_info(self) -> str:
        return "This product is a subscription"
