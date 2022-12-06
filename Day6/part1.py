file = open('Day6/input.txt','r')
line = file.readline()

def is_isogram(string):
    for i in string:
        if string.count(i) > 1:
            return False
    return True

def findStartOfPacket(inputText):
    currentIndex = 0
    charsProcessed = 0
    foundIt = False
    
    while foundIt == False:
        currentBatch = inputText[currentIndex:currentIndex+4]
        if is_isogram(currentBatch):
            foundIt = True
            charsProcessed = currentIndex + 4
            break
        else:
            currentIndex += 1


    return charsProcessed

print(findStartOfPacket(line))