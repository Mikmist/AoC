use regex::Regex;

mod aoc;

#[derive(Clone, Debug)]
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

    pub fn pull_by_direction(&mut self, other: &Moon, i: usize) {
        if other.pos[i] > self.pos[i]
        {
            self.vel[i] += 1;
        }
        else if other.pos[i] < self.pos[i]
        {
            self.vel[i] -= 1;
        }
    }

    pub fn pull(&mut self, other: &Moon) {
        for i in 0..3 {
            self.pull_by_direction(other, i)
        }
    }

    pub fn update_position(&mut self) {
        for i in 0..3 {
            self.pos[i] = self.pos[i] + self.vel[i];
        }
    }

    pub fn get_energy(&self) -> i64 {
        let mut kin = 0;
        let mut pot = 0;

        for i in 0..3 {
            kin += self.vel[i].abs();
            pot += self.pos[i].abs();
        }

        kin as i64 * pot as i64
    }
}

#[derive(Clone, Debug)]
struct System {
    moons: Vec<Moon>,
}

impl System {

    pub fn from_lines(lines: Vec<String>) -> Self {
        let mut moons = Vec::new();

        for line in lines {
            moons.push(Moon::from_line(line).expect("Something went wrong!"));
        }
        System {
            moons: moons,
        }
    }

    pub fn step(&mut self) {
        let clone_system = self.clone();
        for i in 0..self.moons.len() {
            for j  in 0..self.moons.len() {
                self.moons[i].pull(&clone_system.moons[j]);
            }
        }
        for i in 0..self.moons.len() {
            self.moons[i].update_position();
        }
    }

    pub fn get_energy(&self) -> i64 {
        self.moons.iter().map(|moon| moon.get_energy()).sum()
    }

}

fn main() {
    let lines = aoc::get_input_lines("input".to_string());
    let mut system: System = System::from_lines(lines);
    let mut step = 0;
    let max_steps: i64 = 4686774924;

    while step < max_steps {
        system.step();
        step += 1
    }

    println!("{:?}", system.get_energy());
}
