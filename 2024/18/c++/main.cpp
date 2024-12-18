#include <iostream>
#include <string>
#include <unordered_set>
#include <queue>
#include <valarray>
#include <vector>
#include <__ranges/split_view.h>

#include "map.h"
#include "utils.h"

struct Triple {
    Coordinate first;
    int pathLength;
    int heuristic;
};

int getHeuristic(Coordinate current, Coordinate goal) {
    return std::abs(current.x - goal.x)+std::abs(current.y - goal.y);
}

int getAnswer(Map& map) {
    auto cmp = [](const Triple& l, const Triple& r) {
        return l.pathLength + l.heuristic > r.pathLength + r.heuristic;
    };
    std::priority_queue<Triple, std::vector<Triple>, decltype(cmp)> q(cmp);
    // std::queue<CoordinateWithPathLength> q;
    std::unordered_map<Coordinate, int> visited;
    q.emplace(map.find('S').value(), 0, 0);
    const auto end = map.find('E').value();

    while (!q.empty()) {
        auto [current, pathLength, heuristic] = q.top(); q.pop();
        // printf("Popping item: (%d,%d) with length %d.\n", current.x, current.y, pathLength);
        visited[current] = pathLength;
        if (map.get(current) == '#') continue;
        if (map.get(current) == 'E') {
            return pathLength;
        }
        for (int i = 0; i < 4; i++) {
            const auto [transX, transY] = dirTransforms[i%4];
            if (const char neighbour = map.get(current.x + transX, current.y + transY); neighbour != '-' &&neighbour != '#') {
                const Coordinate next = {current.x + transX, current.y + transY};
                if (visited.contains(next) && visited[next] <= pathLength+1) continue;
                // if (visited.contains(nextBiDir) && visited[nextBiDir] < prio+increase || prio+increase > max) continue;
                q.emplace(next, pathLength+1, getHeuristic(next, end));
            }
        }
    }
    return -1;
}

int main() {
    std::vector<std::string> lines = readFile("../input/input");
    Map map(71, 71);
    std::vector<Coordinate> corruptedBytes;
    for (const auto& line : lines) {
        auto parts = split(line, ',');
        corruptedBytes.emplace_back(std::stoi(parts[0]), std::stoi(parts[1]));
    }
    map.set(0, 0, 'S');
    map.set(70, 70, 'E');
    for (int i = 0; i < corruptedBytes.size(); i++) {
        map.set(corruptedBytes[i], '#');
        const int max = getAnswer(map);
        if (i == 1024) {
            printf("Part A: %d\n", max);
        }
        if (max == -1) {
            printf("Part B: %d,%d\n", corruptedBytes[i].x, corruptedBytes[i].y);
            break;
        }
    }

    return 0;
}
