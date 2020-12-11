import time

def in_seats(seats, i, j):
    if i < 0 or j < 0:
        return False
    try:
        seats[int(i)][int(j)]
    except (ValueError, IndexError):
        return False
    else:
        return True


# Returns True if a neighbour is found, else False
def explore_visible_line(seats, i, j, i_modifier, j_modifier):
    if not in_seats(seats, i + i_modifier, j + j_modifier):
        return False
    if seats[i + i_modifier][j + j_modifier] == 'L':
        return False
    if seats[i + i_modifier][j + j_modifier] == '#':
        return True
    return False or explore_visible_line(seats, i + i_modifier, j + j_modifier, i_modifier, j_modifier)


def count_visible_neighbours(seats):
    counts = []
    for i in range(len(seats)):
        counts_row = []
        row = seats[i]
        for j in range(len(row)):
            char = row[j]
            length = len(row) - 1
            count = 0
            count += 1 if explore_visible_line(seats, i, j, 0, 1) else 0
            count += 1 if explore_visible_line(seats, i, j, 1, 1) else 0
            count += 1 if explore_visible_line(seats, i, j, 1, 0) else 0
            count += 1 if explore_visible_line(seats, i, j, 1, -1) else 0
            count += 1 if explore_visible_line(seats, i, j, 0, -1) else 0
            count += 1 if explore_visible_line(seats, i, j, -1, -1) else 0
            count += 1 if explore_visible_line(seats, i, j, -1, 0) else 0
            count += 1 if explore_visible_line(seats, i, j, -1, 1) else 0
            counts_row.append(count)
        counts.append(counts_row)
    return counts


def count_direct_neighbours(seats):
    counts = []
    for i in range(len(seats)):
        counts_row = []
        row = seats[i]
        for j in range(len(row)):
            length = len(row) - 1
            count = 0
            if i > 0:
                if j > 0 and seats[i - 1][j - 1] == '#':
                    count += 1
                if seats[i - 1][j] == '#':
                    count += 1
                if j < length and seats[i - 1][j + 1] == '#':
                    count += 1
            if j > 0 and seats[i][j - 1] == '#':
                count += 1
            if j < length and seats[i][j + 1] == '#':
                count += 1
            if i < len(seats) - 1:
                if j > 0 and seats[i + 1][j - 1] == '#':
                    count += 1
                if seats[i + 1][j] == '#':
                    count += 1
                if j < length and seats[i + 1][j + 1] == '#':
                    count += 1
            counts_row.append(count)
        counts.append(counts_row)
    return counts


def print_seats(seats, neighbour_map):
    for i in range(len(seats)):
        for char in seats[i]:
            print(char, end='')
        print(' ', end='')
        for number in neighbour_map[i]:
            print(number, end=',')
        print()
    print()


def calculate_occupied(algorithm, seats):
    change = True
    neighbour_map = []
    while change:
        change = False
        seats_replace = []
        if algorithm == 'direct':
            neighbour_map = count_direct_neighbours(seats)
        if algorithm == 'visible':
            neighbour_map = count_visible_neighbours(seats)
        # print_seats(seats, neighbour_map)
        for i in range(len(seats)):
            new_row = []
            for j in range(len(seats[i])):
                char = seats[i][j]
                seated_neighbours = neighbour_map[i][j]
                if char == 'L' and seated_neighbours == 0:
                    new_state = '#'
                    change = True
                elif char == '#' and (algorithm == 'direct' and seated_neighbours > 3 or algorithm == 'visible' and seated_neighbours > 4):
                    new_state = 'L'
                    change = True
                else:
                    new_state = char
                new_row.append(new_state)
            seats_replace.append(new_row)
        seats = seats_replace

    count_occupied = 0
    for row in seats:
        for char in row:
            if char == '#':
                count_occupied += 1
    return count_occupied


seats = []
with open('../input/input') as data:
    for line in data:
        row = []
        for character in line.strip():
            row.append(character)
        seats.append(row)

print('Part 1:', calculate_occupied('direct', [row[:] for row in seats]))
print('Part 2:', calculate_occupied('visible', [row[:] for row in seats]))