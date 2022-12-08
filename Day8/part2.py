file = open('Day8/input.txt', 'r')
lines = file.read().splitlines()

class tree:
    def __init__(self, row, column, scenicScore) -> None:
        self.row = row
        self.column = column
        self.scenicScore = scenicScore

trees = []
numberOfColumns = len(lines[0])

# for each column in each row...
for row, line in enumerate(lines):
    for column in range(numberOfColumns):
        currentNumber = line[column]
        scenicScoreRight = 0
        scenicScoreLeft = 0
        scenicScoreAbove = 0
        scenicScoreBelow = 0        
        compareWith = None

        # check to the right
        columnCounter = column + 1
        while(columnCounter < numberOfColumns):
            compareWith = line[columnCounter]
            scenicScoreRight += 1
            if(compareWith >= currentNumber):
                break
            columnCounter += 1
        
        # check to the left
        columnCounter = column - 1
        while(columnCounter >= 0):
            compareWith = line[columnCounter]
            scenicScoreLeft += 1
            if(compareWith >= currentNumber):
                break
            columnCounter -= 1
        
        # check up
        rowCounter = row - 1
        while(rowCounter >= 0):
            compareWith = lines[rowCounter][column]
            scenicScoreAbove += 1
            if(compareWith >= currentNumber):
                break
            rowCounter -= 1
        
        # check down
        rowCounter = row + 1
        while(rowCounter >= 0 and rowCounter < len(lines)):
            compareWith = lines[rowCounter][column]
            scenicScoreBelow += 1
            if(compareWith == currentNumber):
                break
            rowCounter += 1

        trees.append(tree(row, column, scenicScoreBelow*scenicScoreAbove*scenicScoreLeft*scenicScoreRight))

trees.sort(key=lambda x: x.scenicScore, reverse=True)

print(trees[0].scenicScore)