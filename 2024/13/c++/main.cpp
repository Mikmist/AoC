#include <iostream>
#include <string>
#include <vector>
#include "utils.h"

int solution(uint64_t aX, uint64_t aY, uint64_t bX, uint64_t bY, uint64_t prizeX, uint64_t prizeY) {
    uint64_t solution = 1000000000;
    for (int i = 0; i <= 100; i++) {
        for (int j = 0; j <= 100; j++) {
            if (i * aX + j * bX == prizeX && i * aY + j * bY == prizeY) {
                if (i*3 + j < solution) solution = i*3 + j;
            }
        }
    }
    return solution == 1000000000 ? 0 : solution;
}

auto cost(int64_t a, int64_t c, int64_t b, int64_t d, int64_t e, int64_t f) -> uint64_t {
    // dn = (a • d) - (c • b)
    // x = [(e • d) - (f • b)] ÷ dn
    // y = [(a • f) - (c • e)] ÷ dn
    // https://www.1728.org/cramer.htm
    e += 10000000000000;
    f += 10000000000000;
    const int64_t dn = a * d - c * b;
    const int64_t xDet = (e * d) - (f * b);
    const int64_t yDet = (a * f) - (c * e);
    const int64_t x = xDet / dn, y = yDet / dn;
    if (xDet % dn != 0 || yDet % dn != 0 || x < 0 || y < 0) return 0;
    return 3 * x + 1 * y;
}

uint64_t getAnswer(const std::vector<std::string> &lines, bool partB) {
    int aX, aY, bX, bY, prizeX, prizeY;
    uint64_t sum = 0;
    for (int i = 0; i < lines.size(); i++) {
        sscanf(lines[i++].c_str(), "Button A: X+%d, Y+%d", &aX, &aY);
        sscanf(lines[i++].c_str(), "Button B: X+%d, Y+%d", &bX, &bY);
        sscanf(lines[i++].c_str(), "Prize: X=%d, Y=%d", &prizeX, &prizeY);
        if (partB) sum += cost(aX, aY, bX, bY, prizeX, prizeY);
        else sum += solution(aX, aY, bX, bY, prizeX, prizeY);
    }
    return sum;
}
//37128
//74914228471331
int main() {
    const std::vector<std::string> lines = readFile("../input/input");

    std::cout << "Part A: " << getAnswer(lines, false) << std::endl;
    std::cout << "Part B: " << getAnswer(lines, true) << std::endl;

    return 0;
}
