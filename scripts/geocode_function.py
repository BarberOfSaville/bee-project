#Brian Saville
#July 15, 2026

#A function for grabbing lat/long from an inputted address.

from geopy.geocoders import Nominatim
import time
geolocator = Nominatim(user_agent="bee_project", timeout = 10)

def get_lat_long(address):
    """Returns latitude and longitude for an inputted address."""
    
    location = geolocator.geocode(address)
    coords = [0,0]
    coords[0] = location.latitude
    coords[1] = location.longitude

    return coords

get_lat_long("1086 E 180th St, Bronx, NY")

def get_lat_long_all(df):
    """Gathers latitude and longitude for addresses in a sheet."""

    #create coordinates dictionary
    coord_lookup = {}

    df["latitude"] = None
    df["longitude"] = None

    unique_address = df["address"].drop_duplicates()

    for address in unique_address:
        print(f"Geocoding: {address}")
        coord_lookup[address] = get_lat_long(address)
        time.sleep(1)

    for index, row in df.iterrows():
        address = row["address"]
        lat, lon = coord_lookup[address]
        df.loc[index, "latitude"] = lat
        df.loc[index, "longitude"] = lon

    return df



