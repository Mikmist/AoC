with open('../input/input') as data:
    galaxies = set() 
    non_empty_cols = set()
    data_copy = []
    for line in data:
        data_copy.append(line.strip())
        x = 0
        for i in line.strip():
            if i == '#':
                non_empty_cols.add(x)
            x += 1
    expanders = {}
    
    c = 0
    for i in range(len(data_copy[0])):
        expanders[i] = c
        if i not in non_empty_cols:
            c += 999_999

    y = 0
    for line in data_copy:
        x = 0
        f = False
        for i in line:
            if i == '#':
                galaxies.add((x+expanders[x],y))
                f = True
            x += 1
        y += 1
        if not f:
            y += 999_999
    s = 0

    for i in range(len(galaxies)):
        g = galaxies.pop()
        for j in galaxies:
            s += abs(g[0]-j[0]) + abs(g[1]-j[1])
    print(s)
