#include <iostream>
#include <map>
#include <string>
#include <unordered_set>
#include <queue>
#include <vector>

#include "Computer.h"
#include "map.h"
#include "utils.h"

void printProgram(std::vector<uint64_t> program) {
    for (uint64_t i = 0; i < program.size(); i++) {
        std::cout << program[i] << " ";
    }
    std::cout << std::endl;
}
uint64_t result = UINT64_MAX;
void emulateProgram(uint64_t a, const std::vector<uint64_t> &program, uint64_t depth, std::vector<uint64_t> currentOut) {
    if (depth == program.size()) {
        for (int i = 0; i < program.size(); i++) {
            if (program[program.size()-i-1] != currentOut[i]) {
                return;
            }
            uint64_t res = (a >> 3);
            if (res < result) result = res;
            // std::cout << "a: " << a << std::endl;
        }
    }
    if (depth > program.size()) return;
    // printf("reach %d a: %d\n", depth, a);
    uint64_t backupA = a;
    for (int i = 0; i < 8; i++) {
        a = backupA + i;
        uint64_t b = a % 8;
        b ^= 5;
        uint64_t c = a / std::pow(2, b);
        b ^= 6;
        // a /= 8;
        b ^= c;
        // printf("i: %d, a: %d, b(out): %d, program: %d\n", i, a, b%8, program[program.size() - depth]);
        if (b%8 == program[program.size() - depth - 1]) {
            std::vector<uint64_t> newOut = currentOut;
            newOut.push_back(b%8);
            if (newOut.size() == program.size()) {
                // std::cout << "A:" << a <<std::endl;
                // printProgram(newOut);
            }
            emulateProgram(a<<3, program, depth+1, newOut);
        }
    }
}

int emulateProgram(int a, int b, int c) {
    b  = a%8;
    b ^= 5;
    c  = a / std::pow(2,b);
    b ^= 6;
    a /= 8;
    b ^= c;
    printf("i: %d, a: %d, b(out): %d, c: %d\n",  a, b%8, c);
    return b;
}

int main() {
    std::vector<std::string> lines = readFile("../input/input");
    Computer computer(lines);
    // tests();

    computer.run();
    std::cout << "Part A: " << computer.getFormattedOutput() << std::endl;

    for (int i : computer.program) {
        std::cout << i << " ";
    } std::cout << std::endl;

    // Part B
    // while (true) {

    // }
    int a=-1, b, c;
    for (int i = 0; i < 8; i++) {
        std::vector<int> options;
        emulateProgram(0, computer.program, 0, {});
    }
    std::cout << "Part B: " << result << std::endl;

    return 0;
}
