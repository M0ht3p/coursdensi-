use std::io::{self, Write};
use std::process::Command;

fn main() {
    let output = Command::new("cmd")
        .args(["/C", "netsh wlan show profiles"])
        .output()
        .expect("Failed to run netsh wlan show profiles");

    let profiles = String::from_utf8_lossy(&output.stdout);

    let mut names = Vec::new();

    for line in profiles.lines() {
        if line.contains("All User Profile") {
            if let Some((_, value)) = line.split_once(':') {
                names.push(value.trim().to_string());
            }
        }
    }

    if names.is_empty() {
        println!("No WiFi profiles found.");
        return;
    }

    for (i, name) in names.iter().enumerate() {
        println!("[{}] {}", i + 1, name);
    }

    print!("\nChoose WiFi number: ");
    io::stdout().flush().unwrap();

    let mut choice = String::new();
    io::stdin()
        .read_line(&mut choice)
        .expect("Failed to read user input");

    let index: usize = match choice.trim().parse() {
        Ok(n) => n,
        Err(_) => {
            println!("\nInvalid number.");
            return;
        }
    };

    if index == 0 || index > names.len() {
        println!("\nInvalid selection.");
        return;
    }

    let wifi = &names[index - 1];

    let command = format!(r#"netsh wlan show profile "{}" key=clear"#, wifi);

    let output = Command::new("cmd")
        .args(["/C", &command])
        .output()
        .expect("Failed to get WiFi profile details");

    let result = String::from_utf8_lossy(&output.stdout);

    let password = result
        .lines()
        .find_map(|line| {
            if line.contains("Key Content") {
                line.split_once(':').map(|(_, value)| value.trim().to_string())
            } else {
                None
            }
        });

    match password {
        Some(password) => println!("\nPassword: {}", password),
        None => println!("\nPassword: No password found or profile is open."),
    }
}
