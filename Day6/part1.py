file = open('Day6/input.txt','r')
line = file.readline()

def is_isogram(string):
    for i in string:
        if string.count(i) > 1:
            return False
    return True

def findStartOfPacket(inputText):
    currentIndex = 0
    
    while True:
        currentBatch = inputText[currentIndex:currentIndex+4]
        if is_isogram(currentBatch):
            break
        else:
            currentIndex += 1

    return currentIndex + 4

print(findStartOfPacket(line))