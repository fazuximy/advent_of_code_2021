# -*- coding: utf-8 -*-
"""
Created on Wed Dec  8 18:02:30 2021

@author: Fazuximy
"""

import pandas as pd
import numpy as np

# --- Day 8: Seven Segment Search ---
# You barely reach the safety of the cave when the whale smashes into the cave mouth, collapsing it. Sensors indicate another exit to this cave at a much greater depth, so you have no choice but to press on.

# As your submarine slowly makes its way through the cave system, you notice that the four-digit seven-segment displays in your submarine are malfunctioning; they must have been damaged during the escape. You'll be in a lot of trouble without them, so you'd better figure out what's wrong.

# Each digit of a seven-segment display is rendered by turning on or off any of seven segments named a through g:

#   0:      1:      2:      3:      4:
#  aaaa    ....    aaaa    aaaa    ....
# b    c  .    c  .    c  .    c  b    c
# b    c  .    c  .    c  .    c  b    c
#  ....    ....    dddd    dddd    dddd
# e    f  .    f  e    .  .    f  .    f
# e    f  .    f  e    .  .    f  .    f
#  gggg    ....    gggg    gggg    ....

#   5:      6:      7:      8:      9:
#  aaaa    aaaa    aaaa    aaaa    aaaa
# b    .  b    .  .    c  b    c  b    c
# b    .  b    .  .    c  b    c  b    c
#  dddd    dddd    ....    dddd    dddd
# .    f  e    f  .    f  e    f  .    f
# .    f  e    f  .    f  e    f  .    f
#  gggg    gggg    ....    gggg    gggg
 
# So, to render a 1, only segments c and f would be turned on; the rest would be off. To render a 7, only segments a, c, and f would be turned on.

# The problem is that the signals which control the segments have been mixed up on each display. The submarine is still trying to display numbers by producing output on signal wires a through g, but those wires are connected to segments randomly. Worse, the wire/segment connections are mixed up separately for each four-digit display! (All of the digits within a display use the same connections, though.)

# So, you might know that only signal wires b and g are turned on, but that doesn't mean segments b and g are turned on: the only digit that uses two segments is 1, so it must mean segments c and f are meant to be on. With just that information, you still can't tell which wire (b/g) goes to which segment (c/f). For that, you'll need to collect more information.

# For each display, you watch the changing signals for a while, make a note of all ten unique signal patterns you see, and then write down a single four digit output value (your puzzle input). Using the signal patterns, you should be able to work out which pattern corresponds to which digit.

# For example, here is what you might see in a single entry in your notes:

# acedgfb cdfbe gcdfa fbcad dab cefabd cdfgeb eafb cagedb ab |
# cdfeb fcadb cdfeb cdbaf
# (The entry is wrapped here to two lines so it fits; in your notes, it will all be on a single line.)

# Each entry consists of ten unique signal patterns, a | delimiter, and finally the four digit output value. Within an entry, the same wire/segment connections are used (but you don't know what the connections actually are). The unique signal patterns correspond to the ten different ways the submarine tries to render a digit using the current wire/segment connections. Because 7 is the only digit that uses three segments, dab in the above example means that to render a 7, signal lines d, a, and b are on. Because 4 is the only digit that uses four segments, eafb means that to render a 4, signal lines e, a, f, and b are on.

# Using this information, you should be able to work out which combination of signal wires corresponds to each of the ten digits. Then, you can decode the four digit output value. Unfortunately, in the above example, all of the digits in the output value (cdfeb fcadb cdfeb cdbaf) use five segments and are more difficult to deduce.

# For now, focus on the easy digits. Consider this larger example:

# be cfbegad cbdgef fgaecd cgeb fdcge agebfd fecdb fabcd edb |
# fdgacbe cefdb cefbgd gcbe
# edbfga begcd cbg gc gcadebf fbgde acbgfd abcde gfcbed gfec |
# fcgedb cgb dgebacf gc
# fgaebd cg bdaec gdafb agbcfd gdcbef bgcad gfac gcb cdgabef |
# cg cg fdcagb cbg
# fbegcd cbd adcefb dageb afcb bc aefdc ecdab fgdeca fcdbega |
# efabcd cedba gadfec cb
# aecbfdg fbg gf bafeg dbefa fcge gcbea fcaegb dgceab fcbdga |
# gecf egdcabf bgf bfgea
# fgeab ca afcebg bdacfeg cfaedg gcfdb baec bfadeg bafgc acf |
# gebdcfa ecba ca fadegcb
# dbcfg fgd bdegcaf fgec aegbdf ecdfab fbedc dacgb gdcebf gf |
# cefg dcbef fcge gbcadfe
# bdfegc cbegaf gecbf dfcage bdacg ed bedf ced adcbefg gebcd |
# ed bcgafe cdgba cbgef
# egadfb cdbfeg cegd fecab cgb gbdefca cg fgcdab egfdb bfceg |
# gbdfcae bgc cg cgb
# gcafb gcf dcaebfg ecagb gf abcdeg gaef cafbge fdbac fegbdc |
# fgae cfgab fg bagce

# Because the digits 1, 4, 7, and 8 each use a unique number of segments, you should be able to tell which combinations of signals correspond to those digits. Counting only digits in the output values (the part after | on each line), in the above example, there are 26 instances of digits that use a unique number of segments (highlighted above).

# In the output values, how many times do digits 1, 4, 7, or 8 appear?

path = r"Z:\python_stuff\advent_of_code_2021\days\8\\"
file = "input.XSCORE.txt"

# Importing the text file
digit_file = open(path+file, "r")
digit_report = digit_file.read()
# Splitting the text file into rows
digit_list = digit_report.split("\n")
# Closing file
digit_file.close()

# Seperating the segment signal patterns from the output
digit_lists = [i.split("| ") for i in digit_list][:-1]

# Getting a list of all the segment signal patterns
unique_signal_pattern = [i[0] for i in digit_lists]
unique_signal_pattern_list = [i.split() for i in unique_signal_pattern]
final_unique_signals = [[list(j) for j in i] for i in unique_signal_pattern_list]

# Getting a list of all the output
output_digits = [i[1] for i in digit_lists]
output_digits_list = [i.split() for i in output_digits]
final_output_digits = [[list(j) for j in i] for i in output_digits_list]

# Calculating the length of all the output digits
output_digit_length = [[len(j) for j in i] for i in final_output_digits]

# Flatten the list
output_digit_length_flat = [item for sublist in output_digit_length for item in sublist]

# Counting all the output digits with segment length of 2, 3, 4 and 7 to find the digits 1, 7, 4 and 8
number_of_1_4_7_8 = [output_digit_length_flat.count(i) for i in [2,3,4,7]]

print("The Answer to Day 8 Part One: \nThe digits 1, 4, 7, or 8 appear a total of: {} times".format(sum(number_of_1_4_7_8)))

# --- Part Two ---
# Through a little deduction, you should now be able to determine the remaining digits. Consider again the first example above:

# acedgfb cdfbe gcdfa fbcad dab cefabd cdfgeb eafb cagedb ab |
# cdfeb fcadb cdfeb cdbaf
# After some careful analysis, the mapping between signal wires and segments only make sense in the following configuration:

#  dddd
# e    a
# e    a
#  ffff
# g    b
# g    b
#  cccc
 
# So, the unique signal patterns would correspond to the following digits:

# acedgfb: 8
# cdfbe: 5
# gcdfa: 2
# fbcad: 3
# dab: 7
# cefabd: 9
# cdfgeb: 6
# eafb: 4
# cagedb: 0
# ab: 1

# Then, the four digits of the output value can be decoded:

# cdfeb: 5
# fcadb: 3
# cdfeb: 5
# cdbaf: 3

# Therefore, the output value for this entry is 5353.

# Following this same process for each entry in the second, larger example above, the output value of each entry can be determined:

# fdgacbe cefdb cefbgd gcbe: 8394
# fcgedb cgb dgebacf gc: 9781
# cg cg fdcagb cbg: 1197
# efabcd cedba gadfec cb: 9361
# gecf egdcabf bgf bfgea: 4873
# gebdcfa ecba ca fadegcb: 8418
# cefg dcbef fcge gbcadfe: 4548
# ed bcgafe cdgba cbgef: 1625
# gbdfcae bgc cg cgb: 8717
# fgae cfgab fg bagce: 4315

# Adding all of the output values in this larger example produces 61229.

# For each entry, determine all of the wire/segment connections and decode the four-digit output values. What do you get if you add up all of the output values?

print("The Answer to Day 8 Part One: \nThe digits 1, 4, 7, or 8 appear a total of: {} times".format(sum(number_of_1_4_7_8)))

# Loop through all the lines of signal pattern segments and output digits
    # A deduction algorithm is applied to the signal pattern segments in order to find what segments each number include
all_output_number = []
for display_numb in range(len(final_output_digits)):

    # Creating a dataframe of the signal patterns and their segment length for easier indexing   
    length_df = pd.DataFrame(zip([len(i) for i in final_unique_signals[display_numb]],final_unique_signals[display_numb]))
    length_df.columns = ["length","segments"]
    
    # We know 1 is the only digit with a segment length of 2, so we find the correct segment names
    cf = length_df[length_df["length"] == 2]["segments"].values[0]
    # We know 7 is the only digit with a segment length of 3, so we find the correct segment names
    acf = length_df[length_df["length"] == 3]["segments"].values[0]
    # We deduce segment a from digit 1 and 7 segments
    a = [i for i in acf if i not in cf]
    
    # We know 4 is the only digit with a segment length of 4, so we find the correct segment names
    bdcf = length_df[length_df["length"] == 4]["segments"].values[0]
    # We deduce segment bd from digit 1 and 4 segments
    bd = [i for i in bdcf if i not in cf]
    
    # Both digit 2, 3 and 5 share a segment length of 5
    digit_2_3_5 = list(length_df[length_df["length"] == 5]["segments"].values)
    # We know that all these digits only share segment a, d and g
    adg = [i for i in digit_2_3_5[0] if ((i in digit_2_3_5[1]) & (i in digit_2_3_5[2]))]
    # g is deduced from adg, acf and bd
    g = [i for i in adg if (i not in acf) & (i not in bd)]
    # d is deduced from adg, acf and bd
    d = [i for i in adg if (i not in acf) & (i in bd)]
    # d is deduced from bd and d
    b = [i for i in bd if i not in d]
    
    # Both digit 0, 6 and 9 share a segment length of 6
    digit_0_6_9 = list(length_df[length_df["length"] == 6]["segments"].values)
    
    # We know that 0 is the only of these three digits that does not have segment d
    abcefg = digit_0_6_9[np.argmax([d[0] not in i for i in digit_0_6_9])]
    # e is deduced from abcefg cf, a, b, g and d
    e = [i for i in abcefg if i not in (cf+a+b+g)]
    
    # We know that 9 is the only of these three digits that does not have segment e
    acdeg = digit_2_3_5[np.argmax([e[0] in i for i in digit_2_3_5])]
    # c is deduced from acdeg, a, d, e and g
    c = [i for i in acdeg if i not in (a+d+e+g)]
    # f is deduced from cf and c
    f = [i for i in cf if i not in c]
    
    # All the segments for each digit is collected into a list of all the digits
    digit_segment_list = [a + b + c + e + f + g, # digit 0
                        c + f, # digit 1
                        a + c + d + e + g, # digit 2
                        a + c + d + f + g, # digit 3
                        b + c + d + f, # digit 4
                        a + b + d + f + g, # digit 5
                        a + b + d + e + f + g, # digit 6
                        a + c + f, # digit 7
                        a + b + c + d + e + f + g, # digit 8
                        a + b + c + d + f + g] # digit 8
    
    # A dataframe is created from that list with, with the number itself and the length of the segments for each number
    final_digit_segments = pd.DataFrame({"number": range(10), "segments":digit_segment_list, "length": [len(i) for i in digit_segment_list]})
    
    real_digit_output = []
    # The four output digits are iterated through to find their true number
    for output_digit in final_output_digits[display_numb]:
            
        # Only the digits with the same segment length are kept
        relevant_digits = final_digit_segments[final_digit_segments["length"] == len(output_digit)].reset_index(drop = True)
    
        # if there is only one digit in the dataframe that is chosen
        if len(relevant_digits["number"]) == 1:
            real_digit_output.append(relevant_digits["number"].values[0])
            
        # If there are multiple digits in the dataframe, the digit with completely matching segments are chosen
        if len(relevant_digits["number"]) > 1:
            real_digit_output.append(relevant_digits.loc[(np.argmax([set(output_digit) == set(i) for i in list(relevant_digits["segments"])])),"number"])

        # If the dataframe is empty an error is printed since that should not happen
        elif len(relevant_digits["number"]) < 1:
            print("ERROR: COULD NOT FIND NUMBER")
                
    # The digits are combined into the true number for the output
    final_output = sum([i * 10 ** (3-j) for j,i in enumerate(real_digit_output)])
    
    # The number is append to the list to keep all the true numbers
    all_output_number.append(final_output)

print("The Answer to Day 8 Part Two: \nThe sum of all the output digits are: {}".format(sum(all_output_number)))



