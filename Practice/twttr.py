vowels = ["A", "E", "I", "O", "U", "a", "e", "i", "o", "u"]

def main():
    words =  input("Enter a text: ")
    shorten(words)
    
def shorten(words):
    '''Implement a function called shorten that accepts a str as input and returns that same input 
    with all vowels removed.
    '''
    for vowel in vowels:
        words = words.replace(vowel, "")
    print(words)
    
main()