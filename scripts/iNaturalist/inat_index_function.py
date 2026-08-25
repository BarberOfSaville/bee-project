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
    common_name = species["preferred_common_name"]
    species_info["common_name"] = common_name

    #scientific name
    sci_name = species["name"]
    species_info["scientific_name"] = sci_name

    #genus
    genus_id = species["parent_id"]
    genus_url = "https://api.inaturalist.org/v1/taxa/" + str(genus_id)
    response = requests.get(genus_url)
    genus_data = response.json()
    genus_results = genus_data["results"][0]
    genus = genus_results["name"]
    species_info["genus"] = genus

    #family
    family_id = str(genus_results["parent_id"])
    family_url = "https://api.inaturalist.org/v1/taxa/" + str(family_id)
    response = requests.get(family_url)
    family_data = response.json()
    family_results = family_data["results"][0]
    family = family_results["name"]
    species_info["family"] = family

    #order
    order_id = str(family_results["parent_id"])
    order_url = "https://api.inaturalist.org/v1/taxa/" + str(order_id)
    response = requests.get(order_url)
    order_data = response.json()
    order_results = order_data["results"][0]
    order = order_results["name"]
    species_info["order"] = order

    return(species_info)

