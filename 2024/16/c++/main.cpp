#include <iostream>
#include <string>
#include <unordered_set>
#include <queue>
#include <vector>
#include "map.h"
#include "utils.h"

int getAnswer(Map& map) {
    auto reindeer = map.find('S').value();
    using PrioDirectionalCoordinate = std::pair<int, DirectionalCoordinate>;
    auto cmp = [](const PrioDirectionalCoordinate& l, const PrioDirectionalCoordinate& r) {
        return l.first > r.first;
    };
    std::priority_queue<PrioDirectionalCoordinate, std::vector<PrioDirectionalCoordinate>, decltype(cmp)> q(cmp);
    std::unordered_map<DirectionalCoordinate, int> visited;
    q.push({0, {reindeer.x, reindeer.y, 0}});
    q.push({1000, {reindeer.x, reindeer.y, 3}});

    while (!q.empty()) {
        auto [prio, diCoord] = q.top(); q.pop();
        visited[diCoord] = prio;
        if (map.get(diCoord.x, diCoord.y) == '#') continue;
        if (map.get(diCoord.x, diCoord.y) == 'E') return prio;
        for (int i = 0; i < 4; i++) {
            const auto [transX, transY] = dirTransforms[(diCoord.direction+i)%4];
            if (char neighbour = map.get(diCoord.x + transX, diCoord.y + transY); neighbour != '#' && i != 2) {
                const DirectionalCoordinate nextBiDir = {diCoord.x + transX, diCoord.y + transY, (diCoord.direction+i)%4};
                const int increase = i == 0 ? 1 : 1001;
                if (visited.contains(nextBiDir) && visited[nextBiDir] < prio+increase) continue;
                q.emplace(prio + increase, nextBiDir);
            }
        }
    }
    return 0;
}

void getAnswerB(Map& map, Map& mapB, const int max) {
    auto reindeer = map.find('S').value();
    using PrioDirectionalCoordinate = std::pair<int, std::pair<DirectionalCoordinate, std::vector<Coordinate>>>;
    auto cmp = [](const PrioDirectionalCoordinate& l, const PrioDirectionalCoordinate& r) {
        return l.first > r.first;
    };
    std::priority_queue<PrioDirectionalCoordinate, std::vector<PrioDirectionalCoordinate>, decltype(cmp)> q(cmp);
    std::unordered_map<DirectionalCoordinate, int> visited;
    q.push({0, {{reindeer.x, reindeer.y, 0}, {{reindeer.x, reindeer.y}}}});
    q.push({1000, {{reindeer.x, reindeer.y, 3}, {{reindeer.x, reindeer.y}}}});

    while (!q.empty()) {
        auto [prio, val] = q.top(); q.pop();
        visited[val.first] = prio;
        if (map.get(val.first.x, val.first.y) == '#') continue;
        if (map.get(val.first.x, val.first.y) == 'E') {
            for (const auto& coordinate : val.second) {
                mapB.set(coordinate, 'O');
            }
            continue;
        }
        for (int i = 0; i < 4; i++) {
            const auto [transX, transY] = dirTransforms[(val.first.direction+i)%4];
            if (char neighbour = map.get(val.first.x + transX, val.first.y + transY); neighbour != '#' && i != 2) {
                const DirectionalCoordinate nextBiDir = {val.first.x + transX, val.first.y + transY, (val.first.direction+i)%4};
                const int increase = i == 0 ? 1 : 1001;
                if (visited.contains(nextBiDir) && visited[nextBiDir] < prio+increase || prio+increase > max) continue;
                std::vector<Coordinate> path = val.second;
                path.push_back({val.first.x, val.first.y});
                q.push({prio + increase, {nextBiDir, path}});
            }
        }
    }
}

int main() {
    std::vector<std::string> lines = readFile("../input/input");
    Map map(lines);
    Map mapB(lines);

    int max = getAnswer(map);
    std::cout << "Part A: " << max << std::endl;
    getAnswerB(map, mapB, max);
    std::cout << "Part B: " << mapB.findAll('O').size()+1 << std::endl;

    return 0;
}
