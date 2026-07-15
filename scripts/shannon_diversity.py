#Brian Saville
#June 1, 2026
#Attempting a program that calculates Shannon Diversity
#from inputted species data

#import necessary libraries
import math

#Greet the user
print("Welcome to Brian's Shannon Diversity Index calculator!")

#Generate prompt for user input.
prompt = "Name the first species. "

#Generate dictionary 
species_list = {}
num_species = 0
input_active = True

while input_active:
    #Prompt the user to enter species
    species = input(prompt)

    #Stop if the user enters "done"
    if species == "done":
        break

    #Prompt user to enter the number of individuals seen
    count = input("What was the frequency of " + species + "? ")

    #Store species and count in a dictionary
    species_list[species] = count

    #Iterate number of species
    num_species += 1
    if num_species > 0:
        prompt = "Name the next species.\n" \
        "(If you're done entering species, type 'done'.) "

#Calculate Shannon Diversity

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
    print("Count: " + count)


#Print the species richness
print("\nYour species richness is " + str(position) + ".")

#Print the Shannon Index
print("\nYour Shannon Diversity Index is " + str(sdi) + ".\n")