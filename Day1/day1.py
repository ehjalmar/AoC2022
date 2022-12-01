import math

file=open('Day1/input.txt', 'r')
lines = file.readlines()

calories = 0
maxCalories = 0

for line in lines:
    if line == "\n":
        if(calories > maxCalories):
            maxCalories = calories
        calories = 0
    else:
        calories = calories + int(line.replace("\n", ""))

print("Max Calories: " + str(maxCalories))