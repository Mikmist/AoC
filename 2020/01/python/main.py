data_list = []

with open('../input/input') as data:
    for line in data.read().split(' '):
        data_list.append(int(line))

# Part 1
found = False
for i in data_list:
    if found:
        break
    for j in data_list:
        if i + j == 2020:
            print(i * j)
            found = True
            break

# Part 2
found = False
for i in data_list:
    if found:
        break
    for j in data_list:
        if found:
            break
        for k in data_list:
            if (i + j + k) == 2020:
                print(i * j * k)
                found = True
                break
