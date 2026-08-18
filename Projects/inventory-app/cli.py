'''Interactive command-line front end for the inventory app.

The only file in this project that calls input()/print(). Owns the menu
loop and all user interaction; delegates every actual decision (adding,
finding, removing, totaling, saving, loading) to Inventory/Item, which
know nothing about the CLI that's driving them.
'''

from item import Item
from inventory import Inventory

def print_menu():
    print("\nWhat would you like to do?")
    print("1. Add item")
    print("2. Remove item")
    print("3. Find item")
    print("4. List all items")
    print("5. Show total value")
    print("6. Save to file")
    print("7. Load from file")
    print("8. Quit")
    
def add_item(inventory):
    name = input("What's the item called? ").strip()
    try:
        price = float(input("How much does it cost? $"))
        quantity = int(input("How many do you have? "))
    except ValueError:
        print("That doesn't look right: price should be a number, quantity a whole number.")
        return
    inventory.add_item(Item(name, price, quantity))
    print(f"Got it, added {name} to your inventory.")

def remove_item(inventory):
    name = input("Which item would you like to remove? ").strip()
    if inventory.remove_item(name):
        print(f"Removed {name}.")
    else:
        print(f"Couldn't find '{name}' in your inventory.")


def find_item(inventory):
    name = input("What are you looking for? ").strip()
    item = inventory.find_item(name)

    if item is not None:
        print(item)
    else:
        print(f"Couldn't find '{name}' in your inventory.")
        
def list_items(inventory):
    if not inventory.items:
        print("Your inventory is empty right now.")
        return

    for item in inventory.items:
        print(item)

def show_total(inventory):
    print(f"Your inventory is worth ${inventory.total_value()}.")

def save(inventory):
    file_name = input("Save as (e.g. inventory.json): ").strip()
    inventory.save_to_file(file_name)
    print(f"Saved to {file_name}.")

def load(inventory):
    file_name = input("Load from which file? ").strip()

    try:
        inventory.load_from_file(file_name)
        print(f"Loaded {file_name}: you're all set.")

    except FileNotFoundError:
        print(f"Couldn't find a file called {file_name}.")
        
def main():
    inventory = Inventory()
    actions = {
        "1": add_item,
        "2": remove_item,
        "3": find_item,
        "4": list_items,
        "5": show_total,
        "6": save,
        "7": load
    }
    
    while True:
        print_menu()
        choice = input("Choose an option: ").strip()
        if choice == '8':
            print('Goodbye!')
            break
        action = actions.get(choice)
        if action:
            action(inventory)
        else:
            print("Not a valid option: pick a number from 1 to 8.")
        
        
        
if __name__ == "__main__":
    main()