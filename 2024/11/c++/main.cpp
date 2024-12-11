#include <iostream>
#include <string>
#include <vector>
#include <cmath>
#include "utils.h"

std::vector<uint64_t> getResult(const uint64_t& number) {
    const uint8_t numDigits = (number == 0) ? 0 : 1 + std::floor(std::log10(number));
    if (numDigits & 1) {
        return { number * 2024 };
    }
    const uint64_t pow10 = std::pow(10, numDigits/2);

    return {number / pow10, number % pow10};
}

std::unordered_map<uint64_t, uint64_t> getStones(const std::string& input) {
    std::unordered_map<uint64_t, uint64_t> stones;
    for (const auto& part : split(input, ' ')) {
        stones.insert({std::stoul(part), 1});
    }
    return stones;
}

uint64_t getAnswer(const std::vector<std::string> &lines, const int blinks) {
    auto stones = getStones(lines[0]);
    std::unordered_map<uint64_t, std::vector<uint64_t>> results;

    for(uint64_t i = 0; i < blinks; i++) {
        std::unordered_map<uint64_t, uint64_t> nextStones;
        for(const auto& pair : stones) {
            const uint64_t& stone = pair.first;
            if(stone == 0) {
                nextStones[1] += pair.second;
                continue;
            }

            auto& res = results[stone];
            if(res.empty()) {
                res = getResult(stone);
            }

            for(const uint64_t& val : res) {
                nextStones[val] += pair.second;
            }
        }

        stones = nextStones;
    }

    size_t out = 0;
    for(const auto& pair : stones) {
        out += pair.second;
    }

    return out;
}



int main() {
    const std::vector<std::string> lines = readFile("../input/input");
    getResult(253000);

    std::cout << "Part A: " << getAnswer(lines, 25) << std::endl;
    std::cout << "Part B: " << getAnswer(lines, 75) << std::endl;

    return 0;
}
