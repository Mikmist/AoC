direction=90
x=0
y=0
with open('../input/input') as data:
	for line in data:
		command = line.strip()[0]
		amount = int(line.strip()[1:])
		if command == 'F':
			if direction == 90:
				command = 'E'
			if direction == 180:
				command = 'S'
			if direction == 270:
				command = 'W'
			if direction == 0:
				command = 'N'
		if command == 'N':
			y += amount
		if command == 'S':
			y -= amount
		if command == 'E':
			x += amount
		if command == 'W':
			x -= amount
		if command == 'L':
			direction -= amount
		if command == 'R':
			direction += amount
		if direction > 359:
			direction -= 360
		if direction < 0:
			direction += 360

print('Part 1:', abs(x) + abs(y))

waypointx=10
waypointy=1

def rotateWaypoints(rotation):
	global waypointx
	global waypointy
	if rotation == 90:
		temp = waypointy
		waypointy = waypointx * -1
		waypointx = temp
		
	if rotation == 180:
		waypointx = waypointx * -1
		waypointy = waypointy * -1
		
	if rotation == 270:
		temp = waypointy
		waypointy = waypointx
		waypointx = temp * -1
		
x=0
y=0
with open('../input/input') as data:
	for line in data:
		command = line.strip()[0]
		amount = int(line.strip()[1:])
		if command == 'F':
			x += amount*waypointx
			y += amount*waypointy
		if command == 'N':
			waypointy += amount
		if command == 'S':
			waypointy -= amount
		if command == 'E':
			waypointx += amount
		if command == 'W':
			waypointx -= amount
		if command == 'L':
			amount = 360 - amount
			command = 'R'
		if command == 'R':
			rotateWaypoints(amount)

print('Part 2:', abs(x) + abs(y))