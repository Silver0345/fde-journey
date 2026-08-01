
def main():
    greetinng = greet()
    
    if greetinng == "hello":
        print("$0")
    elif greetinng[0] == "h" and greetinng != "hello":
        print("$20")
    else:
        print("$100")
        
def greet():
    
    greetinng = input("Greeting: ").lower()
    return greetinng

main()