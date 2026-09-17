#Brian Saville
#August 26th, 2026

#The Moment of Truth!
#Attempt to use my iNat code to generate the Bee Dex.

from inat_download_function import inat_download
from inat_list_function import inat_list

#Manhattan
nyc_bee_params = {
    "taxon_id": 630955,
    "quality_grade": "research",
    "place_id": 1264,
    "per_page" : 200,
    "order_by": "id",
    "order" : "asc",
    "fields": "id,taxon.id,taxon.name,taxon.rank,observed_on",
    "rank" : "species"
}

citybees = inat_download(nyc_bee_params)
inat_list(citybees, "manhattan_bees")

#Bronx
bronx_bee_params = {
    "taxon_id": 630955,
    "quality_grade": "research",
    "place_id": 1189,
    "per_page" : 200,
    "order_by": "id",
    "order" : "asc",
    "fields": "id,taxon.id,taxon.name,taxon.rank,observed_on",
    "rank" : "species"
}

bxbees = inat_download(bronx_bee_params)
inat_list(bxbees, "bronx_bees")


#debugging no common names 
megachile_params = {
    "taxon_id": 52784,
    "quality_grade": "research",
    "place_id": 1264,
    "per_page" : 200,
    "order_by": "id",
    "order" : "asc",
    "fields": "id,taxon.id,taxon.name,taxon.rank,observed_on",
    "rank" : "species"
}

megachile = inat_download(megachile_params)
inat_list(megachile, "nyc_megachile")



