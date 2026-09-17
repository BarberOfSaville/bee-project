#Brian Saville
#June 11, 2026
#Recreating the shannon/simpson calculator as a function.

def diversity(species_list):
    """Calculate Shannon and Simpson Diversity 
    from an inputted dictionary"""
    import math

    total_indivs = 0
    for species, count in species_list.items():
        individuals = int(count)
        total_indivs += individuals

    #Calculate proportions for each species
    proportions = []
    for species, count in species_list.items():
        if count == 0:
            continue
        else: 
            individuals = int(count)
            proportion = individuals / total_indivs
            proportions.append(proportion)

    #Calculate the natural log of the proportions
    log_proportions = []
    for proportion in proportions:
        log = math.log(proportion)
        log_proportions.append(log)

    #Multiply proportions by the nat logs
    position = 0
    prop_times_log = []
    for log_proportion in log_proportions:
        product = log_proportion * proportions[position]
        prop_times_log.append(product)
        position += 1

    #Calculate Shannon Index
    sdi = 0
    for value in prop_times_log:
        sdi += value
    sdi = sdi * -1

    #CALULATING SIMPSON'S
    #Calculate numerator
    numerator = 0
    for species, count in species_list.items():
        count_int = int(count)
        count_int = count_int * (count_int - 1)
        numerator += count_int

    #Calculate denominator
    denominator = total_indivs * (total_indivs - 1)

    #Calculate Simpson's Index
    simpson = 1 - (numerator / denominator)
    
    return(sdi, simpson)