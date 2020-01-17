import csv
import re

in_file = open("abcde4.csv", "r")
reader = csv.reader(in_file)
out_file = open("abcde4Per.csv", "w")
writer = csv.writer(out_file)

for row in reader:


    #newrow = [print(item) for item in row]
    newrow = [re.sub(r"\\/", "/", item) for item in row]
    newrow = ",".join(newrow)
    newrow = newrow.encode('utf-8').decode('unicode-escape')
    newrow = newrow.encode('utf-16', 'surrogatepass').decode('utf-16')
    #
    print(newrow)
    writer.writerow([newrow])

in_file.close()
out_file.close()

