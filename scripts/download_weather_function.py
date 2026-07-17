#Brian Saville
#July 15, 2026

#a function to download weather data.
#inputs: station, start datetime, end datetime

from datetime import datetime
import meteostat
import pandas as pd

def download_weather(station, start, end):
    """Downloads weather data for inputted station, start, end times"""

    #round start and end time to nearest hour
        #so they're usable by meteostat
    start = start.round(freq = "h")
    end = end.round(freq = "h")

    #gather weather data from meteostat
    grabweather = meteostat.hourly(station, start, end)
    df = grabweather.fetch()

    return df
