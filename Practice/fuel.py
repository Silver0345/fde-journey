'''implement a program that prompts the user for a fraction, formatted as X/Y, wherein X is a non-negative integer and Y is a positive integer,
   and then outputs, as a percentage rounded to the nearest integer, how much fuel is in the tank. If, though, 1% or less remains, output E instead
   to indicate that the tank is essentially empty. And if 99% or more remains, output F instead to indicate that the tank is essentially full.
'''

def main():
    
    x, y = get_valid_range()   
    print(guage(x, y))

def convert(frac):
      
    x, y = frac.split("/")
    x = int(x)
    y = int(y)
    
    if y == 0:
        raise ZeroDivisionError("Zero denominator.")
                        
    elif x > y:
        raise ValueError("x should be less than y.")
    else:
        return x, y
            
    
def get_valid_range():
    while True:
        try:   
            frac = input("Enter a fraction (a/b): ").strip()
            x, y = convert(frac)
            return x, y
        except (ValueError, ZeroDivisionError):
            continue
           
def guage(num, denom):
    result = (num / denom) * 100
    result = int(result)

    if result <= 1:
        return "E"
    elif result >= 99:
        return "F"
    else:
        return f"{result}%"

if "__main__" == __name__:    
    main()