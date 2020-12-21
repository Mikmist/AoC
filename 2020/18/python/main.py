def calculateCleanEquation(equation):
    val = int(equation[0])
    equation = equation[1:]
    while len(equation) > 0:
        if equation[0] == '*':
            val *= int(equation[1])
        if equation[0] == '+':
            val += int(equation[1])
        equation = equation[2:]
    return val


def formatEquation(rest):
    if len(rest) == 0:
        return []
    index = 0
    while len(rest) != index:
        if rest[index] == '(':
            rest[index:] = formatEquation(rest[index + 1:])
        if rest[index] == ')':
            return [calculateCleanEquation(rest[:index])] + rest[index+1:]
        index += 1
    return calculateCleanEquation(rest)


def addParatheses(equation):
    index = 0
    while len(equation) > index:
        if equation[index] == '+':
            if equation[index - 1].isnumeric():
                if equation[index + 1].isnumeric():
                    equation.insert(index + 2, ')')
                else:
                    temp_index = index + 1 
                    paratheses = 1
                    while paratheses > 0:
                        temp_index += 1
                        if equation[temp_index] == ')':
                            paratheses -= 1
                        if equation[temp_index] == '(':
                            paratheses += 1
                    equation.insert(temp_index + 1, ')')
                equation.insert(index - 1, '(')
                index += 2
            if equation[index - 1] == ')':
                paratheses = 1
                temp_index = index - 1
                while paratheses > 0:
                    temp_index -= 1
                    if equation[temp_index] == ')':
                        paratheses += 1
                    if equation[temp_index] == '(':
                        paratheses -= 1
                temp_index_i = temp_index
                if equation[index + 1].isnumeric():
                    equation.insert(index + 2, ')')
                else:
                    temp_index = index + 1 
                    paratheses = 1
                    while paratheses > 0:
                        temp_index += 1
                        if equation[temp_index] == ')':
                            paratheses -= 1
                        if equation[temp_index] == '(':
                            paratheses += 1
                    equation.insert(temp_index + 1, ')')
                equation.insert(temp_index_i, '(')
                index += 2
        index += 1
    return equation


equation_sum = 0
equation_sum_part_2 = 0
with open('../input/input') as data:
    for line in data:
        formatted = line.strip().replace(' ', '')
        equation_sum += formatEquation(list(formatted))
        equation_sum_part_2 += formatEquation(addParatheses(list(formatted)))
print('Part 1:', equation_sum)
print('Part 2:', equation_sum_part_2)