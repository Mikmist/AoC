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

Map::Map(const Map& map) {
    std::vector<std::vector<char>> data;
    for (int i = 0; i < map.height; i++) {
        std::vector<char> row;
        for (int j = 0; j < map.width; j++) {
            row.push_back(map.data[i][j]);
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

char Map::get(const int x, const int y) const {
    if (x < 0 || x >= width || y < 0 || y >= height) {
        return '-';
    }
    return data[y][x];
}

char Map::get(const Coordinate coordinate) const {
    return this->get(coordinate.x, coordinate.y);
}

void Map::set(const int x, const int y, const char val) {
    if (x < 0 || x >= width || y < 0 || y >= height) {
        return;
    }
    this->data[y][x] = val;
}

void Map::set(const Coordinate coordinate, const char val) {
    return this->set(coordinate.x, coordinate.y, val);
}
