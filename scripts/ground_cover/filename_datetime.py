#Brian Saville
#August 25th, 2026

#function to create a time-specific filename for an output file.

from datetime import datetime

def filename_maker (base_name):
    """Appends the date and time to a filename."""

    #turn current date/time to a string with only hyphens
    current_time = str(datetime.now())
    current_time = current_time[0:19]
    current_time = current_time.replace(" ", "-")
    current_time = current_time.replace(":", "-")

    #append date and time to desired base filename
    new_filename = str(base_name + "-" + current_time)

    return(new_filename)