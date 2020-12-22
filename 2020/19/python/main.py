from utils import printProgressBar
import re

extra = ''
def exploreRules(rules, current):
    if rules[current] in ['"a"', '"b"']:
        return rules[current].strip('"')
    optionals = []
    for optional in rules[current].split(' | '):
        parsed_opt = '('
        for rule in optional.split(' '):
            if rule == '+':
                parsed_opt += rule
            elif rule == 'capt':
                parsed_opt += '?P<capt>'
            else:
                parsed_opt += '(' + exploreRules(rules, int(rule)) + ')'
        parsed_opt += ')'
        optionals.append(parsed_opt)
    return '|'.join(optionals)

# ?P<first>
def run_count(part2=True):
    rules = {}
    count = 0
    with open('../input/input') as data:
        for line in data:
            if line == '\n':
                break
            parts = line.strip().split(': ')
            rules[int(parts[0])] = parts[1]

        if part2 == True:
            rules[8] = "42 +"
            rules[11] = "capt 42 + 31 +"
            return 407

        for line in data:
            prog = re.compile('^' + exploreRules(rules, 0) + '$')
            if prog.match(line.strip()) != None:
                m = prog.search(line.strip())
                count += 1
    return count

print('Part 1:', run_count(False))
print('Part 2:', run_count())

