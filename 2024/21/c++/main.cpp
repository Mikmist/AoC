#include <iostream>
#include <string>
#include <unordered_set>
#include <queue>
#include <valarray>
#include <vector>
#include <__ranges/split_view.h>

#include "map.h"
#include "utils.h"

struct Triple {
    Coordinate first;
    int pathLength;
    int heuristic;
    std::optional<Coordinate> startOfCheat;
    std::optional<Coordinate> endOfCheat;
    int timeSinceCheat;
    std::vector<Coordinate> path;
    std::vector<char> pathDirections;
};

int getHeuristic(Coordinate current, Coordinate goal) {
    return std::abs(current.x - goal.x)+std::abs(current.y - goal.y);
}

std::vector<Triple> getAnswer(const Map& map, Coordinate start, Coordinate end, int max) {
    auto cmp = [](const Triple& l, const Triple& r) {
        return l.pathLength + l.heuristic > r.pathLength + r.heuristic;
    };
    std::priority_queue<Triple, std::vector<Triple>, decltype(cmp)> q(cmp);
    std::unordered_map<Coordinate, int> visited;
    std::unordered_set<std::string> solutions;
    q.emplace(start, 0, 0, std::nullopt, std::nullopt, -1, std::vector<Coordinate>());
    std::vector<Triple> answers;

    while (!q.empty()) {
        auto cur = q.top();
        auto [current, pathLength, heuristic, startOfCheat, endOfCheat, timeSinceCheat, path, pathDirections] = cur; q.pop();
        // printf("Popping item: (%d,%d) with length %d.\n", current.x, current.y, pathLength);
        path.push_back(current);
        cur.path.push_back(current);
        visited[current] = pathLength;
        if (map.get(current) == '#') continue;
        if (current == end) {
            answers.push_back(cur);
            if (cur.pathLength > max || max == 1) {
                return answers;
            }
        }
        for (int j = 0; j < 4; j++) {
            const auto [transX, transY] = dirTransforms[j%4];
            const char dirChar = dirChars[j%4];
            if (const char neighbour = map.get(current.x + transX, current.y + transY); neighbour != '-'  || neighbour != '#') {
                const Coordinate next = {current.x + transX, current.y + transY};
                if (visited.contains(next) && visited[next] <= pathLength+1) continue;

                if (timeSinceCheat == 0) endOfCheat = next;
                auto pathDirectionsCopy = pathDirections;
                pathDirectionsCopy.push_back(dirChar);
                q.emplace(next, pathLength+1, getHeuristic(next, end), startOfCheat, endOfCheat, timeSinceCheat-1, path, pathDirectionsCopy);
            }
        }
    }
    return answers;
}

std::optional<Triple> getAnswer(const Map& map, Coordinate start, Coordinate end) {
    auto cmp = [](const Triple& l, const Triple& r) {
        return l.pathLength + l.heuristic > r.pathLength + r.heuristic;
    };
    std::priority_queue<Triple, std::vector<Triple>, decltype(cmp)> q(cmp);
    std::unordered_map<Coordinate, int> visited;
    std::unordered_set<std::string> solutions;
    q.emplace(start, 0, 0, std::nullopt, std::nullopt, -1, std::vector<Coordinate>());

    while (!q.empty()) {
        auto cur = q.top();
        auto [current, pathLength, heuristic, startOfCheat, endOfCheat, timeSinceCheat, path, pathDirections] = cur; q.pop();
        // printf("Popping item: (%d,%d) with length %d.\n", current.x, current.y, pathLength);
        path.push_back(current);
        cur.path.push_back(current);
        visited[current] = pathLength;
        if (map.get(current) == '#') continue;
        if (current == end) {
            return cur;
        }
        for (int j = 0; j < 4; j++) {
            const auto [transX, transY] = dirTransforms[j%4];
            const char dirChar = dirChars[j%4];
            if (const char neighbour = map.get(current.x + transX, current.y + transY); neighbour != '-'  || neighbour != '#') {
                const Coordinate next = {current.x + transX, current.y + transY};
                if (visited.contains(next) && visited[next] <= pathLength+1) continue;

                if (timeSinceCheat == 0) endOfCheat = next;
                auto pathDirectionsCopy = pathDirections;
                pathDirectionsCopy.push_back(dirChar);
                q.emplace(next, pathLength+1, getHeuristic(next, end), startOfCheat, endOfCheat, timeSinceCheat-1, path, pathDirectionsCopy);
            }
        }
    }
    return std::nullopt;
}

void pause() {
    std::cin.get();
}

std::vector<std::string> exploreMap(const Map& map, std::string line, std::unordered_map<char, Coordinate>& locationMap) {
    std::vector<std::string> possibleOutputs;
    auto start = locationMap['A'];
    for (const auto& nextCoord : line) {
        std::vector<std::string> possibility;
        auto end = locationMap[nextCoord];
        Triple baseline = getAnswer(map, start, end).value();
        std::vector<Triple> answers = getAnswer(map, start, end, baseline.pathLength);
        // std::cout << "pathLength: " << baseline.pathLength << std::endl;
        // std::cout << answers.size() << std::endl;
        for (const Triple& answer : answers) {
            std::string output;
            for (auto pathItem : answer.pathDirections) {
                output += pathItem;
            };
            output += 'A';
            possibility.push_back(output);
        }
        if (possibleOutputs.empty()) possibleOutputs = possibility;
        else {
            std::vector<std::string> newPossibleOutputs;
            for (const auto& p : possibleOutputs) {
                for (const auto& q : possibility) {
                    newPossibleOutputs.push_back(p+q);
                }
            }
            possibleOutputs = newPossibleOutputs;
        }
        start = end;
    }
    return possibleOutputs;
}

int main() {
    std::vector<std::string> lines = readFile("../input/test");
    const std::vector<std::string> keyPadLines = readFile("../input/keypad");
    const std::vector<std::string> commandPadLines = readFile("../input/commandpad");
    Map keyPad(keyPadLines);
    keyPad.print();
    Map commandPad(commandPadLines);
    commandPad.print();
    std::unordered_map<char, Coordinate> locationsNumbers;
    locationsNumbers['0'] = {2, 4};
    locationsNumbers['A'] = {3, 4};
    locationsNumbers['1'] = {1, 3};
    locationsNumbers['2'] = {2, 3};
    locationsNumbers['3'] = {3, 3};
    locationsNumbers['4'] = {1, 2};
    locationsNumbers['5'] = {2, 2};
    locationsNumbers['6'] = {3, 2};
    locationsNumbers['7'] = {1, 1};
    locationsNumbers['8'] = {2, 1};
    locationsNumbers['9'] = {3, 1};
    std::unordered_map<char, Coordinate> keypadLocations;
    keypadLocations['^'] = {2, 1};
    keypadLocations['A'] = {3, 1};
    keypadLocations['<'] = {1, 2};
    keypadLocations['v'] = {2, 2};
    keypadLocations['>'] = {3, 2};

    int sum = 0;
    for (const auto& line : lines) {
        int thirdRobotMin = INT_MAX;
        std::cout << line << std::endl;
        std::vector<std::string> firstRobots = exploreMap(keyPad, line, locationsNumbers);
        for (const auto& firstRobot : firstRobots) {
            std::cout << firstRobot << std::endl;
            std::vector<std::string> secondRobots = exploreMap(commandPad, firstRobot, keypadLocations);
            for (const auto& secondRobot : secondRobots) {
                std::cout << secondRobot << std::endl;
                std::vector<std::string> thirdRobots = exploreMap(commandPad, secondRobot, keypadLocations);
                for (const auto& thirdRobot : thirdRobots) {
                    if (thirdRobot.size() < thirdRobotMin) thirdRobotMin = thirdRobot.size();
                    // std::cout << thirdRobot << std::endl;
                }
            }
        }
        // continue;
        // std::string thirdRobot = exploreMap(commandPad, secondRobot, keypadLocations);

        // std::cout << thirdRobot << "\n";
        // std::cout << secondRobot << "\n";
        // std::cout << firstRobot << "\n";
        // std::cout << line << "\n";
        std::cout << std::stoi(line.substr(0, 3)) << " " << thirdRobotMin << std::endl;
        sum += (std::stoi(line.substr(0, 3)) * thirdRobotMin);
    }

    std::cout << "Part A: " << sum << '\n';
    return 0;
}
