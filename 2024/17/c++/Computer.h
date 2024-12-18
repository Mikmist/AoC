//
// Created by Zino Holwerda on 17/12/2024.
//

#ifndef COMPUTER_H
#define COMPUTER_H
#include <vector>


class Computer {
public:
    explicit Computer(std::vector<std::string>& lines);
    Computer(uint64_t instructionPointer, std::vector<uint64_t> program, uint64_t A, uint64_t B, uint64_t C);
    Computer(std::vector<uint64_t> program, uint64_t A, uint64_t B, uint64_t C);

    int instructionPointer;
    std::vector<uint64_t> program;
    std::vector<uint64_t> output;
    uint64_t A;
    uint64_t B;
    uint64_t C;

    void run();
    std::string getFormattedOutput() const;
private:
    void adv(uint64_t comboOperand);
    void bxl(uint64_t comboOperand);
    void bst(uint64_t comboOperand);
    bool jnz(uint64_t comboOperand);
    void bxc();
    void out(uint64_t comboOperand);
    void bdv(uint64_t comboOperand);
    void cdv(uint64_t comboOperand);

    uint64_t getComboOperandValue(uint64_t comboOperand) const;
    void division(uint64_t inRegister, uint64_t comboOperand, uint64_t& outRegister);
};

void tests();


#endif //COMPUTER_H
