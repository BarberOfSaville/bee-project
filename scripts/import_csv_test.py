#Brian Saville
#July 15, 2026

#Testing importing data csvs and working with them.

import pandas as pd
from geocode_function import get_lat_long
from nearest_station_function import nearest_station
from download_weather_function import download_weather
from timestamp_function import timestamp_add
from summarize_weather_function import summarize_weather
from bowl_date_function import bowl_date

#read CSV and clean out empty rows
collections = pd.read_csv("../data/raw/collections.csv")
collections = collections.dropna(how = "all")

#add timestamps to the dataframe for later use.
collections = timestamp_add(collections)

#convert start timestamp for bowl days.
collections = bowl_date(collections)

#first, we'll test it out for one row.
    #Drew Gardens, 5/19/26, 9:10-9:40AM.
#designate the first row.
row = collections.iloc[0]
print(row["address"])
print(row["date"])

#get coordinates for the first row
coords = get_lat_long(row["address"])
print(coords)

#Get the weather station for the first row
station = nearest_station(coords)
print(station)

#Download weather for the first row
weather = download_weather(station, row["weather_start_dt"], 
                           row["end_dt"])
print(weather)

#Summarize relevant weather values
weather_summary = summarize_weather(weather)
print(weather_summary)
