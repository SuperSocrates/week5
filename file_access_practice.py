import csv

publishers = []
with open("books.csv", encoding='utf-8') as file:
    reader = csv.reader(file)
    for row in reader:
        publishers.append(row[3])

print(publishers)
