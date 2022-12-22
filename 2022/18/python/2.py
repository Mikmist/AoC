from dataclasses import dataclass, field
from typing import Any
from queue import PriorityQueue

@dataclass(order=True)
class PItem:
    priority: int
    item: Any=field(compare=False)

cubes = set()
def add_air_cubes(x, y, z, xd, yd, zd, xb, yb, zb):
    global cubes
    if x < xd or y < yd or z < zd or x > xb or y > yb or z > zb:
        return
    if (x,y,z) in cubes:
        return

    q = PriorityQueue()
    q.put(PItem(0, (x,y,z)))
    while not q.empty():
        item = q.get()
        x, y, z = item.item
    
        for i,j,k in [(1,0,0), (-1,0,0), (0,1,0), (0,-1,0), (0,0,1), (0,0,-1)]:
            if x+i < xd or y+j < yd or z+k < zd or x+i > xb or y+j > yb or z+k > zb:
                continue
            if (x+i,y+j,z+k) in cubes:
                continue
            cubes.add((x+i,y+j,z+k))
            q.put(PItem(item.priority+1, (x+i,y+j,z+k)))

def calculate_side_coords(sides, x,y,z):
    sides[0].add((x+1,y,z))
    sides[1].add((x,y+1,z))
    sides[2].add((x,y,z+1))
    sides[3].add((x-1,y,z))
    sides[4].add((x,y-1,z))
    sides[5].add((x,y,z-1))
        
    s = 6
    for i in range(6):
        if (x,y,z) in sides[i]: s -= 2
    return s

def calculate_face_sizes(xd, xb, yd, yb, zd, zb):
    if (xd==0): xb-1
    if (yd==0): yb-1
    if (zd==0): zb-1
    return xb*yb*2+xb*zb*2+zb*yb*2

with open('../input/input') as data:
    cnt_a = 0; xd=1000; yd=1000; zd=1000; xb=0; yb=0; zb=0; 
    sides = [set() for _ in range(6)]
    for line in data:
        x,y,z = [int(i) for i in line.strip().split(',')]
        xb = max(xb, x)
        yb = max(yb, y)
        zb = max(zb, z)
        xd = min(xd, x)
        yd = min(yd, y)
        zd = min(zd, z)
        cubes.add((x,y,z))
        cnt_a += calculate_side_coords(sides,x,y,z)
    print(len(cubes))
    for i in range(xd,xb+1):
        add_air_cubes(i, y, z, xd, yd, zd, xb, yb, zb)
    print(len(cubes))
    for i in range(yd,yb+1):
        add_air_cubes(x, i, z, xd, yd, zd, xb, yb, zb)
    print(len(cubes))
    for i in range(zd,zb+1):
        add_air_cubes(x, y, i, xd, yd, zd, xb, yb, zb)
    print(cubes)
    print(xb, yb, zb, (xb+1)*yb*(zb+1))
    print("Part 1: ", cnt_a)
    #print("Part 2: ", cnt_a - ((xb+1)*yb*(zb+1)-len(cubes))*6)

    sides = [set() for _ in range(6)]
    cnt = 0
    for x,y,z in cubes:
        cnt += calculate_side_coords(sides,x,y,z)
    
    print("Part 2: ",calculate_face_sizes(xd,xb,yd,yb,zd,zb)-2)
        
