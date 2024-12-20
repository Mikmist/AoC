#include <iostream>
#include <string>
#include <unordered_set>
#include <vector>

#include "utils.h"

std::unordered_map<std::string, uint64_t> cache;

uint64_t matches(const std::string& design, const std::unordered_set<std::string>& options) {
    if (design.empty()) return 1;
    if (cache.contains(design)) return cache[design];

    uint64_t ways = 0;
    for (const auto& option : options) {
        if (design.substr(0, option.size()) == option) {
            ways += matches(design.substr(option.size()), options);
        }
    }
    cache[design] = ways;
    return ways;
}

int main() {
    const std::vector<std::string> lines = readFile("../input/input");
    bool initLine = true;
    int count = 0;
    uint64_t countB = 0;
    int largestOption = 0;
    std::unordered_set<std::string> options;
    for (const auto& line : lines) {
        if (initLine) {
            for (auto optionArray = split(line, ','); auto& option : optionArray) {
                std::erase_if(option, isspace);
                if (option.size() > largestOption) largestOption = option.size();
                options.insert(option);
            }
            initLine = false;
            continue;
        }
        if (line.empty()) continue;

        auto res = matches(line, options);
        countB += res;
        if (res > 0) count++;
    }

    std::cout << "Part A: " << count << std::endl;
    std::cout << "Part B: " << countB << std::endl;

    return 0;
}
