data_list = []

with open('data') as data:
    for line in data:
        data_list.append(int(line))

# Part 1
for i in data_list:
    for j in data_list:
        if i + j == 2020:
            print(i * j)
            break

# Part 2
for i in data_list:
    for j in data_list:
        for k in data_list:
            if (i + j + k) == 2020:
                print(i * j * k)
                break
