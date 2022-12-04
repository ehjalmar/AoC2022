import elf

file=open("Day4/input.txt", 'r')
lines=file.readlines()
fullyContainsOther = 0

for line in lines:
    # split into ranges and create Elfs
    ranges = line.strip('\n').split(',')
    elf1 = elf.Elf(ranges[0])
    elf2 = elf.Elf(ranges[1])

    # Check if one range fully contains the other
    if(elf1.WorkingRangeStart <= elf2.WorkingRangeStart and elf1.WorkingRangeEnd >= elf2.WorkingRangeEnd):
        # Elf 1 range contains range of elf2
        print(elf1.WorkingRange + " contains " + elf2.WorkingRange)
        fullyContainsOther += 1
    elif(elf2.WorkingRangeStart <= elf1.WorkingRangeStart and elf2.WorkingRangeEnd >= elf1.WorkingRangeEnd):
        # Elf 2 range contains range of elf1
        print(elf2.WorkingRange + " contains " + elf1.WorkingRange)
        fullyContainsOther += 1
    
print(fullyContainsOther)