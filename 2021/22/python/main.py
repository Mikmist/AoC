import re, collections


on = {}
cubes = collections.Counter()

with open('../input/test') as data:
    for line in data:
        # Part A, slow and naive.
        task = line.strip().split()[0]
        x, y, z = line.strip().split()[1].split(",")
        z_list = list(map(int, z[2:].split("..")))
        for zCur in range(max(z_list[0], -50), min(50, z_list[1]) + 1):
            y_list = list(map(int, y[2:].split("..")))
            for yCur in range(max(y_list[0], -50), min(50, y_list[1]) + 1):
                x_list = list(map(int, x[2:].split("..")))
                for xCur in range(max(x_list[0], -50), min(50, x_list[1]) + 1):
                    if task == "on":
                        on[(zCur, yCur, xCur)] = True
                    elif (zCur, yCur, xCur) in on:
                        on.pop((zCur, yCur, xCur))
        # Part B, fast and cheaky
        sign = 1 if task == "on" else -1
        minX, maxX, minY, maxY, minZ, maxZ = map(int, re.findall("-?\d+", line))
        newCubes = collections.Counter()
        # Turn off intersection
        for (curMinX, curMaxX, curMinY, curMaxY, curMinZ, curMaxZ), curSign in cubes.items():
            intersectXMin = max(curMinX, minX)
            intersectXMax = min(curMaxX, maxX)
            intersectYMin = max(curMinY, minY)
            intersectYMax = min(curMaxY, maxY)
            intersectZMin = max(curMinZ, minZ)
            intersectZMax = min(curMaxZ, maxZ)
            if intersectXMin <= intersectXMax and intersectYMin <= intersectYMax and intersectZMin <= intersectZMax:
                newCubes[(intersectXMin, intersectXMax, intersectYMin, intersectYMax, intersectZMin, intersectZMax)] -= curSign
        # If task is 'on' turn the new cube on.
        if sign == 1:
            newCubes[(minX, maxX, minY, maxY, minZ, maxZ)] = sign
        cubes.update(newCubes)
    print(len(on))
    print(sum((xMax - xMin + 1) * (yMax - yMin + 1) * (zMax - zMin + 1) * sign 
        for (xMin, xMax, yMin, yMax, zMin, zMax), sign in cubes.items()))


        

    