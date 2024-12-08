#include <iostream>
#include <map>
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

int getAnswer(Map& map, std::unordered_map<char, std::vector<Coordinate>> coordinates, bool partB) {
    std::unordered_set<Coordinate> nodes;
    int count = 0;
    int countT = 0;
    for (const auto &it : coordinates) {
        bool inLine = it.second.size() > 2 && partB;
        for (const auto &coord : it.second) {
            for (const auto &other : it.second) {
                bool goOnce = true;
                if (coord == other) {
                    continue;
                }
                int x = coord.x; int y = coord.y;
                const int differenceX = coord.x - other.x;
                const int differenceY = coord.y - other.y;
                if (inLine) map.set(x, y, '#');
                while (goOnce || inLine) {
                    x += differenceX;
                    y += differenceY;
                    if (map.get(x, y) != '-') {
                        map.set(x, y, '#');
                        goOnce = false;
                    } else {
                        break;
                    }
                }
            }
        }
    }
    map.print();
    for (int i = 0; i < map.height; i++) {
        for (int j = 0; j < map.width; j++) {
            if (map.get(j, i) == '#') {
                count++;
            }
        }
    }
    return count;
}

int main() {
    const std::vector<std::string> lines = readFile("../input/input");

    Map map(lines);
    std::unordered_map<char, std::vector<Coordinate>> coordinates;
    for (int i = 0; i < map.height; i++) {
        for (int j = 0; j < map.width; j++) {
            auto current = map.get(j, i);
            if (map.get(j, i) == '.') {
                continue;
            }
            if (!coordinates.contains(current)) {
                coordinates[current] = std::vector<Coordinate>();
            }
            coordinates[map.get(j, i)].push_back({j, i});
        }
    }

    std::cout << "Part A: " << getAnswer(map, coordinates, false) << std::endl;
    std::cout << "Part B: " << getAnswer(map, coordinates, true) << std::endl;

    return 0;
}
