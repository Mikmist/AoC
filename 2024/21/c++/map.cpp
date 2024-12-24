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

Map::Map(const int width, const int height) {
    this->width = width;
    this->height = height;
    std::vector<std::vector<char>> data;
    for (int i = 0; i < height; i++) {
        std::vector<char> row;
        for (int j = 0; j < width; j++) {
            row.push_back('.');
        }
        data.push_back(row);
    }
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

void Map::printWithCharacter(const int x, const int y, const char character) const {
    std::cout << "print:" << std::endl;

    for (int i = 0; i < this->height; i++) {
        for (int j = 0; j < this->width; j++) {
            if (j == x && i == y) std::cout << character;
            else std::cout << this->data[i][j];
        } std::cout << std::endl;
    }
}

std::optional<Coordinate> Map::find(const char character) const {
    for (int i = 0; i < this->height; i++) {
        for (int j = 0; j < this->width; j++) {
            if (character == this->data[i][j]) return Coordinate(j, i);
        }
    }
    return std::nullopt;
}

std::vector<Coordinate> Map::findAll(const char character) const {
    std::vector<Coordinate> coordinates;
    for (int i = 0; i < this->height; i++) {
        for (int j = 0; j < this->width; j++) {
            if (character == this->data[i][j]) {
                coordinates.push_back(Coordinate(j, i));
            }
        }
    }
    return coordinates;
}

char Map::get(const int x, const int y) const {
    if (x < 0 || x >= width || y < 0 || y >= height) {
        return '-';
    }
    // if (data[y][x] == '1') return '.';
    // if (data[y][x] == '2') return '.';
    return data[y][x];
}

int Map::getInt(const int x, const int y) const {
    if (x < 0 || x >= width || y < 0 || y >= height) {
        return -2;
    }
    return data[y][x] - '0';
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
