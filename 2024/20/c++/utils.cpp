//
// Created by Zino Holwerda on 04/12/2024.
//

#include "utils.h"
#include <sstream>

std::vector<std::string> readFile(const std::string& fileName) {
    std::vector<std::string> lines;
    std::ifstream file(fileName);

    if (!file.is_open()) {
        std::cerr << "Error opening file " << fileName << std::endl;
        throw std::runtime_error("Error opening file");
    }

    std::string line;

    while (std::getline(file, line, '\n')) {
        lines.push_back(line);
    }

    file.close();
    return lines;
}

std::vector<std::string> split(const std::string& s, char delim) {
    std::vector<std::string> tokens;
    std::string token;
    std::stringstream ss(s);
    while (getline(ss, token, delim)) {
        tokens.push_back(token);
    }
    return tokens;
}

void printProgressBar(const int part, const int total) {
    float progress = static_cast<float>(part) / static_cast<float>(total);
    int barWidth = 70;

    std::cout << "[";
    int pos = barWidth * progress;
    for (int i = 0; i < barWidth; ++i) {
        if (i < pos) std::cout << "=";
        else if (i == pos) std::cout << ">";
        else std::cout << " ";
    }
    std::cout << "] " << int(progress * 100.0) << " %\r";
    std::cout.flush();
}