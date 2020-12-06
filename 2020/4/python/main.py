from utils import submit
import re

def validate(field_type, value):
    if (field_type == 'byr'):
        return int(value) >= 1920 and int(value) <= 2002
    if (field_type == 'iyr'):
        return int(value) >= 2010 and int(value) <= 2020
    if (field_type == 'eyr'):
        return int(value) >= 2020 and int(value) <= 2030
    if (field_type == 'hgt'):
        if (value[-2:] == 'cm'):
            return int(value[:-2]) >= 150 and int(value[:-2]) <= 193
        elif (value[-2:] == 'in'):
            return int(value[:-2]) >= 59 and int(value[:-2]) <= 76
    if (field_type == 'hcl'):
        p = re.compile('([a-f]|[0-9]){6}')
        return value[0] == '#' and p.match(value[1:]) != None
    if (field_type == 'ecl'):
        return value in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
    if (field_type == 'pid'):
        p = re.compile('([0-9]){9}')
        return p.match(value) != None
    if (field_type == 'cid'):
        return True
    return False

def verifyPassportData(passport_data):
    required_vars = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
    for i in passport_data:
        for j in required_vars:
            parts = i.split(':')
            if j == parts[0]:
                if validate(parts[0], parts[1]):
                    required_vars.remove(j)
                else:
                    return False
    return len(required_vars) == 0

count = 0
with open('../input/input') as data:
    passport_data = []
    for line in data:
        if (line == '\n'):
            # We wanna parse the data here.
            if verifyPassportData(passport_data):
                count += 1
            passport_data = []
            continue
        passport_data += line.strip().split(' ')

print(count)
