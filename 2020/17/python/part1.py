from copy import deepcopy

class EnergyGrid:
    def __init__(self, width, cycles):
        self.size = width + (7*2)
        self.grid = [[['.' for k in range(self.size)] for j in range(self.size)] for i in range(self.size)]
        self.cycles = cycles

    def set_base_element(self, value, x, y, z=0):
        if value == '.':
            return
        self.grid[z+7][y+7][x+7] = value

    def print_z_slice(self, z):
        for i in range(len(self.grid[z])):
            print('z:', z, ' | y', i, '\t', ''.join(self.grid[z][i]))
        print
    
    def count_neighbours(self, x, y, z):
        count = 0
        for i in [-1,0,1]:
            for j in [-1,0,1]:
                for k in [-1,0,1]:
                    if i == 0 and j == 0 and k == 0:
                        continue
                    if self.grid[z + i][y + j][x + k] == '#':
                        count += 1
        return count

    def run_cycles(self, should_print=False):
        for i in range(self.cycles):
            new_cylce_grid = [[['.' for k in range(self.size)] for j in range(self.size)] for i in range(self.size)]

            for z in range(1, self.size - 1):
                for x in range(1, self.size - 1): 
                    for y in range(1, self.size - 1):
                        if self.grid[z][y][x] == '#' and not self.count_neighbours(x, y, z) in [2, 3]:
                            new_cylce_grid[z][y][x] = '.'
                        elif self.grid[z][y][x] == '.' and self.count_neighbours(x, y, z) == 3:
                            new_cylce_grid[z][y][x] = '#'
                        else:
                            new_cylce_grid[z][y][x] = self.grid[z][y][x]
            self.grid = deepcopy(new_cylce_grid)
            if should_print:
                print('After cycle:', i + 1)
                self.print_z_slice(7)
        count = 0
        for z in range(1, self.size - 1):
            for x in range(1, self.size - 1): 
                for y in range(1, self.size - 1):
                    if self.grid[z][y][x] == '#':
                        count += 1
        return count

with open('../input/input') as data:
    grid = EnergyGrid(8, 6)
    y = 0
    for line in data:
        x = 0
        for element in line.strip():
            grid.set_base_element(element, x, y)
            x += 1
        y += 1
        
    print('Part 1:', grid.run_cycles())