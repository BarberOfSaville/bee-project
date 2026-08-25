#Brian Saville
#July 17, 2026

#A function to backdate bowl trapping events
#to consider the whole deployment period in weather collection.

import pandas as pd
from datetime import datetime

def bowl_date(df):
    """Create weather_start_dt based on collection method."""
    
    df["weather_start_dt"] = df["start_dt"]
    #creates a new column, as not to overwrite the start time

    mask = df["method"] == "bowl"
    #creates a list of which items in the method column we care about

    df.loc[mask, "weather_start_dt"] = (
        df.loc[mask, "start_dt"] - pd.Timedelta(days=1)
    )
    #locates items that meet the critera, subtracts one day from them

    return df




