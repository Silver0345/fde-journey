'''Item: a single inventory entry (name, price, quantity).

Pure data and behavior only, no input()/print() anywhere in this file, so
it can be built from a CLI prompt, a loaded JSON file, or a test equally
well. to_dict()/from_dict() handle the conversion to/from the plain-dict
shape json.dump()/json.load() require.
'''

class Item:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
        
    def __str__(self):
        return f"Name: {self.name} at ${self.price}, {self.quantity} Qt."
    
    def total_price(self):
        total = self.price * self.quantity
        
        return round(total, 2)
    
    def to_dict(self):
        return {'name': self.name, 'price': self.price, 'quantity': self.quantity}
    
    @classmethod
    def from_dict(cls, data):
        return cls(data['name'], data['price'], data['quantity'])
    
    