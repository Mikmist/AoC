#include <iostream>
#include <string>
#include <unordered_set>
#include <vector>
#include "map.h"
#include "utils.h"

auto getDirTransforms() {
    std::unordered_map<char, std::pair<int, int>> dirTransforms;
    dirTransforms['^'] = {0, -1};
    dirTransforms['v'] = {0,  1};
    dirTransforms['<'] = {-1, 0};
    dirTransforms['>'] = {1,  0};
    return dirTransforms;
}

void moveAll(Map& map, Coordinate& robot, int x, int y, std::pair<int, int> direction) {
    do {
        map.set(x, y, map.get(x - direction.first, y - direction.second));
        x -= direction.first;
        y -= direction.second;
        map.set(x, y,'.');
    } while (x != robot.x || y != robot.y);
    robot.x += direction.first;
    robot.y += direction.second;
}

void getAnswer(Map& map, const std::vector<std::string> &instructions) {
    auto dirTransforms = getDirTransforms();
    auto robot = map.find('@').value();
    for (auto instruction : instructions) {
        for (auto character : instruction) {
            auto transform = dirTransforms[character];
            char res = ' '; int x = robot.x, y = robot.y;
            do {
                x += transform.first;
                y += transform.second;
                res = map.get(x, y);
                if (res == '#') break;
                if (res == '.') moveAll(map, robot, x, y, transform);
            } while (res == 'O');
        }
    }
}

bool canBoxMove(Map& map, const int x, const int y, std::pair<int, int>& direction, char& directionChar) {
    const char cur = map.get(x, y);
    if (cur == '.') return true;
    if (cur == '#') return false;
    if (directionChar == '>' || directionChar == '<') {
        return canBoxMove(map, x + direction.first, y + direction.second, direction, directionChar);
    }
    bool valid = canBoxMove(map, x + direction.first, y + direction.second, direction, directionChar);
    if (cur == '[') {
        return valid && canBoxMove(map, x + direction.first + 1, y + direction.second, direction, directionChar);
    }
    if (cur == ']') {
        return valid && canBoxMove(map, x + direction.first - 1, y + direction.second, direction, directionChar);
    }
}

void moveBox(Map& map, const int x, const int y, std::pair<int, int>& direction) {
    if (map.get(x - direction.first, y - direction.second) == '@') return;
    map.set(x, y, map.get(x - direction.first, y - direction.second));
    map.set(x - direction.first, y - direction.second, '.');
}

void moveAllBoxes(Map &map, const int x, const int y, std::pair<int, int>& direction, char& directionChar) {
    const char cur = map.get(x, y);
    if (cur == '.') {
        moveBox(map, x, y, direction);
        return;
    }
    if (directionChar == '>' || directionChar == '<') {
        moveAllBoxes(map, x + direction.first, y + direction.second, direction, directionChar);
    } else {
        moveAllBoxes(map, x + direction.first, y + direction.second, direction, directionChar);
        if (cur == '[') moveAllBoxes(map, x + direction.first + 1, y + direction.second, direction, directionChar);
        if (cur == ']') moveAllBoxes(map, x + direction.first - 1, y + direction.second, direction, directionChar);
    }
    moveBox(map, x, y, direction);
}

bool tryMoveBox(Map& map, int x, int y, std::pair<int, int> direction, char directionChar) {
    if (map.get(x, y) == '#' || map.get(x, y) == '.') return false;
    if (canBoxMove(map, x, y, direction, directionChar)) {
       moveAllBoxes(map, x, y, direction, directionChar);
        return true;
    }
    return false;
}

void getAnswerB(Map& map, const std::vector<std::string> &instructions) {
    auto dirTransforms = getDirTransforms();
    auto robot = map.find('@').value();

    // std::cout << robot.x << " " << robot.y << std::endl;
    for (const auto& instruction : instructions) {
        for (auto character : instruction) {
            auto transform = dirTransforms[character];
            char res = ' '; int x = robot.x, y = robot.y;
            x += transform.first;
            y += transform.second;
            res = map.get(x, y);
            if (res == '#') continue;
            const bool movedBox = tryMoveBox(map, x, y, transform, character);
            if (res == '.' || movedBox) {
                map.set(x, y, '@');
                map.set(robot.x, robot.y, '.');
                robot.x = x; robot.y = y;
            }
        }
    }
}

int main() {
    std::vector<std::string> lines = readFile("../input/input");
    std::vector<std::string> mapLines;
    std::vector<std::string> instructions;
    bool passed = false;
    for (std::string &line: lines) {
        if (line.empty()) passed = true;
        else if (!passed) mapLines.push_back(line);
        else instructions.push_back(line);
    }

    Map map(mapLines);

    getAnswer(map, instructions);
    int sum = 0;
    for (auto coordinate : map.findAll('O')) {
        sum += (coordinate.x + 100 * coordinate.y);
    }
    std::cout << "Part A: " << sum << std::endl;

    // PART B
    std::vector<std::string> mapLinesB;
    for (auto& line: mapLines) {
        std::string lineB;
        for (auto& character: line) {
            if (character == '#') lineB += "##";;
            if (character == 'O') lineB += "[]";;
            if (character == '@') lineB += "@.";;
            if (character == '.') lineB += "..";;
        }
        mapLinesB.push_back(lineB);
    }
    Map mapB(mapLinesB);
    getAnswerB(mapB, instructions);
    sum = 0;
    for (auto coordinate : mapB.findAll('[')) {
        sum += (coordinate.x + 100 * coordinate.y);
    }
    std::cout << "Part B: " << sum << std::endl;

    return 0;
}
