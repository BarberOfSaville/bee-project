#Brian Saville
#September 17th, 2026

#Early attempts at reading groundcover data from text files

import pandas as pd
from filename_datetime import filename_maker
from diversity_function import diversity

#pick a test file (West 123rd St Garden)
file = "w123"
filepath = "../../data/groundcover_input/" + file + ".txt"

#set groundcover types to count
total_squares = 0
vegetable = 0
flower = 0
wild = 0
lawn = 0
soil = 0
impervious = 0
mulch = 0

with open(filepath) as f:
  for line in f:
        if line == '\n':
            break #end at a blank line to ignore any notes
        else:
            for char in line:
                if char != "\n" and char != "x":
                    total_squares += 1
                if char == "V":
                    vegetable += 1
                if char == "F":
                    flower += 1
                if char == "W":
                    wild += 1
                if char == "L":
                    lawn += 1
                if char == "S":
                    soil += 1
                if char == "I":
                    impervious += 1
                if char == "M":
                    mulch += 1
f.close()

#create list of square count values
categories = ["vegetable", "flower", "wild", "lawn", "soil", 
              "impervious", "mulch", "TOTAL"]
gridlist = [vegetable, flower, wild, lawn, soil, impervious, mulch,
             total_squares]

#Calculate percentages
sqm = total_squares * 4
v_pct = round(vegetable/total_squares *100, 2)
f_pct = round(flower/total_squares *100, 2)
w_pct = round(wild/total_squares *100, 2)
l_pct = round(lawn/total_squares *100, 2)
s_pct = round(soil/total_squares *100, 2)
i_pct = round(impervious/total_squares *100, 2)
m_pct = round(mulch/total_squares *100, 2)
pct_list = [v_pct, f_pct, w_pct, l_pct, s_pct, i_pct, m_pct]
total_pct = sum(pct_list)
pct_list.append(total_pct)

#Calculate areas
v_sqm = vegetable * 4
f_sqm = flower * 4
w_sqm = wild * 4
l_sqm = lawn * 4
s_sqm = soil * 4
i_sqm = impervious * 4
m_sqm = mulch * 4
sqm_list = [v_sqm, f_sqm, w_sqm, l_sqm, s_sqm, i_sqm, m_sqm]
total_sqm = sum(sqm_list)
sqm_list.append(total_sqm)

#Generate a dictionary pairing categories with area
categories_div = categories[:-1]
sqm_div = sqm_list[:-1]
cover_dict = dict(zip(categories_div, sqm_div))

#Calculate Shannon/Simpson Diversity for ground cover
div_indices = diversity(cover_dict)
sdi = round(div_indices[0], 3)
simpson = round(div_indices[1], 3)

#compiling the data into a dataframe
summary = pd.DataFrame({file : categories,
                        "squares" : gridlist,
                        "percent" : pct_list,
                        "area (sq m)" : sqm_list,
                        "shannon" : "",
                        "simpson" : ""}
)
#Add shannon and simpson diversity indices
summary.loc[0, "shannon"] = str(sdi)
summary.loc[0, "simpson"] = str(simpson)

#Export dataframe
new_filename = filename_maker(file)
summary.to_csv("../../data/groundcover_output/" + new_filename + ".csv", index=False)
print("Output saved as " + new_filename + ".csv.")