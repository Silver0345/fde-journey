import emoji
import sys

'''implement a program that prompts the user for a str in English and then outputs the “emojized” version of that str, 
converting any codes (or aliases) therein to their corresponding emoji.
'''
sen = input("Enter a sentence with emoticons: ")

print(emoji.emojize(sen))