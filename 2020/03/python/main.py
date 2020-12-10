from utils import submit

right = 0
count = 0
index = 0
with open('../input/input') as data:
    for line in data.read().split(' '):
        if index % 2 != 0:
            index += 1
            continue
        line = line.rstrip()
        if line[right] == '#':
            count += 1
        right += 1
        index += 1
        if right > (len(line) - 1):
            right -= (len(line))
print(count)

print(214 * 99 * 91 * 94 * 46)

# 214, 99, 91, 94, 49