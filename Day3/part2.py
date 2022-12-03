import string

file=open('Day3/input.txt', 'r')
lines = file.readlines()

totalSum = 0

for index in range(0, len(lines), 3):
    elf1 = lines[index].strip('\n')
    elf2 = lines[index + 1].strip('\n')
    elf3 = lines[index + 2].strip('\n')
    badgeItem = None
    # for each char in first elf, check if that exists in 2 and 3
    for char1 in elf1:
        for char2 in elf2:
            if(char1 == char2):
                for char3 in elf3:
                    if(char1 == char3):
                        badgeItem = char1
                        break
    # calculate priority
    priority = string.ascii_letters.index(badgeItem) + 1
    totalSum += priority

print(totalSum)    