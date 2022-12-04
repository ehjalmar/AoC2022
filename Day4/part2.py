import elf

file=open("Day4/input.txt", 'r')
lines=file.readlines()

overlaps = 0

for line in lines:
    # split into ranges and create Elfs
    ranges = line.strip('\n').split(',')
    elf1 = elf.Elf(ranges[0])
    elf2 = elf.Elf(ranges[1])

    # Check if one range overlaps with the other
    if(elf1.WorkingRangeStart <= elf2.WorkingRangeStart and elf2.WorkingRangeStart <= elf1.WorkingRangeEnd):
        print(elf2.WorkingRange + " starts before " + elf1.WorkingRange + " ends")
        overlaps += 1
    elif(elf2.WorkingRangeStart <= elf1.WorkingRangeStart and elf1.WorkingRangeStart <= elf2.WorkingRangeEnd):
        print(elf1.WorkingRange + " starts before " + elf2.WorkingRange + " ends")
        overlaps += 1
    
print(overlaps)