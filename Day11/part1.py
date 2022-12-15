file = open('Day11/input.txt', 'r')
lines = file.read().splitlines()

class Monkey:
    def __init__(self, number, operator, secondInput, items, divisibleBy, destinationTrue, destinationFalse) -> None:
        self.Number = number
        self.Operator = operator
        self.SecondInput = secondInput
        self.Items = items
        self.DivisibleBy = divisibleBy
        self.DestinationTrue = destinationTrue
        self.DestinationFalse = destinationFalse
    
    def addItem(self, newItem):
        self.Items.append(newItem)

    def inspect(self):
        for item in self.Items:
            secondOperator = None
            if(self.SecondInput == 'old'):
                secondOperator = item
            else:
                secondOperator = int(self.SecondInput)

            result = 0
            if(self.Operator == '*'):
                result = item * secondOperator
            else:
                result = item + secondOperator
            
            result =  int(result / 3)

            if(result % self.DivisibleBy == 0):
                monkies[self.DestinationTrue].addItem(result)
            else:
                monkies[self.DestinationFalse].addItem(result)
            
            monkeyThrows[self.Number] += 1
        
        self.Items = []
        
        

monkies = []
currentLine = 0

while(currentLine < len(lines)):
    if(lines[currentLine] == ''):
        currentLine += 1 # Skip empty line
    
    monkeyNr =  int(lines[currentLine].strip('Monkey ').strip(':'))
    currentLine += 1
    startingItems = [int(x) for x in lines[currentLine].strip('  Starting items: ').split(',')]
    currentLine += 1
    operator = lines[currentLine].split(' ')[6]
    secondInput = lines[currentLine].split(' ')[7]
    currentLine += 1
    divisibleBy = int(lines[currentLine].split(' ')[5])
    currentLine += 1
    destinationTrue = int(lines[currentLine].split(' ')[9])
    currentLine += 1
    destinationFalse = int(lines[currentLine].split(' ')[9])
    currentLine += 1
    monkies.append(Monkey(monkeyNr, operator, secondInput, startingItems, divisibleBy, destinationTrue, destinationFalse))

rounds = 20
monkeyThrows = [0] * len(monkies)

for round in range(rounds):
    for monkey in monkies:
        monkey.inspect()

monkeyThrows = sorted(monkeyThrows, key=int, reverse=True)

print('Monkey business: ' + str(monkeyThrows[0]*monkeyThrows[1]))