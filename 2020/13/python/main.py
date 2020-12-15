with open('../input/input') as data:
    estimate = 0
    smallest_remainder = 99999999999
    smallest_id = 0
    wait = 0
    for line in data:
        estimate = int(line)
        break
    for line in data:
        for bus_id_str in line.split(','):
            if bus_id_str == 'x':
                continue
            bus_id = int(bus_id_str)
            remainder = estimate // bus_id * bus_id + bus_id
            if remainder < smallest_remainder:
                smallest_id = bus_id
                smallest_remainder = remainder
    print('Part 1:', smallest_id * (smallest_remainder - estimate))

with open('../input/input') as data:
    bus_id_mod_result = {}
    for line in data:
        break
    for line in data:
        for pos, bus_id in enumerate(line.split(',')):
            if bus_id == 'x':
                continue
            bus_id = int(bus_id)
            bus_id_mod_result[bus_id] = (bus_id - pos) % bus_id

# Chinese remainder theorem
from sympy.ntheory.modular import crt 
print('Part 2:', crt(bus_id_mod_result.keys(), bus_id_mod_result.values())[0])
