use std::{
    process::Command,
    process::Output,
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

pub fn submit() -> Output {
    if cfg!(target_os = "windows") {
        Command::new("cmd")
                .args(&["/C", "echo hello"])
                .output()
                .expect("failed to execute process")
    } else {
        Command::new("sh")
                .arg("-c")
                .arg("echo hello")
                .output()
                .expect("failed to execute process")
    }
}
