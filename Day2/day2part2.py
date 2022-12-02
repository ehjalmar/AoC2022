import math

file=open('Day2/input.txt', 'r')
lines = file.readlines()

rounds = list()

for line in lines:
    actions = list(filter(None, line.strip('\n').split(' ')))
#    print(actions)
    opponentAction = actions[0]
    myResultShouldBe = actions[1]
    if(opponentAction == "A"): # ROCK
        if(myResultShouldBe == "X"): # LOOSE
            rounds.append("A Z")
        elif(myResultShouldBe == "Y"): # DRAW
            rounds.append("A X")
        elif(myResultShouldBe == "Z"): # WIN
            rounds.append("A Y")
    elif(opponentAction == "B"): # PAPER
        if(myResultShouldBe == "X"): # LOOSE
            rounds.append("B X")
        elif(myResultShouldBe == "Y"): # DRAW
            rounds.append("B Y")
        elif(myResultShouldBe == "Z"): # WIN
            rounds.append("B Z")
    elif(opponentAction == "C"): # SCISSORS
        if(myResultShouldBe == "X"): # LOOSE
            rounds.append("C Y")
        elif(myResultShouldBe == "Y"): # DRAW
            rounds.append("C Z")
        elif(myResultShouldBe == "Z"): # WIN
            rounds.append("C X")

myTotalScore = 0

for rond in rounds:
    actions = rond.split(' ')
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