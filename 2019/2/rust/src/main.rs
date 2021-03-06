mod intcode;
mod aoc;

fn main() {
    let lines = aoc::get_input_lines(String::from("input"));

    for line in lines {
        let mut computer = intcode::Computer::with_input(line, Vec::new());
        computer.intcode[1] = 12;
        computer.intcode[2] = 2;
        computer.run().expect("Some error occured.");
        println!("Answer: {:?}", computer.intcode[0]);
    }

    aoc::submit(1, 15);
}
