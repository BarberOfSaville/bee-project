#Brian Saville
#July 15, 2026

#a function to download weather data.
#inputs: station, start datetime, end datetime

from datetime import datetime
import meteostat

def download_weather(station, start, end):
    """Downloads weather data for inputted station, start, end times"""
    grabweather = meteostat.hourly(station, start, end)
    df = grabweather.fetch()

    return df

