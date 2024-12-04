//
// Created by Zino Holwerda on 04/12/2024.
//

#ifndef MAP_H
#define MAP_H
#include <vector>
#include <iostream>

class Map {
    public:
    unsigned long width;
    unsigned long height;
    std::vector<std::vector<char>> data;
    explicit Map(const std::vector<std::string> &lines);
    void print() const;
    char get(int x, int y) const;
};

#endif //MAP_H
