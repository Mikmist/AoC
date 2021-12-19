import itertools;

def rotate(l,x):
  x%=len(l)
  if x==0:
    return l.copy()
  ans=l[x:]+l[0:x]
  return ans


def generateVariations():
    rotations=[(1,1,1),(-1,-1,1),(-1,1,-1),(1,-1,-1)]
    permsutations=[[(0,1),(1,1),(2,1)],[(1,1),(0,1),(2,-1)]]
    variations=[]
    for i in rotations:
        for perms in permsutations:
            for j in range(len(perms)):
                cur=rotate(perms,j)
                variations.append([(cur[t][0],cur[t][1]*i[t]) for t in range(3)])
    return variations


with open("../input/input") as file:
    scanners = []
    count = 0
    for i in file.readlines():
        i=i.strip('\n')
        if len(i)==0:
            continue
        elif i.find("scanner")!=-1:
            scanners.append([])
            count += 1
        else:
            scanners[-1].append([int(x) for x in i.split(',')])
    
    done=set([0])
    undone=set(range(1,count))
    variations = generateVariations()
    positions = {}
    positions[0] = (0,0,0)

    while len(undone)!=0:
        i=done.pop()
        new_done=set()
        new_scanner_list = []
        for scannerIdx in undone:
            scannerFinished = False
            for variation in variations:
                if not scannerFinished:
                    current_points = []
                    for point in scanners[scannerIdx]:
                        current_points.append([point[variation[i][0]] * variation[i][1] for i in range(3)])
                    for ogPoint in scanners[i]:
                        if scannerFinished:
                            break
                        for mapping_point in current_points:
                            matching_points = []
                            x,y,z = [ogPoint[i] - mapping_point[i] for i in range(3)]
                            current_set=set([tuple(T) for T in scanners[i]])
                            known_set=set()
                            for T in current_points:
                                known_set.add(tuple([T[0]+x,T[1]+y,T[2]+z]))
                            if len(known_set.intersection(current_set))>=12:
                                new_done.add(scannerIdx)
                                undone-=new_done
                                done|=new_done
                                got_ans=True
                                positions[scannerIdx]=(x,y,z)
                                scanners[scannerIdx]=list(known_set)
                                scannerFinished=True
                                break


totalPoints=set()
for i in scanners:
    for j in i:
        totalPoints.add(tuple(j))
print("Part A:", len(totalPoints))

distance = 0
for i in positions.values(): 
    for j in positions.values():
        distance = max(distance, abs(i[0] - j[0]) + abs(i[1] - j[1]) + abs(i[2] - j[2]))

print("Part B:", distance)