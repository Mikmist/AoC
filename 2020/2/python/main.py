import re

count = 0
with open('../input/input') as data:
    for line in data:
        parts = line.split(' ')
        number_range = parts[0].split('-')
        count_chars = int(parts[2].count(parts[1][0]))
        if count_chars >= int(number_range[0]) and count_chars <= int(number_range[1]):
            count += 1

print("part 1: " + str(count))

count = 0
with open('../input/input') as data:
    for line in data:
        parts = line.split(' ')
        number_range = parts[0].split('-')
        string = parts[2][:-1]
        if bool(string[int(number_range[0]) - 1] == parts[1][0]) != bool(string[int(number_range[1]) - 1] == parts[1][0]):
            count += 1

print("part 2: " + str(count))
