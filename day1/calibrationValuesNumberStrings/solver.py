# From each line, the calibration value consists of the first and the last digit
# This solver calulates the sum of the calibration values provided in input.txt
# The difference between this and the previous solver is that it also accepts "one" as 1, etc.

import os
import numbers

file_path = os.getcwd() + "/day1/input.txt"

# Number Strings
number_strings = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

# All Calibration Numbers
calib_nums = []

with open(file_path) as file:
    for line in file:
        line = line.rstrip() # Remove trailing whitespaces

        # Filter for numbers
        numbers = []
        for index, char in enumerate(line):
            if char.isnumeric():
                numbers.append(char)
            else:
                # Go through each word in number_strings
                for number_index, word in enumerate(number_strings):
                    word_length = len(word)
                    
                    built_word = ""
                    # Get the next n (= length of number string) chars from the current line
                    # and build a word with it
                    for x in range(0, word_length):
                        built_word = built_word + line[index + x] if index + x < len(line) else built_word
                    
                    # If the built word is the number_string we're checking, add it's corresponding
                    # int value
                    if built_word == word:
                        numbers.append(number_index + 1)
                    
                    
        
        # Get first and last Number, to make calibration value
        calib_num = f"{numbers[0]}{numbers[-1]}"
        calib_nums.append(int(calib_num))

# Make sum of all calibration numbers
result = 0
for num in calib_nums:
    result = result + num

print(result)