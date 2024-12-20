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
    std::optional<Coordinate> startOfCheat;
    std::optional<Coordinate> endOfCheat;
    int timeSinceCheat;
    std::vector<Coordinate> path;
};

int getHeuristic(Coordinate current, Coordinate goal) {
    return std::abs(current.x - goal.x)+std::abs(current.y - goal.y);
}

std::optional<Triple> getAnswer(const Map& map, Coordinate start, Coordinate end) {
    auto cmp = [](const Triple& l, const Triple& r) {
        return l.pathLength + l.heuristic > r.pathLength + r.heuristic;
    };
    std::priority_queue<Triple, std::vector<Triple>, decltype(cmp)> q(cmp);
    // std::queue<CoordinateWithPathLength> q;
    std::unordered_map<Coordinate, int> visited;
    std::unordered_set<std::string> solutions;
    q.emplace(start, 0, 0, std::nullopt, std::nullopt, -1, std::vector<Coordinate>());

    while (!q.empty()) {
        auto cur = q.top();
        auto [current, pathLength, heuristic, startOfCheat, endOfCheat, timeSinceCheat, path] = cur; q.pop();
        // printf("Popping item: (%d,%d) with length %d.\n", current.x, current.y, pathLength);
        path.push_back(current);
        cur.path.push_back(current);
        visited[current] = pathLength;
        if (map.get(current) == '#' && timeSinceCheat < 0) continue;
        if (current == end) {
            if (timeSinceCheat >= 0) {
                cur.endOfCheat = current;
            }
            return cur;
        }
        for (int j = 0; j < 4; j++) {
            const auto [transX, transY] = dirTransforms[j%4];
            if (const char neighbour = map.get(current.x + transX, current.y + transY); neighbour != '-' && (timeSinceCheat > 0 || neighbour != '#')) {
                const Coordinate next = {current.x + transX, current.y + transY};
                if (visited.contains(next) && visited[next] <= pathLength+1) continue;

                if (neighbour == 'C' &&  !startOfCheat.has_value()) {
                    startOfCheat = current;
                    timeSinceCheat = 20;
                }
                if (timeSinceCheat == 0) endOfCheat = next;
                q.emplace(next, pathLength+1, getHeuristic(next, end), startOfCheat, endOfCheat, timeSinceCheat-1, path);
            }
        }
    }
    return std::nullopt;
}

void pause() {
    std::cin.get();
}

int main() {
    std::vector<std::string> lines = readFile("../input/input");
    Map map(lines);
    // map.print();
    const auto start = map.find('S').value();
    const auto end = map.find('E').value();
    std::unordered_map<std::string, int> maxes;
    const Triple normal = getAnswer(map, start, end).value();

    // Old disfunctional part A
    // for (int i = 1; i < map.height-1; i++) {
    //     printProgressBar(i, map.height);
    //     for (int j = 1; j < map.width-1; j++) {
    //         std::optional<Triple> max;
    //         const auto m = map.get(j, i);
    //         map.set(j, i, 'C');
    //         if (m == '#') {
    //             max = getAnswer(map, start, end);
    //             if (max.has_value()) {
    //                 int m = max.value().pathLength;
    //                 if (normal.pathLength-m >= 50) {
    //                     std::string string_rep = max.value().startOfCheat.value().to_string() + '-' + max.value().endOfCheat.value().to_string();
    //                     if (!maxes.contains(string_rep)) maxes[string_rep] = 1;
    //                     else maxes[string_rep]++;
    //                 }
    //             }
    //         }
    //         map.set(j, i, m);
    //     }
    // }

    // Part B
    int countA = 0, countB = 0;
    for (int i = 0; i < normal.path.size(); i++) {
        Coordinate current = normal.path[i];
        for (int j = 0; j < normal.path.size(); j++) {
            Coordinate other = normal.path[j];
            if (current == other) continue;
            if (auto d = std::abs(current.x - other.x) + std::abs(current.y - other.y); d <= 20)
                if (j-i-d >= 100) countB++;
            if (auto d = std::abs(current.x - other.x) + std::abs(current.y - other.y); d <= 2)
                if (j-i-d >= 100) countA++;
        }
    }

    std::cout << "Part A: " << countA << '\n';
    std::cout << "Part B: " << countB << '\n';
    return 0;
}
