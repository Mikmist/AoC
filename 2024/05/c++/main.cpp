#include <iostream>
#include <string>
#include <unordered_set>
#include <vector>
#include "utils.h"

class Container {
public:
    std::vector<int> data;
    bool valid;
};

Container trialRun(std::vector<int>& input, const std::unordered_map<int, std::vector<int>>& rules) {
    std::vector<int> passedItems;
    bool valid = true;
    for (int i = 0; i < input.size(); i++) {
        auto item = input[i];
        if (rules.contains(item)) {
            std::vector<int> rulesForItem = rules.find(item)->second;
            for (auto& alreadyFoundItem : rulesForItem) {
                for (const auto& passedItem : passedItems) {
                    if (passedItem == alreadyFoundItem) {
                        valid = false;

                        for (int j = 0; j <= i; j++) {
                            if (input[j] == passedItem) {
                                passedItems.insert(passedItems.begin() + j, item);
                                break;
                            }
                        }
                        for (int j = i+1; j < input.size(); j++) {
                            passedItems.push_back(input[j]);
                        }
                        return Container(passedItems, valid);
                    }
                }
            }
        }
        passedItems.push_back(item);
    }
    return Container(passedItems, valid);
}

int getAnswer(std::vector<std::vector<int>> input, const std::unordered_map<int, std::vector<int>>& rules, bool partA) {
    int sum = 0;

    for (auto& inputItem : input) {
        bool valid;
        do {
            auto result = trialRun(inputItem, rules);
            valid = result.valid;

            if (valid) {
                sum += result.data[result.data.size()/2];
            } else {
                inputItem = result.data;
            }
        } while (!valid && !partA);
    }

    return sum;
}

int main() {
    const std::vector<std::string> lines = readFile("../input/input");

    bool firstParse = true;
    std::vector<std::vector<int>> input;
    std::unordered_map<int, std::vector<int>> rules;
    std::vector<std::string> result;
    for (const auto& line : lines) {
        if (line.empty()) {
            firstParse = false;
            continue;
        }
        if (firstParse) {
            result = split(line, '|');
            auto num = stoi(result[0]);
            if (rules.contains(num)) {
                rules.find(num)->second.push_back(stoi(result[1]));
            } else {
                rules.insert({num, {stoi(result[1])}});
            }
        } else {
            result = split(line, ',');
            std::vector<int> inputItem;
            for (const auto& item : result) {
                inputItem.push_back(std::stoi(item));
            }
            input.push_back(inputItem);
        }
    }

    int answer = getAnswer(input, rules, true);
    std::cout << "Part A: " << answer << std::endl;
    std::cout << "Part B: " << getAnswer(input, rules, false) - answer << std::endl;

    return 0;
}
