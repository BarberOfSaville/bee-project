#Brian Saville
#July 15, 2026

#Summarize weather function
#Averages relevant weather parameters from inputted data frame.

from datetime import datetime
import meteostat

def summarize_weather(df):
    """Returns average weather values from weather dataframe."""
    return {
        "mean_temp" : round(df["temp"].mean(), 1),
        "mean_rhum" : round(df["rhum"].mean(), 1),
        "max_wspd" : round(df["wspd"].max(), 1),
        "total_prcp" : round(df["prcp"].sum(), 1)
    }