use std::io;
use std::f32;

fn get_value(i: f32) -> f32 {
    let value: f32 = (i/3.).floor() - 2.;
    if value < 0. {
        return 0.;
    } else {
        return value + get_value(value);
    }
}

fn main() {
    let mut line;
    let mut sum = 0.0_f32;
    let mut trimmed = " ";
    
    while trimmed != "-1" {
        line = String::new();
        io::stdin().read_line(&mut line)
            .expect("Failed to read line.");    
         
        trimmed = line.trim();

        if trimmed == "-1" {
            break;
        }
        
        match trimmed.parse::<f32>() {
            Ok(i) => sum += get_value(i),
            Err(..) => println!("this was not an integer: {}", trimmed),
        };
    }

    println!("sum: {}", sum);
}
