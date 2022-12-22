
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
  
    

with open('../input/test') as data:
    sides = [set() for _ in range(6)]
    cnt = 0
    for line in data:
        x,y,z = [int(i) for i in line.strip().split(',')]
        print(x,y,z)
        cnt += calculate_side_coords(sides,x,y,z)
    print(cnt)
        
