import math

file=open('Day2/input.txt', 'r')
lines = file.readlines()

myTotalScore = 0

for line in lines:
    actions = list(filter(None, line.strip('\n').split(' ')))
#    print(actions)
    opponentAction = actions[0]
    myAction = actions[1]
    if(myAction == "X"): # ROCK
        myTotalScore += 1
        if(opponentAction == "A"): # DRAW
            myTotalScore += 3
        elif(opponentAction == "C"): # WIN
            myTotalScore += 6
    elif(myAction == "Y"): # PAPER
        myTotalScore += 2
        if(opponentAction == "B"):
            myTotalScore += 3
        elif(opponentAction == "A"):
            myTotalScore += 6
    elif(myAction == "Z"): # SCISSORS
        myTotalScore += 3
        if(opponentAction == "C"):
            myTotalScore += 3
        elif(opponentAction == "B"):
            myTotalScore += 6

print(myTotalScore)