import json

taqueria = {
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}



with open("taqueria.json", mode='w') as file:
    json.dump(taqueria, file, indent=4)
    
    
with open("taqueria.json", mode='r') as file:
    menu = json.load(file)
    
for name, price in menu.items():
    print(f"name: {name}: price: ${price}" )