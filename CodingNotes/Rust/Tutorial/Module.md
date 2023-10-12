---
tags: rust, module, cargo, crate, package
---
# Rust Module

Modules in Rust help in splitting a program into logical units for better readability and organization. Once a program gets larger, it is important to split it into multiple files or namespaces. Modules help in structuring our program. A module is a collection of items: functions, structs and even other modules.

## Defining a Module in Rust

The `mod` keyword is used to define a module. The syntax of module is:

```rust
// syntax of a module
mod module_name {
  // code
}
```

Here, `module_name` is the name of the module.

Now, let's define a module.
```rust
// a module named config
mod config {
    // a function print inside of the module 
    fn print() {
        println!("config!");
    }
}
```

In the above example, we create a module named `config` using the `mod` keyword. Inside the module we can define multiple items. Here, we have defined the `print()` function.

## Visibility of Items inside a Module in Rust

Items inside a module can be private or public. By default, a module is private. It means items inside the module cannot be accessed outside of the module.

The `pub` keyword can be used to give an item public visibility. Let's look at an example.

```rust
mod config {
    // items in modules by default have private visibility
    fn select() {
        println!("called config::select");
    }

    // use the `pub` keyword to override private visibility
    pub fn print() {
        println!("called config::print");
    }
}
```

Here, we define a module named `config` with two functions `select()` and `print()`. The `print()` function starts with the `pub` keyword which means it has public visibility. However, the `select()` function does not. If we compile the above program, we don't get any output because we have not used the functions yet.

Now, let's call the functions inside the module.
```rust
mod config {
    // items in modules by default have private visibility
    fn select() {
        println!("called config::select");
    }

    // use the `pub` keyword to override private visibility
    pub fn print() {
        println!("called config::print");
    }
}

fn main() {
    // public items inside module can be accessed outside the parent module
    // call public print function from display module
    config::print();
}
```

**Output:**
```
called config::print
```

Here, we call the public function `print()` inside of the `config` module using the syntax `config::print()`. The `::` operator is used to separate the module name and the item to call inside the module.

However, private items inside of the module are not accessible outside the module. If we call the private function `select()` inside the `config` module, we get a compilation error.

```rust
mod config {
    // items in modules by default have private visibility
    fn select() {
        println!("called config::select");
    }

    // use the `pub` keyword to override private visibility
    pub fn print() {
        println!("called config::print");
    }
}

fn main() {
    // private items inside module cannot be accessed outside the parent module
    // calling private select function inside config module will cause a compilation error
    config::select();
}
```

The error mentions that the ``function `select` is private``. Thus, visibility of items inside a module is an important design consideration.

> **Note:** A module can also have public visibility when used together with the `pub` keyword.

### Example: Using Module in Rust

```rust
mod player {
    // private function
    fn focus() {
        println!("called player::focus");
    }

    // public function
    pub fn shift() {
        println!("called player::shift");
    }

    // public function
    pub fn jump() {
        // call private function focus and shift inside the module
        focus();
        shift();
        println!("called player::jump");
    }
}

fn main() {
    // call public function jump from player module
    player::jump();
}
```

**Output**
```
called player::focus
called player::shift
called player::jump
```

Here, we define multiple functions inside the `player` module. Notice that we are able to call the private function `focus()` in another function `jump()` inside the same module.

## Nested Modules

A module can be defined inside another module. This is known as module nesting. Let's look at an example.

```rust
// nested module
pub mod player {
    pub mod sprite {
        pub fn create() {
            println!("called player::sprite::create");
        }
    }
}

fn main() {
    // call public function create from sprite module which is inside player module 
    player::sprite::create();
}
```

**Output**
```
called player::sprite::create
```

Here, we have a `sprite` module nested within the `player` module.

We define a public function `create()` inside of the `sprite` module which is called using `player::sprite::create()` outside the module in the `main()` function.

---

## The use keyword in Rust

We can use the `use` keyword to bring items inside a module into the current scope. The `use` keyword helps us eliminate writing out the full module path to call functions.

Let's rewrite our nested module example with the help of the `use` keyword.

```rust
// nested module
pub mod player {
    pub mod sprite {
        pub fn create() {
            println!("called player::sprite::create");
        }
    }
}

// bring the create function into scope
use player::sprite::create;

fn main() {
    // call public function directly
    create();
}
```

**Output**
```
called player::sprite::create
```

Here, we use the `use` keyword to bring the `create()` function into the current scope from the `sprite` module which is inside the `player` module. This allows us to call the `create()` function directly, without having to fully qualify the name as `player::sprite::create()`.

# Rust Crate and Package

A crate can contain one or more Rust modules, which in turn can contain code, such as functions, types, and constants.

A crate is of two types:
- A **binary crate** is a Rust program that compiles to an executable or multiple executables and has a `main()` function for each executable.
- A **library crate** doesn't compile to an executable and doesn't have a `main()` function. A library crate generally defines a shared functionality that can be used in multiple projects.

Crates can be bundled together into a package.

## Creating a Package in Rust

Packages can be created using the [Cargo package manager](https://doc.rust-lang.org/cargo/), which is built into Rust. Cargo comes pre-installed with Rust. We can use cargo to create a package. A **package** contains one or more crates that provides a set of functionality.

> **Note:** A package can contain many binary crates, but at most only one library crate.

### Creating a Binary Package in Rust
  
To create a binary package, we can use the `cargo` command in the terminal.

```
$ cargo new hello_world --bin
```

**Output**
```
Created binary (application) `hello_world` package
```

We create a binary package `hello_world` using `cargo` and the `--bin` option. It is the default cargo behavior.

Let's look at the contents of the `hello_world` package.

hello_world
├── Cargo.toml
└── src
    └── main.rs

Here,
- `hello_world` is the package directory
- `Cargo.toml` is a file that contains metadata about the crate, such as its name, version, and dependencies
- `src/main.rs` is the crate root and contains the source code of the binary package

### Creating a Library Package in Rust

Similarly, we can create a library package in Rust using cargo.

```
$ cargo new hello_world_lib --lib
```

**Output**
```
Created library `hello_world_lib` package
```

We create a library package `hello_world_lib` using cargo and the `--lib` option.

Let's look at the contents of the `hello_world_lib` package.

hello_world_lib
├── Cargo.toml
└── src
    └── lib.rs

Here,
- `hello_world_lib` is the package directory
- `Cargo.toml` is a file that contains metadata about the crate, such as its name, version, and dependencies
- `src/lib.rs` is the crate root and contains the source code of the library package

A package can contain `src/main.rs` and `src/lib.rs`. In this case, it has two crates: a binary and a library, both with the same name as the package. For example,

hello_world
├── Cargo.toml
└── src
    └── lib.rs
    └── main.rs

> **Note:** Cargo by convention passes the crate root files to the Rust compiler to build the library or binary.


# Rust Cargo

Cargo is the Rust package manager. It comes pre-installed with Rust and can be used to package dependencies, manage them as well as build and distribute our own packages/libraries.

## Features of Cargo in Rust

Cargo is a command line tool for Rust which comes with these features:

- **Dependency management** 
	- Cargo makes it easy to manage the dependencies of our project, including adding, updating, and removing dependencies.

- **Building and packaging** 
	- Cargo can automatically build and package our Rust projects, creating binary or library code that can be shared with others.

- **Document generation** 
	- Cargo can automatically generate documentation for our code, making it easier for other developers to understand and use our library.

- **Download crates**   
	- Cargo can download and install libraries from [crates.io](https://crates.io/), which is a central repository for Rust crates.

- **Run a binary or tests**   
	- Cargo can build our source code, run the executable binary and also run our tests.
## Dependency Management with Cargo in Rust

One of the primary features of cargo is that it can download, manage external libraries.

Let's look at an example of how we can use an external crate from [crates.io](https://crates.io/). **crates.io** is a central repository where we can pull and publish shared libraries for Rust.

Start by creating a Rust project using cargo:

```
$ cargo new hello_world
```

Now,

- `Cargo.toml` file in the root of our project directory `hello_world` is used to manage the dependencies.

If we want to use the "[rand](https://crates.io/crates/rand)" crate, we add the following line to the `[dependencies]` section of the `Cargo.toml`.

```
[package]
name = "hello_world"
version = "0.1.0"
edition = "2021"

# See more keys and their definitions at https://doc.rust-lang.org/cargo/reference/manifest.html

[dependencies]
rand = "0.8.5"
```

> **Note**: We can also add dependency to our project using the command `cargo add rand`.

- Next, we'll need to import the crate in our `src/main.rs` Rust file. We can do this by using `extern crate <crate_name>` line at the top of the file.  
      
    ```
    extern crate rand;
    ```
    
- Now, we can use the "rand" crate to generate a random number between **1** and **6**. The `use` keyword is used here to import items (such as functions, types, and constants) from the "rand" crate in the current scope.  
      
```rust
extern crate rand;

use rand::Rng;

fn main() {
	let mut rng = rand::thread_rng();

	// simulate rolling a die
	println!("roll = {}", rng.gen_range(1..=6));
}

# Output: roll = 5
```

## Building and Running Project with Cargo in Rust

We can use cargo to install, build and run our `hello_world` project with the "rand" crate. Here's how:

**Build the project**  
  
```
$ cargo build
```

**Output:**
```
Compiling libc v0.2.139
Compiling cfg-if v1.0.0
Compiling ppv-lite86 v0.2.17
Compiling getrandom v0.2.8
Compiling rand_core v0.6.4
Compiling rand_chacha v0.3.1
Compiling rand v0.8.5
Compiling hello_world v0.1.0 (/experiments/rust-practice/hello_world)
  Finished dev [unoptimized + debuginfo] target(s) in 2.57s
```


The `cargo build` command first installs any crates that are in use inside the `src/` directory and then proceeds to compile the project.

**Run the project**

```
$ cargo run
```

**Output:**
```
Finished dev [unoptimized + debuginfo] target(s) in 0.05s
    Running `target/debug/hello_world`
roll = 5
```

## Useful Cargo Commands in Rust

Cargo can do a bunch of repetitive tasks for us. Here are some of the commonly used cargo commands.

|Command|Description|
|---|---|
|`cargo new`|Create a new Rust project with basic directory structure|
|`cargo build`|Build (compile) the current project and generate a binary executable|
|`cargo run`|Build and run your current project (cargo build + run)|
|`cargo check`|Build the current project without generating a binary executable|
|`cargo add`|Add a new dependency and include it in `Cargo.toml` file|
|`cargo update`|Update all dependencies of current project to latest version|