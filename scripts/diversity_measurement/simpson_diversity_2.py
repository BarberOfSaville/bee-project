#Brian Saville
#June 1, 2026
#Attempting a program that calculates Simpson Diversity
    #from inputted species data
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

#Calculate Simpson Diversity

#Calculate total individuals
total_indivs = 0

for species, count in species_list.items():
    individuals = int(count)
    total_indivs += individuals

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

#Print a species list
print("\n--- SPECIES LIST ---")
species_count = 0
for species, count in species_list.items():
    print("\nSpecies: " + species.title())
    print("Count: " + count)
    species_count += 1


#Print the species richness
print("\nYour species richness is " + str(species_count) + ".")

#Print the Shannon Index
print("\nYour Simpson Diversity Index is " + str(simpson) + ".\n")