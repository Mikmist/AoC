#include <iostream>
#include <string>
#include <vector>
#include "utils.h"

void printList(std::vector<int> list, int indexIndicator = -1) {
    if (indexIndicator != -1) {
        for (int i = 0; i < list.size(); i++ ) {
            if (i == indexIndicator) std::cout << 'v';
            else std::cout << ' ';
        } std::cout << std::endl;
    }
    for (const int i : list) {
        if (i == -1) std::cout << '.';
        else std::cout << i;
    } std::cout << std::endl;
}

void solveListForB(std::vector<int> &list, int id) {
    std::vector<std::pair<int, int>> requiredBlockSizes;
    for (int i = list.size()-1; i > 0 && id > 0; i--) {
        if (list[i] == -1) continue;
        int requiredBlockSize = 1;
        while (list[i-1] == id) {
            requiredBlockSize += 1;
            i--;
        }
        requiredBlockSizes.emplace_back(requiredBlockSize, i);
        id--;
    }
    for (int i = 0; i < requiredBlockSizes.size(); i++) {
        auto [requiredBlockSize, index] = requiredBlockSizes[i];
        for (int j = 0; j < list.size(); j++) {
            if (list[j] != -1 || j >= index ) continue;
            int availableBlockSize = 0;
            int cur = j;
            while (list[cur] == -1) {
                availableBlockSize += 1;
                cur++;
            }
            if (requiredBlockSize <= availableBlockSize) {
                for (int k = 0; k < requiredBlockSize; k++) {
                    list[j+k] = requiredBlockSizes.size()-i;
                    list[index+k] = -1;
                }
                break;
            }
        }
    }
}

void solveListForA(std::vector<int> &list) {
    int reverseIndex = list.size() - 1;
    for (int i = 0; i < list.size(); i++) {
        if (reverseIndex <= i) break;
        if (list[i] == -1) {
            while (list[reverseIndex] == -1) {
                reverseIndex--;
            }
            list[i] = list[reverseIndex];
            list[reverseIndex] = -1;
            reverseIndex--;
        }
    }
}

unsigned long getAnswer(const std::vector<std::string> &lines, bool partA) {
    int cnt = 0; unsigned long sum = 0; int id = 0;
    std::vector<int> list;
    for (const char c: lines[0]) {
        const int num = c - '0';
        if (cnt++ % 2 == 0) {
            for (int i = 0; i < num; i++) {
                list.push_back(id);
            }
            id++;
        } else {
            for (int i = 0; i < num; i++) {
                list.push_back(-1);
            }
        }
    }

    if (partA) solveListForA(list);
    else solveListForB(list, id-1);

    for (int i = 0; i < list.size(); i++) {
        if (list[i] != -1) sum += (list[i] * i);
    }
    return sum;
}

int main() {
    const std::vector<std::string> lines = readFile("../input/input");

    std::cout << "Part A: " << getAnswer(lines, true) << std::endl;
    std::cout << "Part B: " << getAnswer(lines, false) << std::endl;

    return 0;
}
