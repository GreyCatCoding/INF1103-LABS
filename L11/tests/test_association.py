import pytest
from supplier import Supplier
from physical_product import PhysicalProduct
from digital_product import DigitalProduct

def test_physical_product_association():
    supplier = Supplier("S001", "Supplier One" ,"abc.gmail.com")
    product = PhysicalProduct("P001", "Physical Product", 100.0, 10, supplier, 2.5)
    assert product.supplier == supplier

def test_digital_product_association():
    supplier = Supplier("S002", "Supplier Two", "xyz.gmail.com")
    product = DigitalProduct("D001", "Digital Product", 50.0, 5, supplier, 500.0)
    assert product.supplier == supplier

def test_shared_supplier_survives_del():
    # One supplier object, shared by two different products
    supplier = Supplier("S003", "Acme Supplies", "sales@acme.com")
    physical = PhysicalProduct("P002", "Desk Lamp", 35.0, 8, supplier, 1.2)
    digital = DigitalProduct("D002", "Lamp Manual PDF", 2.0, 100, supplier, 15.0)

    # Each product can reach its supplier through the association
    physical.supplier.display_information()
    digital.supplier.display_information()

    # Both products point to the SAME supplier object, not two copies
    assert physical.supplier is digital.supplier

    # Remove the name `supplier`; the object lives on because the products still reference it
    original_supplier_id = physical.supplier.supplier_id
    del supplier

    print("After del supplier:")
    physical.supplier.display_information()
    digital.supplier.display_information()

    assert physical.supplier.supplier_id == original_supplier_id
    assert digital.supplier.supplier_id == original_supplier_id

if __name__ == "__main__":
    pytest.main()

