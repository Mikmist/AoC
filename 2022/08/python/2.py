from collections import defaultdict

def explore_directions(map, i, j, height):
    total = 1
    cnt =1 
    o = i+1
    while o < len(map)-1:
        if map[o][j] < height:
            cnt += 1
        else:
            break
        o += 1
    o = i-1
    total *= cnt
    cnt = 1
    while o >= 1:
        if map[o][j] < height:
            cnt += 1
        else:
            break
        o -= 1
    k = j+1
    total *= cnt
    cnt = 1
    while k < len(map)-1:
        if map[i][k] < height:
            cnt += 1
        else:
            break
        k += 1
    k = j-1
    total *= cnt
    cnt = 1
    while k >= 1:
        if map[i][k] < height:
            cnt += 1
        else:
            break
        k -= 1
    total *= cnt
    return total

with open('../input/input') as data:
    map = []
    for line in data:
        row = []
        for num in line.strip():
            row.append(int(num))
        map.append(row)
    score = 0
    for i in range(1, len(map) - 1):
        for j in range(1, len(map) - 1):
            tmp= explore_directions(map, i, j, map[i][j])
            if tmp>score:
                score = tmp

    print(score)
