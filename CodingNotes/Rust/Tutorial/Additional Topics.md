---
tags: rust, pattern_matching, generics, traits, file_handling, macros, threads
---
# Rust Pattern Matching

Pattern matching is a way to match the structure of a value and bind variables to its parts. It is a powerful way to handle data and control flow of a Rust program.

We generally use the `match` expressions when it comes to pattern matching.

The syntax of the `match` expressions is:

```rust
match VALUE {
    PATTERN => EXPRESSION,
    PATTERN => EXPRESSION,
    PATTERN => EXPRESSION,
}
```

Here, `PATTERN => EXPRESSION` are called patterns, a special syntax in Rust which usually works together with the `match` keyword.

## Matching a Variable in Rust

We can pattern match against the value of a variable. This is useful if our code wants to take some action based on a particular value. For example,

```rust
fn main() {
    let x = 2;

    // use of match expression to pattern match against variable x
    match x {
        1 => println!("x is 1"),
        2 => println!("x is 2"),
        _ => println!("x is something else"),
    }
}
```

**Output:**
```
x is 2
```

Here, we have used the `match` expression to match against `x`. In the `match` body, we pattern matched with values `1`, `2` and `_`.

```rust
1 => println!("x is 1"),
2 => println!("x is 2"),
_ => println!("x is something else"),
```

Because the value of x is `2`, the pattern that matches is:

```rust
2 => println!("x is 2")
```

Thus, `x` is 2 is printed on the screen.

Notice that we also match against underscore `_`. The `_` has a special meaning in pattern matching, if all the other patterns do not match, it defaults to `_`.

> **Note**: `match` body (also known as match arms) should always ensure that all possible cases are being handled. If all possible cases are not handled, the Rust program fails to compile.

## Matching an Enum In Rust

Pattern matching is extensively used to match enum variants. For example,

```rust
fn main() {
    enum Color {
        Red,
        Green,
        Blue,
    }

    let my_color = Color::Green;

    // use of match expression to match against an enum variant
    match my_color {
        Color::Red => println!("The color is red"),
        Color::Green => println!("The color is green"),
        Color::Blue => println!("The color is blue"),
    }
}
```

**Output:**
```
The color is green
```


Here, we created a pattern in the `match` expression to match against all enum variants.

```rust
Color::Red => println!("The color is red"),
Color::Green => println!("The color is green"),
Color::Blue => println!("The color is blue"),
```

Because the value of `my_color` is `Color::Green`, the pattern that it matches is:

```rust
Color::Green => println!("The color is green"),
```

Thus, `The color is green` is printed on the screen.

## Matching Option and Result Type in Rust

The most common case for pattern matching is with `Option` and `Result` enum types. Both the `Option` and `Result` type have two variants.

`Option` type has:
- `None` → to indicate failure with no value
- `Some(T)` → a value with type T

`Result` type has:
- `Ok(T)` → operation succeeded with value T
- `Err(E)` → operation failed with an error E

Let's look at examples of how we can use pattern matching on these types.

### Example: Matching Option Type in Rust

```rust
fn main() {
    let my_option: Option<i32> = Some(222);
    
    // use of match expression to match Option type
    match my_option {
        Some(value) => println!("The option has a value of {}", value),
        None => println!("The option has no value"),
    }
}
```

**Output:**
```
The option has a value of 222
```

In this example, `my_option` is an `Option` type that contains either a `Some` variant with an `i32` value or a `None` variant.

The `match` expression compares the value of `my_option` to the `Some` and `None` variants, and binds the value of `Some` variant to the `value` variable.

When a match is found, the corresponding code block is executed.

```rust
Some(value) => println!("The option has a value of {}", value),
```

Thus, `The option has a value of 222` is printed on the screen.

### Example: Matching Result Type in Rust

```rust
fn main() {
    let my_result: Result<i32, &str> = Ok(100);

    // use of match expression to match Result type
    match my_result {
        Ok(value) => println!("The result is {}", value),
        Err(error) => println!("The error message is {}", error),
    }
}
```

**Output**
```
The result is 100
```

In this example, `my_result` is a `Result` type that contains either an `Ok` variant with an `i32` value, or an `Err` variant with an error message of type `&str`.

The match expression compares the value of `my_result` to the `Ok` and `Err` variants, and binds the value of `Ok` variant to the `value` variable or the `Err` variant to the `error` variable.

```rust
Ok(value) => println!("The result is {}", value),
Err(error) => println!("The error message is {}", error),
```

When a match is found, the corresponding code block is executed.

```rust
Ok(value) => println!("The result is {}", value),
```

Thus, `The result is 100` is printed on the screen.

## `if let` Expression in Rust

The `if let` expression in Rust is a shorthand for a `match` expression with only one pattern/arm to match.

It allows us to match on a value and then execute code only if the match is successful.

```rust
fn main() {
    let my_option: Option<i32> = Some(222);

    // use of if let expression on the Option type
    if let Some(value) = my_option {
        println!("The option has a value of {}", value);
    } else {
        println!("The option has no value");
    }
}
```

**Output**
```
The option has a value of 222
```

Here, the `if let` expression is matching on the `my_option` variable and binding the value of `Some` variant to the `value` variable.

If the match is successful, the code inside the `if` block is executed. If the match is not successful, the code inside the `else` block is executed.

# Rust Generics

Generics allows us to write code that is flexible and can be reused with different types of data, without having to write separate implementations for each type. It helps us write code that can handle values of any type in a type-safe and efficient way.

With the help of generics, we can define placeholder types for our methods, functions, structs, enums and traits.

## Using Generics in Rust

We can understand generics by taking a look at [Rust Hashmap](https://www.programiz.com/rust/hashmap). HashMap uses generics which allows creation of reusable and efficient code, as a single implementation that works with different types.

A Rust HashMap has two generic types, one for the key and the second for the value. A HashMap type looks like this:

```rust
HashMap<K, V>
```

where `<K, V>`: `K` is the type of the key and `V` is the type of the value. Now, when we create a HashMap we can set any type to `K` and `V`.

```rust
let mut numbers: HashMap<i32, &str> = HashMap::new();
```

Here, the angle bracket `<i32, &str>` notation denotes the type of key and type of value of the HashMap. The type of the key `K` is `i32` and the type of the value `V` is `&str`.

Similarly, we create a HashMap and set the type of both key and value to `&str`.

```rust
let mut language_codes: HashMap<&str, &str> = HashMap::new();
```

Using generics to define the type of HashMap helps us work with numerous arbitrary types available in Rust.

**Note:**
- Generics or generic types use a single character like `K`, `V`, `T`, `U` to distinguish from actual concrete types like `String`, `&str`, `i32`.
- As a convention,
    - `T`, `U` are used for arbitrary types
    - `K`, `V` are used for key-value types
    - `E` is used for error type

### Example: Using Generics in Rust

```rust
use std::collections::HashMap;

fn main() {
    // Create a HashMap with types i32 and &str
    let mut numbers: HashMap<i32, &str> = HashMap::new();

    // Insert values to numbers HashMap
    numbers.insert(1, "One");
    numbers.insert(2, "Two");

    println!("Numbers: {:?}", numbers);
    
    // Create a HashMap with types &str and &str   
    let mut language_codes: HashMap<&str, &str> = HashMap::new();

    // Insert values to language_codes HashMap
    language_codes.insert("EN", "English");
    language_codes.insert("NE", "Nepali");
    
    println!("Language Codes: {:?}", language_codes);
}
```

**Output**
```
Numbers: {1: "One", 2: "Two"}
Language Codes: {"EN": "English", "NE": "Nepali"}
```

Here, we create two HashMap data structures: `HashMap<i32, &str>` and `HashMap<&str, &str>`. This is possible because HashMap implementation uses generics and can work with different types.

## Generic Struct in Rust

We can create a generic struct data structure in Rust with the help of generics. For example, we can declare a struct with generic parameter(s).

```rust
struct Point<T> {
    x: T,
    y: T,
}
```

Here, we create a struct `Point` with generic type parameter `T` in angle brackets. Inside the body of the struct, we use the `T` data type for `x` and `y`.

Now, to use the generic struct `Point` we can initialize it and bind it to a variable.

```rust
let int_point = Point { x: 1, y: 2 };
let float_point = Point { x: 1.1, y: 2.2 };
```

Here, we initialize the `Point` struct twice, first with integer values and second with float values.

### Example: Generic Struct in Rust

```rust
fn main() {
    // defining a struct with generic data type
    #[derive(Debug)]
    struct Point<T> {
        x: T,
        y: T,
    }
    
    // initializing a generic struct with i32 data type
    let int_point = Point { x: 1, y: 2 };
    
    // initializing a generic struct with f32 data type
    let float_point = Point { x: 1.1, y: 2.2 };
    
    println!("int_point: {:?}", int_point);
    println!("float_point: {:?}", float_point);
}
```

**Output**
```
int_point: Point { x: 1, y: 2 }
float_point: Point { x: 1.1, y: 2.2 }
```

## Generic Function in Rust

We can also create functions with generic types as parameter(s).

Here is the syntax of a generic function.

```rust
// generic function with single generic type
fn my_function<T>(x: T, y: T) -> T {
    // function body
    // do something with `x` and `y`
}

// generic function with multiple generic types
fn my_function<T, U>(x: T, y: U) {
    // function body
    // do something with `x` and `y`
}
```

Here, `<T>` in the function definition signifies a generic function over type `T`. Similarly, `<T, U>` signifies a generic function over type `T` and `U`.

### Example: Generic Function in Rust

```rust
fn main() {
    // generic function to find minimum between two inputs
    fn min<T: PartialOrd>(a: T, b: T) -> T {
        if a < b {
            return a;
        } else {
            return b;
        }
    }

    // call generic function with integer type as parameters    
    let result1 = min(2, 7);

    // call generic function with float type as parameters
    let result2 = min(2.1, 1.1);
    
    println!("Result1 = {}", result1);
    println!("Result2 = {}", result2);
}
```

**Output**
```
Result1 = 2
Result2 = 1.1
```

In this example, we create a function `min()` with generic type arguments `a: T` and `b: T`. The type parameter `T` is declared with the syntax `<T: PartialOrd>`, which means that `T` can be any type that implements the `PartialOrd` trait.

The `PartialOrd` trait provides methods for comparing values of a type, such as `<` and `>`. This feature of Rust is called Trait bounds. If we don't use `<T: PartialOrder>`, Rust will throw a compile error: `` error[E0369]: binary operation `<` cannot be applied to type `T` ``

Thus, we should restrict the parameter `T` to `PartialOrd` from the `std::cmp` module.

# Rust Trait

A Rust trait defines shared functionality for multiple types. Rust traits promote type-safety, prevent errors at compile time, and act like interfaces in other languages with some distinctions.

## Defining a Trait in Rust

We can define a Rust trait using the `trait` keyword followed by the trait name and the methods that are part of the trait. Let's look at the syntax of a trait.

```rust
trait TraitName {
    fn method_one(&self, [arguments: argument_type]) -> return_type;
    fn method_two(&mut self, [arguments: argument_type]) -> return_type;
    ...
}
```

- `TraitName` - name of the trait.
- `method_one()` and `method_two()` - names of the methods in the trait.
- `&self` and `&mut self` - references to the self value. A method can take either a mutable or immutable reference to the current object, depending on whether it needs to modify its value.
- `[arguments: argument_type]` (optional) - list of arguments, where each argument has a name and a type.
- `return_type` - type that method returns.

Now, let's define a trait.

```rust
trait MyTrait {
    fn method_one(&self);
    fn method_two(&mut self, arg: i32) -> bool;
}
```

Here, we declare a trait called `MyTrait` with method signatures for `method_one(&self)` and `method_two(&mut self, arg: i32) -> bool`. The method signatures describe the behaviors of the types that implement this trait.

A trait can have multiple method signatures in its body, one per line. Traits by default do nothing and only are definitions. In order to use a trait, a type needs to implement it.


## Implementing a Trait in Rust

To implement a trait, we use the `impl` keyword. The syntax for the implementation (impl) block is:

```rust
impl TraitName for TypeName {
    fn method_one(&self, [arguments: argument_type]) -> return_type {
        // implementation for method_one
    }

    fn method_two(&mut self, [arguments: argument_type]) -> return_type {
        // implementation for method_two
    }

    ...
}
```

Here, `TraitName` is the name of the trait being implemented and `TypeName` is the name of the type that is implementing the trait.

> **Note:** The implementation of a trait must have the same signature as the methods in the trait, including the name, the argument types, and the return type.

Now, let's implement the trait. We will use the `MyTrait` as the trait and `MyStruct` as the type for which we implement the trait.

```rust
trait MyTrait {
    // method signatures
    fn method_one(&self);
    fn method_two(&mut self, arg: i32) -> bool;
}

struct MyStruct {
    value: i32,
}

impl MyTrait for MyStruct {
    // implementation of method_one
    fn method_one(&self) {
        println!("The value is: {}", self.value);
    }

    // implementation of method_two
    fn method_two(&mut self, arg: i32) -> bool {
        if arg > 0 {
            self.value += arg;
            return true;
        } else {
            return false;
        }
    }
}
```

In this example,
- `method_one()` takes a reference to self and prints its value `self.value` field.
- `method_two()` takes a mutable reference to self and an argument `arg` of type `i32`. If `arg` is greater than zero, we add `arg` to the value field and return `true`, otherwise we return `false`.

### Example: Defining, Implementing and Using a Trait in Rust

```rust
// Define a trait Printable
trait Printable {
    fn print(&self);
}

// Define a struct to implement a trait
struct Person {
    name: String,
    age: u32,
}

// Implement trait Printable on struct Person
impl Printable for Person {
    fn print(&self) {
        println!("Person {{ name: {}, age: {} }}", self.name, self.age);
    }
}

// Define another struct to implement a trait
struct Car {
    make: String,
    model: String,
}

// Define trait Printable on struct Car
impl Printable for Car {
    fn print(&self) {
        println!("Car {{ make: {}, model: {} }}", self.make, self.model);
    }
}

// Utility function to print any object that implements the Printable trait
fn print_thing<T: Printable>(thing: &T) {
    thing.print();
}

fn main() {
    // Instantiate Person and Car
    let person = Person { name: "Hari".to_string(), age: 31 };
    let car = Car { make: "Tesla".to_string(), model: "Model X".to_string() };
    
    // Call print_thing with reference of Person and Car
    print_thing(&person);
    print_thing(&car);
}
```

**Output**
```
Person { name: Hari, age: 31 }
Car { make: Tesla, model: Model X }
```

In this example, we define a `Printable` trait and implement it for two structs: `Person` and `Car`. The `Printable` trait requires the method name `print` for implementers.

In the `main()` function, we instantiate `Person` and `Car`, and pass it to the `print_thing()` function. The `print_thing` is a generic function that can accept reference to any object that implements the `Printable` trait.

To learn more about generics in Rust, visit [_Rust Generics_](https://www.programiz.com/rust/generics).