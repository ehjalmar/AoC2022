file = open('Day8/input.txt', 'r')
lines = file.read().splitlines()

class tree:
    def __init__(self, row, column, height) -> None:
        self.row = row
        self.column = column
        self.height = height

trees = []

# for each column in each row...
for row, line in enumerate(lines):
    for column in range(len(line)):
        currentNumber = line[column]
        trees.append(tree(row, column, currentNumber))

visibleOnEdge = 0

for currentTree in trees:
    if(currentTree.row == 0 or currentTree.row == len(lines)-1): # don't count first or last row
        continue
    if(currentTree.column == 0 or currentTree.column == len(lines[0])-1): # don't count first or last column
        continue
    
    higherRight = len(list(filter(lambda tree: tree.row == currentTree.row and tree.column > currentTree.column and tree.height >= currentTree.height, trees))) # Right
    higherLeft = len(list(filter(lambda tree: tree.row == currentTree.row and tree.column < currentTree.column and tree.height >= currentTree.height, trees))) # Left
    higherAbove = len(list(filter(lambda tree: tree.row < currentTree.row and tree.column == currentTree.column and tree.height >= currentTree.height, trees))) # Above
    higherBelow = len(list(filter(lambda tree: tree.row > currentTree.row and tree.column == currentTree.column and tree.height >= currentTree.height, trees))) # Below
    
    #print(currentTree.row.__str__() + " " + currentTree.column.__str__())
    
    if(higherRight == 0 or higherLeft == 0 or higherAbove == 0 or higherBelow == 0):
        visibleOnEdge += 1

frame = len(lines) * 2
frame += (len(lines[0]) * 2) - 4

print(frame + visibleOnEdge)