# -*- coding: utf-8 -*-
"""
Created on Tue Dec  7 18:20:28 2021

@author: Fazuximy
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import re

# --- Day 7: The Treachery of Whales ---
# A giant whale has decided your submarine is its next meal, and it's much faster than you are. There's nowhere to run!

# Suddenly, a swarm of crabs (each in its own tiny submarine - it's too deep for them otherwise) zooms in to rescue you! They seem to be preparing to blast a hole in the ocean floor; sensors indicate a massive underground cave system just beyond where they're aiming!

# The crab submarines all need to be aligned before they'll have enough power to blast a large enough hole for your submarine to get through. However, it doesn't look like they'll be aligned before the whale catches you! Maybe you can help?

# There's one major catch - crab submarines can only move horizontally.

# You quickly make a list of the horizontal position of each crab (your puzzle input). Crab submarines have limited fuel, so you need to find a way to make all of their horizontal positions match while requiring them to spend as little fuel as possible.

# For example, consider the following horizontal positions:

# 16,1,2,0,4,2,7,1,2,14

# This means there's a crab with horizontal position 16, a crab with horizontal position 1, and so on.

# Each change of 1 step in horizontal position of a single crab costs 1 fuel. You could choose any horizontal position to align them all on, but the one that costs the least fuel is horizontal position 2:

# Move from 16 to 2: 14 fuel
# Move from 1 to 2: 1 fuel
# Move from 2 to 2: 0 fuel
# Move from 0 to 2: 2 fuel
# Move from 4 to 2: 2 fuel
# Move from 2 to 2: 0 fuel
# Move from 7 to 2: 5 fuel
# Move from 1 to 2: 1 fuel
# Move from 2 to 2: 0 fuel
# Move from 14 to 2: 12 fuel

# This costs a total of 37 fuel. This is the cheapest possible outcome; more expensive outcomes include aligning at position 1 (41 fuel), position 3 (39 fuel), or position 10 (71 fuel).

# Determine the horizontal position that the crabs can align to using the least fuel possible. How much fuel must they spend to align to that position?


path = r"Z:\python_stuff\advent_of_code_2021\days\7\\"
file = "input.XSCORE.txt"

# Importing the text file
crab_file = open(path+file, "r")
crab_report = crab_file.read()
# Splitting the text file into rows
crab_list = crab_report.split(",")
# Closing file
crab_file.close()

# Cleaning the crab horizontal position list
cleaned_crab_list = [int(re.sub("\D","",i)) for i in crab_list]

# Plotting the data to see how the horizontal positions for the crabs are distributed
plt.hist(cleaned_crab_list)

# The median is used to get an idea of where the best horizontal position would be
horizontal_median = int(np.median(cleaned_crab_list))

# A test range is created 100 position before and after the median
test_range = list(range(horizontal_median-100,horizontal_median+100))
fuel_usage_list = []
# The data test range is iterated through calculating the summed distance to the horizontal position for the crabs
# The position with the least fuel consumption is then chosen
for horizontal_position in test_range:
    fuel_usage_list.append(sum(abs(np.array(cleaned_crab_list)-horizontal_position)))

# The position was actually the median
print("The Answer to Day 7 Part One: \nThe fuel consumption to horizontal position {} will be: {}".format(test_range[np.argmin(fuel_usage_list)],int(min(fuel_usage_list))))


# --- Part Two ---
# The crabs don't seem interested in your proposed solution. Perhaps you misunderstand crab engineering?

# As it turns out, crab submarine engines don't burn fuel at a constant rate. Instead, each change of 1 step in horizontal position costs 1 more unit of fuel than the last: the first step costs 1, the second step costs 2, the third step costs 3, and so on.

# As each crab moves, moving further becomes more expensive. This changes the best horizontal position to align them all on; in the example above, this becomes 5:

# Move from 16 to 5: 66 fuel
# Move from 1 to 5: 10 fuel
# Move from 2 to 5: 6 fuel
# Move from 0 to 5: 15 fuel
# Move from 4 to 5: 1 fuel
# Move from 2 to 5: 6 fuel
# Move from 7 to 5: 3 fuel
# Move from 1 to 5: 10 fuel
# Move from 2 to 5: 6 fuel
# Move from 14 to 5: 45 fuel

# This costs a total of 168 fuel. This is the new cheapest possible outcome; the old alignment position (2) now costs 206 fuel instead.

# Determine the horizontal position that the crabs can align to using the least fuel possible so they can make you an escape route! How much fuel must they spend to align to that position?


# Since we can no longer use the median directly, the test range starts from the median to 2000 (further away than any crab)
    # The median is chosen as a start point since it cannot be less than that given the higher fuel consumption for longer distance and the shape of the position distribution
    # The loop will be stopped when the fuel consumption will start to increase again
test_range = list(range(horizontal_median,2000))
fuel_usage_list = []
for horizontal_position in test_range:
    horizontal_difference = abs(np.array(cleaned_crab_list)-horizontal_position)
    # The formula (n ** 2 + n)/2) is used to calculate the new fuel consumption
    fuel_usage_list.append(sum((horizontal_difference ** 2 + horizontal_difference)/2))
    # Used to first start indexing list when it is long enough
    if len(fuel_usage_list) > 3:
        # When the two previous fuel consumption numbers are less than the new fuel consumption number, the loop is stopped
            # Two are chosen since it is more robust towards noise than one
        if (fuel_usage_list[-2] < fuel_usage_list[-1]) & (fuel_usage_list[-3] < fuel_usage_list[-1]):
            break

print("The Answer to Day 7 Part Two: \nThe fuel consumption to horizontal position {} with crap engineering will be: {}".format(test_range[np.argmin(fuel_usage_list)],int(min(fuel_usage_list))))
