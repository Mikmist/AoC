with open('../input/input') as data:
    inp = data.read().split('\n\n')
    stack_lines = inp[0].split('\n')[:-1]
    amount_of_stacks = (len(stack_lines[0]) + 1) // 4
    stacks = [[] for x in range(amount_of_stacks)]
    for stack_line in reversed(stack_lines):
        idx = 0
        while idx < len(stack_line):
            if stack_line[idx] == '[':
                stacks[idx//4].append(stack_line[idx+1])
                idx += 2
            idx += 1

    for i in inp[1].strip().split('\n'):
        p=i.split(' ')
        #from 3, count 1, to 5
        stacks[int(p[5])-1].extend(stacks[int(p[3])-1][-int(p[1]):])
        stacks[int(p[3])-1] = stacks[int(p[3])-1][:-int(p[1])]
    answer = ""
    for i in stacks:
        answer += i.pop()
    print(answer)
