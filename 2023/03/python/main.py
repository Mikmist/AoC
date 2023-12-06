def check_pos(map, x, y, number):
    if (x-len(number),y) in map:
        return int(number)
    if (x+1,y) in map:
        return int(number)
    for i in range(2+len(number)):
        if (x-i+1,y+1) in map:
            return int(number)
        if (x-i+1,y-1) in map:
            return int(number)

    return 0 

def check_pos_p2(map, x, y):
    cnt = set()
    ratio = 1
    for i in range(-1,2): 
        for j in range(-1,2):
            if (x+i,y+j) in map:
                val, id = map[(x+i,y+j)]
                if id not in cnt:
                    cnt.add(id)
                    ratio *= val
    if len(cnt) == 2:
        return ratio
    return 0


with open('../input/input') as data:
    map = {}
    sum = 0
    sum_p2 = 0
    number_map = {}
    y = 0
    data_copy = []
    for line in data:
        data_copy.append(line)
        x = 0
        for char in line.strip():
            if char != '.':
                map[(x,y)] = char
            x += 1
        y += 1
    y = 0
    cnt = 0
    for line in data_copy:
        x = 0
        number = ''
        for char in line.strip():
            if char.isnumeric():
                number += char
            elif number != '':
                sum += check_pos(map, x-1, y, number)
                for i in range(len(number)):
                    number_map[(x-i-1,y)] = (int(number), cnt)
                cnt += 1
                number = ''
            x += 1
        if number != '':
            sum += check_pos(map, x-1, y, number)
            for i in range(len(number)):
                number_map[(x-i-1,y)] = (int(number), cnt)
            cnt += 1
        y += 1

    y = 0
    for line in data_copy:
        x = 0
        for char in line.strip():
            if char == '*':
                #print(check_pos_p2(number_map, x, y))
                sum_p2 += check_pos_p2(number_map, x, y)
            x += 1
        y += 1
    print(sum)
    print(sum_p2)
