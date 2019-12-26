mod aoc;
mod intcode;
use std::collections::HashMap;

#[derive(PartialEq, Clone, Copy, Debug)]
enum Tile {
    Empty,
    Wall,
    Block,
    HorizontalPaddle,
    Ball
}

impl Tile {
    fn try_from(value: i64) -> Result<Tile, String> {
        match value {
            0 => Ok(Tile::Empty),
            1 => Ok(Tile::Wall),
            2 => Ok(Tile::Block),
            3 => Ok(Tile::HorizontalPaddle),
            4 => Ok(Tile::Ball),
            _ => Err(format!("bad tile given {:?}", value)),
        }
    }
}

fn main() {
    let lines = aoc::get_input_lines(String::from("input"));

    for line in lines {
        let mut computer = intcode::Computer::new(line);
        match computer.intcode.insert(0, 2) { _ => ()};

        let mut score = 0; let mut output;
        let mut ball: (i64, i64) = (0,0);
        let mut paddle: (i64, i64) = (0,0);
        let mut tiles: HashMap<(i64,i64), Tile> = HashMap::new();
        let mut blocks = 0;
        let mut input = 0;


        loop {
            output = computer.run(vec![input]).expect("Error in computer.");
            let mut index = 0;

            while output.len() > index {
                let pos = (output[index] as i64, output[index+1] as i64);
                let value = output[index+2];

                if pos == (-1 as i64, 0 as i64) {
                    score = value;
                } else {
                    // println!("Pos: {:?} value: {:?}", pos, value);
                    let tile = Tile::try_from(value).expect("Failed to parse type.");

                    if tile == Tile::Ball {
                        ball = pos;
                    }

                    if tile == Tile::HorizontalPaddle {
                        paddle = pos;
                    }

                    match tiles.insert(pos, tile) {
                         Some(Tile::Block) => blocks -= 1,
                         _ => {
                             if tile == Tile::Block {
                                 blocks += 1;
                             }
                         },
                    }
                }

                index += 3;
            }

            println!("Ball -> pos: {:?}", ball);
            println!("Paddle -> pos: {:?}", paddle);
            if ball.0 < paddle.0 {
                input = -1;
            } else if ball.0 > paddle.0 {
                input = 1;
            } else {
                input = 0;
            }

            println!("Blocks: {:?}", blocks);
            if (blocks == 0) {
                println!("Score: {:?}", score);
                break;
            }
            // for _i in 0..30000000 {

            // }
        }
        aoc::submit(2, score);
    }
}
