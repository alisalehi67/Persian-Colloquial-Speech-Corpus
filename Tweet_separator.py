
import csv

in_file = open("abcd.csv", "r")
reader = csv.reader(in_file)
out_file = open("abcde.csv", "w")
writer = csv.writer(out_file)

for row in reader:
    if row:
        writer.writerow(row)

in_file.close()
out_file.close()

newcsv = open('abcde.csv', 'r')
csvreader = csv.reader(newcsv)
col4 = open('abcde4.csv', 'w')
col4writer = csv.writer(col4)

rows=[]
for row in csvreader:
    column4= row[3]
    rows.append(column4)
for item in rows:
    print(item)
    col4writer.writerow([item])

newcsv.close()
col4.close()

