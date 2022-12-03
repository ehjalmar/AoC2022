import string

file=open('Day3/input.txt', 'r')
lines = file.readlines()

totalSum = 0

for line in lines:
    line = line.strip('\n')
    errorInCompartment = None
    # Split into compartments
    compartment1 = line[:len(line)//2]
    compartment2 = line[len(line)//2:]
    # for each char in first compartment, check if it exists in second
    for char1 in compartment1:
        for char2 in compartment2:
            if(char1 == char2):
                errorInCompartment = char1
                break
    # calculate priority
    priority = string.ascii_letters.index(errorInCompartment) + 1
    totalSum += priority

print(totalSum)    