class Node:
    def __init__(self, name, contains):
        self.name = name
        self.contains = contains


class Bag:
    def __init__(self, name, amount):
        self.name = name
        self.amount = amount

# Basic parsing for both parts.
nodes = {}
with open('../input/input') as data:
    for line in data:
        parts = line.strip().split(' ')
        name = parts[0] + " " + parts[1]
        index = 0
        contains = []
        for part in parts:
            if part.isnumeric():
                contains.append(Bag(parts[index + 1] + " " + parts[index + 2], int(part)))
            index += 1
        node = Node(name, contains)
        nodes[name] = node

# Start part 1
options = {}
foundNew = True
while foundNew:
    foundNew = False
    for index in nodes:
        node = nodes[index]
        for option in node.contains:
            if option.name in options or option.name == 'shiny gold':
                if node.name not in options:
                    options[node.name] = node
                    foundNew = True
print("Part 1:", len(options))

# Start part 2
def exploreContains(contains):
    if len(contains) == 0:
        return 0
    cur_count = 0
    for element in contains:
        node = nodes[element.name]
        cur_count += element.amount + (element.amount * exploreContains(node.contains))
    return cur_count

count = 0
for index in nodes:
    node = nodes[index]
    if node.name == 'shiny gold':
        count += int(exploreContains(node.contains))

print("Part 2:", count)