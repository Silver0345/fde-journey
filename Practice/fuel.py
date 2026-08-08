'''implement a program that prompts the user for a fraction, formatted as X/Y, wherein X is a non-negative integer and Y is a positive integer,
   and then outputs, as a percentage rounded to the nearest integer, how much fuel is in the tank. If, though, 1% or less remains, output E instead
   to indicate that the tank is essentially empty. And if 99% or more remains, output F instead to indicate that the tank is essentially full.
'''

def main():
    
    x, y = get_fraction()
    check_fuel(x, y)

def get_fraction():
    
    while True:
        frac = input("Enter a fraction (a/b): ")
        try:
            
            x, y = frac.split("/")
            x = int(x)
            y = int(y)
        except ValueError as e:
            print("Invalid input. ")
            continue
            
        if x > y or y == 0:
            continue
        else:
            return x, y
        
def check_fuel(num, denom):
    result = (num / denom) * 100
    result = int(result)

    if result <= 1:
        print("E")
    elif result >= 99:
        print("F")
    else:
        print(f"{result}%")
    
main()