#Brian Saville
#July 15, 2026

#A function for grabbing lat/long from an inputted address.

from geopy.geocoders import Nominatim
geolocator = Nominatim(user_agent= "bee_project")

def get_lat_long(address):
    """Returns latitude and longitude for an inputted address."""
    location = geolocator.geocode(address)
    coords = [0,0]
    coords[0] = location.latitude
    coords[1] = location.longitude

    return coords

get_lat_long("1086 E 180th St, Bronx, NY")