file = open('Day10/input.txt', 'r')
lines = file.read().splitlines()

x = 1
currentCycle = 0
totalSum = 0

def appendCycle(cycleNumber, sum):
    currentCycle = cycleNumber + 1
    if(currentCycle in (20,60,100,140,180,220)):
        sum += x * currentCycle
    return currentCycle, sum

for line in lines:
    instruction = line.split(' ')
    
    if(instruction[0] == 'noop'):
        currentCycle, totalSum = appendCycle(currentCycle, totalSum)
    else: # addx
        addxValue = int(instruction[1])
        for i in range(2):
            currentCycle, totalSum = appendCycle(currentCycle, totalSum)
        x += addxValue
    

print(totalSum)