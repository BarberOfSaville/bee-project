#Brian Saville
#August 7th, 2026
#Function to make a species list CSV from downloaded iNat data.

from collections import Counter
import pandas as pd
from filename_datetime import filename_maker
from inat_index_function import inat_index
import time

def inat_list(observations, filename):
    """Generates a species list CSV from downloaded iNaturalist data."""

    #collapsing the species into a checklist
    species = set()

    for obs in observations:
        if obs["taxon"]["rank"] == "species":
            species.add(obs["taxon"]["id"])

    #count observations per species
    species_counts = Counter()

    for obs in observations:
        if obs["taxon"]["rank"] == "species":
            species_counts[obs["taxon"]["id"]] += 1

    #Converting this count into a table
    species_df = pd.DataFrame(
        species_counts.items(),
        columns=["ID", "Observations"]
    )

    #Add species info
    for i, taxon_id in enumerate(species_df["ID"]):

        species_info = inat_index(taxon_id)

        species_df.loc[i, "common_name"] = species_info["common_name"]
        species_df.loc[i, "scientific_name"] = species_info["scientific_name"]
        species_df.loc[i, "genus"] = species_info["genus"]
        species_df.loc[i, "family"] = species_info["family"]
        species_df.loc[i, "order"] = species_info["order"]

        print("Added info for " + species_df.loc[i, "common_name"])
        time.sleep(1)

    #Sorting that dataframe
    species_df = species_df.sort_values(
        by="Observations",
        ascending=False
    )

    new_filename = filename_maker(filename)

    location = "C:/Users/brigu/Documents/_Fordham/_PhD_RESEARCH/bee-project-coding/data/inat_output/" + new_filename + ".csv"

    #Exporting the dataframe
    species_df.to_csv(location, index=False)

    print("Huzzah! Species list exported as " + new_filename + ".csv")
