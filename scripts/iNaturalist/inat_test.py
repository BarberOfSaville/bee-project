#Brian Saville
#July 31, 2026
#A test of grabbing iNaturalist data using Python.

import requests
from collections import Counter

#making the request
url = "https://api.inaturalist.org/v2/observations"

bee_id = 630955
bronx_id = 1189
manhattan_id = 1264

params = {
    "taxon_id": bee_id,
    "quality_grade": "research",
    "place_id": 1264,
    "per_page" : 200,
    "fields": "taxon.id,taxon.name,taxon.rank,observed_on"
}

response = requests.get(url, params=params)

print(response.status_code)
#200. It works!

#convert response to Python
data = response.json()

#Extract the species
obs = data["results"][0]

print(obs["taxon"]["name"])

for obs in data["results"]:
    print(obs["taxon"]["name"])


#collapsing the species into a checklist
species = set()

for obs in data["results"]:
    if obs["taxon"]["rank"] == "species":
        species.add(obs["taxon"]["name"])

print(species)


#count observations per species
species_counts = Counter()

for obs in data["results"]:
    if obs["taxon"]["rank"] == "species":
        species_counts[obs["taxon"]["name"]] += 1

print("\n".join(species_counts))