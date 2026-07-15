#Brian Saville
#June 1, 2026
#Attempting a program that calculates Shannon Diversity
    #from inputted species data.
#This version includes the added step of calculating richness 
#   from list of individuals.

#import necessary libraries
import math

#Greet the user
print("Welcome to Brian's Shannon Diversity Index calculator!")

#Generate prompt for user input.
prompt = "What species is the first individual? "

#Generate list of individual observations
observations = []
input_active = True

while input_active:
    #Prompt the user to enter species
    observation = input(prompt)

    #Stop if the user enters "done"
    if observation == "done":
        break

    #Store the observation in a dictionary
    observations.append(observation)

    #Alter prompt to reflect plurality:
    if len(observations) > 0:
        prompt = "What species is the next individual?\n" \
        "(If you're done entering observations, type 'done'.) "

#Generate dictionary 
species_list = {}
num_species = 0
input_active_2 = True

for observation in observations:
    #If it's not a new species, iterate its count in the dictionary
    if observation in species_list.keys():
        num = int(species_list[observation])
        num += 1
        new_num = str(num)
        species_list[observation] = new_num
    #If it is a new species, add it as a key in the dictionary
    #and set its count to 1
    else: 
        species_list[observation] = "1"


#CALCULATING SHANNON DIVERSITY

#Calculate total individuals
total_indivs = 0

for species, count in species_list.items():
    individuals = int(count)
    total_indivs += individuals


#Calculate proportions for each species
proportions = []
for species, count in species_list.items():
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

#Print a species list
print("\n--- SPECIES LIST ---")
for species, count in species_list.items():
    print("\nSpecies: " + species.title())
    print("Abundance: " + count)



#Print the species richness
print("\nYour species richness is " + str(position) + ".")

#Print the Shannon Index
print("\nYour Shannon Diversity Index is " + str(sdi) + ".\n")