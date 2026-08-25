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
from filename_datetime import filename_maker

#read CSV and clean out empty rows
collections = pd.read_csv("../../data/weather_input/collections.csv")
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

    #run weather master function and add to results df
    results.append(weather_master(row))

results = pd.DataFrame(results)

#create a unique filename for the output
filename_base = "weather_summary"
filename = filename_maker(filename_base)

#output the results dataframe as a CSV
results.to_csv("../../data/weather_output/" + filename + ".csv", index=False)

#Print a message confirming it all went successfully.
print("Output saved as " + filename + ".csv.")
