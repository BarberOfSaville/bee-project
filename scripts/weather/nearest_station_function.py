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

def station_all(df):
    """Gathers nearest weather stations for coordinates in a sheet."""

    #create stations ditionary
    station_lookup = {}
    
    df["station"] = None

    for index, row in df.iterrows():

        coords = (row["latitude"], row["longitude"])

        if coords not in station_lookup:
            station_lookup[coords] = nearest_station(coords)

        df.loc[index, "station"] = station_lookup[coords]

        #print a message for debugging
        print("Nearest station for {coords} is " + station_lookup[coords] + ".")

    return df