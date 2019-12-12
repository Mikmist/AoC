mod aoc;

fn main() {
    let lines = aoc::get_input_lines("input".to_string());
    for line in lines {
        println!("{:?}", line);
    }
}
