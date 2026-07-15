#Brian Saville
#July 15, 2026

#A function to return the nearest weather station
#for inputted coordinates

from datetime import datetime
import meteostat

def nearest_station(lat_long):
    """Returns nearest weather station for inputted coordinates"""
    location = meteostat.Point(lat_long[0], lat_long[1])
    stations = meteostat.stations.nearby(location, limit = 1)
    station_id = stations.index[0]
    return station_id

