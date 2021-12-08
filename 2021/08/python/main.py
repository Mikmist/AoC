from itertools import permutations

with open('../input/input') as data:
    # The numbers and their mapping.
    numbers = {
        "abcefg": 0, "cf": 1,"acdeg": 2, "acdfg": 3, "bcdf": 4,
        "abdfg": 5, "abdefg": 6, "acf": 7, "abcdefg": 8, "abcdfg": 9,
    }
    
    possibilties = set(numbers.keys())
    realTotal = 0
    for line in data.read().splitlines():
        for perms in permutations('abcdefg'):
            valid = True
            mapping = { "a": perms[0], "b": perms[1], "c": perms[2], "d": perms[3], "e": perms[4], "f": perms[5], "g": perms[6] }
            values = line.replace(" | ", " ").split(" ")

            # Check if all values work in the mapping of this permuation.
            for value in values:
                current_map = "".join(sorted(mapping[letter] for letter in value))
                if current_map not in possibilties:
                    valid = False
                    break
            if valid:
                break

        total = []
        for value in line.split(" | ")[1].split(" "):
            total.append(str(numbers["".join(sorted([mapping[letter] for letter in value]))]))

        realTotal += int("".join(total))
    print("Part A: Can only be found in the land of D.")
    print("Part B: " + str(realTotal))

