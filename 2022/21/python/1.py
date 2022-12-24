def do_operation(value, monkeys_solved):
    if value[1] == '/':
        return int(monkeys_solved[value[0]]) / int(monkeys_solved[value[2]])
    if value[1] == '*':
        return int(monkeys_solved[value[0]]) * int(monkeys_solved[value[2]])
    if value[1] == '-':
        return int(monkeys_solved[value[0]]) - int(monkeys_solved[value[2]])
    if value[1] == '+':
        return int(monkeys_solved[value[0]]) + int(monkeys_solved[value[2]])


with open('../input/input') as data:
    monkeys_solved = {}
    unsolved_monkeys = {}
    root_monkeys = {}
    for line in data:
        p = line.strip()
        parts = p.split(': ')
        value = parts[1].split(' ')
        if len(value) > 1:
            unsolved_monkeys[parts[0]] = value
        else: 
            monkeys_solved[parts[0]] = int(parts[1])
    solved_any = True
    while solved_any:
        solved_any = False
        for monkey in list(unsolved_monkeys.keys()):
            value = unsolved_monkeys[monkey]
            if value[0] in monkeys_solved and value[2] in monkeys_solved:
                monkeys_solved[monkey] = do_operation(value, monkeys_solved)
                del unsolved_monkeys[monkey]
                solved_any = True

    print(monkeys_solved)
    print(unsolved_monkeys)

