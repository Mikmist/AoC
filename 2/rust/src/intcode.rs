#[derive(Clone)]
enum Operation {
    Mult(i32, i32, i32),
    Add(i32, i32, i32),
}


#[derive(Clone)]
struct Process {
    operation: Operation,
    step_size: i32,
}

#[derive(Clone)]
pub struct Computer {
    intcode: Vec<i32>,
    input: Vec<i32>,
    output: Vec<i32>,
    index: i32,
}

impl Computer {
    pub fn with_input_and_index(intcode: String, input: Vec<i32>, index: i32) -> Computer {
        Computer {
            intcode: intcode.split(",")
                .map(|s| s.parse().unwrap())
                .collect(),
            input: input,
            output: Vec::new(),
            index: 0,
        }
    }

    pub fn with_input(intcode: String, input: Vec<i32>) -> Computer {
        Computer::with_input_and_index(intcode, input, 0)
    }

    pub fn run(&mut self) -> Result<Vec<i32>, &'static str> {
        loop {
            let process = self.parse_instruction(1)?;
            
            break;
        }

        Ok(self.output.to_vec())
    }

    fn parse_instruction(&mut self, instruction: i32) -> Result<Process, &'static str> {
        match instruction {
            1 => Ok(Process {
                operation: Operation::Add(1,1,1),
                step_size: 4,
            }),
            2 => Ok(Process {
                operation: Operation::Mult(1,1,1),
                step_size: 4,
            }),
            _ => Err("Not a know instruction"),
        }
    }
}

#[test]
fn test_from_intcode() {
    let computer = Computer::from_intcode(String::from("1,0,0,0,99"), Vec::new());
    assert_eq!(computer.intcode, vec![1,0,0,0,99]);
}

#[test]
fn test_run() {
    let computer = Computer::from_intcode(String::from("1,0,0,0,99"), Vec::new());
    computer.run();
}

#[test]
fn test_instruction_1() {
    let computer = Computer::from_intcode(String::from("1,0,0,0,99"), Vec::new());
    computer.run();
}
