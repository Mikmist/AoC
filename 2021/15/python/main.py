import heapq
from dataclasses import dataclass, field
from typing import Any
import time

@dataclass(order=True)
class PrioritizedItem:
    x: int=field(compare=False)
    y: int=field(compare=False)
    risk: int


def getValueAt(chitonMap, x, y):
    if (y < 0 or x < 0 or y > len(chitonMap) - 1 or x > len(chitonMap[y]) - 1):
        return -1
    return chitonMap[y][x]


def search(chitonMap):
    heap = [PrioritizedItem(0, 0, 0)]
    visited = {}
    heapq.heapify([heap])
    while(len(heap) > 0):
        current = heapq.heappop(heap)
        currentValue = getValueAt(chitonMap, current.x, current.y)
        if currentValue == -1 or str(current.x)+","+str(current.y) in visited:
            continue
        
        if (current.y == len(chitonMap) - 1 and current.x == len(chitonMap[current.y]) - 1):
            return current.risk
        
        visited[str(current.x)+","+str(current.y)] = current.risk      
        for x, y in [(-1, 0), (1, 0), (0, 1), (0, -1)]:  
            nextValue = getValueAt(chitonMap, current.x + x, current.y + y)
            visIdx = str(current.x + x)+","+str(current.y + y)
            if nextValue != -1 and (not visIdx in visited or visited[visIdx] > current.risk + nextValue):
                heapq.heappush(heap, PrioritizedItem(current.x + x, current.y + y, current.risk + nextValue))

def printMap(chitonMap):
    for y in range(len(chitonMap)):
        for x in range(len(chitonMap[y])):
            print(chitonMap[y][x], end="")
        print()


with open('../input/input') as data:
    chitonMapA = []
    chitonMapB = []
    for line in data:
        row = []
        currentValue = int(line)
        while(currentValue > 0):
            digit = currentValue % 10
            row.append(digit)
            currentValue //= 10
        row.reverse()
        chitonMapA.append(row)
        # search(chitonMap)
    size = len(chitonMapA)
    chitonMapB = [[0 for i in range(size*5)] for j in range(size*5)]
    for y in range(5):
        for x in range(5):
            for j in range(size):
                for i in range(size):
                    chitonMapB[y*size + j][x*size + i] = (chitonMapA[j][i] + y + x - 1) % 9 + 1
    
    start = time.perf_counter()
    print("Part A: ", search(chitonMapA))
    print("Part B: ", search(chitonMapB))
    print(f"Perfomance Timer: {round((time.perf_counter() - start)*100)/100} sec")

    