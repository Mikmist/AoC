class Node:
    def __init__(self, instruction, value, visited):
        self.instruction = instruction
        self.value = value
        self.visited = visited


parsed_data = []
with open('../input/input') as data:
    for line in data:
        instruction = line[0:3]
        value = int(line[3:].strip())
        parsed_data.append(Node(instruction, value, False))


accumulator = 0
index = 0
while True:
    current = parsed_data[index]
    if current.visited == True:
        break
    if current.instruction == 'nop':
        index += 1
    elif current.instruction == 'acc':
        accumulator += current.value
        index += 1
    elif current.instruction == 'jmp':
        index += current.value
    current.visited = True
print('Part 1:', accumulator)

def test():
    accumulator = 0
    index = 0
    while True:
        if index == len(parsed_data):
            print('Part 2:', accumulator)
            return 0
        current = parsed_data[index]
        if current.visited == True:
            return 1
        if current.instruction == 'nop':
            index += 1
        elif current.instruction == 'acc':
            accumulator += current.value
            index += 1
        elif current.instruction == 'jmp':
            index += current.value
        current.visited = True

def resetVisited():
    for i in parsed_data:
        i.visited = False

index = 0
for i in parsed_data:
    inc = 0
    if i.instruction == 'jmp':
        i.instruction = 'nop'
        if test() == 1:
            i.instruction = 'jmp'
            resetVisited()
        else:
            break
    if i.instruction == 'nop':
        i.instruction = 'jmp'
        if test() == 1:
            i.instruction = 'nop'
            resetVisited()
        else:
            break