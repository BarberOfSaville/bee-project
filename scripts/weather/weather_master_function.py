#Brian Saville
#July 17, 2026

#Master function for performing weather data collection
    #for a row of a data CSV.

import pandas as pd
from geocode_function import get_lat_long
from nearest_station_function import nearest_station
from download_weather_function import download_weather
from timestamp_function import timestamp_add
from summarize_weather_function import summarize_weather
from bowl_date_function import bowl_date

def weather_master(row):
    """
    
    Takes a row of a datasheet and gathers weather data for it.
    
    """
    row = row.copy()

    #print info for debugging purposes
    print("Station:", row["station"])
    print("Start:", row["weather_start_dt"])
    print("End:", row["end_dt"])

    #download weather
    weather = download_weather(row["station"], row["weather_start_dt"], 
                           row["end_dt"])
    
    #summarize relevant weather values
    weather_summary = summarize_weather(weather)

    #add values from the weather summary to the row
    for key, value in weather_summary.items():
        row[key] = value

    return row



