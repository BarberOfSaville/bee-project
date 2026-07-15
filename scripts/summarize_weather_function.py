#Brian Saville
#July 15, 2026

#Summarize weather function
#Averages relevant weather parameters from inputted data frame.

from datetime import datetime
import meteostat

def summarize_weather(df):
    """Returns average weather values from weather dataframe."""
    temp_mean = df["temp"].mean()
    rhum_mean = df["rhum"].mean()
    wspd_max = df["wspd"].max()
    prcp_tot = df["prcp"].sum()
    weather_vals = [float(temp_mean), float(rhum_mean), float(wspd_max), 
                    float(prcp_tot)]

    return weather_vals