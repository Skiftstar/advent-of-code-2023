import os

file_path = os.getcwd() + "/day2/input.txt"

# All Powers of the Games
# The Power is the Number of Cubes of each color multiplied
game_powers = []

with open(file_path) as file:
    for line in file:
        line = line.rstrip() # Remove trailing whitespaces

        game_id = int(line.split(":")[0].split(" ")[1])
        cube_sets = line.split(":")[1].split(";")

        game_max_cubes = dict(red=0, blue=0, green=0)

        for cube_set in cube_sets:
            cube_counts = cube_set.split(", ")
            
            for cube_count in cube_counts:
                cube_count = cube_count.strip() # Remove leading and trailing whitespace

                color = cube_count.split(" ")[1]
                amount = int(cube_count.split(" ")[0])

                # Store highest Number of cubes for that color
                if amount > game_max_cubes[color]:
                    game_max_cubes[color] = amount

        # Calculate Game Power
        game_power = game_max_cubes["blue"] * game_max_cubes["green"] * game_max_cubes["red"]
        game_powers.append(game_power)

# Make sum of all game_ids
result = 0
for num in game_powers:
    result = result + num

print(result)