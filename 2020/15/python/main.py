from utils import printProgressBar


class NumberMemory:
    def __init__(self, number, lastTurn):
        self.number = number
        self.lastTurn = lastTurn
        self.turnBeforeLast = -1

    def difference(self):
        if self.turnBeforeLast == -1:
            return 0
        return self.lastTurn - self.turnBeforeLast

    def numberSpoken(self, turn):
        self.turnBeforeLast = self.lastTurn
        self.lastTurn = turn

    def isFirstTime(self):
        return self.turnBeforeLast == -1


with open('../input/input') as data:
    turn = 1
    lastNumber = None
    numbers = {}
    for line in data:
        for val in line.strip().split(','):
            number = int(val)
            numbers[number] = NumberMemory(number, turn)
            lastNumber = number
            turn += 1

    while turn < 30000001:
        if lastNumber in numbers:
            if numbers[lastNumber].isFirstTime():
                currentNumber = 0
                if currentNumber in numbers:
                    numbers[currentNumber].numberSpoken(turn)
                else:
                    numbers[currentNumber] = NumberMemory(currentNumber, turn)
            else:
                currentNumber = numbers[lastNumber].difference()
                if currentNumber in numbers:
                    numbers[currentNumber].numberSpoken(turn)
                else:
                    numbers[currentNumber] = NumberMemory(currentNumber, turn)
        else:
            currentNumber = 0
            if currentNumber in numbers:
                numbers[currentNumber].numberSpoken(turn)
            else:
                numbers[currentNumber] = NumberMemory(currentNumber, turn)
        if turn == 2020:
            print('Part 1:', currentNumber)
        if turn % 100000 == 0:
            printProgressBar(turn, 30000000, 'Progress:')
        if turn == 30000000:
            print('Part 2:', currentNumber)
        lastNumber = currentNumber
        turn += 1