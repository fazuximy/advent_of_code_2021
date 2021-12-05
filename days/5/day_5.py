# -*- coding: utf-8 -*-
"""
Created on Sun Dec  5 15:36:32 2021

@author: Fazuximy
"""
import pandas as pd

# --- Day 5: Hydrothermal Venture ---
# You come across a field of hydrothermal vents on the ocean floor! These vents constantly produce large, opaque clouds, so it would be best to avoid them if possible.

# They tend to form in lines; the submarine helpfully produces a list of nearby lines of vents (your puzzle input) for you to review. For example:

# 0,9 -> 5,9
# 8,0 -> 0,8
# 9,4 -> 3,4
# 2,2 -> 2,1
# 7,0 -> 7,4
# 6,4 -> 2,0
# 0,9 -> 2,9
# 3,4 -> 1,4
# 0,0 -> 8,8
# 5,5 -> 8,2

# Each line of vents is given as a line segment in the format x1,y1 -> x2,y2 where x1,y1 are the coordinates of one end the line segment and x2,y2 are the coordinates of the other end. These line segments include the points at both ends. In other words:

# An entry like 1,1 -> 1,3 covers points 1,1, 1,2, and 1,3.
# An entry like 9,7 -> 7,7 covers points 9,7, 8,7, and 7,7.
# For now, only consider horizontal and vertical lines: lines where either x1 = x2 or y1 = y2.

# So, the horizontal and vertical lines from the above list would produce the following diagram:

# .......1..
# ..1....1..
# ..1....1..
# .......1..
# .112111211
# ..........
# ..........
# ..........
# ..........
# 222111....

# In this diagram, the top left corner is 0,0 and the bottom right corner is 9,9. Each position is shown as the number of lines which cover that point or . if no line covers that point. The top-left pair of 1s, for example, comes from 2,2 -> 2,1; the very bottom row is formed by the overlapping lines 0,9 -> 5,9 and 0,9 -> 2,9.

# To avoid the most dangerous areas, you need to determine the number of points where at least two lines overlap. In the above example, this is anywhere in the diagram with a 2 or larger - a total of 5 points.

# Consider only horizontal and vertical lines. At how many points do at least two lines overlap?


path = r"Z:\python_stuff\advent_of_code_2021\days\5\\"
file = "input.XSCORE.txt"

# Importing the text file
vent_line_file = open(path+file, "r")
vent_line_report = vent_line_file.read()
# Splitting the text file into rows
vent_line_list = vent_line_report.split("\n")
vent_line_file.close()

vent_line_list_sep = [[j.split(",") for j in i.split(" -> ")] for i in vent_line_list][:-1]

vent_line_list_1 = [i[0] for i in vent_line_list_sep]
vent_line_list_2 = [i[1] for i in vent_line_list_sep]

x_list = []
y_list = []
for i in range(len(vent_line_list_1)):
    
    if int(vent_line_list_2[i][0]) < int(vent_line_list_1[i][0]):
        x_list.append(list(range(int(vent_line_list_2[i][0]),int(vent_line_list_1[i][0])+1)))
    elif int(vent_line_list_2[i][0]) > int(vent_line_list_1[i][0]):
        x_list.append(list(range(int(vent_line_list_1[i][0])*,int(vent_line_list_2[i][0])+1)))
    else:
        x_list.append([int(vent_line_list_2[i][0])])
    
    
    if int(vent_line_list_2[i][1]) < int(vent_line_list_1[i][1]):
        y_list.append(list(range(int(vent_line_list_2[i][1]),int(vent_line_list_1[i][1])+1)))
    elif int(vent_line_list_2[i][1]) > int(vent_line_list_1[i][1]):
        y_list.append(list(range(int(vent_line_list_1[i][1]),int(vent_line_list_2[i][1])+1)))
    else:
        y_list.append([int(vent_line_list_2[i][1])])


vertical_lines = [j for j,i in enumerate(x_list) if len(i) == 1]

horizontal_lines = [j for j,i in enumerate(y_list) if len(i) == 1]

relevant_lines = pd.Series(vertical_lines + horizontal_lines).unique()


relevant_x_list = [x_list[i] for i in relevant_lines]

relevant_y_list = [y_list[i] for i in relevant_lines]

relevant_final_lines = []
for i in range(len(relevant_x_list)):
    if len(relevant_x_list[i]) > len(relevant_y_list[i]):
        times = int(len(relevant_x_list[i])/len(relevant_y_list[i]))
        long_y_list = relevant_y_list[i] * times
        relevant_final_lines.append([str(relevant_x_list[i][j])+","+str(long_y_list[j]) for j in range(len(long_y_list))])
    elif len(relevant_x_list[i]) < len(relevant_y_list[i]):
        times = int(len(relevant_y_list[i])/len(relevant_x_list[i]))
        long_x_list = relevant_x_list[i] * times
        relevant_final_lines.append([str(long_x_list[j])+","+str(relevant_y_list[i][j]) for j in range(len(long_x_list))])
    else:
        relevant_final_lines.append([str(relevant_x_list[i][0]) + "," + str(relevant_y_list[i][0])])
        

flat_final_lines = [element for sublist in relevant_final_lines for element in sublist]     

final_lines_series = pd.Series(flat_final_lines)
overlapping_points = len(final_lines_series[final_lines_series.duplicated()].unique())

print("The Answer to Day 5 Part One: \nConsidering the horizontal and vertical lines, the number of unique overlapping points are: {}".format(overlapping_points))


# --- Part Two ---
# Unfortunately, considering only horizontal and vertical lines doesn't give you the full picture; you need to also consider diagonal lines.

# Because of the limits of the hydrothermal vent mapping system, the lines in your list will only ever be horizontal, vertical, or a diagonal line at exactly 45 degrees. In other words:

# An entry like 1,1 -> 3,3 covers points 1,1, 2,2, and 3,3.
# An entry like 9,7 -> 7,9 covers points 9,7, 8,8, and 7,9.
# Considering all lines from the above example would now produce the following diagram:

# 1.1....11.
# .111...2..
# ..2.1.111.
# ...1.2.2..
# .112313211
# ...1.2....
# ..1...1...
# .1.....1..
# 1.......1.
# 222111....

# You still need to determine the number of points where at least two lines overlap. In the above example, this is still anywhere in the diagram with a 2 or larger - now a total of 12 points.

# Consider all of the lines. At how many points do at least two lines overlap?

x_list = []
y_list = []

for i in range(len(vent_line_list_1)):
    
    if int(vent_line_list_2[i][0]) < int(vent_line_list_1[i][0]):
        x_list.append(list(range(int(vent_line_list_1[i][0]),int(vent_line_list_2[i][0])-1,-1)))
    elif int(vent_line_list_2[i][0]) > int(vent_line_list_1[i][0]):
        x_list.append(list(range(int(vent_line_list_1[i][0]),int(vent_line_list_2[i][0])+1,1)))
    else:
        x_list.append([int(vent_line_list_2[i][0])])
    
    
    if int(vent_line_list_2[i][1]) < int(vent_line_list_1[i][1]):
        y_list.append(list(range(int(vent_line_list_1[i][1]),int(vent_line_list_2[i][1])-1,-1)))
    elif int(vent_line_list_2[i][1]) > int(vent_line_list_1[i][1]):
        y_list.append(list(range(int(vent_line_list_1[i][1]),int(vent_line_list_2[i][1])+1,1)))
    else:
        y_list.append([int(vent_line_list_2[i][1])])
        
    if i == 553:
        print(vent_line_list_2[i][0]),int(vent_line_list_1[i][0])


all_x_list = [i for i in x_list]

all_y_list = [i for i in y_list]

all_final_lines = []
for i in range(len(all_x_list)):
    if len(all_x_list[i]) > len(all_y_list[i]):
        times = int(len(all_x_list[i])/len(all_y_list[i]))
        long_y_list = all_y_list[i] * times
        all_final_lines.append([str(all_x_list[i][j])+","+str(long_y_list[j]) for j in range(len(long_y_list))])
    elif len(all_x_list[i]) < len(all_y_list[i]):
        times = int(len(all_y_list[i])/len(all_x_list[i]))
        long_x_list = all_x_list[i] * times
        all_final_lines.append([str(long_x_list[j])+","+str(all_y_list[i][j]) for j in range(len(long_x_list))])
    else:
        if len(all_y_list[i]) == 1:
            all_final_lines.append([str(all_x_list[i][0]) + "," + str(all_y_list[i][0])])
        else:
            print([str(all_x_list[i][j])+","+str(all_y_list[i][j]) for j in range(len(all_y_list[i]))])
            all_final_lines.append([str(all_x_list[i][j])+","+str(all_y_list[i][j]) for j in range(len(all_y_list[i]))])

flat_all_final_lines = [element for sublist in all_final_lines for element in sublist]     

final_all_lines_series = pd.Series(flat_all_final_lines)
all_overlapping_points = len(final_all_lines_series[final_all_lines_series.duplicated()].unique())

print("The Answer to Day 5 Part Two: \nConsidering all the lines, the number of unique overlapping points are: {}".format(all_overlapping_points))

