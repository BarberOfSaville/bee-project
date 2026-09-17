#Brian Saville
#September 17th, 2026

#Outputs a visualization of a garden based on a text file.

import pandas as pd
from filename_datetime import filename_maker
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle

#pick a test file (West 123rd St Garden)
file = "peaceful"
filepath = "../../data/groundcover_input/" + file + ".txt"

#create dataframe to represent grid
grid = pd.DataFrame()
row = 0
col = 0

#Use the text file to generate a dataframe
with open(filepath) as f:
  for line in f:
        if line == '\n':
            break #end at a blank line to ignore any notes
        else:
            for char in line:
                if char == "\n":
                    continue
                if char == "x":
                    grid.loc[row, col] = "x"
                if char == "V":
                    grid.loc[row, col] = "V"
                if char == "F":
                    grid.loc[row, col] = "F"
                if char == "W":
                    grid.loc[row, col] = "W"
                if char == "L":
                    grid.loc[row, col] = "L"
                if char == "S":
                    grid.loc[row, col] = "S"
                if char == "I":
                    grid.loc[row, col] = "I"
                if char == "M":
                    grid.loc[row, col] = "M"
                col += 1
        col = 0
        row += 1

#Convert df to list
grid = grid.values.tolist()

#define colors to be used in the grid
colors = {"V" : (60/255, 193/255, 82/255),
          "W" : (58/255, 112/255, 33/255),
          "F" : (255/255, 165/255, 243/255),
          "L" : (182/255, 255/255, 0/255),
          "S" : (181/255, 124/255, 86/255),
          "I" : (192/255, 192/255, 192/255),
          "M" : (255/255, 129/255, 91/255),
          "x" : "white"}

#Generate the figure
fig, ax = plt.subplots()

for y, row in enumerate(grid):
    for x, cover in enumerate(row):

        ax.add_patch(
            Rectangle((x, y), 1, 1, facecolor = colors[cover])
        )

        if cover == "x":
            ax.plot([x, x + 1], [y, y + 1], color="black")
            ax.plot([x, x + 1], [y + 1, y], color="black")

plt.title(file.capitalize() + " Garden Ground Cover Plot")
ax.set_xlim(0, len(grid[0]))
ax.set_ylim(len(grid), 0)
ax.set_aspect("equal")

#Save the figure
file = file + "_plot"
new_filename = filename_maker(file)
plt.savefig("../../data/groundcover_output/" + new_filename + ".png", dpi = 300)
print("Output saved as " + new_filename + ".png.")

#Show figure
#plt.show()