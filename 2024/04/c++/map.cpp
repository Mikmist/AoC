//
// Created by Zino Holwerda on 04/12/2024.
//

#include "map.h"

Map::Map(const std::vector<std::string>& lines) {
    std::vector<std::vector<char>> data;
    for (const auto& line : lines) {
        std::vector<char> row;
        for (const auto& c : line) {
            row.push_back(c);
        }
        data.push_back(row);
    }
    width = data[0].size();
    height = data.size();
    this->data = data;
}

void Map::print() const {
    std::cout << "print:" << std::endl;
    for (const auto& row : this->data) {
        for (const auto& c : row) {
            std::cout << c << " ";
        }
        std::cout << std::endl;
    }
}

char Map::get(int x, int y) const {
    if (x < 0 || x >= width || y < 0 || y >= height) {
        return '-';
    }
    return data[y][x];
}
