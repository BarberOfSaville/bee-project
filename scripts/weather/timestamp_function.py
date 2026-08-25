#Brian Saville
#July 17, 2026

#converts date/time data from CSV to timestap objects
#in datetime format for downstream use.

import pandas as pd
from datetime import datetime

def timestamp_add(df):
    """Adds timestamp columns to field data CSV."""
    df["start_dt"] = pd.to_datetime(
        df["date"] + " " + df["start"]
    )

    df["end_dt"] = pd.to_datetime(
        df["date"] + " " + df["end"]
    )

    return(df)