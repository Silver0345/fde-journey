'''In a file called bank.py, implement a program that prompts the user for a greeting
   and outputs, depending on that greeting, a dollar value, per the below.
   If the user's greeting starts with "hello", output $0.
   If the user's greeting starts with an "h" (but not "hello"), output $20.
   For any other greeting, output $100.
   Ignore any leading or trailing whitespace, and treat greetings case-insensitively.
'''


def main():
    greeting = greet()
    
    while True:
        
        if greeting == '':
            greeting = input("Please enter a valid greeting: ").strip().lower()
            continue
        elif greeting == "hello":
            print("$0")
            break
        elif greeting[0] == "h":
            print("$20")
            break
        else:
            print("$100")
            break
        
def greet():
    
    greeting = input("Greeting: ").strip().lower()
    return greeting

main()