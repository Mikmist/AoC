def who_win(a, b):
    if a == 'A':
        if b == 'X':
            return 0
        if b == 'Y':
            return 1
        if b == 'Z':
            return -1
    if a == 'B':
        if b == 'X':
            return -1
        if b == 'Y':
            return 0 
        if b == 'Z':
            return 1
    if a == 'C':
        if b == 'X':
            return 1 
        if b == 'Y':
            return -1
        if b == 'Z':
            return 0 

def get_value(type):
    values = {
            'X': 1,
            'Y': 2,
            'Z': 3
            }
    return values[type]

def run(type):
    with open(type) as data:
        total = 0
        for line in data:
            a, b = line.strip().split(' ')
            if who_win(a, b) == 0:
                total += 3
            if who_win(a, b) == 1:
                total += 6
            total += get_value(b)
            print(total)
            
run('../input/test')
run('../input/input')
