import time

rock_patterns = [
        ([(0,0),(1,0),(2,0),(3,0)], 0), 
        ([(1,0),(0,1),(1,1),(2,1),(1,2)], 2),
        ([(2,2),(2,1),(0,0),(1,0),(2,0)], 2),
        ([(0,0),(0,1),(0,2),(0,3)], 3),
        ([(0,0),(1,0),(0,1),(1,1)], 1)
        ]

def let_rock_fall(map, rock_moves, spawn, commands, rock, k, highest_y, len_commands, rock_index):
    #print(map, spawn, rock, k)
    j = 0
    x_track = 0
    y_track = 0
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
                if (rock_index, k) in rock_moves:
                    #print("Cycle", rock_index, x_track, y_track, k)
                    cycle = True
                else:
                    rock_moves.add((rock_index, k))
                return (k, highest_y+spawn[1]+1, rock[0][0]+spawn[0] == 1, cycle)
        j += 1
        if ignore_move:
            #print(f"Push {commands[k%len(commands)]} but nothing happens.")
            continue
        spawn[0]+=x_cur
        spawn[1]+=y_cur
        x_track += x_cur
        y_track += y_cur

def print_current(map, highest_y):
    for y in range(highest_y, -2, -1):
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

def run(path):
    with open(path) as data:
        commands = []
        map = {}
        rock_cycles = set()
        highest_rock = 0
        for line in data:
            for i in line.strip():
                commands.append(i)
        len_commands = len(commands)
        i = 0
        p = 0
        k = 0
        st = time.time()
        cycles = 0
        low = 0
        cycle_heights = []
        while i < 200_000:
            spawn = [2, highest_rock + 3]
            rock, highest_x = rock_patterns[i%5]

            k, high_y, rock_centered, cycle = let_rock_fall(map, rock_cycles, spawn, commands, rock, k, highest_x, len_commands, i%5)
            if cycle: 
                cycles+=1
            else: cycles = 0; low = high_y; 
            if i%5==0:
                #i=0
                p+=1

            if cycle and cycles == len_commands*5:
                print(len(rock_cycles), len_commands*5)
                print("Cycles", cycles, low, high_y, (1_000_000_000_000//cycles)*(high_y-low), 1_000_000_000_000%cycles)
                cycle_heights.append( high_y-low)
                cycles = 0
                rock_cycles = set()
                if len(cycle_heights) == 5: break

            highest_rock = max(highest_rock, high_y)
            #print_current(map, highest_rock)

            #print(high_y)
            i += 1
        print(time.time() - st)
        print(highest_rock-2)
        print(cycle_heights)

print("Test")
run('../input/test')
print("Input")
run('../input/input')
