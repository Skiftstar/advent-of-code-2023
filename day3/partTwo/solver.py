import os

file_path = os.getcwd() + "/day3/input.txt"

# All Part IDs with Gears adjacent
part_ids_with_gears = []

# Stores what indexes need to be a symbol for the number to be considered a part number
number_indexes = []
# Stores in what indexes a gear is stored
gear_index = []
# Stores what indexes to ignore (from multichar numbers)
ignore = []

# Cancels the search early if the number is too big
def in_array(index) -> bool:
    for num in gear_index:
        if (num > index):
            return False
        elif num == index:
            return True
    return False

with open(file_path) as file:
    index = 0

    for line in file:
        line = line.rstrip() # Remove trailing whitespaces

        for line_index, char in enumerate(line):
            line_length = len(line)
            # If the index is part of a multichar number, ignore it
            if index in ignore:
                ignore.pop(0)
                index = index + 1
                continue

            # If char is a number
            if char.isnumeric():
                word = char
                counter = line_index + 1

                # Builds the whole number
                while counter < len(line) and line[counter].isnumeric():
                    word = word + line[counter]
                    ignore.append(index + (counter - line_index))
                    counter = counter + 1
                
                word_length = counter - line_index

                # Save all of the indexes to check later on
                indexes_to_check = []
                if line_index > 0:
                    upper_left = index - line_length - 1
                    left = index - 1
                    bottom_left = index + line_length - 1

                    indexes_to_check.append(upper_left)
                    indexes_to_check.append(left)
                    indexes_to_check.append(bottom_left)
                if line_index + word_length < line_length:
                    upper_right = index - line_length + word_length 
                    right = index + word_length
                    bottom_right = index + line_length + word_length

                    indexes_to_check.append(upper_right)
                    indexes_to_check.append(right)
                    indexes_to_check.append(bottom_right)

                # Right above and below number
                for x in range(0, word_length):
                    indexes_to_check.append(index - line_length + x)
                    indexes_to_check.append(index + line_length + x)

                number_indexes.append(dict(number=int(word), check=indexes_to_check))

            # If the character is a symbol (so not a number or a .)
            # Note its index
            elif char == '*':
                gear_index.append(index)

            index = index + 1
        
# Check the indexes for all the part numbers
for obj in number_indexes:
    check_indexes = obj['check']
    number = obj['number']
    for index in check_indexes:
        if in_array(index):
            part_ids_with_gears.append(dict(number=number, index=index))

# Gear Ratios
ratios = []

# Gears that have already been checked
checked_indexes = []

for index, obj in enumerate(part_ids_with_gears):
    # If Gear has already been checked, ignore
    if obj['index'] in checked_indexes:
        continue

    numbers_with_same_gear = []
    for compare_index, compare in enumerate(part_ids_with_gears):
        # Ignore same object
        if index == compare_index:
            continue
        
        # If objects share same gear
        if obj['index'] == compare['index']:
            numbers_with_same_gear.append(compare['number'])
    
    # If gear is only adjacent to two part numbers (= Gear is Valid), then make gear ratio
    if len(numbers_with_same_gear) == 1:
        ratios.append(numbers_with_same_gear[0] * obj['number'])

    # Mark Gear as 'checked'
    checked_indexes.append(obj['index'])
            
# Make sum of all ratios
result = 0
for num in ratios:
    result = result + num

print(result)