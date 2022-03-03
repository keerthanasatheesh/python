import csv
with open('character.csv', 'w', newline='') as file:
 writer = csv.writer(file)
 writer.writerow(["SN", "Books", "characters"])
 writer.writerow([1, "Aadujeevitham", "najeeb"])
 writer.writerow([2, "Rendamoozam", "Beema"])
with open('character.csv', 'r') as file:
 reader = csv.reader(file)
 for row in reader:
     print(row[1]+" "+row[2])
