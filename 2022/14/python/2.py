import time

class Map:
    def __init__(self):
        self.xmin = 0
        self.xmax = 0
        self.ymin = 500
        self.ymax = 500
        self.map = {}
        self.cnt = 0

    def add_line_to_map(self, start, end):
        if start[0] == end[0]:
            q = max(start[1], end[1])
            w = min(start[1], end[1])
            if start[0] > self.ymax: self.ymax = start[0]
            if start[0] < self.ymin: self.ymin = start[0]
            if q > self.xmax: self.xmax = q 
            if w < self.xmin: self.xmin = w 
            for i in range(w, q+1):
                self.map[(i, start[0])] = '#'
        else:
            q = max(start[0], end[0])
            w = min(start[0], end[0])
            if start[1] > self.xmax: self.xmax = start[1]
            if start[1] < self.xmin: self.xmin = start[1]
            if q > self.ymax: self.ymax = q 
            if w < self.ymin: self.ymin = w 
            for i in range(w, q+1):
                self.map[(start[1], i)] = '#'

    def return_sand_move(self, x, y):
        if (x+1, y) not in self.map:
            return (x+1, y)
        if (x+1, y-1) not in self.map:
            return (x+1, y-1)
        if (x+1, y+1) not in self.map:
            return(x+1, y+1) 
        return (x,y) 


    def drop_sand_till_abyss(self, animate):
        self.add_line_to_map([self.ymin-500, self.xmax+2], [self.ymax+500, self.xmax+2])
        while True:
            current_sand = (0, 500)
            new_pos = self.return_sand_move(current_sand[0], current_sand[1])
            if new_pos == current_sand:
                self.map[current_sand] = 'o'
                self.cnt += 1
                break
            while new_pos != current_sand:
                current_sand = new_pos
                new_pos = self.return_sand_move(current_sand[0], current_sand[1])
            self.map[current_sand] = 'o'
            self.cnt += 1
            if animate: map.draw()

    def draw(self):
        for x in range(self.xmin, self.xmax+1):
            for y in range(self.ymin, self.ymax+1):
                if (x,y) in self.map:
                    print(self.map[(x,y)], end='')
                else:
                    print('.', end='')
            print()

with open('../input/input') as data:
    map = Map()
    animate = False
    for line in data:
        p = line.strip().split(' -> ')
        i = 0
        while i < len(p) - 1:
             map.add_line_to_map([int(x) for x in p[i].split(',')], [int(x) for x in p[i+1].split(',')])
             i+=1
    map.drop_sand_till_abyss(animate)
    print(map.cnt)
