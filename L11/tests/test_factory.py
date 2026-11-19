import pytest

from supplier import Supplier
from product import Product
from physical_product import PhysicalProduct
from digital_product import DigitalProduct
from subscription_product import SubscriptionProduct
from product_factory import ProductFactory


def make_supplier() -> Supplier:
    return Supplier("S001", "Office Supplies Co", "sales@office.example")


@pytest.mark.parametrize(
    "product_type, expected_class",
    [
        ("physical", PhysicalProduct),
        ("p", PhysicalProduct),
        ("digital", DigitalProduct),
        ("d", DigitalProduct),
        ("subscription", SubscriptionProduct),
        ("s", SubscriptionProduct),
    ],
)
def test_factory_creates_the_right_product_type(product_type, expected_class):
    product = ProductFactory.create(product_type, "X001", "Item", 10.0, 5, make_supplier())
    assert isinstance(product, expected_class)
    assert isinstance(product, Product)


def test_factory_passes_extra_attribute_on():
    lamp = ProductFactory.create("physical", "P001", "Desk Lamp", 25.0, 10, make_supplier(), 1.2)
    editor = ProductFactory.create("digital", "D001", "Photo Editor", 49.9, 100, make_supplier(), 350.0)
    plan = ProductFactory.create("subscription", "S001", "Cloud Plan", 9.9, 50, make_supplier(), 12)

    assert lamp.weight == pytest.approx(1.2)
    assert editor.download_size == pytest.approx(350.0)
    assert plan.duration == 12


def test_factory_rejects_unknown_product_type():
    with pytest.raises(ValueError, match="Unknown product type: service"):
        ProductFactory.create("service", "S001", "Installation", 30.0, 5, make_supplier())
