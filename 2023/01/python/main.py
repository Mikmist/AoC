with open('../input/input') as data:
    sum = 0
    sum_p2 = 0
    numbers = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    for line in data:
        parsed = line.strip()
        parsed_2 = line.strip()
        fnum_p1 = 0
        fnum_p2 = 0
        lnum_p1 = 0
        lnum_p2 = 0
        for i in parsed:
            if i.isnumeric() and fnum_p1 == 0:
                fnum_p1 = i
            if i.isnumeric():
                lnum_p1 = i
        sum += int(fnum_p1 + lnum_p1)
        for i in range(len(parsed_2)):
            if parsed_2[i].isnumeric() and fnum_p2 == 0:
                fnum_p2 = parsed_2[i]
            if parsed_2[i].isnumeric():
                lnum_p2 = parsed_2[i]
            for j, num in enumerate(numbers):
                if parsed[i:i+5] == num or parsed[i:i+4] == num or parsed[i:i+3] == num:
                    lnum_p2 = str(j+1)
                if fnum_p2 == 0 and (parsed[i:i+5] == num or parsed[i:i+4] == num or parsed[i:i+3] == num):
                    fnum_p2 = str(j+1)
        sum_p2 += int(str(fnum_p2) + lnum_p2)

    print(sum)
    print(sum_p2)
