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

int getNumbersDistanceFromLines(const std::vector<std::string>& lines) {
    std::vector<int> leftNumbers;
    std::vector<int> rightNumbers;
    int sum = 0;

    for (const auto& line : lines) {
        std::cout << line << std::endl;
        std::istringstream iss(line);
        int number;
        if (iss >> number) {
            leftNumbers.push_back(number);
        }
        if (iss >> number) {
            rightNumbers.push_back(number);
        }
    }

    std::ranges::sort(leftNumbers);
    std::ranges::sort(rightNumbers);

    for (int i = 0; i <= leftNumbers.size(); i++) {
        // std::cout << leftNumbers[i] << " " << rightNumbers[i] << std::endl;
        int number = (std::abs(leftNumbers[i] - rightNumbers[i]));
        sum += number;
        // std::cout << number << std::endl;
    }

    return sum;
}

int partTwo(const std::vector<std::string>& lines) {
    std::vector<int> leftNumbers;
    std::unordered_map<int, int> map;
    int sum = 0;

    for (const auto& line : lines) {
        std::cout << line << std::endl;
        std::istringstream iss(line);
        int number;
        if (iss >> number) {
            leftNumbers.push_back(number);
        }
        if (iss >> number) {
            if (map.contains(number)) {
                map[number]++;
            } else {
                map[number] = 1;
            }
        }
    }

    for (int i = 0; i <= leftNumbers.size(); i++) {
        int multiplier = map[leftNumbers[i]];
        if (multiplier == 0) {
            continue;
        }
        int number = leftNumbers[i] * multiplier;
        sum += number;
        std::cout << number << std::endl;
    }

    return sum;
}

int main() {
    // TIP Press <shortcut actionId="RenameElement"/> when your caret is at the // <b>lang</b> variable name to see how CLion can help you rename it.
    const std::vector<std::string> lines = readFile("../input/input");

    std::cout << getNumbersDistanceFromLines(lines) << std::endl;
    std::cout << partTwo(lines) << std::endl;

    return 0;
}
