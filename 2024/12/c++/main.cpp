#include <iostream>
#include <string>
#include <unordered_set>
#include <vector>
#include "map.h"
#include "utils.h"

int dfs(
    Map& map, std::unordered_set<Coordinate>& coordinates,
    std::unordered_set<DirectionalCoordinate>& neighbours,
    const int x, const int y, const char last, const int dir
    ) {
    const char cur = map.get(x, y);
    if (cur == '-' || cur != last) {
        neighbours.insert({x, y, dir});
        return 1;
    }
    if (coordinates.contains(Coordinate(x, y))) {
        return 0;
    }
    coordinates.insert({x, y});
    return dfs(map, coordinates, neighbours, x + 1, y, cur, 0) +
        dfs(map, coordinates, neighbours, x, y + 1, cur, 1) +
        dfs(map, coordinates, neighbours, x - 1, y, cur, 2) +
        dfs(map, coordinates, neighbours, x, y - 1, cur, 3);
}

int calculateEdges(std::unordered_set<DirectionalCoordinate> &coordinates) {
    int count = 0;
    for (const auto coordinate : coordinates) {
        const int dir = coordinate.direction;
        if (dir == 1 || dir == 3) {
            int x = coordinate.x+1;
            while (coordinates.contains({x, coordinate.y, dir})) {
                coordinates.erase({x, coordinate.y, dir});
                x++;
            }
            x = coordinate.x-1;
            while (coordinates.contains({x, coordinate.y, dir})) {
                coordinates.erase({x, coordinate.y, dir});
                x--;
            }
        } else {
            int y = coordinate.y+1;
            while (coordinates.contains({coordinate.x, y, dir})) {
                coordinates.erase({coordinate.x, y, dir});
                y++;
            }
            y = coordinate.y-1;
            while (coordinates.contains({coordinate.x, y, dir})) {
                coordinates.erase({coordinate.x, y, dir});
                y--;
            }
        }
        count++;
    }
    return count;
}

int getAnswer(Map& map, const bool partB) {
    int sum = 0, sumB = 0;
    std::unordered_set<Coordinate> coordinates;
    int lastSize = 0;
    for (int i = 0; i < map.height; ++i) {
        for (int j = 0; j < map.width; ++j) {
            if (coordinates.contains({j, i})) {
                continue;
            }
            std::unordered_set<DirectionalCoordinate> neighbours;
            sum += dfs(map, coordinates, neighbours, j, i, map.get(j, i), 0) * (coordinates.size() - lastSize);
            sumB += calculateEdges(neighbours) * (coordinates.size() - lastSize);
            lastSize = coordinates.size();
        }
    }
    return partB ? sumB : sum;
}

int main() {
    const std::vector<std::string> lines = readFile("../input/input");

    Map map(lines);

    std::cout << "Part A: " << getAnswer(map, false) << std::endl;
    std::cout << "Part B: " << getAnswer(map, true) << std::endl;

    return 0;
}
