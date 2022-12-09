from collections import defaultdict

class Board:
    def __init__(self):
        self.xT = 0
        self.yT = 0
        self.xH = 0
        self.yH = 0
        self.visitedH = defaultdict(int)
        self.visitedT = defaultdict(int)

    def compute_tail_move(self, direction):
        x_move = abs(self.xT - self.xH)
        y_move = abs(self.yT - self.yH)
        if x_move > 1 and y_move > 0:
            self.yT = self.yH
        if y_move > 1 and x_move > 0:
            self.xT = self.xH
        if x_move > 1:
            self.xT += 1 if direction == 'R' else -1
        if y_move > 1:
            self.yT += 1 if direction == 'U' else -1
        self.visitedT[(self.xT, self.yT)] += 1
        print(len(self.visitedT))


    def move(self, direction, amount):
        for i in range(0, amount):
            if direction == 'R':
                self.xH += 1
            if direction == 'L':
                self.xH -= 1
            if direction == 'D':
                self.yH -= 1
            if direction == 'U':
                self.yH += 1
            self.compute_tail_move(direction)
    
    def draw(self):
        for y in range(4, -1, -1):
            for x in range(0, 6):
                if x == self.xH and y == self.yH:
                    print('H', end='')
                elif x == self.xT and y == self.yT:
                    print('T', end='')
                elif x == 0 and y == 0:
                    print('s', end='')
                else:
                    print('.', end='')
            print('\n')
        print()


with open('../input/input') as data:
    board = Board()
    for line in data:
        print(line.strip())
        parts = line.strip().split(' ')
        board.move(parts[0], int(parts[1]))
