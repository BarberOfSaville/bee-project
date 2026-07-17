#Brian Saville
#July 17, 2026

#A script for collecting weather data 
#using the functions I've written.

import pandas as pd
import time
from datetime import datetime
import geocode_function
import nearest_station_function
from download_weather_function import download_weather
from timestamp_function import timestamp_add
from summarize_weather_function import summarize_weather
from bowl_date_function import bowl_date
from weather_master_function import weather_master

#read CSV and clean out empty rows
collections = pd.read_csv("../data/raw/collections.csv")
collections = collections.dropna(how = "all")

#add timestamps to the dataframe for later use.
collections = timestamp_add(collections)
collections = bowl_date(collections)

#gather latitude and longitude and add to all rows.
geocode_function.get_lat_long_all(collections)

#gather nearest station and add to all rows.
nearest_station_function.station_all(collections)

results = []

for index, row in collections.iterrows():

    #run the master weather function on the row
    weather_summary = weather_master(row)

    #add results to the results dataframe
    results.append(weather_summary)

results = pd.DataFrame(results)

#output the results dataframe as a CSV
results.to_csv("../data/processed/weather_summary.csv", index=False)
