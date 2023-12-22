import os

file_path = os.getcwd() + "/day4/input.txt"

# All Card Points
card_points = []

card_amounts = [1]

with open(file_path) as file:
    index = 0

    for index, line in enumerate(file):
        line = line.rstrip() # Remove trailing whitespaces

        if index > len(card_amounts) - 1:
            card_amounts.append(1)

        cards_of_this_num = card_amounts[index]

        print(f"Processing {cards_of_this_num} instances of Card {index + 1}")

        # Remove Card Label
        line = line.split(": ")[1]
        winning_numbers = line.split(" | ")[0].split(" ")
        own_numbers = line.split(" | ")[1].split(" ")

        for x in range(0, cards_of_this_num):
            matching_number_amount = 0
            for number in own_numbers:
                if len(number) == 0: continue

                if number in winning_numbers:
                    matching_number_amount = matching_number_amount + 1
                    index_of_copy = index + matching_number_amount
                    if index_of_copy > len(card_amounts) - 1:
                        card_amounts.append(2)
                    else:
                        card_amounts[index_of_copy] = card_amounts[index_of_copy] + 1
        
# Make sum of all part ids
result = 0
for num in card_amounts:
    result = result + num

print(result)