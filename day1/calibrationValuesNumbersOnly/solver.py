# From each line, the calibration value consists of the first and the last digit
# This solver calulates the sum of the calibration values provided in input.txt

import os
import numbers

file_path = os.getcwd() + "/day1/input.txt"

# All Calibration Numbers
calib_nums = []

with open(file_path) as file:
    for line in file:
        line = line.rstrip() # Remove trailing whitespaces

        # Filter for numbers
        numbers = []
        for char in line:
            if char.isnumeric():
                numbers.append(char)
        
        # Get first and last Number, to make calibration value
        calib_num = f"{numbers[0]}{numbers[-1]}"
        calib_nums.append(int(calib_num))

# Make sum of all calibration numbers
result = 0
for num in calib_nums:
    result = result + num

print(result)