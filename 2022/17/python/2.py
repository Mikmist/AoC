import time

rock_patterns = [
        ([(0,0),(1,0),(2,0),(3,0)], 0), 
        ([(1,0),(0,1),(1,1),(2,1),(1,2)], 2),
        ([(2,2),(2,1),(0,0),(1,0),(2,0)], 2), ([(0,0),(0,1),(0,2),(0,3)], 3),
        ([(0,0),(1,0),(0,1),(1,1)], 1)
        ]

def let_rock_fall(map, height_differences, spawn, commands, rock, k, highest_y, len_commands, rock_index):
    #print(map, spawn, rock, k)
    j = 0
    cycle=False
    while True:
        x_cur = 0; y_cur = 0
        ignore_move = False
        if j % 2 == 0:
            if commands[k] == '>': x_cur = 1
            else: 
                x_cur = -1
            k += 1
            if k == len_commands:
                k = 0
        else:
            y_cur = -1

        for x,y in rock:
            loc = x+spawn[0]+x_cur, y+spawn[1]+y_cur
            #print(loc, j, x_cur, y_cur)
            if j % 2 == 0 and (loc in map or loc[0] < 0 or loc[0] > 6):
                ignore_move = True
            elif loc in map or loc[1] < 0:
                for x,y in rock:
                    map[(x+spawn[0],y+spawn[1])] = '#'
                return (k, rock_patterns[rock_index][1]+spawn[1], rock[0][0]+spawn[0] == 1)
        j += 1
        if ignore_move:
            #print(f"Push {commands[k%len(commands)]} but nothing happens.")
            continue
        spawn[0]+=x_cur
        spawn[1]+=y_cur

def print_current(map, ys, highest_y):
    for y in range(highest_y, ys, -1):
        if y == -1 :
            print('+', end='')
        else:
            print('|', end='')
        for x in range(0, 7):
            if (x,y) in map:
                print('#', end='')
            elif y == -1:
                print('-', end='')
            else:
                print('.', end='')
        if y == -1 :
            print('+', end='')
        else:
            print('|', end='')
        print()

def is_sealed(map, max):
    b = 0
    for i in range(7):
        b = (b << 1) if (i,max) in map else (b << 1) + 1 
    print(b, bin(b))
    possible_seals = [127, 126, 62, 63, 31]
    return b in possible_seals


def contains(small, big):
    for i in xrange(len(big)-len(small)+1):
        for j in xrange(len(small)):
            if big[i+j] != small[j]:
                break
        else:
            return i, i+len(small)
    return False


def has_cycle(l, min_length):
    if min_length<len(l)//2: return None
    for i in range(min_length, len(l)//2):
        for k in range(len(l)-i):
            res = contains(l[k:k+i], l[k+i:]) 
            if res: return res
    return None
            
            
    


def run(path):
    with open(path) as data:
        commands = []
        map = {}
        height_differences = [] 
        height_differences_set = set() 
        highest_rock = 0
        for line in data:
            for i in line.strip():
                commands.append(i)
        len_commands = len(commands)
        i = 0
        k = 0
        high_y = 0
        st = time.time()
        while i < 200000:
            spawn = [2, highest_rock + 3]
            rock, highest_x = rock_patterns[i%5]

            k, highest_part, rock_centered = let_rock_fall(map, height_differences, spawn, commands, rock, k, highest_x, len_commands, i%5)
            print(height_differences)
            print(high_y)
            print_current(map, high_y-10, high_y)
            print(has_cycle(height_differences, 10))
            if has_cycle(height_differences, 15) != None:
                 exit()
                 print(height_differences)
                 print(f"k: {k}, i: {i}, h: {high_y}, len: {len(height_differences_set)},  sum: {sum([i[2] if i[2]>0 else 0 for i in list(height_differences_set)])}")
                 v = (1_000_000_000_000-2500)//(len(height_differences)) * sum([i[2] if i[2]>0 else 0 for i in list(height_differences_set)]) + h
                 print("Cycles", high_y, v, 1_000_000_000_000%(len(height_differences)))
                 return
            if i <= 2500:
                 h = high_y
            if i > 2500: 
                 height_differences.append((k, i%5,highest_part-high_y))
                 height_differences_set.add((k, i%5,highest_part-high_y))
            high_y = max(high_y, highest_part)

            highest_rock = max(highest_rock, high_y)
            #print_current(map, highest_rock)

            #print(high_y)
            i += 1
        print(time.time() - st)
        print(highest_rock-2)

print("Test")
run('../input/test')
#print("Input")
#run('../input/input')
