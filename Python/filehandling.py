import csv
import json

# with open('sample.csv', mode='r') as file:
#     csv_reader = csv.reader(file)
#     for row in csv_reader:
#         print(row)





data = [
    {'name': 'ACME', 'shares': 100, 'price': 542.23},
    {'name': 'reliance', 'shares': 100, 'price': 942.23},
    {'name': 'coco-cola', 'shares': 100, 'price': 442.23},
    {'name': 'tata_steel', 'shares': 100, 'price': 342.23},
]

with open('data_file.json', 'w') as file:
    json.dump(data, file, indent=4)

with open('data_file.json', 'r') as file:
    data = json.load(file)
    print(data)



