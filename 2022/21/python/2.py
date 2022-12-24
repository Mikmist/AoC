def do_operation(value, monkeys_solved):
    if value[1] == '/':
        return int(monkeys_solved[value[0]]) / int(monkeys_solved[value[2]])
    if value[1] == '*':
        return int(monkeys_solved[value[0]]) * int(monkeys_solved[value[2]])
    if value[1] == '-':
        return int(monkeys_solved[value[0]]) - int(monkeys_solved[value[2]])
    if value[1] == '+':
        return int(monkeys_solved[value[0]]) + int(monkeys_solved[value[2]])


def solve_other_way(value, operation, result, unknown):
    if unknown:
        if operation == '+':
            return result - value
        if operation == '-':
            return value - result
        if operation == '*':
            return result // value
        if operation == '/':
            return result // value
    else:
        if operation == '+':
            return result - value
        if operation == '-':
            return value + result
        if operation == '*':
            return result // value
        if operation == '/':
            return result * value


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
    if unsolved_monkeys['root'][0].isnumeric():
        monkeys_solved[unsolved_monkeys['root'][2]] = int(monkeys_solved[unsolved_monkeys['root'][0]])
    else:
        monkeys_solved[unsolved_monkeys['root'][0]] = int(monkeys_solved[unsolved_monkeys['root'][2]])
    del unsolved_monkeys['root']
    del unsolved_monkeys['humn']

    while len(unsolved_monkeys):
        for monkey in list(unsolved_monkeys.keys()):
            value = unsolved_monkeys[monkey]
            if monkey in monkeys_solved:
                if value[0] in monkeys_solved:
                    monkeys_solved[value[2]] = solve_other_way(int(monkeys_solved[value[0]]), value[1], monkeys_solved[monkey], 1)
                    del unsolved_monkeys[monkey]
                elif value[2] in monkeys_solved:
                    monkeys_solved[value[0]] = solve_other_way(int(monkeys_solved[value[2]]), value[1], monkeys_solved[monkey], 0)
                    del unsolved_monkeys[monkey]
    print(monkeys_solved['humn'])

