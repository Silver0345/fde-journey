'''In a file called scourgify.py, implement a program that:
Expects the user to provide two command-line arguments: the name of an existing
CSV file to read as input, whose columns are, in order, name and house, and the
name of a new CSV to write as output, whose columns should be, in order, first,
last, and house. Converts that input to that output, splitting each name into
a first name and last name. If the user does not provide exactly two
command-line arguments, or if the first cannot be read, exits via sys.exit
with an error message.
'''

import sys
import csv


if len(sys.argv) != 3:
    sys.exit("Usage: python scourgify.py before.csv after.csv")

input_file = sys.argv[1]
output_file = sys.argv[2]

try:
    with open(input_file) as infile, open(output_file, mode="w", newline="") as outfile:
        reader = csv.DictReader(infile)
        writer = csv.DictWriter(outfile, fieldnames=["first", "last", "house"])
        writer.writeheader()
        for row in reader:
            last, first = row["name"].split(", ")
            writer.writerow({"first": first, "last": last, "house": row["house"]})
except FileNotFoundError:
    sys.exit(f"Could not read {input_file}")