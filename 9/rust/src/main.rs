mod aoc;
mod intcode;

fn main() {
    let lines = aoc::get_input_lines(String::from("test"));

    for line in lines {
        let mut computer = intcode::Computer::with_input(line, vec![1]);
        println!("{:?}", computer.run());
    }
}
