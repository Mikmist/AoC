use std::{
    process::Command,
    fs::File,
    io::{prelude::*, BufReader},
};

pub fn get_input_lines(name: String) -> Vec<String> {
    let path = "../input/";
    let file = File::open(format!("{}{}", path, name)).expect("No such file");
    let buf = BufReader::new(file);
    buf.lines()
        .map(|l| l.expect("Could not parse line"))
        .collect()
}

pub fn submit(part: i32, answer: i64) {
    let submit = Command::new("bash")
            .arg("-c")
            .arg(format!("./submit {} {}", part, answer))
            .output()
            .expect("failed to execute process")
            .stdout;

    match submit[0] as char {
        '0' => println!("Success."),
        '1' => println!("The submit was too low."),
        '2' => println!("The submit was too high."),
        '3' => println!("Too fast retried, careful don't do it too often."),
        _ => println!("Some error."),
    }
}
