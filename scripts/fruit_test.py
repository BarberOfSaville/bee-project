#Brian Saville
#June 23, 2026
#Learning how to read/write CSVs in Python.

import csv

#reading a csv
with open("data/test_fruits.csv", newline = "") as fruits:
    fruitreader = csv.reader(fruits, delimiter=",")
    for row in fruitreader:
        print(row)

#writing a csv
with open("data/veggies.csv", "w", newline = "") as csvfile:
    veggiewriter = csv.writer(csvfile)
    veggiewriter.writerow(["Vegetable", "Color", "Rating"])
    veggiewriter.writerow(["broccoli", "green", "3"])
    veggiewriter.writerow(["carrot", "orange", "5"])
    veggiewriter.writerow(["onion", "purple", "2"])
    veggiewriter.writerow(["potato", "brown", "4"])
    veggiewriter.writerow(["zucchini", "green", "5"])