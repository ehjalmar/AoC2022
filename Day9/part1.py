file = open('Day9/input.txt')
lines = file.read().splitlines()

class Position:
    def __init__(self, x , y) -> None:
        self.x = x
        self.y = y

visited = []

def followHead(currentPositionHead, currentPositionTail):
    changedVert = False
    changedHor = False
    if(currentPositionHead.y - currentPositionTail.y == 2):
        currentPositionTail.y += 1
        changedHor = True
    if(currentPositionHead.y - currentPositionTail.y == -2):
        currentPositionTail.y -= 1
        changedHor = True
    if(currentPositionHead.x - currentPositionTail.x == 2):
        currentPositionTail.x += 1
        changedVert = True
    if(currentPositionHead.x - currentPositionTail.x == -2):
        currentPositionTail.x -= 1
        changedVert = True
    if(changedHor):
        currentPositionTail.x = currentPositionHead.x
    elif(changedVert):
        currentPositionTail.y = currentPositionHead.y

currentPositionHead = Position(1000,1000)
currentPositionTail = Position(1000,1000)
visited.append(currentPositionTail.x.__str__() + "  " + currentPositionTail.y.__str__())

for line in lines:
    move = line.split(' ')
    for step in range(int(move[1])):
        if(move[0] == 'U'):
            currentPositionHead.y += 1
            followHead(currentPositionHead, currentPositionTail)
        elif(move[0] == 'D'):
            currentPositionHead.y -= 1
            followHead(currentPositionHead, currentPositionTail)
        elif(move[0] == 'L'):
            currentPositionHead.x -= 1
            followHead(currentPositionHead, currentPositionTail)
        elif(move[0] == 'R'):
            currentPositionHead.x += 1
            followHead(currentPositionHead, currentPositionTail)
        if(currentPositionTail.x.__str__() + "  " + currentPositionTail.y.__str__() not in visited): # Don´t add if its already in the list
            visited.append(currentPositionTail.x.__str__() + "  " + currentPositionTail.y.__str__())
 
print(len(visited))
