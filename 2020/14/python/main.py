with open('../input/input') as data:
    current_mask = ''
    memory = {}
    for line in data:
        data_line = line.strip().split(' = ')
        if data_line[0] == 'mask':
            current_mask = data_line[1]
        else:
            val = bin(int(data_line[1]))[2:].zfill(36)
            masked_value=[]
            masked_value[:0] = '000000000000000000000000000000000000'
            for i in reversed(range(len(current_mask))):
                if current_mask[i] in ('1', '0'):
                    masked_value[i] = current_mask[i]
                else:
                    masked_value[i] = val[i]
            val = 0
            for i in range(len(current_mask)):
                if masked_value[35 - i] == '1':
                    val += pow(2, i)

            memory[data_line[0][4:-1]] = val
# print(memory)
print('Part 1:', sum(memory.values()))

# Part Two
mem = {}
file = open('../input/input',mode='r')
for line in file:
    if "mask" in line:
        mask = line.split(" = ")[1]
        continue
    else:
        data_line = line.strip().split(' = ')
        mem_helper = data_line[0]
        value = data_line[1]
        mem_helper = mem_helper.replace("[",",")
        mem_helper = mem_helper.replace("]","")
        value = int(value)
    # Convert Value to binary 36b
    address = f'{int(mem_helper.split(",")[1]):036b}'
    address_helper = []
    for a, m in zip(address,mask):
        if m == 'X' or m == a:
            address_helper.append(m)
        else: 
            address_helper.append("1")
    
    first_x = address_helper.index('X') -1
    replaces = ["1","0"]
    clean_address = address_helper.copy()
    for num in range(0, 2**address_helper.count('X')):
        bin_num = bin(num)[2:].zfill(address_helper.count('X'))
        
        for char in bin_num:
            address_helper[address_helper.index('X')] = char
        
        mem[(''.join(address_helper))] = value
        address_helper = clean_address.copy()
        

print(f"Part 2: {sum(mem.values())}")