#Brian Saville
#August 7, 2026
# A function to download data from iNaturalist
    #based on a dictionary of inputted parameters.

import requests

def inat_download(params):
    """A function for downloading iNaturalist data."""

    url = "https://api.inaturalist.org/v2/observations"
    all_observations = []

    while True:

        response = requests.get(url, params=params)
        data = response.json()

        observations = data["results"]

        if len(observations) == 0:
            break

        all_observations.extend(observations)

        print("Downloaded: " + str(len(all_observations)) + " observations.")

        params["id_above"] = observations[-1]["id"]

    return all_observations