import pytest

from supplier import Supplier
from inventory import Inventory, load_products
from main_program import MainProgram

BRIEF_PRODUCTS_CSV = (
    "product_type,product_id,name,price,stock_quantity\n"
    "physical,P001,Desk Lamp,25.00,10\n"
    "digital,D001,Photo Editor,49.90,100\n"
    "service,S001,Installation,30.00,5\n"
    "physical,P002,Office Chair,abc,3\n"
    "physical,P003,Monitor Stand,39.50,7\n"
)


def make_supplier() -> Supplier:
    return Supplier("S001", "Office Supplies Co", "sales@office.example")


def fake_inputs(monkeypatch, answers: list[str]) -> None:
    """Make input() return each answer in turn, as if the user typed them."""
    remaining = list(answers)
    monkeypatch.setattr("builtins.input", lambda prompt="": remaining.pop(0))


def test_get_positive_float_keeps_asking_until_valid(monkeypatch, capsys):
    fake_inputs(monkeypatch, ["abc", "-5", "12.50"])
    program = MainProgram(Inventory("unused.json"))

    value = program.get_positive_float("Enter product price: ")

    output = capsys.readouterr().out
    assert value == pytest.approx(12.5)
    assert "valid number" in output
    assert "greater than zero" in output


def test_get_non_negative_int_accepts_zero(monkeypatch):
    fake_inputs(monkeypatch, ["-1", "0"])
    program = MainProgram(Inventory("unused.json"))
    assert program.get_non_negative_int("Enter product stock: ") == 0


def test_load_products_skips_bad_rows_and_loads_the_rest(tmp_path, capsys):
    csv_path = tmp_path / "products.csv"
    csv_path.write_text(BRIEF_PRODUCTS_CSV)
    inventory = Inventory("unused.json")

    load_products(str(csv_path), inventory, make_supplier())

    output = capsys.readouterr().out
    loaded_ids = [product.product_id for product in inventory.products]
    assert loaded_ids == ["P001", "D001", "P003"]
    assert "Unknown product type: service" in output
    assert "3 products loaded." in output
    assert "Load attempt finished." in output


def test_load_products_handles_missing_file(tmp_path, capsys):
    inventory = Inventory("unused.json")

    load_products(str(tmp_path / "missing.csv"), inventory, make_supplier())

    output = capsys.readouterr().out
    assert "Products file not found" in output
    assert "products loaded" not in output
    assert "Load attempt finished." in output
    assert len(inventory.products) == 0
