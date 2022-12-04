from collections import defaultdict

with open('../input/input') as data:
    total = 0
    for line in data:
        line = line.strip()
        hist = defaultdict(int)
        for idx in range(len(line)):
            j = line[idx]
            if idx*2<len(line):
                hist[j] += 1
            else:
                if j in hist:
                    val = ord(j)
                    actual_val =val - ord('a')+ 1 if val > 90 else val - ord('A') + 27
                    total += actual_val 
                    break
        print(total)
