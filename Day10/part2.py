file = open('Day10/input.txt', 'r')
lines = file.read().splitlines()

x1 = 1
x2 = 2
x3 = 3
currentCycle = 0
currentLap = 1

def cycle(cycleNumber, lapNumber, p1, p2, p3):
    cycleNumber += 1
    
    if((cycleNumber/40) % 1 == 0):
        lapNumber += 1
    
    rowCycle = int(cycleNumber - (40 * (lapNumber-1)))
    if(rowCycle in (p1, p2, p3)):
        print('#', end = '')
    else:
        print('.', end = '')
    
    if((cycleNumber/40) % 1 == 0):
        print('')

    return cycleNumber, lapNumber

for line in lines:
    instruction = line.split(' ')
    
    if(instruction[0] == 'noop'):
        currentCycle, currentLap = cycle(currentCycle, currentLap, x1, x2, x3)
    else: # addx
        addxValue = int(instruction[1])
        for i in range(2):
            currentCycle, currentLap = cycle(currentCycle, currentLap, x1, x2, x3)
        x1 += addxValue
        x2 += addxValue
        x3 += addxValue