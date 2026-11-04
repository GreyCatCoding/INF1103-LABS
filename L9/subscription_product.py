from product import Product

class SubscriptionProduct(Product):
    def __init__(self,product_id, name, price, stock, duration):
        super().__init__(product_id,name,price,stock)
        self.__duration = duration

    def display_information(self):
        super().display_information()
        print(f"Duration: {self.__duration} months")

    def get_duration(self):
        return self.__duration

    def get_fulfilment_info(self):
        return "This product is a subscription"
