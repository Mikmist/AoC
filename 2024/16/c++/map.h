//
// Created by Zino Holwerda on 04/12/2024.
//

#ifndef MAP_H
#define MAP_H
#include <vector>
#include <iostream>

const std::vector<std::pair<int, int>> dirTransforms = {{1, 0}, {0, 1}, {-1, 0}, {0, -1}};

class DirectionalCoordinate {
    public:
    int x;
    int y;
    int direction;

    // Equality operator
    bool operator==(const DirectionalCoordinate& other) const {
        return x == other.x && y == other.y && direction == other.direction;
    }
};

namespace std {
    template <>
    struct hash<DirectionalCoordinate> {
        size_t operator()(const DirectionalCoordinate& coord) const noexcept {
            return hash<int>()(coord.x) ^ hash<int>()(coord.y) ^ hash<int>()(coord.direction);
        }
    };
}

class Coordinate {
    public:
    int x;
    int y;

    // Equality operator
    bool operator==(const Coordinate& other) const {
        return x == other.x && y == other.y;
    }
};

namespace std {
    template <>
    struct hash<Coordinate> {
        size_t operator()(const Coordinate& coord) const noexcept {
            return hash<int>()(coord.x) ^ hash<int>()(coord.y);
        }
    };
}

class Map {
    public:
    unsigned long width;
    unsigned long height;
    std::vector<std::vector<char>> data;
    explicit Map(const std::vector<std::string> &lines);
    Map(const Map &other);
    void printWithCharacter(int x, int y, char character = 'X') const;
    void print() const;
    [[nodiscard]] std::optional<Coordinate> find(char character) const;
    [[nodiscard]] std::vector<Coordinate> findAll(char character) const;
    [[nodiscard]] char get(int x, int y) const;
    [[nodiscard]] int getInt(int x, int y) const;
    [[nodiscard]] char get(Coordinate coordinate) const;
    void set(int x, int y, char val);
    void set(Coordinate coordinate, char val);
};

#endif //MAP_H
