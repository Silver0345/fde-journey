fruits = {
    "apple": 130,
    "avocado": 50,
    "banana": 110,
    "cantaloupe": 50,
    "grapefruit": 60,
    "grapes": 90,
    "honeydew melon": 50,
    "kiwifruit": 90,
    "lemon": 15,
    "lime": 20,
    "nectarine": 60,
    "orange": 80,
    "peach": 60,
    "pear": 100,
    "pineapple": 50,
    "plum": 70,
    "pomegranate": 80,
    "strawberry": 30,
    "tangerine": 50,
    "watermelon": 30
}

def main():
    fruit_name = input("Enter the name of a fruit: ").lower()
    get_fruit_calories(fruit_name)
    
def get_fruit_calories(fruit_name):
    
    if fruit_name in fruits:
        calories = fruits[fruit_name]
        print(f"A {fruit_name} has {calories} calories.")
    else:
        print("Sorry, that fruit is not in the list.")
        
main()