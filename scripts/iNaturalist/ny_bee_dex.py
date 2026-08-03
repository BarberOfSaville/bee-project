#Brian Saville
#July 31, 2026
#Gather all bee species obs for Manhattan from iNat.

import requests
from collections import Counter
import pandas as pd
import time

url = "https://api.inaturalist.org/v2/observations"

bee_id = 630955
bronx_id = 1189
manhattan_id = 1264
num_obs = 13651

params = {
    "taxon_id": bee_id,
    "quality_grade": "research",
    "place_id": 1264,
    "per_page" : 200,
    "fields": "taxon.id,taxon.name,taxon.rank,observed_on"
}

all_observations = []
page = 1

#for every page of observations, add results to all_observations list
while page <= 50:
    print(f"Downloading page {page}")

    params["page"] = page

    response = requests.get(url, params=params)
    data = response.json()

    observations = data["results"]

    if len(observations) == 0:
        break

    all_observations.extend(observations)

    page += 1










