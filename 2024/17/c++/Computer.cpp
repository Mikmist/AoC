//
// Created by Zino Holwerda on 17/12/2024.
//

#include "Computer.h"

#include <assert.h>
#include <iostream>
#include <ostream>

Computer::Computer(std::vector<std::string>& lines) {
    sscanf(lines[0].c_str(), "Register A: %d", &A);
    sscanf(lines[1].c_str(), "Register B: %d", &B);
    sscanf(lines[2].c_str(), "Register C: %d", &C);
    for (int j = 9; j < lines[4].size(); j++) {
        char cur = lines[4][j];
        if (lines[4][j] == ',') continue;
        this->program.push_back(cur - '0');
    }
    this->instructionPointer = 0;
}

Computer::Computer(int instructionPointer, std::vector<int> program, int A, int B, int C) {
    this->instructionPointer = instructionPointer;
    this->program = program;
    this->A = A;
    this->B = B;
    this->C = C;
}

Computer::Computer(std::vector<int> program, int A, int B, int C) : Computer(0, std::move(program), A, B, C) {}

void Computer::run() {
    for (; instructionPointer < program.size(); ) {
        int opcode = program[instructionPointer];
        int comboOperand = program[instructionPointer+1];
        // std::cout << opcode << " " << comboOperand << std::endl;
        // printf("Registers (A:%d B:%d C:%d)\n", A, B, C);
        switch (opcode) {
            case 0: adv(comboOperand); break;
            case 1: bxl(comboOperand); break;
            case 2: bst(comboOperand); break;
            case 3: if (jnz(comboOperand)) continue; break;
            case 4: bxc(); break;
            case 5: out(comboOperand); break;
            case 6: bdv(comboOperand); break;
            case 7: cdv(comboOperand); break;
            default: exit(1);
        }
        instructionPointer+=2;
        // std::string input;
        // std::getline(std::cin, input);
        // for (int i = 0; i < output.size(); i++) {
            // std::cout << output[i] << ",";
        // } std::cout << std::endl;
    }
}

void Computer::adv(int comboOperand) { division(A, getComboOperandValue(comboOperand), A); }
void Computer::bdv(int comboOperand) { division(A, getComboOperandValue(comboOperand), B); }
void Computer::cdv(int comboOperand) { division(A, getComboOperandValue(comboOperand), C); }
void Computer::bxl(int comboOperand) { B ^= comboOperand; }
void Computer::bst(int comboOperand) { B = (getComboOperandValue(comboOperand) % 8); }
void Computer::bxc() {
    // printf("B = %d ^ %d = %d\n", B, C, B^C);
    B = B ^ C;
}
void Computer::out(int comboOperand) {
    // printf("out: (%d) %dmod8=%d\n", comboOperand, getComboOperandValue(comboOperand), getComboOperandValue(comboOperand)%8);
    output.push_back(getComboOperandValue(comboOperand)%8);
}

void Computer::division(const int inRegister, const int comboOperand, int &outRegister) {
    outRegister = inRegister/std::pow(2,comboOperand);
    // printf("division: %d/2^%d=%d\n", inRegister, comboOperand, outRegister);
}

int Computer::getComboOperandValue(const int comboOperand) const {
    if (comboOperand == 7) exit(1);
    if (comboOperand == 6) return C;
    if (comboOperand == 5) return B;
    if (comboOperand == 4) return A;
    return comboOperand;
}

bool Computer::jnz(int comboOperand) {
    if (A != 0) {
        instructionPointer = comboOperand % 8;
        return true;
    }
    return false;
}

std::string Computer::getFormattedOutput() const {
    std::string output;
    for (int i = 0; i < this->output.size(); i++) {
        if (i!=0) output += ",";
        output += std::to_string(this->output[i]);
    }
    return output;
}

void tests() {
    std::cout << "Running tests" << std::endl;
    std::cout << "Running test 1: ";
    Computer computer({2,6}, 0, 0, 1);
    computer.run();
    assert(computer.B == 1);
    std::cout << "passed!" << std::endl;

    std::cout << "Running test 2: ";
    computer = Computer({5,0,5,1,5,4}, 10, 0, 1);
    computer.run();
    assert(computer.output[0] == 0); ;
    assert(computer.output[1] == 1); ;
    assert(computer.output[2] == 2); ;
    std::cout << "passed!" << std::endl;

    std::cout << "Running test 3: ";
    computer = Computer({0,1,5,4,3,0}, 2024, 0, 0);
    computer.run();
    assert(computer.output[0] == 4); ;
    assert(computer.output[1] == 2); ;
    assert(computer.output[2] == 5); ;
    assert(computer.A == 0); ;
    std::cout << "passed!" << std::endl;

    std::cout << "Running test 4: ";
    computer = Computer({1,7}, 0, 29, 0);
    computer.run();
    assert(computer.B == 26); ;
    std::cout << "passed!" << std::endl;

    std::cout << "Running test 5: ";
    computer = Computer({4,0}, 0, 2024, 43690);
    computer.run();
    assert(computer.B == 44354); ;
    std::cout << "passed!" << std::endl;

    std::cout << "Finished tests" << std::endl;
}