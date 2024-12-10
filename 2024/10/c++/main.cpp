#include <iostream>
#include <map>
#include <set>
#include <string>
#include <unordered_set>
#include <vector>
#include "map.h"
#include "utils.h"

int dfs(Map& map, std::unordered_set<Coordinate>& coordinates, const int x, const int y, const int last) {
    const int cur = map.getInt(x, y);
    if (cur == -2 || cur != last+1) {
        return 0;
    }
    std::cout << "cur: " << cur << " at (" << x << "," << y << "), " << last << std::endl;
    if (cur == 9 && last == 8) {
        coordinates.insert({x, y});
        return 1;
    }
    return dfs(map, coordinates, x + 1, y, cur) +
        dfs(map, coordinates, x, y + 1, cur) +
        dfs(map, coordinates, x - 1, y, cur) +
        dfs(map, coordinates, x, y - 1, cur);
}

int getAnswer(Map& map, const bool partB) {
    int sum = 0;
    int sumPartB = 0;
    for (int i = 0; i < map.height; ++i) {
        for (int j = 0; j < map.width; ++j) {
            std::unordered_set<Coordinate> coordinates;
            sumPartB += dfs(map, coordinates, j, i, -1);
            sum += coordinates.size();
        }
    }
    return partB ? sumPartB : sum;
}

int main() {
    const std::vector<std::string> lines = readFile("../input/input");

    Map map(lines);
    std::unordered_map<char, std::vector<Coordinate>> coordinates;
    map.print();

    std::cout << "Part A: " << getAnswer(map, false) << std::endl;
    std::cout << "Part B: " << getAnswer(map, true) << std::endl;

    return 0;
}
