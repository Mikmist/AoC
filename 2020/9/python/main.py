# Tests the preamble sum.
def sumExists(index, value, number_list):
    for i in range(25):
        a = number_list[index - i - 1]
        for j in range(25):
            b = number_list[index - j - 1]
            if a == b:
                continue
            if a + b == value:
                return True
    return False

# Part 1
numbers = []
index = 0
error_value = 0
with open('../input/input') as data:
    for line in data:
        value = int(line.strip())
        numbers.append(value)
        if index > 24:
            if not sumExists(index, value, numbers):
                print('Part 1:', value)
                error_value = value
                break
        index += 1

# Part 2, depends on the list created by part 1.
index = 0
for number in numbers:
    summation = number
    summed_numbers = []
    add_index = index + 1
    while summation < error_value:
        summation += numbers[add_index]
        summed_numbers.append(numbers[add_index])
        add_index += 1
    if summation == error_value and len(summed_numbers) > 1:
        print('Part 2:', max(summed_numbers) + min(summed_numbers))
    index += 1
