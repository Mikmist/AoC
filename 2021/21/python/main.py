import copy;
from itertools import permutations
from collections import defaultdict

cache = {}
options = defaultdict(int)
for i in range(1,4):
        for j in range(1,4):
            for k in range(1,4):
                options[sum([i,j,k])] += 1


def dfs(p1Pos, p1Score, p2Pos, p2Score, currentPlayer):
    tp = (p1Pos, p1Score, p2Pos, p2Score)
    total_wins1 = total_wins2 = 0
    if (*tp, currentPlayer) in cache: return cache[(*tp, currentPlayer)]
    if p1Score >= 21:
        return [1,0]
    if p2Score >= 21:
        return [0,1]
    
    
    for increase in options:
        possibilites = options[increase]
        if currentPlayer == 0:
            p1PosNew =  ((p1Pos + increase - 1) % 10) + 1
            total_wins = dfs(p1PosNew, p1Score + p1PosNew, p2Pos, p2Score, 1)
        else: 
            p2PosNew = ((p2Pos + increase - 1) % 10) + 1
            total_wins = dfs(p1Pos, p1Score, p2PosNew, p2Score + p2PosNew, 0)
        total_wins1 += possibilites * total_wins[0]
        total_wins2 += possibilites * total_wins[1]
    cache[(*tp, currentPlayer)] = [total_wins1,total_wins2]
    return [total_wins1,total_wins2]


print("Part B:")
with open('../input/test') as data:
    players = []
    for line in data:
        players.append((int(line.strip().split(' ')[4]),0))
    print(" - Test:", dfs(players[0][0], players[0][1], players[1][0], players[1][1], 0))

with open('../input/input') as data:
    players = []
    for line in data:
        players.append((int(line.strip().split(' ')[4]),0))
    print(" - Real:", dfs(players[0][0], players[0][1], players[1][0], players[1][1], 0))
