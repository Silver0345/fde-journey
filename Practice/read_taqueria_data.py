import csv



with open("taqueria.csv", mode="r", newline="") as file:
    reader = csv.DictReader(file)
       
    for line in reader:
        print(f"{line['name']}: ${line['price']}")