mod aoc;
mod intcode;
use std::collections::HashMap;

fn get_position(current_position: (i32, i32), direction: i32) -> (i32, i32) {
    match direction {
        0 => return (current_position.0, current_position.1 + 1),
        1 => return (current_position.0 + 1, current_position.1),
        2 => return (current_position.0, current_position.1 - 1),
        3 => return (current_position.0 - 1, current_position.1),
        _ => return (0,0)
    }
}

fn main() {
    let lines = aoc::get_input_lines(String::from("input"));

    for line in lines {
        let mut computer = intcode::Computer::new(line);
        let mut map: HashMap<(i32, i32), i64> = HashMap::new();
        let mut output;
        let mut position = (0,0);
        let mut current_colour;
        let mut counter = 0;
        // 0: Up, 1: Right, 2: Down, 3: Left
        let mut direction = 0;

        let mut max_x = 0; let mut min_x = 0; let mut max_y = 0; let mut min_y = 0;

        match map.insert(position, 1) { _ => () }

        loop {
            match map.get(&position) {
                Some(value) => current_colour = *value as i64,
                None => current_colour = 0 as i64,
            }

            output = computer.run(vec![current_colour]).expect("Got an error from the computer.");

            if computer.status == intcode::Status::Finished {
                break;
            }

            if output[1] == 1 {
                direction += 1;
                if direction > 3 {
                    direction = 0;
                }
            } else {
                direction -= 1;
                if direction < 0 {
                    direction = 3;
                }
            }

            match map.insert(position, output[0]) {
                Some(_) => (),
                None => counter += 1,
            }

            position = get_position(position, direction);

            if position.0 < min_x {
                min_x = position.0;
            }
            if position.0 > max_x {
                max_x = position.0;
            }
            if position.1 < min_y {
                min_y = position.1;
            }
            if position.1 > max_y {
                max_y = position.1;
            }
        }

        println!("{:?} {:?} {:?} {:?}", min_y, max_y, min_x, max_x);

        for y in (min_y..max_y+1).rev() {
            for x in min_x..max_x+1 {
                match map.get(&(x,y)) {
                    Some(0) | None => print!("."),
                    Some(1) => print!("#"),
                    _ => (),
                }
            }
            print!("\n");
        }
    }
}
