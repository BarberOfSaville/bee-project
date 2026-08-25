#Brian Saville
#July 15, 2026

#A test of whether I can pass data from one function to another.

from geocode_function import get_lat_long
from nearest_station_function import nearest_station
from download_weather_function import download_weather
from summarize_weather_function import summarize_weather
from datetime import datetime

#input an address, start time, and end time
address = "729 W 186th St, New York, NY"
start = datetime(2025, 7, 6, 9)
end = datetime(2025, 7, 6, 12)

#get coordinates
lat_long = get_lat_long(address)

#determine nearest weather station
station = nearest_station(lat_long)

#gather weather data frame
weather = download_weather(station, start, end)

#summarize desired weather data points
summary = summarize_weather(weather)
