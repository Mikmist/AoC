#include <iostream>
#include <string>
#include <unordered_set>
#include <vector>
#include "map.h"
#include "utils.h"

class Robot {
public:
    Coordinate coordinate;
    Coordinate velocity;
};

int getAnswer(std::vector<Robot> robots, const int seconds, const bool print) {
    const int xMax = 101;
    const int yMax = 103;
    for (Robot &robot: robots) {
        int x = robot.coordinate.x, y = robot.coordinate.y;
        x = (x + robot.velocity.x * seconds) % xMax;
        y = (y + robot.velocity.y * seconds) % yMax;
        if (x < 0) x = x + xMax;
        if (y < 0) y = y + yMax;
        robot.coordinate.x = x;
        robot.coordinate.y = y;
    }
    std::vector<int> counts = {0, 0, 0, 0};
    if (print) {
        for (int y = 0; y < yMax; ++y) {
            for (int x = 0; x < xMax; ++x) {
                auto count = 0;
                for (const Robot &robot: robots) {
                    if (robot.coordinate.x == x && robot.coordinate.y == y) {
                        count++;
                    }
                }
                if (count) std::cout << count;
                else std::cout << '.';
            }
            std::cout << std::endl;
        }
    }
    for (const Robot &robot: robots) {
        if (robot.coordinate.x < xMax / 2 && robot.coordinate.y < yMax / 2) counts[0]++;
        if (robot.coordinate.x > xMax / 2 && robot.coordinate.y < yMax / 2) counts[1]++;
        if (robot.coordinate.x < xMax / 2 && robot.coordinate.y > yMax / 2) counts[2]++;
        if (robot.coordinate.x > xMax / 2 && robot.coordinate.y > yMax / 2) counts[3]++;
    }
    return counts[0] * counts[1] * counts[2] * counts[3];
}

int main() {
    const std::vector<std::string> lines = readFile("../input/input");

    std::vector<Robot> robots;
    for (const auto &line: lines) {
        Robot robot;
        sscanf(line.c_str(), "p=%d,%d v=%d,%d", &robot.coordinate.x, &robot.coordinate.y, &robot.velocity.x,
               &robot.velocity.y);
        robots.push_back(robot);
    }

    std::cout << "Part A: " << getAnswer(robots, 100, false) << std::endl;
    int seconds = 0;
    while (true) {
        int out = getAnswer(robots, seconds, false);
        if (out / 100000000 < 1) {
            getAnswer(robots, seconds, true);
            int input = 0;
            std::cin >> input;
            if (input == 1) {
                break;
            }
        }
        seconds++;
    }
    std::cout << "Part B: " << seconds << std::endl;
    return 0;
}
