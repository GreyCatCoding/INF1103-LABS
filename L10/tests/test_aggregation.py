import pytest
from supplier import Supplier
from physical_product import PhysicalProduct
from digital_product import DigitalProduct
from inventory import Inventory

def test_product_aggregation():
    supplier = Supplier("Supplier1", "S001","contact@supplier.com")
    """Test the aggregation of products with a supplier."""
    physical_product = PhysicalProduct("P001", "Laptop", 1000.0, 10, supplier, 2.5)
    digital_product = DigitalProduct("D001", "E-book", 20.0, 100, supplier, "http://download.com/ebook")

    """Test the aggregation of products with an inventory."""
    inventory = Inventory("test_inventory.json")
    assert inventory.add_product(physical_product) == True
    assert inventory.add_product(digital_product) == True
    assert inventory.search_product("P001") == physical_product
    assert inventory.search_product("D001") == digital_product
    assert inventory.remove_product("P001") == True
    assert inventory.search_product("P001") == None
    assert inventory.remove_product("D001") == True
    assert inventory.search_product("D001") == None