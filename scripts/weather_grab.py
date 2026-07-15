#Brian Saville
#July 15, 2026
#Goal: write a script that can grab weather data 
    #for my data collection dates/times/locations.

#Things to obtain:
    #temperature
    #relative humidity
    #wind speed
    #precipitation
    #cloud cover

from datetime import datetime
import meteostat

#Set location and get weather stations
fordham = meteostat.Point(40.862, -73.885)

stations = meteostat.stations.nearby(fordham, limit = 10)
print(stations)
#LaGuardia station ID = 72503
LGA = "72503"

#set time period 
start = datetime(2025, 7, 6, 9)
end = datetime(2025, 7, 6, 12)

#get hourly data
testweather = meteostat.hourly(LGA, start, end)
df = testweather.fetch()

#print the dataframe
print(df)

#Collect avergaes from across the data collection period
temp_mean = df["temp"].mean()
rhum_mean = df["rhum"].mean()
wspd_max = df["wspd"].max()
prcp_tot = df["prcp"].sum()

#next step: automatically grabbing the nearest weather station
fordham = meteostat.Point(40.862, -73.885)

stations = meteostat.stations.nearby(fordham, limit = 1)
print(stations)

station_id = stations.index[0]
#it works! Gives LGA's ID