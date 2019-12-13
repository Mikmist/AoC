use regex::Regex;


mod aoc;

struct Moon {
    pos: Vec<i32>,
    vel: Vec<i32>,
}

impl Moon {
    pub fn new() -> Self {
        Moon {
            pos: Vec::new(),
            vel: Vec::new(),
        }
    }

    fn from_line(line: String) -> Result<Self, String> {
        let mut moon = Self::new();
        let re = Regex::new(r"^<x=(.+), y=(.+), z=(.+)>$").unwrap();
        
        let groups = if let Some(capture) = re.captures(&line) {
            capture
        } else {
            return Err(format!("Invalid line: {}", line));
        };

        for i in 0..3 {
            let string = groups.get(i+1).unwrap().as_str();
            if let Ok(x) = string.parse() {
                moon.pos.push(x);
                moon.vel.push(0);
            } else {
                return Err(format!("Invalid number: {}", string));
            }
        }

        Ok(moon)
    }
}

fn main() {
    let lines = aoc::get_input_lines("input".to_string());
    let mut moons: Vec<Moon> = Vec::new();

    for line in lines {
        moons.push(Moon::from_line(line).expect("Something went wrong!"));
    }    
}
