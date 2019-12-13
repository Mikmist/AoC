struct Computer {
    intcode: Vec<i32>,
}

impl {
    fn from_intcode(input: String) -> Computer {
        Computer {
            intcode = input.split(",").collect();
        }
    }
}

#[test]
fn test_from_intcode() {
    
}
