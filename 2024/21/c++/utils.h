//
// Created by Zino Holwerda on 04/12/2024.
//

#ifndef UTILS_H
#define UTILS_H

#include <vector>
#include <iostream>
#include <fstream>

std::vector<std::string> readFile(const std::string& fileName);
std::vector<std::string> split(const std::string& s, char delim);
void printProgressBar(int part, int total);

#endif //UTILS_H
