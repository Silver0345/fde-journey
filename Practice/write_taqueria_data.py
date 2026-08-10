import csv

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

rows = [{"name": name, "price": price} for name, price in taqueria.items()]

with open("taqueria.csv", mode='w', newline='') as file:
    writer = csv.DictWriter(file, fieldnames=['name', 'price'])
    writer.writeheader()
    writer.writerows(rows)
    
    