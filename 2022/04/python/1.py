with open('../input/input') as data:
    total = 0
    for line in data:
        sets = [[int(j) for j in i.split('-')] for i in line.strip().split(',')]
        if sets[0][0] <= sets[1][0] and sets[0][1] >= sets[1][1] or sets[1][0] <= sets[0][0] and sets[1][1] >= sets[0][1]:
            total += 1
    print(total)
