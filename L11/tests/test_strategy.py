import inspect

import pytest

from supplier import Supplier
from physical_product import PhysicalProduct
from order import Order
from no_discount import NoDiscount
from percentage_discount import PercentageDiscount
from bulk_discount import BulkDiscount
from student_discount import StudentDiscount


def make_order_of_250(discount=None) -> Order:
    """10 desk lamps at 25.00 each, so the subtotal is 250."""
    supplier = Supplier("S001", "Lamp Co", "sales@lampco.example")
    lamp = PhysicalProduct("P001", "Desk Lamp", 25.0, 50, supplier, 1.2)
    order = Order("O001", discount)
    order.add_order_line(lamp, 10)
    return order


def test_order_uses_no_discount_by_default():
    order = make_order_of_250()
    assert order.calculate_total() == pytest.approx(250.0)


def test_no_discount_returns_total_unchanged():
    assert NoDiscount().apply(250.0) == pytest.approx(250.0)


def test_order_total_with_bulk_discount():
    order = make_order_of_250(BulkDiscount(200, 20))
    assert order.calculate_total() == pytest.approx(230.0)


def test_set_discount_changes_strategy_on_existing_order():
    order = make_order_of_250(BulkDiscount(200, 20))
    assert order.calculate_total() == pytest.approx(230.0)

    order.set_discount(PercentageDiscount(10))
    assert order.calculate_total() == pytest.approx(225.0)


def test_new_strategy_works_without_changing_order():
    order = make_order_of_250(StudentDiscount())
    assert order.calculate_total() == pytest.approx(237.5)


def test_order_contains_no_discount_type_logic():
    order_source = inspect.getsource(Order)
    assert "PercentageDiscount" not in order_source
    assert "BulkDiscount" not in order_source
    assert "StudentDiscount" not in order_source


def test_bulk_discount_threshold_boundary():
    discount = BulkDiscount(200, 20)
    assert discount.apply(199.99) == pytest.approx(199.99)
    assert discount.apply(200.0) == pytest.approx(180.0)
    assert discount.apply(250.0) == pytest.approx(230.0)


@pytest.mark.parametrize("percentage", [0, 100, 150, -5])
def test_percentage_discount_rejects_invalid_percentage(percentage):
    with pytest.raises(ValueError):
        PercentageDiscount(percentage)


@pytest.mark.parametrize("threshold, amount", [(-50, 20), (200, 0), (10, 20)])
def test_bulk_discount_rejects_invalid_settings(threshold, amount):
    with pytest.raises(ValueError):
        BulkDiscount(threshold, amount)
