from collections import defaultdict
from dataclasses import dataclass, field
from typing import Any
from queue import PriorityQueue
import copy

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

def explore_valves(map, direct_lines):
    q = PriorityQueue()
    val = 0; val2 = 0
    q.put(PItem(0, (set({'AA'}), 'AA', 0, 0, 0, 0)))
    while not q.empty():
        a = q.get()
        visisted, name, current_rate, minutes, pr2, last_rate = a.item
        pressure_released = a.priority
        pr2 += (last_rate*(30-minutes))
        val = min(val, pressure_released-(current_rate*(30-minutes)))
        val2 = max(val2, pr2)
        for i in direct_lines[name]:
            distance = direct_lines[name][i]
            cv = copy.deepcopy(visisted)
            cv.add(i)
            cpr = current_rate*(distance+1)
            if minutes+distance+1 <= 30 and i not in visisted:
                q.put(PItem(pressure_released - cpr, (cv, i, current_rate+map[i].rate, minutes+distance+1, pr2, map[i].rate)))
    print(val)

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
        for i in direct_lines:
            print(len(direct_lines[i]))
        print(direct_lines)
        explore_valves(map, direct_lines)

run('../input/input')
run('../input/test')
