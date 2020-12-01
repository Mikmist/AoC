use std::{
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
