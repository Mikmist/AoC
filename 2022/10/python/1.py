class CPU:
    def __init__(self):
        self.cycle = 0
        self.register = 1
        self.signal_sum = 0
   
    def execute_instruction(self, instruction, args = []):
        if instruction == 'noop':
            self.run_cycle()
        if instruction == 'addx':
            self.run_cycle()
            self.run_cycle()
            self.register += int(args[0])

    def run_cycle(self):
        self.cycle += 1
        print(self.cycle - 20 % 40, (self.cycle - 20) % 40)
        if (self.cycle - 20) % 40 == 0:
            self.signal_sum += self.cycle * self.register


with open('../input/input') as data:
    cpu = CPU()
    for line in data:
        args = line.strip().split(' ')
        cpu.execute_instruction(args[0], args[1:])
    print(cpu.signal_sum)
