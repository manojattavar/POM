import csv
with open ("C:\\Users\\029693744\\PycharmProjects\\microFocus\\emailCSV.csv",'r') as csv_file:
    reader = csv.reader(csv_file)
    next(reader) # skip first row
    for row in reader:
        print(row)