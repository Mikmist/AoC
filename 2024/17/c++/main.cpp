#include <iostream>
#include <map>
#include <string>
#include <unordered_set>
#include <queue>
#include <vector>

#include "Computer.h"
#include "map.h"
#include "utils.h"

uint64_t result = UINT64_MAX;
void emulateProgram(uint64_t a, const std::vector<uint64_t> &program, uint64_t depth, std::vector<uint64_t> currentOut) {
    if (depth == program.size()) {
        for (int i = 0; i < program.size(); i++) {
            if (program[program.size()-i-1] != currentOut[i]) {
                return;
            }
            uint64_t res = (a >> 3);
            if (res < result) result = res;
        }
    }
    if (depth > program.size()) return;
    uint64_t backupA = a;
    for (int i = 0; i < 8; i++) {
        a = backupA + i;
        uint64_t b = a % 8;
        b ^= 5;
        uint64_t c = a / std::pow(2, b);
        b ^= 6;
        // No need for division as we are calculating up.
        // a /= 8;
        b ^= c;
        if (b%8 == program[program.size() - depth - 1]) {
            std::vector<uint64_t> newOut = currentOut;
            newOut.push_back(b%8);
            if (newOut.size() == program.size()) {
            }
            emulateProgram(a<<3, program, depth+1, newOut);
        }
    }
}

int main() {
    std::vector<std::string> lines = readFile("../input/input");
    Computer computer(lines);

    computer.run();
    std::cout << "Part A: " << computer.getFormattedOutput() << std::endl;

    emulateProgram(0, computer.program, 0, {});
    std::cout << "Part B: " << result << std::endl;

    return 0;
}
