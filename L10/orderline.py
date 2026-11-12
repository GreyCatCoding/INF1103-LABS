from product import Product

"""association: an order line is associated with a single product"""
class OrderLine:
    def __init__(self, product: Product, quantity: int) -> None:
        self.__product = product
        self.__quantity = quantity

    @property
    def product(self) -> Product:
        return self.__product

    @property
    def quantity(self) -> int:
        return self.__quantity

    def calculate_subtotal(self) -> float: 
        return self.product.price * self.quantity 