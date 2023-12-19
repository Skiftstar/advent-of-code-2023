import os

file_path = os.getcwd() + "/day2/input.txt"

# Config of Cubes for possible Game
config = dict(blue=14, green=13, red=12)

# All Possible Games
possible_games = []

with open(file_path) as file:
    for line in file:
        line = line.rstrip() # Remove trailing whitespaces

        game_id = int(line.split(":")[0].split(" ")[1])
        cube_sets = line.split(":")[1].split(";")
        invalid_game = False

        for cube_set in cube_sets:

            cube_counts = cube_set.split(", ")
            for cube_count in cube_counts:
                cube_count = cube_count.strip() # Remove leading and trailing whitespace

                color = cube_count.split(" ")[1]
                amount = int(cube_count.split(" ")[0])

                if amount > config[color]:
                    invalid_game = True
                    break

            if invalid_game:
                break

        if invalid_game:
            continue

        possible_games.append(game_id)

# Make sum of all game_ids
result = 0
for num in possible_games:
    result = result + num

print(result)