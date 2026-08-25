#Brian Saville
#July 31, 2026
#A test of grabbing iNaturalist data using Python.

import requests
from collections import Counter
import pandas as pd
from inat_download_function import inat_download
from inat_list_function import inat_list

#Testing my new functions out.
#Goal: get a list of bird species in Suffolk County

params = {
    "taxon_id": 3,
    "quality_grade": "research",
    "place_id": 2410,
    "per_page" : 200,
    "order_by": "id",
    "order" : "asc",
    "fields": "id,taxon.id,taxon.name,taxon.rank,observed_on"
}

birds = inat_download(params)

inat_list(birds, "birds_suffolk_checklist")

#That pretty much worked!!
#For a smaller test easier for debugging, I'll do reptiles of Nassau County.

reptile_params = {
    "taxon_id": 26036,
    "quality_grade": "research",
    "place_id": 142,
    "per_page" : 200,
    "order_by": "id",
    "order" : "asc",
    "fields": "id,taxon.id,taxon.name,taxon.rank,observed_on"
}

reptiles = inat_download(reptile_params)

inat_list(reptiles, "reptiles_nassau_checklist")

#testing grabbing 
url = "https://api.inaturalist.org/v1/taxa/39682"

response = requests.get(url)
taxon_data = response.json()

print(taxon_data)
print(taxon_data.keys())
print('hehe')
print(taxon_data["results"][0].keys())

snapper = taxon_data["results"][0]

print(snapper["id"])
print(snapper["name"])
print(snapper["rank"])
print(snapper["preferred_common_name"])
print(snapper["ancestry"])
print(snapper["complete_rank"])
print(snapper["parent_id"])
#48460/1/2/355675/26036/39532/39680/39681
    #39681 is the genus

url = "https://api.inaturalist.org/v1/taxa/39681"
response = requests.get(url)
taxon_data = response.json()
next_level = taxon_data["results"][0]
print(next_level["id"])
print(next_level["name"])
print(next_level["rank"])
print(next_level["observations_count"])
