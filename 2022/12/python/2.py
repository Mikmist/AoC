from queue import Queue

def explore_map(map, height, width, goal, start):
    q = Queue()
    q.put((start[0],start[1],0))
    visited = {(start[0], start[1])}
    while not q.empty():
        x, y, steps = q.get()
        if x == goal[0] and y == goal[1]:
            return steps
        for x1, y1 in [(1,0), (0,1), (-1,0), (0, -1)]:
            x2 = x1 + x
            y2 = y1 + y
            if (x2,y2) in visited:
                continue
            if x2 > -1 and x2 < width and y2 > -1 and y2 < height and map[y2][x2] - map[y][x]  < 2: 
                q.put((x2, y2, steps+1)) 
                visited.add((x2,y2))
    return 9999999999
                

with open('../input/input') as data:
    map = [[ord(char) for char in line.strip()] for line in data]
    goal = None
    res = 1000000000
    for y in range(len(map)):
        for x in range(len(map[y])):
            if map[y][x] == ord('E'):
                goal = (x,y)
                map[y][x] = ord('z')
            if map[y][x] == ord('S'):
                map[y][x] = ord('a') 
    for y in range(len(map)):
        for x in range(len(map[y])):
            if map[y][x] == ord('a'):
                start = (x,y)
                res = min(res, explore_map(map, len(map), len(map[0]), goal, start))
    print(res)

