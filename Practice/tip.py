def main():
    dollars = dollars_to_float(input("How much was the meal?: "))
    percent = percent_to_float(input("What percentage would you like to tip?: "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f} as a tip.")
    
def dollars_to_float(d):
    '''Convert a string in the format of $##.## to a float.'''
    return float(d.replace('$', ''))

def percent_to_float(p):
    '''accept a str as input (formatted as ##%, wherein each # is a decimal digit), 
    remove the trailing %, and return the percentage as a float. For instance, given 15% as input, it should return 0.15'''
    return float(p.replace('%', '')) / 100

main()
