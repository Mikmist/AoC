from utils import submit

with open('../input/input') as data:
    highest = 0
    seats = []
    for line in data.read().split(' '):
        index = 0
        row = 0
        rowHigher = 127
        rowLower = 0
        column = 0
        columnHigher = 7
        colunnLower = 0
        for letter in line:
            if index <= 6:
                if index == 6:
                    if letter == 'F':
                        row = rowLower
                    if letter == 'B':
                        row = rowHigher
                else:
                    if letter == 'F':
                        rowHigher -= (rowHigher - rowLower + 1) // 2
                    if letter == 'B':
                        rowLower += ((rowHigher - rowLower + 1) // 2)
            else:
                if index == 9:
                    if letter == 'L':
                        column = colunnLower
                    if letter == 'R':
                        column = columnHigher
                else:
                    if letter == 'L':
                        columnHigher -= (columnHigher - colunnLower + 1) // 2
                    if letter == 'R':
                        colunnLower += ((columnHigher - colunnLower + 1) // 2)
            index += 1
        seatID = row * 8 + column
        seats.append(seatID)
        if seatID > highest:
            highest = seatID

print('Part 1:', highest)
seats.sort()
last = seats[0] - 1
for seat in seats:
    if last + 1 != seat:
        print('Part 2:', seat - 1)
    last = seat