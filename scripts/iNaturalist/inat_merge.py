#Brian Saville
#August 26, 2026

#Function to merge two iNat dex CSVs into one.

import pandas as pd
from filename_datetime import filename_maker

def inat_merge (csv_1, csv_2, filename):
    """Takes two iNat index CSVs and combines them into one."""

    #read the CSVs
    df1 = pd.read_csv(csv_1)
    df2 = pd.read_csv(csv_2)

    #rename the observation columns
    df1 = df1.rename(columns={"observations": "obs_A"})
    df2 = df2.rename(columns={"observations": "obs_B"})

    #merge all species from both files
    merged = pd.merge(df1, df2, on="id", how = "outer",
                      suffixes = ("_1", "_2"))

    #fill missing observation counts with 0
    merged["obs_A"] = merged["obs_A"].fillna(0)
    merged["obs_B"] = merged["obs_B"].fillna(0)

    #combined observations
    merged["obs_total"] = (merged["obs_A"] + merged["obs_B"])

    #combine taxonomic information
    merged["common_name"] = (
        merged["common_name_1"]
        .combine_first(merged["common_name_2"])
    )

    merged["scientific_name"] = (
        merged["scientific_name_1"]
        .combine_first(merged["scientific_name_2"])
    )

    merged["genus"] = (
        merged["genus_1"]
        .combine_first(merged["genus_2"])
    )

    merged["family"] = (
        merged["family_1"]
        .combine_first(merged["family_2"])
    )

    merged["order"] = (
        merged["order_1"]
        .combine_first(merged["order_2"])
    )

    #Keep the desired columns
    merged = merged[["id", 
                    "scientific_name", "genus", "family", "order",
                    "obs_A", "obs_B", "obs_total"]]

    #Sort by total observations
    merged = merged.sort_values(by = "obs_total", ascending = False)

    #export as a csv with the desired name.
    new_filename = filename_maker(filename)
    location = "C:/Users/brigu/Documents/_Fordham/_PhD_RESEARCH/bee-project-coding/data/inat_output/" + new_filename + ".csv"
    merged_df.to_csv(location, index=False)

    #Confirm that the function ran successfully.
    print("Merged species list exported as " + new_filename + ".csv")

    return(merged)

#then, testing it out for the first time.
file1 = "C:/Users/brigu/Documents/_Fordham/_PhD_RESEARCH/bee-project-coding/data/inat_input/mbees.csv"
file2 = "C:/Users/brigu/Documents/_Fordham/_PhD_RESEARCH/bee-project-coding/data/inat_input/bxbees.csv"
filename = "m_bx_bees"

merged_df = inat_merge(file1, file2, filename)

