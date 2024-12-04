#include <iostream>
#include <string>
#include <fstream>
#include <sstream>
#include <vector>
#include <stdexcept>
#include <regex>
#include <numeric>

std::vector<std::string> readFile(const std::string& fileName) {
    std::vector<std::string> lines;
    std::ifstream file(fileName);

    if (!file.is_open()) {
        std::cerr << "Error opening file " << fileName << std::endl;
        throw std::runtime_error("Error opening file");
    }

    std::string line;

    while (std::getline(file, line, '\n')) {
        lines.push_back(line);
    }

    file.close();
    return lines;
}

int getAnswer(const std::vector<std::string>& lines, bool partA) {
    int sum = 0;
    bool enabled = true;

    for (const auto& line : lines) {
        std::regex word_regex(R"(mul\(\d+,\d+\)|don't\(\)|do\(\))");
        auto words_begin =
            std::sregex_iterator(line.begin(), line.end(), word_regex);
        auto words_end = std::sregex_iterator();

        for (std::sregex_iterator i = words_begin; i != words_end; ++i)
        {
            const std::smatch& match = *i;
            std::string match_str = match.str();
            if (match_str == "don't()" || match_str == "do()") {
                enabled = (match_str == "do()");
                continue;
            }

            std::stringstream stream(match_str.substr(4,  match_str.length()-5));
            std::string part;
            std::vector<int> parts;
            while (std::getline(stream, part, ',')) {
                parts.push_back(std::stoi(part));
            }
            if (enabled || partA) {
                sum += std::reduce(parts.begin(), parts.end(), 1, std::multiplies());
            }
        }
    }
    return sum;
}

int main() {
    const std::vector<std::string> lines = readFile("../input/input");

    std::cout << "Part A: " << getAnswer(lines, true) << std::endl;
    std::cout << "Part B: " << getAnswer(lines, false) << std::endl;

    return 0;
}
