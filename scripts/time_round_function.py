#Brian Saville
#July 17, 2026

#Rounds timestamp data to the nearest hour.
#For making field observation data compatible with meteostat.

#UPDATE: I discovered while making it that this function already exists.
#so, sort of useless, but... good problem-solving exercise for me.

import pandas as pd
from datetime import datetime

def time_round_hour(timestamp):
    """Rounds a pandas timestamp to the nearest hour."""

    #I realized there was already a function for this halfway through.
    time = timestamp
    time = time.round(freq="h")

    return time

time = pd.Timestamp("2026-06-01 09:00:00")
new_day= time.day

if(new_day > 1):
    time = time.replace(day = new_day-1)
    print(time)
elif(new_day == 1):
    new_month = time.month
    time = time.replace(month = new_month-1)
    if(time.month in [1, 3, 5, 7, 8, 10, 12]):
        time = time.replace(day = 31)
    else:
        time = time.replace(day = 30)

ts = pd.Timestamp("2024-08-31 16:16:30")
ts.day
31