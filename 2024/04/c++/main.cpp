#include <iostream>
#include <string>
#include <vector>
#include "map.h"
#include "utils.h"


int checkNeighbours(const Map& map, const char last, const int x, const int y, const int xDir, const int yDir) {
    int val = 0;
    if (last == 'S') {
        return 1;
    }
    auto const cur = map.get(x+xDir, y+yDir);
    if (last == 'X' && cur == 'M' || last == 'M' && cur == 'A' || last == 'A' && cur == 'S') {
        val += checkNeighbours(map, cur, x+xDir, y+yDir, xDir, yDir);
    }
    return val;
}

int getAnswer(const Map& map, bool partA) {
    int sum = 0;
    for (int i = 0; i < map.width; i++) {
        for (int j = 0; j < map.height; j++) {
            if (partA && map.get(i, j) == 'X') {
                for (int iDir = -1; iDir <= 1; iDir++) {
                    for (int jDir = -1; jDir <= 1; jDir++) {
                        if (i == 0 && j == 0) continue;
                        sum += checkNeighbours(map, 'X', i, j, iDir, jDir);
                    }
                }
            } else if (!partA && map.get(i, j) == 'A') {
                auto const a = map.get(i-1, j-1);
                auto const b = map.get(i+1, j+1);
                auto const c = map.get(i-1, j+1);
                auto const d = map.get(i+1, j-1);

                if ((a == 'M' && b == 'S' || a == 'S' && b == 'M') &&
                    (c == 'M' && d == 'S' || c == 'S' && d == 'M')) {
                    sum += 1;
                }
            }
        }
    }
    return sum;
}

int main() {
    const std::vector<std::string> lines = readFile("../input/input");

    const Map map(lines);

    std::cout << "Part A: " << getAnswer(map, true) << std::endl;
    std::cout << "Part B: " << getAnswer(map, false) << std::endl;

    return 0;
}
