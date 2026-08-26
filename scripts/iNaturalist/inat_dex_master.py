#Brian Saville
#August 26th, 2026
#Master script for running the iNaturalist "pokedex" code.

#This script takes an iNaturalist species taxon ID and place ID and
#returns a CSV list of species with observations that match the 
#inputted taxon/place parameters. 

import requests
from collections import Counter
import pandas as pd
from inat_download_function import inat_download
from inat_list_function import inat_list

#PARAMETERS FOR THE USER TO SET:
#(Taxon and place IDs can be found in iNaturalist URLs.)
taxon_id = 630955
place_id = 1264
filename = "manhattan_bees"

#Gather parameters
params = {
    "taxon_id": taxon_id,
    "quality_grade": "research",
    "place_id": place_id,
    "per_page" : 200,
    "order_by": "id",
    "order" : "asc",
    "fields": "id,taxon.id,taxon.name,taxon.rank,observed_on",
    "rank" : "species"
}

#Download iNaturalist data based on given parameters
df = inat_download(params)

#Compile observations into a CSV
#contains common name, scientific name, genus, family, order
#sorted by observation count
inat_list(df, filename)
