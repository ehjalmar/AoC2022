class Elf:
    def __init__(self, workingRange):
        self.WorkingRange = workingRange
        self.WorkingRangeStart = int(workingRange.split('-')[0])
        self.WorkingRangeEnd = int(workingRange.split('-')[1])