# -*- coding: utf-8 -*-
"""
Created on Mon Dec  6 18:16:24 2021

@author: Fazuximy
"""

import re
import numpy as np

# --- Day 6: Lanternfish ---
# The sea floor is getting steeper. Maybe the sleigh keys got carried this way?

# A massive school of glowing lanternfish swims past. They must spawn quickly to reach such large numbers - maybe exponentially quickly? You should model their growth rate to be sure.

# Although you know nothing about this specific species of lanternfish, you make some guesses about their attributes. Surely, each lanternfish creates a new lanternfish once every 7 days.

# However, this process isn't necessarily synchronized between every lanternfish - one lanternfish might have 2 days left until it creates another lanternfish, while another might have 4. So, you can model each fish as a single number that represents the number of days until it creates a new lanternfish.

# Furthermore, you reason, a new lanternfish would surely need slightly longer before it's capable of producing more lanternfish: two more days for its first cycle.

# So, suppose you have a lanternfish with an internal timer value of 3:

# After one day, its internal timer would become 2.
# After another day, its internal timer would become 1.
# After another day, its internal timer would become 0.
# After another day, its internal timer would reset to 6, and it would create a new lanternfish with an internal timer of 8.
# After another day, the first lanternfish would have an internal timer of 5, and the second lanternfish would have an internal timer of 7.
# A lanternfish that creates a new fish resets its timer to 6, not 7 (because 0 is included as a valid timer value). The new lanternfish starts with an internal timer of 8 and does not start counting down until the next day.

# Realizing what you're trying to do, the submarine automatically produces a list of the ages of several hundred nearby lanternfish (your puzzle input). For example, suppose you were given the following list:

# 3,4,3,1,2

# This list means that the first fish has an internal timer of 3, the second fish has an internal timer of 4, and so on until the fifth fish, which has an internal timer of 2. Simulating these fish over several days would proceed as follows:

# Initial state: 3,4,3,1,2
# After  1 day:  2,3,2,0,1
# After  2 days: 1,2,1,6,0,8
# After  3 days: 0,1,0,5,6,7,8
# After  4 days: 6,0,6,4,5,6,7,8,8
# After  5 days: 5,6,5,3,4,5,6,7,7,8
# After  6 days: 4,5,4,2,3,4,5,6,6,7
# After  7 days: 3,4,3,1,2,3,4,5,5,6
# After  8 days: 2,3,2,0,1,2,3,4,4,5
# After  9 days: 1,2,1,6,0,1,2,3,3,4,8
# After 10 days: 0,1,0,5,6,0,1,2,2,3,7,8
# After 11 days: 6,0,6,4,5,6,0,1,1,2,6,7,8,8,8
# After 12 days: 5,6,5,3,4,5,6,0,0,1,5,6,7,7,7,8,8
# After 13 days: 4,5,4,2,3,4,5,6,6,0,4,5,6,6,6,7,7,8,8
# After 14 days: 3,4,3,1,2,3,4,5,5,6,3,4,5,5,5,6,6,7,7,8
# After 15 days: 2,3,2,0,1,2,3,4,4,5,2,3,4,4,4,5,5,6,6,7
# After 16 days: 1,2,1,6,0,1,2,3,3,4,1,2,3,3,3,4,4,5,5,6,8
# After 17 days: 0,1,0,5,6,0,1,2,2,3,0,1,2,2,2,3,3,4,4,5,7,8
# After 18 days: 6,0,6,4,5,6,0,1,1,2,6,0,1,1,1,2,2,3,3,4,6,7,8,8,8,8

# Each day, a 0 becomes a 6 and adds a new 8 to the end of the list, while each other number decreases by 1 if it was present at the start of the day.

# In this example, after 18 days, there are a total of 26 fish. After 80 days, there would be a total of 5934.

# Find a way to simulate lanternfish. How many lanternfish would there be after 80 days?

# Defining path and file
path = r"Z:\python_stuff\advent_of_code_2021\days\6\\"
file = "input.XSCORE.txt"

# Importing the text file
fish_file = open(path+file, "r")
fish_report = fish_file.read()
# Splitting the text file into rows
fish_list = fish_report.split(",")
# Closing file
fish_file.close()

# Removing noise from the fish list
cleaned_fish_list = [int(re.sub("\D","",i)) for i in fish_list]
# Copying the list to a new list
growing_fish_list = cleaned_fish_list.copy()

# Iterating through a list, changing the internal timer and adding new laternfish
for time in range(80):
    growing_fish_list = list(np.asarray(growing_fish_list) - 1)
    fishs_to_add = sum([1 if i < 0 else 0 for i in growing_fish_list])
    growing_fish_list = [6 if i < 0 else i for i in growing_fish_list]
    growing_fish_list = growing_fish_list + [8]*fishs_to_add 

print("The Answer to Day 6 Part One: \nAfter 80 days there would be this number of laternfish: {}".format(len(growing_fish_list)))



# --- Part Two ---
# Suppose the lanternfish live forever and have unlimited food and space. Would they take over the entire ocean?

# After 256 days in the example above, there would be a total of 26984457539 lanternfish!

# How many lanternfish would there be after 256 days?

# I tried the same solution as before but the script crashed due to memory error
"""
# 1st try: The computer dies
growing_fish_list = cleaned_fish_list.copy()
for time in range(256):
    growing_fish_list = list(np.asarray(growing_fish_list) - 1)
    fishs_to_add = sum([1 if i < 0 else 0 for i in growing_fish_list])
    growing_fish_list = [6 if i < 0 else i for i in growing_fish_list]
    growing_fish_list = growing_fish_list + [8]*fishs_to_add 
    print(time)

# 2nd try: The computer dies faster
growing_fish_list = cleaned_fish_list.copy()
for time in range(256):
    growing_fish_list = np.asarray(growing_fish_list) - 1
    fishs_to_add = np.count_nonzero(growing_fish_list < 0)
    growing_fish_list = np.where(growing_fish_list < 0, 6, growing_fish_list)
    growing_fish_list = np.append(growing_fish_list,np.full((fishs_to_add), 8))
"""

# SUCCESS! It helped just counting the internal timers instead
# Counting the number of fishs with different internal timer values
growing_fish_list = cleaned_fish_list.copy()
fish_internal_timer_count = [growing_fish_list.count(i) for i in range(-1,9)]
# Iterating through the 256 days
for time in range(256):
    # Sliding the list value one entry to the left, by removing the first entry and adding an empty one at the end
    fish_internal_timer_count = fish_internal_timer_count[1:]+[0]
    # Counting the number of new fishs to add
    fishs_to_add = fish_internal_timer_count[0]
    # Resetting the internal timer for the fishs which have just created a new fish to 6
    fish_internal_timer_count[7] = fish_internal_timer_count[7]+fishs_to_add
    # Adding the new fish with an internal timer with 8
    fish_internal_timer_count[9] = fish_internal_timer_count[9]+fishs_to_add

# Removing the fish with an internal value of -1 (which have already been reset to 6) and adding the rest together
fish_after_256 = sum(fish_internal_timer_count[1:])

print("The Answer to Day 6 Part Two: \nAfter 256 days there would be this number of laternfish: {}".format(fish_after_256))


