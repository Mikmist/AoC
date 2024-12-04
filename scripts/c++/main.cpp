#include <iostream>
#include <string>
#include <fstream>
#include <sstream>
#include <iostream>
#include <stdexcept>
#include <algorithm>
#include <valarray>
#include <unordered_map>

std::vector<std::string> readFile(const std::string& fileName) {
    std::vector<std::string> lines;
    std::ifstream file(fileName);

    if (!file.is_open()) {
        std::cerr << "Error opening file " << fileName << std::endl;
        throw std::runtime_error("Error opening file");
    }

    std::string line;

    while (std::getline(file, line)) {
        lines.push_back(line);
    }

    file.close();
    return lines;
}

int partOne(const std::vector<std::string>& lines) {
  return 0;
}

int partTwo(const std::vector<std::string>& lines) {
  return 0;
}

int main() {
    const std::vector<std::string> lines = readFile("../input/test");

    std::cout << "Part A:" << partOne(lines) << std::endl;
    std::cout << "Part B:" << partTwo(lines) << std::endl;

    return 0;
}
