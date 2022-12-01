with open('../input/input') as data:
    current_sum = 0
    max_1_sum = 0
    max_2_sum = 0
    max_sum = 0
    for line in data:
        if line == '\n':
            if current_sum > max_sum:
                max_2_sum = max_1_sum
                max_1_sum = max_sum
                max_sum = current_sum
            elif current_sum > max_1_sum:
                max_2_sum = max_1_sum
                max_1_sum = current_sum
            elif current_sum > max_2_sum:
                max_2_sum = current_sum
            current_sum = 0
        else:
            current_sum += int(line)
    print(max_sum + max_1_sum + max_2_sum)
