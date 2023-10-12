---
tags: rust, installation, rust_doc, cargo
---
# Installation
```
$ curl --proto '=https' --tlsv1.2 https://sh.rustup.rs -sSf | sh
```

## Updating and Uninstalling

Once Rust is installed via `rustup`, updating to a newly released version is easy. From your shell, run the following update script:

```console
$ rustup update
```

or 

```console
$ rustup update stable
```

To uninstall Rust and `rustup`, run the following uninstall script from your shell:

```console
$ rustup self uninstall
```

# Local Document

```
$ rustup doc 
$ rustup doc --book
```

# Cargo
- `cargo new <project>`: create a new directory and project 
- `cargo build`
- `cargo run`
- `cargo check`: Cargo also provides a command called cargo check. This command quickly checks your code to make sure it compiles but doesn’t produce an executable. Why would you not want an executable? Often, cargo check is much faster than cargo build because it skips the step of producing an executable. If you’re continually checking your work while writing the code, using cargo check will speed up the process of letting you know if your project is still compiling! As such, many Rustaceans run cargo check periodically as they write their program to make sure it compiles. Then they run cargo build when they’re ready to use the executable.

> **Note**: You won’t just know which traits to use and which methods and functions to call from a crate, so each crate has documentation with instructions for using it. Another neat feature of Cargo is that running the `cargo doc --open` command will build documentation provided by all your dependencies locally and open it in your browser. If you’re interested in other functionality in the `rand` crate, for example, run `cargo doc --open` and click `rand` in the sidebar on the left.


# Guessing Game

```rust
use std::io;
use rand::Rng;
use std::cmp::Ordering;

fn main() {
    println!("Guess the number");

    let secret_number = rand::thread_rng().gen_range(1..=100);
    println!("The secret number is: {secret_number}");

    loop {
        println!("Please input your guess.");
        let mut guess = String::new();

        io::stdin()
            .read_line(&mut guess)
            .expect("Failed to read line");

        let guess: u32 = guess.trim().parse().expect("Please type a number!");
        println!("You guessed: {guess}");

        match guess.cmp(&secret_number) {
            Ordering::Less => println!("Too small!"),
            Ordering::Greater => println!("Too big!"),
            Ordering::Equal => {
                println!("You win!");
                break;
            }
        }
    }
}
```




