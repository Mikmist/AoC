from functools import cache
from utils import printProgressBar

@cache
def is_valid(string, springs):
    cur = 1
    cnt = springs[0]
    cnt2 = springs[0]
    idx = 0
    last = ''
    for i in string:
        if cnt == 0:
            if i == '#':
                return False
            else: 
                if cur < len(springs): 
                    cnt = springs[cur]
                    cnt2 = springs[cur]
                    cur += 1
                continue
        if i == '#' or i == '?':
            if last != '#' and cnt != cnt2:
                return False
            cnt -= 1
            #print(idx, cnt)
        last = i
        idx += 1
    #print(string, springs)
    return cur == len(springs) and cnt == 0

@cache
def fits(string, index, spring):
    #print('fits called', string, index, spring)
    if index+spring>len(string): return False
    if spring+index<len(string) and string[spring+index] == '#': return False
    for i in range(spring):
        if string[index+i] == '.':
            return False
    if spring+index+1<len(string) and string[spring+index] == '#': return False
    return True 

@cache
def explore(string, index, current_spring, springs):
    #print('explore{', 'string:', string, 'index:',index, 'current_spring:',current_spring, 'springs:', springs, 'len:', len(string), '}')
    if index >= len(string) or current_spring == len(springs):
        #print(' return end')
        return 1 if is_valid(string, springs) else 0
    if string[index] == '.':
        #print(' current dot skip next')
        return explore(string, index+1, current_spring, springs)

    spring = springs[current_spring]
    if fits(string, index, spring):
        #print('   ', string, index, spring)
        cp = string[:index] + ''.join(['#' for _ in range(spring)])  + string[index+spring:]
        cp1 = string[:index] + '.'  + string[index+1:]
        #print('  fits', index, len(cp), len(cp1), cp, cp1, spring)
        #print(string[index])
        cnt = explore(cp, index+spring+1, current_spring+1, springs)
        if string[index] == '?':
            cnt += explore(cp1, index+1, current_spring, springs)
        return cnt 

    if string[index] == '?':
        cp = string[:index] + '.'  + string[index+1:]
        #print('  tame', len(cp), cp, spring)
        return explore(cp, index+1, current_spring, springs) + (1 if is_valid(string, springs) else 0)

    if is_valid(string, springs):
        #print(' -  return 1  - ', index, string,is_valid(string, springs))
        return 1
    #print(' -  return 0  - ', index, string,is_valid(string, springs), springs)
    return 0


with open('../input/input') as data:
    s = 0
    index = 0
    for line in data:
        parts = line.split()
        springs = tuple(map(int, parts[1].split(',')))
        #print('\n\n\n               ', parts[0], ' ----------------------------------')
        printProgressBar(index, 1000)
        cnt = explore('?'.join(parts[0]*5), 0, 0, springs*5)
        s += cnt
        #print('----------------- cnt:', cnt, parts[0])
        index += 1
    print(s)
#is_valid('.#.##########?#.#', [1,10,2])
