def value_of_choice(a, b):
    if a == 'A':
        if b == 'X':
            return 3
        if b == 'Y':
            return 1
        if b == 'Z':
            return 2 
    if a == 'B':
        if b == 'X':
            return 1
        if b == 'Y':
            return 2 
        if b == 'Z':
            return 3
    if a == 'C':
        if b == 'X':
            return 2 
        if b == 'Y':
            return 3 
        if b == 'Z':
            return 1 

def run(type):
    with open(type) as data:
        total = 0
        for line in data:
            a, b = line.strip().split(' ')
            if b == 'Y':
                total += 3
            if b == 'Z':
                total += 6
            total += value_of_choice(a, b)
            print(total)
            
run('../input/test')
run('../input/input')
