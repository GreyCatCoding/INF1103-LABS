from inventory import Inventory
from physical_product import PhysicalProduct
from digital_product import DigitalProduct
from subscription_product import SubscriptionProduct
from supplier import Supplier

inventory = Inventory() 

def test_one_loop_gives_each_product_its_own_behaviour():
    # 1. supplier
    supplier = Supplier("SUP3", "Supplier Three", "supplier3@example.com")
    # 2. create one product of each type
    physical_product = PhysicalProduct("P2", "Physical Product 2", 100.0, 10, supplier, 1.5)
    digital_product = DigitalProduct("D2", "Digital Product 2", 50.0, 5, supplier, 500)
    subscription_product = SubscriptionProduct("S1", "Subscription Product 1", 20.0, 1, supplier, 12)
    # 3. create inventory object and add products to it
    inventory = Inventory()
    inventory.add_product(physical_product)
    inventory.add_product(digital_product)
    inventory.add_product(subscription_product)
    # 4. expected fulfilment info for each product type
    expected = [
        "This product requires physical shipping",
        "This product is delivered digitally",
        "This product is a subscription"
    ]
    # 5. Loop over each product in the inventory and check its fulfilment info
    results = []

    for product in inventory.products:
        product.display_information()
        info = product.get_fulfilment_info()
        print(info)
        results.append(info)
        # 6. check that the info is one of the expected strings
        assert info in expected

    assert sorted(results) == sorted(expected)

