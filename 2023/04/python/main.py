with open('../input/input') as data:
    p1 = 0
    cards = []
    for line in data:
        sets = [set([int(b) for b in (a.strip().split())]) for a in line.strip().split(':')[1].split('|')]
        p1 += 1<<len(sets[0].intersection(sets[1]))>>1
        cards.append((sets, len(sets[0].intersection(sets[1]))))
    counts = [1 for _ in range(len(cards))]
    for i, card in enumerate(cards):
        sets, matches = card
        for j in range(matches):
            if i+j+1 < len(counts):
                counts[i+j+1] += 1 * counts[i]
    print(p1)
    print(sum(counts))
