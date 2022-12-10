class CPU:
    def __init__(self):
        self.cycle = 0
        self.register = 1
   
    def execute_instruction(self, instruction, args = []):
        if instruction == 'noop':
            self.run_cycle()
        if instruction == 'addx':
            self.run_cycle()
            self.run_cycle()
            self.register += int(args[0])

    def run_cycle(self):
        self.cycle += 1
        m = self.cycle % 40
        if self.register <= m <= (self.register + 2):
            print('#', end='')
        else:
            print('.', end='')
        if m == 0:
            print()


with open('../input/input') as data:
    cpu = CPU()
    for line in data:
        args = line.strip().split(' ')
        cpu.execute_instruction(args[0], args[1:])
