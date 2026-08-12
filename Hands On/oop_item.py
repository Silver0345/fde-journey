'''Models Item and Inventory classes.

Item stores a name, price, and quantity, with a classmethod (get) that
builds an instance from user input and a total_price method. Inventory
holds a collection of Item instances via composition (a list attribute,
not inheritance) and sums their value with total_value.
'''

class Item:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
    
    def __str__(self):
        return f"Name: {self.name} at ${self.price}, {self.quantity} Qt." 
    
    @classmethod
    def get(cls):
        name = input("Name: ")
        price = float(input("Price: "))
        quantity = int(input("Quantity: "))
        return cls(name, price, quantity)
        
    def total_price(self):
        total = self.price * self.quantity
        return f"Name: {self.name}, total: ${round(total,2)}"

class Inventory:
    def __init__(self):
        self.items = []
        
    def add_item(self, item):
        self.items.append(item)
    
    def total_value(self):
        total = sum(i.price * i.quantity for i in self.items)
        return f'Total Value: {round(total,2)}'   
    
def main():
    my_item = Item.get()
    my_inventory = Inventory()
    my_inventory.add_item(my_item)
    my_item2 = Item.get()
    my_inventory.add_item(my_item2)
    my_item3 = Item.get()
    my_inventory.add_item(my_item3)
    print(my_inventory.total_value())
    
    
if __name__ == "__main__":
    main()