with open('../input/input') as data:
    for line in data.readlines():
        cnt = 0
        str = ''
        flg = True
        for char in line:
            idx = str.find(char)
            if idx != -1:
                str = str[idx+1:]
            str += char
            cnt+=1
            if flg and len(str) == 4:
                print("Part 1:", cnt)
                flg = False
            if len(str) == 14:
                print("Part 2:", cnt)
                break
