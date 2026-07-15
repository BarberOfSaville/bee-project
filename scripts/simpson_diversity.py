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