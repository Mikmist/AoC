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

/**
 * type is defined as true for increasing and false for decreasing
 */
bool checkNumbers(int index, const int last, const bool type, std::vector<int> &numbers) {
    if (numbers.size() == index) {
        return true;
    }
    if (int const difference = std::abs(numbers[index] - last);
        last != -1 && (difference < 1 || difference > 3) ||
        index > 1 && type != last < numbers[index]) {
        return false;
    }
    return checkNumbers(index + 1, numbers[index], last < numbers[index],  numbers);
}

int getAnswer(const std::vector<std::string>& lines, bool part) {
    int count = 0;

    for (const auto& line : lines) {
        std::vector<int> numbers;
        std::istringstream iss(line);

        int number;
        while (iss >> number) {
            numbers.push_back(number);
        }

        if (part) {
            for (int i = 0; i < numbers.size(); ++i) {
                std::vector<int> numbersCopy = numbers;
                numbersCopy.erase(numbersCopy.begin() + i);
                if (checkNumbers(0, -1, false, numbersCopy)) {
                    count++;
                    break;
                }
            }
        }
        else {
            if (checkNumbers(0, -1, false, numbers)) count++;
        }
    }

    return count;
}

int main() {
    const std::vector<std::string> lines = readFile("../input/input");

    std::cout << "Part A:" << getAnswer(lines, false) << std::endl;
    std::cout << "Part B:" << getAnswer(lines, true) << std::endl;

    return 0;
}
