import re;

class Map:
    def __init__(self):
        self.xmin = -10
        self.xmax = 30
        self.ymin = -10
        self.ymax = 30
        self.map = {}
        self.sensor_ranges = []
        self.possibilities = []

    def add_sensor_and_beacon(self, sx, sy, bx, by):
        print(sx, sy, bx, by)
        self.map[(sx, sy)] = 'S'
        self.map[(bx, by)] = 'B'
        self.xmin=min(min(sx,bx), self.xmin)
        self.xmax=max(max(sx,bx), self.xmax)
        self.ymin=min(min(sy,by), self.ymin)
        self.ymax=max(max(sy,by), self.ymax)
        
        manhatten_distance = abs(sx-bx) + abs(sy-by)
        self.sensor_ranges.append((sx, sy, manhatten_distance))
        
        for y in range(0, manhatten_distance+1+1):
            xm = manhatten_distance + 1 - y 
            #self.map[sx-xm,sy+y] = '#'
            #self.map[sx-xm,sy-y] = '#'
            #self.map[sx+xm,sy+y] = '#'
            #self.map[sx+xm,sy-y] = '#'
            self.possibilities.append((sx-xm,sy+y))
            self.possibilities.append((sx-xm,sy-y))
            self.possibilities.append((sx+xm,sy+y))
            self.possibilities.append((sx+xm,sy-y))

    def is_in_sensor_range(self, i):
        for sx, sy, man in self.sensor_ranges:
            man_i = abs(sx-i[0]) + abs(sy-i[1])
            if man_i <= man: return True


    def check(self, max_d):
        for i in self.possibilities:
            if (not self.is_in_sensor_range(i)) and i[0] > 0 and i[0] <= max_d and i[1] > 0 and i[1] <= max_d:
                print(i[0]*4_000_000+i[1])
                self.map[i[0], i[1]] = 'I'

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
    for line in data:
        sx, sy, bx, by = [int(x) for x in re.findall("[-\d]+", line.strip())]
        map.add_sensor_and_beacon(sx, sy, bx, by)
    map.check(4_000_000)
