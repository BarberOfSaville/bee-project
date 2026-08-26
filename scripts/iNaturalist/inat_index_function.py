#Brian Saville
#August 25th, 2026

#Function that accepts an iNat species ID and returns a dictionary
    #containing: common name: species, genus, family, order?

import requests

def inat_index(taxon_id):
    """Takes an iNat species ID and returns a dict with info."""

    #Gather infromation from iNaturalist
    id = str(taxon_id)
    url = "https://api.inaturalist.org/v1/taxa/" + id
    response = requests.get(url)
    taxon_data = response.json()
    species = taxon_data["results"][0]

    #Create dictionary and populate with the relevant info
    species_info = {}

    #taxon ID
    id = species["id"]
    species_info["taxon_id"] = id

    #common name
    common_name = species.get("preferred_common_name")
    species_info["common_name"] = common_name

    #scientific name
    sci_name = species["name"]
    species_info["scientific_name"] = sci_name

    #reading ancestors dictionary to get genus/family/class
    for ancestor in species["ancestors"]:

        if ancestor["rank"] == "genus":
            species_info["genus"] = ancestor["name"]

        if ancestor["rank"] == "family":
            species_info["family"] = ancestor["name"]

        if ancestor["rank"] == "order":
            species_info["order"] = ancestor["name"]

    return(species_info)

