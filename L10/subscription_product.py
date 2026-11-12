from product import Product
from supplier import Supplier

class SubscriptionProduct(Product):
    def __init__(self,product_id:str, name:str, price:float, stock:int,supplier:Supplier, duration:int):
        super().__init__(product_id,name,price,stock,supplier)
        self.__duration = duration

    def display_information(self):
        super().display_information()
        print(f"Duration: {self.__duration} months")
        
    @property
    def duration(self):
        """property for subscription duration"""
        return self.__duration

    def get_fulfilment_info(self):
        return "This product is a subscription"
