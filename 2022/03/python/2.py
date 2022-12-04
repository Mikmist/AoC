from collections import defaultdict

with open('../input/input') as data:
    total = 0
    hist = [defaultdict(int),defaultdict(int)]
    gC = 0
    for line in data:
        if gC==2:
            for j in line.strip():
                if j in hist[0] and j in hist[1]:
                    val = ord(j)
                    actual_val =val - ord('a')+ 1 if val > 90 else val - ord('A') + 27
                    total += actual_val 
                    break
            gC=0
            hist = [defaultdict(int), defaultdict(int)]
            continue 
        else: 
            for j in line.strip():
                hist[gC][j] += 1
        gC += 1
    print(total)
