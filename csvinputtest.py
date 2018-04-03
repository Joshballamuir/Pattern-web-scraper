import csv

file = input("Enter your filepath")

with open(file, 'r') as f:
    reader = csv.reader(f)
    your_list = list(reader)
print(your_list)
