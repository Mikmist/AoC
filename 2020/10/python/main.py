adapters = []
with open('../input/input') as data:
    for line in data:
        adapters.append(int(line))

adapters.append(0)

# Part 1
adapters.sort()
one_differences = 0
# Starts at 1 to account for our own device going 3 higher.
three_differences = 0
index = 0
while index < len(adapters):
    if index + 1 != len(adapters):
        difference = adapters[index + 1] - adapters[index]
    else:
        difference = 3
    if difference == 1:
        one_differences += 1
    if difference == 3:
        three_differences += 1
    index += 1

print('Part 1:', one_differences * three_differences)

# Part 2
def count_options(index, nodes, lookup):
    result = 0

    indexes_to_visit = []
    if index not in lookup:
        for i in range(index + 1, index + 4):
            if i < len(nodes):
                if nodes[i] - nodes[index] in (1, 2, 3):
                    indexes_to_visit.append(i)
            else:
                break

        if indexes_to_visit:
            for index_to_visit in indexes_to_visit:
                result += count_options(index_to_visit, nodes, lookup)
                lookup[index] = result
        else:
            return 1
    print(lookup)
    return lookup[index]
    
print(count_options(0, adapters, {}))
