use std::collections::HashMap;

#[derive(Clone, PartialEq)]
enum Operation {
    End,
    Mult(i64, i64, usize),
    Add(i64, i64, usize),
    Input(usize),
    Output(i64),
    Jit(i64, usize),
    Jif(i64, usize),
    LessThan(i64, i64, usize),
    Equals(i64, i64, usize),
    AdjustRelative(i64)
}

#[derive(Clone)]
struct Process {
    operation: Operation,
    step_size: usize,
}

#[derive(Clone)]
pub struct Computer {
    pub intcode: HashMap<usize,i64>,
    input: Vec<i64>,
    output: Vec<i64>,
    index: usize,
    relative_base: usize,
}

impl Computer {
    pub fn with_input_and_index(intcode_string: String, input: Vec<i64>, index: usize) -> Computer {
        let intcode_vec: Vec<i64> = intcode_string.split(",").map(|s| s.parse().unwrap()).collect();
        let mut intcode: HashMap<usize,i64> = HashMap::new();

        for i in 0..intcode_vec.len() {
            intcode.insert(i, intcode_vec[i]);
        }

        Computer {
            intcode: intcode,
            input: input,
            output: Vec::new(),
            index: index,
            relative_base: 0,
        }
    }

    pub fn with_input(intcode: String, input: Vec<i64>) -> Computer {
        Computer::with_input_and_index(intcode, input, 0)
    }

    pub fn run(&mut self) -> Result<Vec<i64>, &'static str> {
        self.output = Vec::new();

        loop {
            let process = self.parse_process()?;

            if process.operation == Operation::End {
                break;
            }

            match self.execute_instruction(&process) {
                None => self.index += process.step_size,
                Some(step_size) => self.index += step_size,
            }
        }

        Ok(self.output.to_vec())
    }

    fn execute_instruction(&mut self, process: &Process) -> Option<usize> {
        let mut step_size: Option<usize> = None;

        match process.operation {
            Operation::Mult(a, b, pos) => self .intcode.insert(pos, a * b),
            Operation::Add(a, b, pos) => self.intcode.insert(pos, a + b),
            Operation::Input(pos) =>  {
                self.intcode.insert(pos, self.input[0]);
                self.input.remove(0);
            },
            Operation::Output(pos) => self.output.push(pos as i64),
            Operation::Jit(a, b) => {
                if a != 0 {
                    self.index = b as usize;
                    step_size = Some(0);
                }
            },
            Operation::Jif(a, b) => {
                if a == 0 {
                    self.index = b as usize;
                    step_size = Some(0);
                }
            },
            Operation::LessThan(a, b, pos) => {
                if a < b {
                    self.intcode[&pos] = 1;
                } else {
                    self.intcode[&pos] = 0;
                }
            },
            Operation::Equals(a, b, pos) => {
                if a == b {
                    self.intcode[&pos] = 1;
                } else {
                    self.intcode[&pos] = 0;
                }
            },
            Operation::AdjustRelative(a) => self.relative_base = (self.relative_base as i64 + a) as usize,
            Operation::End => (),
        }

        step_size
    }

    fn parse_process(&mut self) -> Result<Process, &'static str> {
        let instruction = self.intcode[&self.index] % 100;

        match instruction {
            1 => Ok(Process {
                operation: Operation::Add(
                    self.parse_arg_value_from_mode(1),
                    self.parse_arg_value_from_mode(2),
                    self.parse_pos_from_mode(3),
                ),
                step_size: 4,
            }),
            2 => Ok(Process {
                operation: Operation::Mult(
                    self.parse_arg_value_from_mode(1),
                    self.parse_arg_value_from_mode(2),
                    self.parse_pos_from_mode(3),
                ),
                step_size: 4,
            }),
            3 => Ok(Process {
                operation: Operation::Input(
                    self.parse_pos_from_mode(1)
                ),
                step_size: 2,
            }),
            4 => Ok(Process {
                operation: Operation::Output(
                    self.parse_arg_value_from_mode(1)
                ),
                step_size: 2,
            }),
            5 => Ok(Process {
                operation: Operation::Jit(
                    self.parse_arg_value_from_mode(1),
                    self.parse_pos_from_mode(2)
                ),
                step_size: 3,
            }),
            6 => Ok(Process {
                operation: Operation::Jif(
                    self.parse_arg_value_from_mode(1),
                    self.parse_pos_from_mode(2)
                ),
                step_size: 3,
            }),
            7 => Ok(Process {
                operation: Operation::LessThan(
                    self.parse_arg_value_from_mode(1),
                    self.parse_arg_value_from_mode(2),
                    self.parse_pos_from_mode(3)
                ),
                step_size: 4,
            }),
            8 => Ok(Process {
                operation: Operation::Equals(
                    self.parse_arg_value_from_mode(1),
                    self.parse_arg_value_from_mode(2),
                    self.parse_pos_from_mode(3)
                ),
                step_size: 4,
            }),
            9 => Ok(Process {
                operation: Operation::AdjustRelative(
                    self.parse_arg_value_from_mode(1),
                ),
                step_size: 2,
            }),
            99 => Ok(Process {
                operation: Operation::End,
                step_size: 0,
            }),
            _ => Err("Not a known instruction"),
        }
    }

    fn parse_arg_value_from_mode(&self, arg_number: usize) -> i64 {
        let mut modes = self.intcode[&self.index] / 100;
        let mut mode = 0;

        for _i in 0..arg_number {
            mode = modes % 10;
            modes /= 10;
        }

        if mode == 1 {
            return self.intcode[&(self.index+arg_number)];
        } else if mode == 2 {
            return self.intcode[&(self.intcode[&(self.relative_base + self.index + arg_number)] as usize)];
        } else {
            return self.intcode[&(self.intcode[&(self.index+arg_number)] as usize)];
        }
    }

    fn parse_pos_from_mode(&self, arg_number: usize) -> usize {
        let mut modes = self.intcode[&self.index] / 100;
        let mut mode = 0;

        for _i in 0..arg_number {
            mode = modes % 10;
            modes /= 10;
        }

        if mode == 1 {
            return self.index+arg_number;
        } else if mode == 2 {
            return self.intcode[&(self.relative_base + self.index + arg_number)] as usize;
        } else {
            return self.intcode[&(self.index+arg_number)] as usize;
        }
    }
}

fn checkHashToVec(hashmap: HashMap<usize,i64>, vec: Vec<i64>) -> bool {
    for i in 0..vec.len() {
        if hashmap[&i] != vec[i] {
            return false;
        }
    }
    return true;
}

#[test]
fn test_from_intcode() {
    let computer = Computer::with_input(String::from("1,0,0,0,99"), Vec::new());
    assert!(checkHashToVec(computer.intcode, vec![1,0,0,0,99]));
}

#[test]
fn test_run() {
    let mut computer = Computer::with_input(String::from("1,0,0,0,99"), Vec::new());
    computer.run();
}

#[test]
fn test_instruction_add() {
    let mut computer = Computer::with_input(String::from("1,0,0,0,99"), Vec::new());
    computer.run();
    assert!(checkHashToVec(computer.intcode, vec![2,0,0,0,99]));
}

#[test]
fn test_instruction_mult() {
    let mut computer = Computer::with_input(String::from("2,3,0,3,99"), Vec::new());
    computer.run();
    assert!(checkHashToVec(computer.intcode, vec![2,3,0,6,99]));
}

#[test]
fn test_instruction_case_1() {
    let mut computer = Computer::with_input(String::from("1,1,1,4,99,5,6,0,99"), Vec::new());
    computer.run();
    assert!(checkHashToVec(computer.intcode, vec![30,1,1,4,2,5,6,0,99]));
}

#[test]
fn test_instruction_input() {
    let input = 3;
    let mut computer = Computer::with_input(String::from("1101,2,1,4,99,0,99"), vec![input]);
    computer.run();
    assert!(checkHashToVec(computer.intcode, vec![input,2,1,4,3,0,99]));
}

#[test]
fn test_parse_modes() {
    let mut computer = Computer::with_input(String::from("01001,1,1,4,99,5,6,0,99"), Vec::new());
    assert_eq!(computer.parse_arg_value_from_mode(1), 1);
    assert_eq!(computer.parse_arg_value_from_mode(2), 1);
}

#[test]
fn test_parse_in_out() {
    let mut computer = Computer::with_input(String::from("3,9,8,9,10,9,4,9,99,-1,8"), vec![8]);
    computer.run();
    assert_eq!(computer.output[0], 1);
    computer = Computer::with_input(String::from("3,9,8,9,10,9,4,9,99,-1,8"), vec![7]);
    computer.run();
    assert_eq!(computer.output[0], 0);
}

#[test]
fn test_parse_in_out_immediate() {
    let mut computer = Computer::with_input(String::from("3,3,1107,-1,8,3,4,3,99"), vec![8]);
    computer.run();
    assert_eq!(computer.output[0], 0);
    computer = Computer::with_input(String::from("3,3,1107,-1,8,3,4,3,99"), vec![7]);
    computer.run();
    assert_eq!(computer.output[0], 1);
}
