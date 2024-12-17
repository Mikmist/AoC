//
// Created by Zino Holwerda on 17/12/2024.
//

#ifndef COMPUTER_H
#define COMPUTER_H
#include <vector>


class Computer {
public:
    explicit Computer(std::vector<std::string>& lines);
    Computer(int instructionPointer, std::vector<int> program, int A, int B, int C);
    Computer(std::vector<int> program, int A, int B, int C);

    int instructionPointer;
    std::vector<int> program;
    std::vector<int> output;
    int A;
    int B;
    int C;

    void run();
    std::string getFormattedOutput() const;
private:
    void adv(int comboOperand);
    void bxl(int comboOperand);
    void bst(int comboOperand);
    bool jnz(int comboOperand);
    void bxc();
    void out(int comboOperand);
    void bdv(int comboOperand);
    void cdv(int comboOperand);

    int getComboOperandValue(int comboOperand) const;
    void division(int inRegister, int comboOperand, int& outRegister);
};

void tests();


#endif //COMPUTER_H
