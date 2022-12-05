class Instruction:
    def __init__(self, instructions) -> None:
        self.amountToMove = int(instructions[1])
        self.fromIndex = int(instructions[3])-1
        self.toIndex = int(instructions[5])-1