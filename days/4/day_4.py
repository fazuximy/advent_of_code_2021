# -*- coding: utf-8 -*-
"""
Created on Sat Dec  4 17:30:29 2021

@author: Fazuximy
"""

import pandas as pd

# --- Day 4: Giant Squid ---
# You're already almost 1.5km (almost a mile) below the surface of the ocean, already so deep that you can't see any sunlight. What you can see, however, is a giant squid that has attached itself to the outside of your submarine.

# Maybe it wants to play bingo?

# Bingo is played on a set of boards each consisting of a 5x5 grid of numbers. Numbers are chosen at random, and the chosen number is marked on all boards on which it appears. (Numbers may not appear on all boards.) If all numbers in any row or any column of a board are marked, that board wins. (Diagonals don't count.)

# The submarine has a bingo subsystem to help passengers (currently, you and the giant squid) pass the time. It automatically generates a random order in which to draw numbers and a random set of boards (your puzzle input). For example:

# 7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1

# 22 13 17 11  0
#  8  2 23  4 24
# 21  9 14 16  7
#  6 10  3 18  5
#  1 12 20 15 19

#  3 15  0  2 22
#  9 18 13 17  5
# 19  8  7 25 23
# 20 11 10 24  4
# 14 21 16 12  6

# 14 21 17 24  4
# 10 16 15  9 19
# 18  8 23 26 20
# 22 11 13  6  5
#  2  0 12  3  7
 
# After the first five numbers are drawn (7, 4, 9, 5, and 11), there are no winners, but the boards are marked as follows (shown here adjacent to each other to save space):

# 22 13 17 11  0         3 15  0  2 22        14 21 17 24  4
#  8  2 23  4 24         9 18 13 17  5        10 16 15  9 19
# 21  9 14 16  7        19  8  7 25 23        18  8 23 26 20
#  6 10  3 18  5        20 11 10 24  4        22 11 13  6  5
#  1 12 20 15 19        14 21 16 12  6         2  0 12  3  7
 
# After the next six numbers are drawn (17, 23, 2, 0, 14, and 21), there are still no winners:

# 22 13 17 11  0         3 15  0  2 22        14 21 17 24  4
#  8  2 23  4 24         9 18 13 17  5        10 16 15  9 19
# 21  9 14 16  7        19  8  7 25 23        18  8 23 26 20
#  6 10  3 18  5        20 11 10 24  4        22 11 13  6  5
#  1 12 20 15 19        14 21 16 12  6         2  0 12  3  7
 
# Finally, 24 is drawn:

# 22 13 17 11  0         3 15  0  2 22        14 21 17 24  4
#  8  2 23  4 24         9 18 13 17  5        10 16 15  9 19
# 21  9 14 16  7        19  8  7 25 23        18  8 23 26 20
#  6 10  3 18  5        20 11 10 24  4        22 11 13  6  5
#  1 12 20 15 19        14 21 16 12  6         2  0 12  3  7
 
# At this point, the third board wins because it has at least one complete row or column of marked numbers (in this case, the entire top row is marked: 14 21 17 24 4).

# The score of the winning board can now be calculated. Start by finding the sum of all unmarked numbers on that board; in this case, the sum is 188. Then, multiply that sum by the number that was just called when the board won, 24, to get the final score, 188 * 24 = 4512.

# To guarantee victory against the giant squid, figure out which board will win first. What will your final score be if you choose that board?


path = r"Z:\python_stuff\advent_of_code_2021\days\4\\"
file = "input.XSCORE.txt"

# Importing the text file
bingo_file = open(path+file, "r")
bingo_data = bingo_file.read()
# Splitting the text file into rows
bingo_list = bingo_data.split("\n\n")
bingo_file.close()

number_order = bingo_list[0].split(",")

full_row = False
full_column = False 
for number in range(1,len(number_order)+1):
    
    if full_row == True or full_column == True:
        break

    for board_num,board in enumerate(bingo_list[1:]):
    
        board_list = [i.split() for i in board.split("\n")]
        
        board_df = pd.DataFrame(board_list)

        full_row = (5 in board_df.isin(number_order[:number]).sum(axis = 0).values)
        full_column = (5 in board_df.isin(number_order[:number]).sum(axis = 1).values)
        
        if full_row == True or full_column == True:
            unmarked_numbers = board_df[~board_df.isin(number_order[:number])]
            unmarked_number_lists = [unmarked_numbers.iloc[:,i].dropna().tolist() for i in range(5)]
            unmarked_number_list = [int(item) for sublist in unmarked_number_lists for item in sublist]
            
            winning_number = int(number_order[(number-1)])
            
            winning_board = board_num
        
            full_row = False
            full_column = False
            
            break
        
            
print("The Answer to Day 4 Part One: \nThe final score of the winning board is: {}".format(sum(unmarked_number_list)*winning_number))


# --- Part Two ---
# On the other hand, it might be wise to try a different strategy: let the giant squid win.

# You aren't sure how many bingo boards a giant squid could play at once, so rather than waste time counting its arms, the safe thing to do is to figure out which board will win last and choose that one. That way, no matter which boards it picks, it will win for sure.

# In the above example, the second board is the last to win, which happens after 13 is eventually called and its middle column is completely marked. If you were to keep playing until this point, the second board would have a sum of unmarked numbers equal to 148 for a final score of 148 * 13 = 1924.

# Figure out which board will win last. Once it wins, what would its final score be?


full_row = False
full_column = False 
winning_boards = []
for number in range(1,len(number_order)+1):

    for board_num,board in enumerate(bingo_list[1:]):
    
        board_list = [i.split() for i in board.split("\n")]
        
        board_df = pd.DataFrame(board_list)

        full_row = (5 in board_df.isin(number_order[:number]).sum(axis = 0).values)
        full_column = (5 in board_df.isin(number_order[:number]).sum(axis = 1).values)
        
        if (full_row == True or full_column == True) and board_num not in winning_boards:
            unmarked_numbers = board_df[~board_df.isin(number_order[:number])]
            unmarked_number_lists = [unmarked_numbers.iloc[:,i].dropna().tolist() for i in range(5)]
            unmarked_number_list = [int(item) for sublist in unmarked_number_lists for item in sublist]
            
            winning_number = int(number_order[(number-1)])
            
            winning_board = board_num
    
            winning_boards.append(winning_board)
    
    full_row = False
    full_column = False

print("The Answer to Day 4 Part Two: \nThe final score of the last winning board is: {}".format(sum(unmarked_number_list)*winning_number))
