// cargo-deps: colored = "2.0"
use colored::*;

fn main() {
    loop {
        let mut line = String::new();
        println!("{} Enter the temperature: ", "?".blue());
        std::io::stdin().read_line(&mut line).expect("Failed to read line");
        match line.trim().parse::<f32>() {
            Ok(temp) => {
                println!("{{ Temperature: {}{} }}", temp.to_string().blue().bold(), "°C/F/K".blue().bold());
                break;
            }
            Err(_) => { eprintln!("{}", "Invalid number — please try again.".red()); }
        }
    }
}