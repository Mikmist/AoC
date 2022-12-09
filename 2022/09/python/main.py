from collections import defaultdict
class Pos:
    def __init__(self):
        self.x = 0
        self.y = 0


class Board:
    def __init__(self):
        self.positions = [Pos() for _ in range(0, 10)]
        self.visitedTails = [defaultdict(int) for _ in range(0, 10)]

    def compute_tail_move(self, number):
        x_move = self.positions[number-1].x - self.positions[number].x
        y_move = self.positions[number-1].y - self.positions[number].y 
        if x_move > 1 or x_move < -1:
            self.positions[number].x += 1 if x_move > 1 else -1
            if y_move == 1 or y_move == -1:
                self.positions[number].y = self.positions[number-1].y
        if y_move > 1 or y_move < -1:
            self.positions[number].y += 1 if y_move > 1 else -1
            if x_move == 1 or x_move == -1:
                self.positions[number].x = self.positions[number-1].x
        self.visitedTails[number][(self.positions[number].x, self.positions[number].y)] += 1


    def move(self, direction, amount):
        for i in range(0, amount):
            if direction == 'R':
                self.positions[0].x += 1
            if direction == 'L':
                self.positions[0].x -= 1
            if direction == 'D':
                self.positions[0].y -= 1
            if direction == 'U':
                self.positions[0].y += 1
            for i in range(1,10):
                self.compute_tail_move(i)
    

    def draw(self):
        for y in range(15, -15, -1):
            for x in range(-15,15):
                if x == self.positions[0].x and y == self.positions[0].y:
                    print('H', end='')
                elif x == self.positions[1].x and y == self.positions[1].y:
                    print('1', end='')
                elif x == self.positions[2].x and y == self.positions[2].y:
                    print('2', end='')
                elif x == self.positions[3].x and y == self.positions[3].y:
                    print('3', end='')
                elif x == self.positions[4].x and y == self.positions[4].y:
                    print('4', end='')
                elif x == self.positions[5].x and y == self.positions[5].y:
                    print('5', end='')
                elif x == self.positions[6].x and y == self.positions[6].y:
                    print('6', end='')
                elif x == self.positions[7].x and y == self.positions[7].y:
                    print('7', end='')
                elif x == self.positions[8].x and y == self.positions[8].y:
                    print('8', end='')
                elif x == self.positions[9].x and y == self.positions[9].y:
                    print('9', end='')
                elif x == 0 and y == 0:
                    print('s', end='')
                else:
                    print('.', end='')
            print('\n')
        print()


with open('../input/input') as data:
    board = Board()
    for line in data:
        parts = line.strip().split(' ')
        board.move(parts[0], int(parts[1]))
    board.draw()
    print(len(board.visitedTails[9]))
