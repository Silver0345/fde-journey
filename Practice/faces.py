def convert(sen):
    '''mplement a function called convert that accepts a str as input and returns that same input 
    with any :) converted to 🙂 (otherwise known as a slightly smiling face) and any :( converted to 🙁
    (otherwise known as a slightly frowning face).
    '''
    sen = sen.replace(':)', '🙂')
    sen = sen.replace(':(', '🙁')
    return sen


def main():
    words =  input("Enter a sentence with emoticons: ")
    print(convert(words))
    
main()