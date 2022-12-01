with open('../input/input') as data:
    current_sum = 0
    max_sum = 0
    for line in data:
        if line == '\n':
            if current_sum > max_sum:
                max_sum = current_sum
            current_sum = 0
        else:
            current_sum += int(line)
    print(max_sum)
