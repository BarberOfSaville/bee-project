#Brian Saville
#July 15, 2026

#Geocoder
#Collect lat/long for a given address.
#to be used for my collection data.

from geopy.geocoders import Nominatim

geolocator = Nominatim(user_agent= "bee_project")
location = geolocator.geocode("578 Stanton Ave, Baldwin, NY")

print(location.latitude)
print(location.longitude)