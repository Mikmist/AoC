import re;

class Map:
    def __init__(self):
        self.xmin = 0
        self.xmax = 0
        self.ymin = 0
        self.ymax = 0
        self.map = {}
        self.ranges = []

    def add_sensor_and_beacon(self, sx, sy, bx, by, y):
        print(sx, sy, bx, by)
        self.map[(sx, sy)] = 'S'
        self.map[(bx, by)] = 'B'
        self.xmin=min(min(sx,bx), self.xmin)
        self.xmax=max(max(sx,bx), self.xmax)
        self.ymin=min(min(sy,by), self.ymin)
        self.ymax=max(max(sy,by), self.ymax)
        manhatten_distance = abs(sx-bx) + abs(sy-by)
        distance_to_y = abs(y-sy)
        #print(distance_to_y, manhatten_distance)
        side = manhatten_distance-distance_to_y
        if side > 0:
            coords = (sx-side, sx+side)
            #for i in range(coords[0], coords[1]+1):
            self.ranges.append(coords)

    def check_y(self, y):
        cnt = 0
        for i in range(self.xmin-1_000_000, self.xmax+1_000_000):
            if i % 10_000 == 0: print(i)
            valid = False
            for c in self.ranges:
                #print(i, c)
                if i >= c[0] and i <= c[1] and (i,y) not in self.map:
                    valid = True
                    break
            if valid: cnt += 1
        return cnt


    def draw(self):
        for y in range(self.ymin, self.ymax+1):
            for x in range(self.xmin, self.xmax+1):
                if (x,y) in self.map:
                    print(self.map[(x,y)], end='')
                else:
                    print('.', end='')
            print()

with open('../input/input') as data:
    map = Map()
    y = 2_000_000
    for line in data:
        sx, sy, bx, by = [int(x) for x in re.findall("[\d]+", line.strip())]
        map.add_sensor_and_beacon(sx, sy, bx, by, y)
    print(map.ranges)
    print(map.check_y(y))
