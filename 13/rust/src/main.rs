mod aoc;
mod intcode;

fn main() {
    let lines = aoc::get_input_lines(String::from("input"));

    for line in lines {
        let mut computer = intcode::Computer::new(line);

        let output = computer.run(vec![]).expect("Error");
        let mut count = 0; let mut index = 2;
        // println!("{:?}", output);
        while output.len() > index {
            if output[index] == 2 {
                count += 1;
            }
            index += 3;
        }

        println!("{:?}", count);
        aoc::submit(1, count);
    }
}
