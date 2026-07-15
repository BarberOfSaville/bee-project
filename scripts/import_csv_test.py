#Brian Saville
#July 15, 2026

#Testing importing data csvs and working with them.

import pandas as pd
from geocode_function import get_lat_long

#read CSV and clean out empty rows
collections = pd.read_csv("../data/raw/collections.csv")
collections = collections.dropna(how = "all")

#first, we'll test it out for one row.
    #Drew Gardens, 5/19/26, 9:10-9:40AM.
#designate the first row.
row = collections.iloc[0]
print(row["address"])
print(row["date"])

#get coordinates for the first row
coords = get_lat_long(row["address"])
print(coords)

#to be continued