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
    queue = [(start, 0)]
    while len(queue) > 0:
        name, distance = queue.pop()
        visisted.add(name)
        if distance > 0 and map[name].rate > 0:
            node_maps[name] = distance
        for i in map[name].connections:
            if i not in visisted or (i in node_maps and distance+1 < node_maps[i]):
                visisted.add(i)
                queue.append((i, distance+1))
    return node_maps

def explore_valves(map, direct_lines):
    q = PriorityQueue()
    val = 0
    q.put(PItem(0, (set({'AA'}), 'AA', 0, 0)))
    while not q.empty():
        a = q.get()
        visisted, name, current_rate, minutes = a.item
        pressure_released = a.priority
        if minutes >= 30:
            continue
        val = min(val, pressure_released-(current_rate*(30-minutes)))
        print(name, visisted, minutes, current_rate)
        for i in direct_lines[name]:
            distance = direct_lines[name][i]
            cv = copy.deepcopy(visisted)
            cv.add(i)
            cpr = current_rate*(distance+1)
            if i not in visisted:
                q.put(PItem(pressure_released - cpr, (cv, i, current_rate+map[i].rate, minutes+distance+1)))
    print(val)


with open('../input/test') as data:
    map = {}
    direct_lines = {}
    for line in data:
        parts = line.strip().split(' ')
        name = parts[1]
        rate = int(parts[4].split('=')[1].replace(';', ''))
        connections = [i.replace(',', '') for i in parts[9:]]
        map[name] = Valve(rate, connections)
    for i in map:
        direct_lines[i] = get_clean_paths(map, i)
    print(direct_lines)
    explore_valves(map, direct_lines)
