#[derive(Clone, PartialEq)]
enum Operation {
    End,
    Mult(i64, i64, i64),
    Add(i64, i64, i64),
    Input(i64),
    Output(i64),
}

#[derive(Clone)]
struct Process {
    operation: Operation,
    step_size: usize,
}

#[derive(Clone)]
pub struct Computer {
    pub intcode: Vec<i64>,
    input: Vec<i64>,
    output: Vec<i64>,
    index: usize,
}

impl Computer {
    pub fn with_input_and_index(intcode: String, input: Vec<i64>, index: usize) -> Computer {
        Computer {
            intcode: intcode.split(",")
                .map(|s| s.parse().unwrap())
                .collect(),
            input: input,
            output: Vec::new(),
            index: index,
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
                println!("Finished");
                break;
            }

            self.execute_instruction(&process);

            self.index += process.step_size;
        }

        Ok(self.output.to_vec())
    }

    fn execute_instruction(&mut self, process: &Process) {
        match process.operation {
            Operation::Mult(a, b, pos) =>
                self.intcode[pos as usize] = a * b,
            Operation::Add(a, b, pos) =>
                self.intcode[pos as usize] = a + b,
            Operation::Input(pos) =>  {
                self.intcode[pos as usize] = self.input[0];
                self.input.remove(0);
            },
            Operation::Output(pos) => self.output.push(pos),
            Operation::End => (),
        }
    }

    fn parse_process(&mut self) -> Result<Process, &'static str> {
        let instruction = self.intcode[self.index] % 100;

        match instruction {
            1 => Ok(Process {
                operation: Operation::Add(
                    self.parse_arg_value_from_mode(1),
                    self.parse_arg_value_from_mode(2),
                    self.parse_arg_value_from_mode(3),
                ),
                step_size: 4,
            }),
            2 => Ok(Process {
                operation: Operation::Mult(
                    self.parse_arg_value_from_mode(1),
                    self.parse_arg_value_from_mode(2),
                    self.parse_arg_value_from_mode(3),
                ),
                step_size: 4,
            }),
            3 => Ok(Process {
                operation: Operation::Input(
                    self.parse_arg_value_from_mode(1)
                ),
                step_size: 2,
            }),
            4 => Ok(Process {
                operation: Operation::Output(
                    self.parse_arg_value_from_mode(1)
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

    fn parse_arg_value_from_mode(&mut self, arg_number: usize) -> i64 {
        let mut instruction = self.intcode[self.index] / 100;
        let mut mode = 0;

        for _i in 0..arg_number {
            mode = instruction % 10;
            instruction /= 10;
        }

        if mode == 1 {
            return self.intcode[self.index+arg_number];
        } else {
            return self.intcode[self.intcode[self.index+arg_number] as usize];
        }
    }
}

#[test]
fn test_from_intcode() {
    let computer = Computer::with_input(String::from("1,0,0,0,99"), Vec::new());
    assert_eq!(computer.intcode, vec![1,0,0,0,99]);
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
    assert_eq!(computer.intcode, vec![2,0,0,0,99]);
}

#[test]
fn test_instruction_mult() {
    let mut computer = Computer::with_input(String::from("2,3,0,3,99"), Vec::new());
    computer.run();
    assert_eq!(computer.intcode, vec![2,3,0,6,99]);
}

#[test]
fn test_instruction_case_1() {
    let mut computer = Computer::with_input(String::from("1,1,1,4,99,5,6,0,99"), Vec::new());
    computer.run();
    assert_eq!(computer.intcode, vec![30,1,1,4,2,5,6,0,99]);
}

#[test]
fn test_parse_modes() {
    let mut computer = Computer::with_input(String::from("01001,1,1,4,99,5,6,0,99"), Vec::new());
    assert_eq!(computer.parse_arg_value_from_mode(1), 1);
    assert_eq!(computer.parse_arg_value_from_mode(2), 1);
    assert_eq!(computer.parse_arg_value_from_mode(3), 1);
    computer = Computer::with_input(String::from("2301,1,1,4,99,5,6,0,99"), Vec::new());
    assert_eq!(computer.parse_arg_value_from_mode(3), 0);
}
