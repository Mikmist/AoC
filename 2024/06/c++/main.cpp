#include <iostream>
#include <string>
#include <unordered_set>
#include <vector>
#include "map.h"
#include "utils.h"

// For direction, we have
// 0 up
// 1 right
// 2 down
// 3 left
const std::vector<std::vector<int>> dirTransforms =
    {{0, -1}, {1, 0}, {0, 1}, {-1, 0}};

void moveGuard(const Map& map, Coordinate& guard, int& direction) {
    char res = map.get(guard.x+dirTransforms[direction][0], guard.y+dirTransforms[direction][1]);
    if (res == '-') {
        guard.x = -1;
        guard.y = -1;
    }
    while (res == '#') {
        direction = (direction + 1) % 4;
        res = map.get(guard.x+dirTransforms[direction][0], guard.y+dirTransforms[direction][1]);
    }

    guard.x += dirTransforms[direction][0];
    guard.y += dirTransforms[direction][1];
}

int getAnswer(Map map, Coordinate guard) {
    int direction = 0;
    std::unordered_set<Coordinate> visited;
    std::unordered_set<DirectionalCoordinate> visitedPartB;

    do {
        visited.insert(guard);
        DirectionalCoordinate dc(guard.x, guard.y, direction);
        if (visitedPartB.contains(dc)) {
            return -1;
        }
        visitedPartB.insert(dc);
        moveGuard(map, guard, direction);
        map.set(guard, '%');
    } while (map.get(guard) != '-');

    return visited.size();
}

int countOptionsPartB(Map map, Coordinate guard) {
    int sum = 0;

    for (int i = 0; i <= map.height; i++) {
        for (int j = 0; j <= map.width; j++) {
            Map copy(map);
            if (copy.get(i, j) != '.') {
                continue;
            }
            copy.set(i, j, '#');
            Coordinate guardCopy(guard.x, guard.y);
            if (getAnswer(copy, guardCopy) == -1) {
                sum += 1;
            }
        }
    }

    return sum;
}

int main() {
    const std::vector<std::string> lines = readFile("../input/input");

    Map map(lines);
    Coordinate guard{};
    for (int i = 0; i < map.height; i++) {
        for (int j = 0; j < map.width; j++) {
            if (map.get(j, i) == '^') {
                guard = Coordinate(j, i);
            }
        }
    }
    map.set(guard, '%');
    // map.print();

    std::cout << "Part A: " << getAnswer(map, guard) << std::endl;
    std::cout << "Careful part B takes about one and half minute." << std::endl;
    std::cout << "Part B: " << countOptionsPartB(map, guard) << std::endl;

    return 0;
}
