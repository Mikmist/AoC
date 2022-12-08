from collections import defaultdict

def get_directional(map, direction, i, j):
    if direction == 0: #L R
        return (map[i][j], i,j)
    if direction == 1: #T B 
        return (map[j][i], j, i)
    if direction == 2: #B T
        return(map[len(map) - j - 1][len(map) - i - 1], len(map) -1-j, len(map)-i-1) 
    if direction == 3: #R L
        return (map[len(map) - i - 1][len(map) - j - 1], len(map) -1-i, len(map)-j-1)

with open('../input/input') as data:
    map = []
    for line in data:
        row = []
        for num in line.strip():
            row.append(int(num))
        map.append(row)
    visible = defaultdict(int) 
    for dir in range(0,4):
        for i in range(len(map)):
            prev = -1
            for j in range(len(map[i])):
                val, x, y = get_directional(map, dir, i, j) 
                if val > prev:
                    visible[(x,y)] += 1
                    prev = val
    cnt = 0
    for i in range(len(map)):
        for j in range(len(map[i])):
            if visible[(i,j)]:
                cnt += 1
    print(cnt)
