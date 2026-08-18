'''Inventory: a collection of Items, managed via composition.

Holds Items in a plain list rather than inheriting from Item, since an
Inventory contains items, it isn't a kind of item itself. No input()/
print() here either, matching item.py's discipline, so this class can be
driven by cli.py, a test suite, or anything else with no changes needed.
save_to_file()/load_from_file() handle JSON persistence between runs.
'''

import json
from item import Item

class Inventory:
    def __init__(self):
        self.items = []
        
    def add_item(self, item):
        self.items.append(item)
    
    def find_item(self, name):
        for item in self.items:
            if item.name == name:
                return item
            
        return None
    
    def remove_item(self, name):
        item = self.find_item(name)
        if item is not None:
            self.items.remove(item)
            return True
        return False
    
    def total_value(self):
        total = sum(item.total_price() for item in self.items)
        return round(total,2)
    
    def save_to_file(self, file_name):
        with open(file_name, mode='w') as file:
            json.dump([item.to_dict() for item in self.items], file, indent=4)
            
    def load_from_file(self, file_name):
        with open(file_name, mode='r') as file:
            data = json.load(file)
            self.items = [Item.from_dict(d) for d in data]
            
            