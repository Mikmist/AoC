#include <iostream>
#include <map>
#include <string>
#include <unordered_set>
#include <queue>
#include <vector>

#include "Computer.h"
#include "map.h"
#include "utils.h"

int main() {
    std::vector<std::string> lines = readFile("../input/test2");
    Computer computer(lines);
    // tests();

    computer.run();
    std::cout << "Part A: " << computer.getFormattedOutput() << std::endl;
    int num = 117440;
    while (num > 0) {
        num /= 8;
        std::cout << "part: " << num % 8 << std::endl;
    }

    uint64_t part = 0;
    for (int j = 9; j < lines[4].size(); j++) {
        char cur = lines[4][j];
        if (lines[4][j] == ',') continue;

        int val = cur-'0';

        for (int i = 0; i < 8; i++) {
            for (int k = 0; k < 8; k++) {
                printf("testing: %d\n", i);
                Computer newComputer({val}, val, 0, 0);
                newComputer.run();
            }
        }
    }

    return 0;
}
