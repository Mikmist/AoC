#include <iostream>
#include <string>
#include <vector>
#include "utils.h"

// For direction, we have
// 0 up
// 1 right
// 2 down
// 3 left

class Equation {
public:
    unsigned long result;
    std::vector<unsigned long> numbers;
};

std::vector<Equation> getEquations(const std::vector<std::string> &lines) {
    std::vector<Equation> equations;
    for (const auto& line: lines) {
        auto parts = split(line, ':');
        std::vector<unsigned long> numbers;
        for (const auto& part: split(parts[1].erase(0, 1), ' ')) {
            numbers.push_back(std::stoi(part));
        }
        equations.push_back({std::stoul(parts[0]), numbers});
    }
    return equations;
}

unsigned long concatenateNumbers(unsigned long a, unsigned long b) {
    return std::stol(std::to_string(a) + std::to_string(b));
}

bool checkEquationWithParams(const Equation& equation, const std::vector<int> &permutation) {
    unsigned long val = equation.numbers[0];
    for (int i = 1; i < equation.numbers.size(); i++) {
        if (permutation[i-1] == 0) val += equation.numbers[i];
        else if (permutation[i-1] == 1) val *= equation.numbers[i];
        else val = concatenateNumbers(val, equation.numbers[i]);
    }
    return val == equation.result;
}

unsigned long getAnswer(const std::vector<std::string> &lines, const bool partB) {
    unsigned long sum = 0;
    auto equations = getEquations(lines);
    for (const auto& equation: equations) {
        bool valid = false;
        const unsigned long length = equation.numbers.size() - 1;
        const int base = partB ? 3 : 2;
        for (int i = 0; i < std::pow(base, length); i++) {
            std::vector<int> permutation(length);
            int num = i;
            for (unsigned long j = 0; j < length; j++) {
                // Relic from bithshifting in part A
                // permutation[(i & (1 << j)) != 0];
                permutation[j] = num % base;
                num /= base;
            }
            if (checkEquationWithParams(equation, permutation)) {
                valid = true;
                break;
            }
        }
        if (valid) {
            sum += equation.result;
        }
    }
    return sum;
}

int main() {
    const std::vector<std::string> lines = readFile("../input/input");

    std::cout << "Part A: " << getAnswer(lines, false) << std::endl;
    std::cout << "Part B: " << getAnswer(lines, true) << std::endl;

    return 0;
}
