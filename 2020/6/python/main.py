with open('../input/input') as data:
    group = {}
    count = 0
    people_count = 0
    answer = 0
    for line in data:
        if line == '\n':
            count += len(group)
            for i in group:
                if people_count == group[i]:
                    answer += 1
            group = {}
            people_count = 0
            continue
        
        for char in line.strip():
            if char not in group:
                group[char] = 1
            else:
                group[char] += 1
        people_count += 1

    # Part 1
    print(count)
    # Part 2
    print(answer)