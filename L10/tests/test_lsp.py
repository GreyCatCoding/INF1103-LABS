from supplier import Supplier
from product import Product
from physical_product import PhysicalProduct
from digital_product import DigitalProduct
from subscription_product import SubscriptionProduct
from inventory import Inventory


def show_product_details(product: Product) -> None:
    """Works with ANY Product - it never checks which subclass it was given."""
    product.display_information()
    print(product.get_fulfilment_info())


def test_show_product_details_works_for_every_type():
    """Test that show_product_details works for every type of product."""
    supplier = Supplier("S001", "Supplier One", "contact@supplier.com")
    products = [
        PhysicalProduct("P001", "Mouse", 29.99, 15, supplier, 0.2),
        DigitalProduct("D001", "E-book", 9.99, 100, supplier, 5.0),
    ]
    for product in products:
        show_product_details(product)          # same function, no changes


def test_inventory_accepts_every_type():
    """Test that the inventory accepts every type of product."""
    supplier = Supplier("S001", "Supplier One", "contact@supplier.com")
    mouse = PhysicalProduct("P001", "Mouse", 29.99, 15, supplier, 0.2)
    ebook = DigitalProduct("D001", "E-book", 9.99, 100, supplier, 5.0)

    inventory = Inventory("test_inventory.json")
    assert inventory.add_product(mouse) is True
    assert inventory.add_product(ebook) is True
    assert inventory.search_product("D001") is ebook
    inventory.display_all()