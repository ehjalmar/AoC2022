import math

file=open('Day1/input.txt', 'r')
lines = file.readlines()

calories = 0
maxCalories = 0
totalCalsPerElf = []

for line in lines:
    if line == "\n":
        if(calories > maxCalories):
            maxCalories = calories
        totalCalsPerElf.append(calories)
        calories = 0
    else:
        calories = calories + int(line.replace("\n", ""))

# Ugly fix for adding last item
totalCalsPerElf.append(calories)


totalCalsPerElf.sort(reverse=True)

index = 0
topThreeCals = 0
while(index < 3):
    topThreeCals += totalCalsPerElf[index]
    index += 1

print("Top Three Calories: " + str(topThreeCals))