'''Tests for Item and Inventory's pure logic.

Nothing here touches the interactive CLI (cli.py) directly, since Item
and Inventory never call input()/print() themselves - these tests call
their methods directly with plain values, no mocking or stdin faking
required.
'''

import pytest

from item import Item
from inventory import Inventory

def test_item_total_price():
    item = Item("Taco", 3, 5)
    assert item.total_price() == 15.00
    
def test_item_to_dict():
    item = Item("Taco", 3.00, 5)
    data = item.to_dict()
    assert data == {"name": 'Taco', 'price': 3.00, 'quantity': 5}

    rebuilt = Item.from_dict(data)
    assert rebuilt.name == "Taco"    
    assert rebuilt.price == 3.00
    assert rebuilt.quantity == 5
    
def test_add_and_find_item():
    inv = Inventory()
    inv.add_item(Item("Taco", 3, 5))
    found = inv.find_item("Taco")
    assert found is not None
    assert found.name == "Taco"
    assert inv.find_item("Pizza") is None

def test_remove_item():
    inv = Inventory()
    inv.add_item(Item("Taco", 3, 5))
    inv.add_item(Item("Salad", 7.50, 2))

    assert inv.remove_item("Taco") is True
    assert inv.find_item("Taco") is None
    assert len(inv.items) == 1

    assert inv.remove_item("Pizza") is False

def test_total_value():
    inv = Inventory()
    inv.add_item(Item("Taco", 3, 5))
    inv.add_item(Item("Salad", 7.50, 2))
    assert inv.total_value() == 30
    
def test_save_and_load(tmp_path):
    inv = Inventory()
    inv.add_item(Item("Taco", 3, 5))
    inv.add_item(Item("Salad", 7.50, 2))
    
    file_path = tmp_path/"inventory.json"
    inv.save_to_file(file_path)
    
    loaded = Inventory()
    loaded.load_from_file(file_path)
    
    assert len(loaded.items) == 2
    assert loaded.find_item("Taco").quantity == 5
    assert loaded.total_value() == 30