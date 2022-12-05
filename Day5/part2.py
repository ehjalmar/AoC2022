import instruction

file=open('Day5/input.txt', 'r')
lines = file.readlines()

# find number of buckets
foundNumberLine = False
indexOfNumberLine = 0
while foundNumberLine != True:
    if(lines[indexOfNumberLine].startswith(' 1 ')):
        foundNumberLine = True
    else:
        indexOfNumberLine += 1

numberLineList = lines[indexOfNumberLine].replace('   ',',').split(',')

# Create list with empty lists within
allStacks = [None] * len(numberLineList)
for index, stack in enumerate(allStacks):
    allStacks[index] = []

startIndexIfInstructions = 0

def findCargo(textInput, charIndex):
    while(textInput[charIndex]==' '):
        charIndex += 4
    return textInput[charIndex+1], charIndex

# Read stacks
for index, line in enumerate(lines):
    
    if(line.startswith(' 1 ')):
        startIndexIfInstructions = index + 2
        break
    
    # Check at which position we can find cargo
    charIndex = 0
    keepLooking = True
    charsInStack = []
    cargo = None
    while(keepLooking):
        cargo, charIndex = findCargo(line, charIndex)
        allStacks[int(charIndex/4)].append(cargo)
        whatsLeftOfLine = line[charIndex+1:].find('[') 
        if(whatsLeftOfLine == -1):
            keepLooking = False
        # Move one step ahead to not reapet last action
        charIndex += 4
    
# Create new list without stacks
instructionsLines = lines[startIndexIfInstructions:]

# Reverse stacks to get them in correct order
for stack in allStacks:
    stack.reverse()

def Union(lst1, lst2):
    final_list = lst1 + lst2
    return final_list

for instructionLine in instructionsLines:
    currentInstruction = instruction.Instruction(instructionLine.strip('\n').split(' '))

    # Copy items to destination
    allStacks[currentInstruction.toIndex] = Union(allStacks[currentInstruction.toIndex], allStacks[currentInstruction.fromIndex][len(allStacks[currentInstruction.fromIndex])-currentInstruction.amountToMove:])
    # Remove from source
    del allStacks[currentInstruction.fromIndex][-currentInstruction.amountToMove:]

message = ''
for stack in allStacks:
    message += stack.pop()

print(message)