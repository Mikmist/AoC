
#[derive(Clone, PartialEq)]
enum Operation {
    End,
    Mult(i32, i32, i32),
    Add(i32, i32, i32),
}

#[derive(Clone)]
struct Process {
    operation: Operation,
    step_size: usize,
}

#[derive(Clone)]
pub struct Computer {
    pub intcode: Vec<i32>,
    input: Vec<i32>,
    output: Vec<i32>,
    index: usize,
}

impl Computer {
    pub fn with_input_and_index(intcode: String, input: Vec<i32>, index: usize) -> Computer {
        Computer {
            intcode: intcode.split(",")
                .map(|s| s.parse().unwrap())
                .collect(),
            input: input,
            output: Vec::new(),
            index: index,
        }
    }

    pub fn with_input(intcode: String, input: Vec<i32>) -> Computer {
        Computer::with_input_and_index(intcode, input, 0)
    }

    pub fn run(&mut self) -> Result<Vec<i32>, &'static str> {
        loop {
            let process = self.parse_instruction()?;
            println!("index: {:?}", self.index);

            if process.operation == Operation::End {
                println!("Finished");
                break;
            }
            self.index += process.step_size;
            println!("index: {:?}", self.index);
        }

        Ok(self.output.to_vec())
    }

    fn parse_instruction(&mut self) -> Result<Process, &'static str> {
        match self.intcode[self.index] {
            1 => Ok(Process {
                operation: Operation::Add(
                    self.intcode[self.index+1],
                    self.intcode[self.index+2],
                    self.intcode[self.index+3]
                ),
                step_size: 4,
            }),
            2 => Ok(Process {
                operation: Operation::Mult(
                    self.intcode[self.index+1],
                    self.intcode[self.index+2],
                    self.intcode[self.index+3]
                ),
                step_size: 4,
            }),
            99 => Ok(Process {
                operation: Operation::End,
                step_size: 0,
            }),
            _ => Err("Not a know instruction"),
        }
    }

    pub fn get_intcode_value(&mut self, index: usize) {
        self.intcode[index];
    }
}

#[test]
fn test_from_intcode() {
    let mut computer = Computer::with_input(String::from("1,0,0,0,99"), Vec::new());
    assert_eq!(computer.intcode, vec![1,0,0,0,99]);
}

#[test]
fn test_run() {
    let mut computer = Computer::with_input(String::from("1,0,0,0,99"), Vec::new());
    computer.run();
}

#[test]
fn test_instruction_1() {
    let mut computer = Computer::with_input(String::from("1,0,0,0,99"), Vec::new());
    computer.run();
}
