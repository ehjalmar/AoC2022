file = open('Day6/input.txt','r')
line = file.readline()

def is_isogram(string):
    for i in string:
        if string.count(i) > 1:
            return False
    return True

def findStartOfMessage(inputText):
    currentIndex = 0
    
    while True:
        currentBatch = inputText[currentIndex:currentIndex+14]
        if is_isogram(currentBatch):
            break
        else:
            currentIndex += 1

    return currentIndex + 14

print(findStartOfMessage(line))