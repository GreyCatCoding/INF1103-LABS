from orderline import OrderLine
from product import Product
from discount_strategy import DiscountStrategy
from no_discount import NoDiscount


class Order: 
    def __init__(self, order_id: str,discount: DiscountStrategy = None) -> None: 
        """Composition: an order is composed of multiple order lines"""
        self.order_id: str = order_id 
        self.order_lines: list[OrderLine] = [] 

        if discount is None:
            discount = NoDiscount()

        self.__discount: DiscountStrategy | None = discount
 
    def add_order_line(self, product: Product, quantity: int) -> None: 
        """Composition: the order creates and owns a new order line for this product and quantity."""
        order_line = OrderLine(product, quantity) 
        self.order_lines.append(order_line)

    def set_discount(self, discount: DiscountStrategy) -> None:
        """Set the discount strategy that will be applied to the order"""
        self.__discount = discount

    def calculate_total(self) -> float:
        total = 0.0
        for order_line in self.order_lines:
            total += order_line.calculate_subtotal()
        return self.__discount.apply(total)

