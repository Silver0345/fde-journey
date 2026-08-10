import sys
import csv
from tabulate import tabulate

if len(sys.argv) > 2:
    sys.exit("Too many arguments.")
elif len(sys.argv) <=1:
    sys.exit("Few argument.")
elif not sys.argv[1].strip().endswith('.csv'):
    sys.exit("Not a python file.")
        
else:
    try:
        filename = sys.argv[1]
        with open(filename, mode='r', newline='') as file:
            data = csv.DictReader(file)
            
            print(tabulate(data, headers="keys", tablefmt="grid"))
    except FileNotFoundError:
        sys.exit("File Not Found.")