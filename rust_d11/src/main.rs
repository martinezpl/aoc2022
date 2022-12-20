use regex::Regex;
use std::collections::VecDeque;
use std::fs;
use std::str::FromStr;

const PART: u8 = 2;

struct Monkey {
    items: VecDeque<u128>,
    operation: (String, u128),
    test_div: u128,
    true_idx: usize,
    false_idx: usize,
    items_inspected: u128,
    product: u128,
}

impl Monkey {
    fn throw_to(&mut self) -> (usize, u128) {
        let mut it = self.items.pop_front().unwrap();
        self.items_inspected += 1;
        if self.operation.0 == "+" {
            it = it + self.operation.1
        } else if self.operation.0 == "*" {
            if self.operation.1 == 0 {
                it *= it
            } else {
                it *= self.operation.1
            }
        }
        if PART == 1 {
            it = it / 3;
        } else {
            it = it % self.product
        }
        if it % self.test_div == 0 {
            (self.true_idx, it)
        } else {
            (self.false_idx, it)
        }
    }

    fn catch(&mut self, item: u128) {
        self.items.push_back(item);
    }
}

fn read_input() -> Vec<String> {
    let inp: Vec<String> = fs::read_to_string("d11.txt")
        .unwrap()
        .split("\n\n")
        .map(|s| String::from(s))
        .collect::<Vec<String>>();
    inp
}

fn fill_monkey_vector(input: Vec<String>, vec: &mut Vec<Monkey>) {
    let inp = input.into_iter();
    let re = regex::Regex::new(r"\d+").unwrap();
    let mut product = 1;
    inp.for_each(|monke_info| {
        let lines = monke_info.lines().collect::<Vec<&str>>();
        let op = lines[2].split("old ").collect::<Vec<&str>>()[1]
            .split(" ")
            .collect::<Vec<&str>>();
        let op = (
            String::from(op[0]),
            op[1].parse::<u128>().unwrap_or_else(|err| 0),
        );
        let div = u128::from_str(&(&re.captures(lines[3]).unwrap())[0]).unwrap();
        product *= div;
        vec.push(Monkey {
            items: re
                .find_iter(lines[1])
                .map(|d| u128::from_str(d.as_str()).unwrap())
                .collect::<VecDeque<u128>>(),
            operation: op,
            test_div: div,
            true_idx: usize::from_str(&(&re.captures(lines[4]).unwrap())[0]).unwrap(),
            false_idx: usize::from_str(&(&re.captures(lines[5]).unwrap())[0]).unwrap(),
            items_inspected: 0,
            product: 1,
        })
    });
    for monkey in vec {
        monkey.product = product;
    }
}

fn main() {
    let mut monkey_vector: Vec<Monkey> = vec![];
    let inp = read_input();
    fill_monkey_vector(inp, &mut monkey_vector);

    let mut round = 1;
    let mut max_rounds = 0;
    if PART == 1 {
        max_rounds = 20;
    } else {
        max_rounds = 10000;
    }
    while round <= max_rounds {
        for i in 0..monkey_vector.len() {
            for _ in 0..monkey_vector[i].items.len() {
                let (recipient_idx, item) = monkey_vector[i].throw_to();
                monkey_vector[recipient_idx].catch(item);
            }
        }
        if round == 20 {
            println!(
                "{:?}",
                monkey_vector
                    .iter()
                    .map(|m| m.items_inspected)
                    .collect::<Vec<u128>>()
            )
        }
        round += 1;
    }
    let mut inspections = monkey_vector
        .iter()
        .map(|m| m.items_inspected)
        .collect::<Vec<u128>>();
    inspections.sort();
    inspections.reverse();
    println!(
        "{}, {}, {}",
        inspections[0] * inspections[1],
        inspections[0],
        inspections[1]
    );
}
