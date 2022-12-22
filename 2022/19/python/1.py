import copy


def simulate_blueprint(minute, ores, robots, blueprint):
    #print(minute, robots, blueprint)
    if minute == 24:
        return ores["geode"]
    for i in robots:
        #print(i, ores[i], robots[i])
        ores[i] += robots[i]
    m = 0
    oc = copy.deepcopy(ores)
    rc = copy.deepcopy(robots)
    m = max(m, simulate_blueprint(minute+1, oc, rc, blueprint))
    if ores["geode"] >= blueprint[3][0] and ores["obisidian"] >= blueprint[3][1]:
        oc = copy.deepcopy(ores)
        rc = copy.deepcopy(robots)
        oc["ore"] -= blueprint[3][0] 
        oc["obsidian"] -= blueprint[3][1]
        rc["geode"] += 1 
        m = max(m, simulate_blueprint(minute+1, oc, rc, blueprint))
    if ores["ore"] >= blueprint[2][0] and ores["clay"] >= blueprint[2][1]:
        oc = copy.deepcopy(ores)
        rc = copy.deepcopy(robots)
        oc["ore"] -= blueprint[2][0] 
        oc["clay"] -= blueprint[2][1]
        rc["obsidian"] += 1 
        m = max(m, simulate_blueprint(minute+1, oc, rc, blueprint))
    if ores["ore"] >= blueprint[1]:
        oc = copy.deepcopy(ores)
        rc = copy.deepcopy(robots)
        oc["ore"] -= blueprint[1] 
        rc["clay"] += 1 
        m = max(m, simulate_blueprint(minute+1, oc, rc, blueprint))
    if ores["ore"] >= blueprint[0]:
        oc = copy.deepcopy(ores)
        rc = copy.deepcopy(robots)
        oc["ore"] -= blueprint[0] 
        rc["ore"] += 1 
        m = max(m, simulate_blueprint(minute+1, oc, rc, blueprint))
    return m


with open('../input/test') as data:
    for blueprint in data.read().split('\n\n'):
        print(blueprint)
        parts = blueprint.split('\n')
        ore_robot = int(parts[1].split(' ')[6])
        clay_robot = int(parts[2].split(' ')[6])
        obs_robot = [int(parts[3].split(' ')[6]), int(parts[3].split(' ')[9])]
        geode_robot = [int(parts[4].split(' ')[6]) , int(parts[3].split(' ')[9])]
        blueprint = [ore_robot, clay_robot, obs_robot, geode_robot]
        robots = {"ore": 1, "clay": 0, "obsidian": 0, "geode": 0}
        ores = {"ore": 1, "clay": 0, "obsidian": 0, "geode": 0}
        simulate_blueprint(0, ores, robots, blueprint)
        print(ore_robot, clay_robot, obs_robot, geode_robot)
