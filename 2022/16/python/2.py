from collections import defaultdict
from dataclasses import dataclass, field
from typing import Any
from queue import PriorityQueue
import copy
import time
import itertools

@dataclass(order=True)
class PItem:
    priority: int
    item: Any=field(compare=False)


class Valve:
    def __init__(self, rate, connections):
        self.rate = rate
        self.connections = connections 

    def __repr__(self):
        return f"Valve({self.rate}, {self.connections})"

def get_clean_paths(map, start):
    node_maps = {} 
    visisted = set()
    queue = PriorityQueue()
    queue.put(PItem(0, start))
    while not queue.empty():
        a = queue.get()
        distance = a.priority
        name = a.item
        visisted.add(name)
        if distance > 0 and map[name].rate > 0:
            node_maps[name] = distance
        for i in map[name].connections:
            if i not in visisted:
                visisted.add(i)
                queue.put(PItem(distance+1, i))
    return node_maps

cache = {}

def explore_valves(map, direct_lines, visisted, name, minutes, last_rate):
    if (minutes, name) in cache:
        return cache[(minutes,name)]
    val = 0
    path = ''
    for i in direct_lines[name]:
        distance = direct_lines[name][i]
        cv = copy.deepcopy(visisted)
        cv.add(i)
        if minutes+distance+1 <= 30 and i not in visisted:
            v, n = explore_valves(map, direct_lines, cv, i, minutes+distance+1, map[i].rate)
            if v > val:
                val = v
                path = n
    return (last_rate*(30) + val, name+','+path)

def run(path):
    with open(path) as data:
        map = {}
        direct_lines = {}
        for line in data:
            parts = line.strip().split(' ')
            name = parts[1]
            rate = int(parts[4].split('=')[1].replace(';', ''))
            connections = [i.replace(',', '') for i in parts[9:]]
            map[name] = Valve(rate, connections)
        for i in map:
            if map[i].rate != 0 or i == 'AA':
                direct_lines[i] = get_clean_paths(map, i)
        print(direct_lines)
        st = time.time()
        #print(explore_valves(map, direct_lines, set({'AA'}), 'AA', 0, 0))
        et = time.time()
        print("Time:", et - st)

        for i in list(itertools.permutations(direct_lines.keys())):
            print(i)


run('../input/test')
run('../input/input')
