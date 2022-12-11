class Monkey:
    def __init__(self, items, operation, operation_value, divider, true_monkey, false_monkey):
        self.inspection = 0
        self.items = items
        self.operation = operation
        self.operation_value = operation_value
        self.divider = divider
        self.true_monkey = true_monkey
        self.false_monkey = false_monkey

    def do_round_for(self, monkeys, common_mod):
        cnt = len(self.items)
        for idx in range(len(self.items)):
            mlt = int(self.operation_value) if self.operation_value != 'old' else int(self.items[idx])
            if self.operation == '*':
                self.items[idx] *= mlt
            if self.operation == '+':
                self.items[idx] += mlt
            self.items[idx] = self.items[idx] % common_mod
        while len(self.items) > 0:
            if self.items[0] % self.divider == 0:
                monkeys[self.true_monkey].receive_item(self.items[0])
            else: 
                monkeys[self.false_monkey].receive_item(self.items[0])
            self.items = self.items[1:]
        return cnt

    def receive_item(self, item):
        self.items.append(item)
            
    def __repr__(self):
        return f"Monkey({self.items}, {self.divider}, {self.operation}, {self.operation_value})"

def parse_monkey(lines):
    items = [int(s.replace(',', '')) for s in lines[1].strip().split(' ')[2:]]
    operation, operation_value = lines[2].strip().split(' ')[4:]
    divider = int(lines[3].strip().split(' ')[3])
    true_monkey = int(lines[4].strip().split(' ')[5])
    false_monkey = int(lines[5].strip().split(' ')[5])
    return Monkey(items, operation, operation_value, divider, true_monkey, false_monkey)

with open('../input/input') as data:
    monkeys = []
    inspection_list = []
    common_mod = 1
    for monkey_block in data.read().split('\n\n'):
        monkey = parse_monkey(monkey_block.split('\n'))
        monkeys.append(monkey)
        inspection_list.append(0)
    for monkey in monkeys:
        common_mod *= monkey.divider
    for round in range(0,10000):
        for idx in range(len(monkeys)):
            inspection_list[idx] += monkeys[idx].do_round_for(monkeys, common_mod)
    print(monkeys)
    inspection_list.sort()
    print(inspection_list[-1] * inspection_list[-2])
