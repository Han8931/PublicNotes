---
tags: rust, error, ownership, borrowing
---
# Error Handling

## Unrecoverable Errors in Rust

Unrecoverable errors are errors from which a program stops its execution. As the name suggests, we cannot recover from unrecoverable errors. These errors are known as **panic** and can be triggered explicitly by calling the `panic!` macro. Let's look at an example that uses the `panic!` macro.

### Example 1: Rust Unrecoverable Errors with panic! Macro

```rust
fn main() {
    println!("Hello, World!");

    // Explicitly exit the program with an unrecoverable error
    panic!("Crash");
}
```

**Output:**
```
Hello, World!
thread 'main' panicked at 'Crash', src/main.rs:5:5
```

Here, the call to the `panic!` macro causes an unrecoverable error.

`thread 'main' panicked at 'Crash', src/main.rs:5:5`

Notice that the program still runs the expressions above `panic!` macro. We can still see `Hello, World!` printed to the screen before the error message. The `panic!` macro takes in an error message as an argument.

### Example 2: Rust Unrecoverable Errors

Unrecoverable errors are also triggered by taking an action that might cause our code to panic. For example, accessing an array past its index will cause a panic.

```rust
fn main() {
    let numbers = [1, 2 ,3];

    println!("unknown index value = {}", numbers[3]);
}
```

**Error:**
```
error: this operation will panic at runtime
 --> src/main.rs:4:42
  |
4 |     println!("unknown index value = {}", numbers[3]);
  |                                          ^^^^^^^^^^ index out of bounds: the length is 3 but the index is 3
  |
```
Here, Rust stops us from compiling the program because it knows the operation will panic at runtime. The array numbers does not have a value at index **3** i.e. `numbers[3]`.

## Recoverable Errors

Recoverable errors are errors that won't stop a program from executing. Most errors are recoverable, and we can easily take action based on the type of error. For example, if you try to open a file that doesn't exist, you can create the file instead of stopping the execution of the program or exiting the program with a panic. Let's look at an example.

```rust
use std::fs::File;

fn main() {
    let data_result = File::open("data.txt");

    // using match for Result type
    let data_file = match data_result {
        Ok(file) => file,
        Err(error) => panic!("Problem opening the data file: {:?}", error),
    };

    println!("Data file", data_file);
}
```

If the `data.txt` file exists, the **output** is:

```
Data file: File { fd: 3, path: "/playground/data.txt", read: true, write: false }
```

If the `data.txt` file doesn't exist, the **output** is:

```
thread 'main' panicked at 'Problem opening the data file: Os { code: 2, kind: NotFound, message: "No such file or directory" }', src/main.rs:8:23
```

## The Result Enum

In the above example, the return type of the `File::open('data.txt')` is a `Result<T, E>`.

The `Result<T, E>` type _returns either a value or an error_ in Rust. It is an `enum` type with two possible variants.

- `Ok(T)` → operation succeeded with value `T`
- `Err(E)` → operation failed with an error `E`

Here, `T` and `E` are generic types. 

The most basic way to see whether a `Result` enum has a value or error is to use pattern matching with a `match` expression.

```rust
// data_file is a Result<T, E>
match data_result {
    Ok(file) => file,
    Err(error) => panic!("Problem opening the data file: {:?}", error),
 };
```

When the result is `Ok`, this code will return the `file`, and when the result is `Err`, it will return a `panic!`.

## The Option Enum

The `Option` type or `Option<T>` type is an `enum` type just like `Result` with two possible variants.
- `None` → to indicate failure with no value
- `Some(T)` → a value with type `T`

Let's look at an example,
```rust
fn main() {
    let text = "Hello, World!";

    //nth returns n-th element of the iterator
    let character_option = text.chars().nth(15); 
    
    // using match for Option type
    let character = match character_option {
        None => "empty".to_string(), // converts the given value to a String
        Some(c) => c.to_string()
    };
    
    println!("Character at index 15 is {}", character);
}
```

**Output**
```
Character at index 15 is empty
```

Here, the method `text.chars().nth(15)` returns an `Option<String>`. So, to get the value out of the `Option`, we use a `match` expression. In the example above, the 15th index of the string text doesn't exist. Thus, the `Option` type returns a `None` which matches the `"empty"` string.

```
None => "empty".to_string() 
```

If we were to get the 11th index of the string text, the `Option` enum would return `Some(c)`, where `c` is the character in the 11th index.

Let's update the above example to find out the 11th index in the string.

```rust
fn main() {
    let text = "Hello, World!";
    
    let character_option = text.chars().nth(11);
    
    // using match for Option type
    let character = match character_option {
        None => "empty".to_string(),
        Some(c) => c.to_string()
    };
    
    println!("Character at index 11 is {}", character);
}
```

**Output**
```
Character at index 11 is d
```

## Difference between Result and Option enum in Rust

`Option` enum can return `None`, which can indicate failure.

However, sometimes it is essential to express why an operation failed. Thus, we have the `Result` enum, which gives us the `Err` with the reason behind the failure of the operation.

In short,
- `Option` is about `Some` or `None` (value or no value)
- `Result` is about `Ok` or `Err` (result or error result)

# Rust unwrap() and expect()

The `unwrap()` are `expect()` utility methods that work with Option and Result types in Rust.

## The unwrap() Method

Unwrap in Rust returns the result of the operation for `Option` and `Result` enums. If unwrap encounters an error `Err` or a `None`, it will panic and stop the program execution. Unwrap method is defined on both `Option` and `Result` type. An `Option` enum type can be handled by using the `match` expression as well as `unwrap()`

### Example: Using the match Expression

```rust
// function to find a user by their username which returns an Option type
fn get_user(username: &str) -> Option<&str> {
    if username.is_empty() {
        return None;
    }

    return Some(username);
}

fn main() {
    // returns an Option
    let user_option = get_user("Hari");

    // use of match expression to get the result out of Option
    let result = match user_option {
        Some(user) => user,
        None => "not found!",
    };

    // print the result
    println!("user = {:?}", result);
}
```

**Output:**
```
user = "Hari"
```

Here, we have a `get_user` function that returns an `Option` type. It can either return `Some(&str)` or `None`. 

Now, this program can use the `unwrap()` method to get rid of the `match` expression which is a little verbose. Let's use `unwrap()` in the above example.

### Example: Using unwrap()

```rust
// function to find a user by their username which return an Option enum
fn get_user(username: &str) -> Option<&str> {
    if username.is_empty() {
        return None;
    }

    return Some(username);
}

fn main() {
    // use of unwrap method to get the result of Option enum from get_user function
    let result = get_user("Hari").unwrap();

    // print the result
    println!("user = {:?}", result);
}
```

**Output:**
```
user = "Hari"
```

Both the `match` expression and `unwrap()` gives us the same output. The only difference being that `unwrap()` will panic if the return value is a `None`.

  
If we update the above program to send an empty username argument to the `get_user()` method. It will panic.
```rust
let result = get_user("").unwrap();
```

The output in this case will be,
```
thread 'main' panicked at 'called `Option::unwrap()` on a `None` value', src/main.rs:12:31ßß
```

## The expect() Method

`expect()` is very similar to `unwrap()` with the addition of a custom panic message as an argument.

The `expect()` method is defined on both `Option` and `Result` type.

Let's update the above example to use `expect()` instead of `unwrap()`.

```rust
// function to find a user by their username which return an Option enum
fn get_user(username: &str) -> Option<&str> {
    if username.is_empty() {
        return None;
    }

    return Some(username);
}

fn main() {
    // use of expect method to get the result of Option enum from get_user function
    let result = get_user("").expect("fetch user");

    // print the result
    println!("user = {:?}", result);
}
```

**Output:**
```
thread 'main' panicked at 'fetch user', src/main.rs:12:31
```

Here, we use the `expect()` with a panic message as the argument.

`expect()` and `unwrap()` will produce the same result if there's no possibility of `Option` returning `None` and `Result` returning `Err`.

> **Note:** `unwrap()` and `expect()` are utility methods to work with `Option` and `Result` types. It makes our program concise and prevents the need to write verbose `match` expressions to return a result.

## The Question Mark (?) Operator

The question mark (`?`) operator is a shorthand for returning the `Result`. It can only be applied to `Result<T, E>` and `Option<T>` type.

When we apply `?` to `Result<T, E>` type:
- If the value is `Err(e)`, it returns an `Err()` immediately
- If the value is `Ok(x)`, it unwraps and returns `x`

Let's look at an example.
```rust
use std::num::ParseIntError;

// Function to parse an integer
fn parse_int() -> Result<i32, ParseIntError> {
    // Example of ? where value is unwrapped
    let x: i32 = "12".parse()?; // x = 12
    
    // Example of ? where error is returned
    let y: i32 = "12a".parse()?; // returns an Err() immediately
    
    Ok(x + y) // Doesn't reach this line
}

fn main() {
    let res = parse_int();

    println!("{:?}", res);
}
```

**Output:**
```
Err(ParseIntError { kind: InvalidDigit })
```

This way, error handling in the function is reduced to a single line of code, making it cleaner and easier to read.

Similarly, when we apply `?` to `Option<T>` type:
- If the value is `None`, then it returns `None`
- If the value is `Some(x)`, then it unwraps the value and returns `x`

> **Note:** The question mark operator (`?`) can only be used in a function that returns `Result` or `Option`.

# Rust Ownership

Rust includes an ownership mechanism to manage the memory of our program. Ownership is a set of rules that ensure memory safety in Rust programs. The ownership feature in Rust allows our program to run without memory leaks and slowness.

## Variable Scope in Rust

A scope is a code block within the program for which a variable is valid. The scope of a variable defines its ownership. For example,

```rust
// `name` is invalid and cannot be used here because it's not yet declared
{ // code block starts here
    let name = String::from("Ram Nepali");   // `name` is valid from this point forward
    
    // do stuff with `name`
} // code block ends
// this scope ends, `name` is no longer valid and cannot be used
```

Here the variable name is only available inside the code block, i.e., between the curly braces `{}`. We cannot use the name variable outside the closing curly brace. Whenever a variable goes out of scope, its memory is freed.

## Ownership Rules in Rust

Rust has some ownership rules. Keep these rules in mind as we work through some examples:
1. Each value in Rust has an owner.
2. There can only be one owner at a time.
3. When the owner goes out of scope, the value will be dropped.

## Data Move in Rust

Sometimes, we might not want a variable to be dropped at the end of the scope. Instead, we want to transfer ownership of an item from one binding (variable) to another.

Here's an example to understand data movement and ownership rules in Rust.

```rust
fn main() {
    // owner of the String value
    // rule no. 1 
    let fruit1 = String::from("Banana");
    
    // ownership moves to another variable
    // only one owner at a time
    // rule no. 2
    let fruit2 = fruit1;
    
    // cannot print variable fruit1 because ownership has moved
    // error, out of scope, value is dropped
    // rule no. 3
    // println!("fruit1 = {}", fruit1);
    
    // print value of fruit2 on the screen
    println!("fruit2 = {}", fruit2);
}
```

**Output:**
```
fruit2 = Banana
```

Let's look into this example in detail, especially these two lines of code:

```rust
let fruit1 = String::from("Banana");
let fruit2 = fruit1;
```

Here, `fruit1` is the owner of the `String`.

A `String` stores data both on the _stack and the heap_. This means that when we bind a `String` to a variable `fruit1`, the memory representation looks like this:

<img src="https://www.programiz.com/sites/tutorial2program/files/rust-memory-representation-of-string.png "Memory representation of a String holding the value"" width=30% style="background-color:white;" \>
- A `String` holds a pointer to the memory that holds the content of the string, a length, and a capacity in the stack. 
- The heap on the right hand side of the diagram holds the contents of the `String`.

Now, when we assign `fruit1` to `fruit2`, this is how the memory representation look

<img src="https://www.programiz.com/sites/tutorial2program/files/rust-memory-representation-of-a-move.png "Memory representation when String value""  width=30% style="background-color:white;" \>

Rust will invalidate (drop) the first variable `fruit1`, and move the value to another variable `fruit2`. This way _two variables cannot point to the same content_. At any point, _there is only one owner of the value._

> **Note:** The above concept is applicable for data types that don't have fixed sizes in memory and use the heap memory to store the contents.

## Data Copy in Rust

_Primitive types like Integers, Floats and Booleans don't follow the ownership rules_. These types have a known size at compile time and are stored entirely on the stack, so copies of the actual values are quick to make. For example,

```rust
fn main() {
    let x = 11;
    
    // copies data from x to y
    // ownership rules are not applied here 
    let y = x;

    println!("x = {}, y = {}", x, y);
}
```

**Output:**
```
x = 11, y = 11
```

Here, `x` variable can be used afterward, unlike a move without worrying about ownership, even though `y` is assigned to `x`. This copying is possible because of the `Copy` trait available in primitive types in Rust. When we assign `x` to `y`, a copy of the data is made. A **trait** is a way to define shared behavior in Rust. 

## Ownership in Functions

Passing a variable to a function will move or copy, just as an assignment. Stack-only types will copy the data when passed into a function. Heap data types will move the ownership of the variable to the function.

Let's take a look at some examples.

### Passing String to a function

```rust
fn main() {
    let fruit = String::from("Apple");  // fruit comes into scope
    
    // ownership of fruit moves into the function
    print_fruit(fruit);
    
    // fruit is moved to the function so is no longer available here
    // error
    // println!("fruit = {}", fruit);
}

fn print_fruit(str: String) {   // str comes into scope
    println!("str = {}", str);
}   // str goes out of scope and is dropped, plus memory is freed
```

**Output:**
```
str = Apple
```

Here, the value of the fruit variable is moved into the function `print_fruit()` because `String` type uses heap memory.

### Passing Integer to a function

```rust
fn main() {
    // number comes into scope
    let number = 10;
    
    // value of the number is copied into the function
    print_number(number);
    
    // number variable can be used here
    println!("number = {}", number);
}

fn print_number(value: i32) { // value comes into scope
    println!("value = {}", value);
}   // value goes out of scope
```

**Output:**
```
value = 10
```

```
number = 10
```

Here, the value of the number variable is copied into the function `print_number()` because the `i32` (integer) type uses stack memory.

# Rust References and Borrowing

**References** in Rust allow us to point to a resource (value) without owning it. This means that the original owner of the resource remains the same. References are helpful when passing values to a function that we do not want to change the ownership of. Creating a reference is known as **borrowing in Rust**.

## Understanding References in Rust

Let's look at an example to learn about references in Rust.

```rust
fn main() {
    let str = String::from("Hello, World!");
    
    // Call function with reference String value
    let len = calculate_length(&str);

    println!("The length of '{}' is {}.", str, len);
}

// Function to calculate length of a string
// It takes a reference of a String as an argument
fn calculate_length(s: &String) -> usize {
    s.len()
}
```

**Output**
```
The length of 'Hello, World!' is 13.
```

In the above example, we define a function called `calculate_length()` which takes a `&String` type as an argument.

The important part here is that _`s` is a reference to a `String` and it doesn't take ownership of the actual value of `String`._

```rust
fn calculate_length(s: &String) -> usize { // s is a reference to a String
    s.len()
}
```

When, `s` goes out of scope, at the end of the function, it is not dropped because it does not have ownership of what it refers to.

The function call looks like:

```rust
let str = String::from("Hello, World!");

let len = calculate_length(&str);
```

The `&str` syntax while calling the function lets us create a **reference** that refers to the value of `str` but does not own it.

The action of creating a reference is known as **borrowing**. Borrowing is when we borrow something, and we are done with it, we give it back. It doesn't make us the owner of the data.

> **Note:** Ampersand (&) represents references, and they allow us to refer to some value without taking ownership of it.

## Modifying a Reference in Rust

By default a reference is always immutable. However, we can use the `&mut` keyword to make a reference mutable.

For example,

```rust
fn main() {
    let mut str = String::from("Hello");
    
    // before modifying the string
    println!("Before: str = {}", str);

    // pass a mutable string when calling the function
    change(&mut str);
    
    // after modifying the string
    println!("After: str = {}", str);
}

fn change(s: &mut String) {
    // push a string to the mutable reference variable
    s.push_str(", World!");
}
```

Here, we set the variable `str` to be mutable. Then we create a mutable reference with `&mut str`, and call the `change()` function with a mutable reference `s: &mut String`.

This allows the `change()` function to modify the value it borrows. Inside the `change()` function, we push a string with `s.push_str(", World!")` to the reference string.

> **Note:** If you have a mutable reference to a value, you can have no other references to that value.

```rust
fn main() {
    let mut str = String::from("hello");

    // mutable reference 1
    let ref1 = &mut str;

    // mutable reference 2
    let ref2 = &mut str;

    println!("{}, {}", ref1, ref2);
}
```

## Rules of References

Rust primarily follows these rules of references at any given time:
1. At any given time, _you can have either one mutable reference or any number of immutable references_.
2. _References must always be valid_.

