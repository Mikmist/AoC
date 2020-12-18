class TicketField:
    def __init__(self, name, ranges):
        self.name = name
        self.ranges = ranges

    def in_range(self, value):
        for i in self.ranges:
            if i.in_range(value):
                return True
        return False

    def __str__(self):
        return f'{self.name} {self.ranges[0].lower}-{self.ranges[0].upper} {self.ranges[1].lower}-{self.ranges[1].upper}'


class Range:
    def __init__(self, lower, upper):
        self.upper = int(upper)
        self.lower = int(lower)

    def in_range(self, value):
        return value >= self.lower and value <= self.upper


with open('../input/input') as data:
    # Rules loop
    allowed_ranges = [False for i in range(1000)]
    ticket_fields = []
    for line in data:
        if line == '\n':
            break
        
        ticket_field = line.strip().split(': ')
        field_ranges = []

        for inclusive_range in ticket_field[1].split(' or '):
            ranges = list(map(int, inclusive_range.split('-')))
            allowed_ranges[ranges[0]:ranges[1] + 1] = [True for i in allowed_ranges[ranges[0]:ranges[1] + 1]]
            field_ranges.append(Range(ranges[0], ranges[1]))
        ticket_fields.append(TicketField(ticket_field[0], field_ranges))    
    
    # Own ticket loop
    count = 0
    for line in data:
        if line == '\n':
            break
        if 'your ticket' in line: 
            continue
        our_ticket = [field.strip() for field in line.split(',')]
        count = len(line.strip().split(','))
    possibities = [[i for i in range(count)] for j in range(count)]


    # Other tickets loop
    errors = 0
    for line in data:
        if line == '\n':
            break
        if 'nearby' in line: 
            continue
        index = 0
        for field in line.split(','):
            if not allowed_ranges[int(field)]:
                errors += int(field)
            else:
                for i in possibities[index]:
                    if not ticket_fields[i].in_range(int(field)):
                        possibities[index].remove(i)
            index += 1
    
    changed = True
    while changed:
        changed = False
        for i in range(len(possibities)):
            if len(possibities[i]) == 1:
                for j in range(len(possibities)):
                    if i != j and possibities[i][0] in possibities[j]:
                        possibities[j].remove(possibities[i][0])
                        changed = True

    departure_multiplication = 1
    for i in range(len(possibities)):
        if 'departure' in ticket_fields[possibities[i][0]].name:
            departure_multiplication *= int(our_ticket[i])

    print('Part 1:', errors)
    print('Part 2:', departure_multiplication)
