import pytest

from supplier import Supplier
from physical_product import PhysicalProduct
from orderline import OrderLine
from order import Order


def make_supplier() -> Supplier:
    return Supplier("S001", "Lamp Co", "sales@lampco.example")


@pytest.mark.parametrize("price", [0, -1.0])
def test_product_rejects_price_of_zero_or_less(price):
    with pytest.raises(ValueError):
        PhysicalProduct("P001", "Desk Lamp", price, 10, make_supplier(), 1.2)


def test_product_rejects_negative_stock():
    with pytest.raises(ValueError):
        PhysicalProduct("P001", "Desk Lamp", 25.0, -1, make_supplier(), 1.2)


def test_product_allows_zero_stock():
    lamp = PhysicalProduct("P001", "Desk Lamp", 25.0, 0, make_supplier(), 1.2)
    assert lamp.stock == 0


def test_update_stock_rejects_negative_and_keeps_old_stock():
    lamp = PhysicalProduct("P001", "Desk Lamp", 25.0, 5, make_supplier(), 1.2)
    with pytest.raises(ValueError):
        lamp.update_stock(-5)
    assert lamp.stock == 5


@pytest.mark.parametrize("quantity", [0, -3])
def test_order_line_rejects_quantity_of_zero_or_less(quantity):
    lamp = PhysicalProduct("P001", "Desk Lamp", 25.0, 5, make_supplier(), 1.2)
    with pytest.raises(ValueError):
        OrderLine(lamp, quantity)


def test_invalid_order_line_is_not_added_to_order():
    lamp = PhysicalProduct("P001", "Desk Lamp", 25.0, 5, make_supplier(), 1.2)
    order = Order("O001")
    with pytest.raises(ValueError):
        order.add_order_line(lamp, 0)
    assert len(order.order_lines) == 0
