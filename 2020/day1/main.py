list = []

with open('data') as data:
    for line in data:
        list.append(int(line))

for i in list:
    for j in list:
        for k in list:
            if (i + j + k) == 2020:
                print(i * j * k)
