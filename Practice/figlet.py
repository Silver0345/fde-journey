'''In a file called figlet.py, implement a program that:
Expects zero or two command-line arguments:
Zero if the user would like to output text in a random font.
Two if the user would like to output text in a specific font, in which case the first of the two should be -f or --font,
and the second of the two should be the name of the font.
Prompts the user for a str of text.
Outputs that text in the desired font.
If the user provides two command-line arguments and the first is not -f or --font, or the second is not the name of a
valid font, the program exits via sys.exit with an error message.
'''

import sys
from pyfiglet import Figlet, FontNotFound

txt = input("Enter a word or a sentence: ")

if len(sys.argv) == 1:
    f = Figlet(font='slant')
    print(f.renderText(txt))
elif len(sys.argv) == 3 and sys.argv[1] in ("-f", "--font"):
    try:
        f = Figlet(font=sys.argv[2])
    except FontNotFound:
        sys.exit(f"Font '{sys.argv[2]}' not found.")
    print(f.renderText(txt))
    
else:
    sys.exit("Please use the -f or --font flag followed by a font name.")

