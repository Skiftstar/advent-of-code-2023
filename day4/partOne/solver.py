import os

file_path = os.getcwd() + "/day4/input.txt"

# All Card Points
card_points = []

with open(file_path) as file:
    index = 0

    for line in file:
        line = line.rstrip() # Remove trailing whitespaces

        card_value = 0.5

        # Remove Card Label
        line = line.split(": ")[1]
        winning_numbers = line.split(" | ")[0].split(" ")
        own_numbers = line.split(" | ")[1].split(" ")
        for number in own_numbers:
            if len(number) == 0: continue

            if number in winning_numbers:
                card_value = card_value * 2

        if card_value > 0.5:
            card_points.append(int(card_value))

        
# Make sum of all part ids
result = 0
for num in card_points:
    result = result + num

print(result)