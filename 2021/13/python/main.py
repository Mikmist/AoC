with open('../input/input') as data:
    coords = {}
    maxY = 0
    maxX = 0
    orders = []
    # Parsing
    for line in data:
        if (line == "\n"):
            break
        x, y = line.strip().split(',')
        maxY = max(maxY, int(y) + 1)
        maxX = max(maxX, int(x) + 1)
        coords[(str(x) + "," + str(y))] = True
    for line in data:
        axis, index = line.strip().split(" ")[-1].split('=')
        orders += [{
            "axis": axis,
            "index": int(index)
        }]
    
    foldingMap = [['.' for x in range(maxX)] for y in range(maxY)]
    for coord in coords:
        coordParts = coord.split(',')
        foldingMap[int(coordParts[1])][int(coordParts[0])] = '#'
    
    first = True
    for order in orders:
        if order['axis'] == 'x':
            for y in range(maxY):
                for x in range(maxX // 2 + 1):
                    if foldingMap[y][order['index'] - x] == '#':
                        continue
                    if foldingMap[y][order['index'] + x] == '#':
                        foldingMap[y][order['index'] - x] = '#'
            maxX = order['index']
        if order['axis'] == 'y':
            for y in range(maxY//2 + 1):
                for x in range(maxX):
                    # print(x, y)
                    if foldingMap[order['index'] - y][x] == '#':
                        continue
                    if foldingMap[order['index'] + y][x] == '#':
                        foldingMap[order['index'] - y][x] = '#'
            maxY = order['index']
        if first:
            countA = 0
            for y in range(maxY):
                for x in range(maxX):
                    if foldingMap[y][x] == '#':
                        countA += 1
            first = False
            print("Part A:", countA)

    print("Part B: Requires reading characters below.")
    for y in range(maxY):
        for x in range(maxX):
            print(foldingMap[y][x], end="")
        print()

