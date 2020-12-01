mod aoc;
mod intcode;

fn main() {
    let lines = aoc::get_input_lines(String::from("input"));

    for line in lines {
        let mut computer = intcode::Computer::with_input(line, vec![5]);
        println!("Output: {:?}", computer.run());
    }
}
