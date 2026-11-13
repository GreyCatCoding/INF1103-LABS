from supplier import Supplier
from physical_product import PhysicalProduct
from digital_product import DigitalProduct
from inventory import Inventory


def make_supplier() -> Supplier:
    return Supplier("S001", "Supplier One", "contact@supplier.com")


def test_inventory_add_find_remove():
    supplier = make_supplier()
    physical_product = PhysicalProduct("P001", "Laptop", 1000.0, 10, supplier, 2.5)
    digital_product = DigitalProduct("D001", "E-book", 20.0, 100, supplier, 5.0)

    inventory = Inventory("test_inventory.json")
    assert inventory.add_product(physical_product) is True
    assert inventory.add_product(digital_product) is True

    # search returns the SAME object that was added, not a copy
    assert inventory.search_product("P001") is physical_product
    assert inventory.search_product("D001") is digital_product

    assert inventory.remove_product("P001") is True
    assert inventory.search_product("P001") is None


def test_product_survives_removal_and_moves_to_another_inventory():
    # Step 1: the product exists BEFORE any inventory does
    supplier = make_supplier()
    laptop = PhysicalProduct("P002", "Laptop", 1000.0, 10, supplier, 2.5)

    # Step 2: add it to Inventory A
    inventory_a = Inventory("test_inventory_a.json")
    inventory_a.add_product(laptop)
    assert inventory_a.search_product("P002") is laptop

    # Step 3: remove it from Inventory A - the product itself must still work
    inventory_a.remove_product("P002")
    assert inventory_a.search_product("P002") is None
    print("After removal from Inventory A:")
    laptop.display_information()
    assert laptop.name == "Laptop"

    # Step 4: add the SAME product object to Inventory B
    inventory_b = Inventory("test_inventory_b.json")
    inventory_b.add_product(laptop)
    assert inventory_b.search_product("P002") is laptop


def test_emptying_inventory_does_not_destroy_products():
    supplier = make_supplier()
    laptop = PhysicalProduct("P003", "Laptop", 1000.0, 10, supplier, 2.5)
    ebook = DigitalProduct("D003", "E-book", 20.0, 100, supplier, 5.0)

    inventory = Inventory("test_inventory.json")
    inventory.add_product(laptop)
    inventory.add_product(ebook)

    # Empty the inventory completely
    inventory.remove_product("P003")
    inventory.remove_product("D003")

    # Both products are still usable outside any inventory
    assert laptop.price == 1000.0
    assert ebook.get_fulfilment_info() == "This product is delivered digitally"
