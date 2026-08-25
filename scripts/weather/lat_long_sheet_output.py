#Brian Saville
#July 31, 2026
#Gathers addresses for a list of sites and returns them in a CSV.

from geopy.geocoders import Nominatim
import geocode_function as gf
import pandas as pd

#read list of sites
sites = pd.read_csv("../data/raw/sites.csv")

#add latitude and longitude to the df
gf.get_lat_long_all(sites)
sites = pd.DataFrame(sites)

#output as a new CSV
sites.to_csv("../data/processed/sites_geocoded.csv", index=False)
