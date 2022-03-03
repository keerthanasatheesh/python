import csv
csv_columns = ['No','Name','Established']
dict_data = [
{'No': 1, 'Name': 'TATA ', 'Established': '1945'},
{'No': 2, 'Name': 'TOYOTA', 'Established': '1900'},
{'No': 3, 'Name': 'VOLKSWAGEN', 'Established': '1850'},
{'No': 4, 'Name': 'DIAMLER', 'Established': '1980'},
]
csv_file = "cars.csv"
with open(csv_file, 'w') as csvfile:
 writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
 writer.writeheader()
 for data in dict_data:
     writer.writerow(data)
with open('cars.csv', 'r') as file:
 reader = csv.reader(file)
 for row in reader:
     print(row)
