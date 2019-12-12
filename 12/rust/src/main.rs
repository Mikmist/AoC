mod file;

fn main() {
    let lines = file::get_input_lines("input".to_string());
    for line in lines {
        println!("{:?}", line);
    }
}
