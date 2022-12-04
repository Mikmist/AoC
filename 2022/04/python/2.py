def compare_sets(set1, set2):
    return set1[0] <= set2[1] and set1[1] >= set2[0]

with open('../input/input') as data:
    total = 0
    for line in data:
        sets = [[int(j) for j in i.split('-')] for i in line.strip().split(',')]
        if compare_sets(sets[0], sets[1]) or compare_sets(sets[1], sets[0]): 
            total += 1
    print(total)


