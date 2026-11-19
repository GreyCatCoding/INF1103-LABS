from supplier import Supplier
from physical_product import PhysicalProduct
from digital_product import DigitalProduct
from order import Order


def make_products() -> tuple[PhysicalProduct, DigitalProduct]:
    supplier = Supplier("S001", "Supplier One", "contact@supplier.com")
    lamp = PhysicalProduct("P001", "Desk Lamp", 10.0, 50, supplier, 1.2)
    ebook = DigitalProduct("D001", "E-book", 20.0, 100, supplier, 5.0)
    return lamp, ebook


def test_order_creates_its_own_order_lines_and_total():
    lamp, ebook = make_products()
    order = Order("O001")

    # The Order is given a product and quantity - it creates the OrderLine itself
    order.add_order_line(lamp, 2)
    order.add_order_line(ebook, 3)

    assert len(order.order_lines) == 2
    for order_line in order.order_lines:
        print(f"{order_line.product.name} x {order_line.quantity} = ${order_line.calculate_subtotal():.2f}")

    # 2 x 10.0 + 3 x 20.0 = 80.0
    assert order.calculate_total() == 80.0


def test_same_product_in_two_orders():
    lamp, _ = make_products()
    order_one = Order("O001")
    order_two = Order("O002")

    order_one.add_order_line(lamp, 1)
    order_two.add_order_line(lamp, 5)

    line_in_order_one = order_one.order_lines[0]
    line_in_order_two = order_two.order_lines[0]

    # Two DIFFERENT OrderLine objects - each Order created and owns its own
    assert line_in_order_one is not line_in_order_two

    # ...but both point at the ONE shared Product (OrderLine -> Product is association)
    assert line_in_order_one.product is lamp
    assert line_in_order_two.product is lamp

    # Each line keeps its own quantity
    assert line_in_order_one.quantity == 1
    assert line_in_order_two.quantity == 5


def test_removing_order_removes_its_lines_but_not_products():
    lamp, ebook = make_products()
    order = Order("O001")
    order.add_order_line(lamp, 2)
    order.add_order_line(ebook, 1)

    # Nothing outside the Order holds the OrderLines, so removing the Order
    # leaves them unreachable - they go with it (composition)
    del order

    # The Products were created outside the Order, so they are unaffected
    assert lamp.name == "Desk Lamp"
    assert ebook.price == 20.0
