from orderline import OrderLine
from product import Product


class Order: 
    def __init__(self, order_id: str): 
        """Composition: an order is composed of multiple order lines"""
        self.order_id: str = order_id 
        self.order_lines: list[OrderLine] = [] 
 
    def add_order_line(self, product: Product, quantity: int) -> None: 
        order_line = OrderLine(product, quantity) 
        self.order_lines.append(order_line)