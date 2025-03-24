use std::io::{self, Write};
use std::{thread, time::Duration,};

fn prog(percent: usize) {
    let width = 50;
    let filled = percent * width / 100;
    let empty = width - filled;

    print!("\r{:3}% ▕{}{} |", percent, "█".repeat(filled), " ".repeat(empty));
    io::stdout().flush().unwrap();
}

fn main() {
    for i in 0..=100 {
        prog(i);
        thread::sleep(Duration::from_millis(20));
    }
}