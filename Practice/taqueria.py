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
def main():
    total = get_order_value()
    
    print(f"Total: ${total:.2f}")
    
def get_order_value():  
    total = 0
    
    while True:
        try:
            item = input("Item: ").title()
            if item in taqueria:
                print(f"{item}: ${taqueria[item]:.2f}")
                total += taqueria[item]
                print(f"Total: ${total:.2f}")
            elif item == "-d".title():
                #print(f"Total: ${total:.2f}")
                break
        except EOFError:
            pass
    return total    
    

main()