---
tags: rust, type_cast, if, loop, array, slice, tuple, struct, variable_scope, closure
---
<a href="https://www.programiz.com/rust"> Reference: Programiz </a>

# Rust Type Casting

Type casting allows us to convert variables of one data type to another. In Rust, we use the `as` keyword to perform type casting. For example,
```rust
// create a floating-point variable
let decimal: f64 = 54.321;

// convert floating point type to integer type
let integer = decimal as u16;
```

Here, `decimal as u16;` expression converts `f64` floating-point type to `u16` integer type.

## Type Conversion: Character to Integer in Rust
```rust
fn main() {
    let character: char = 'A';

    // convert char type to u8 integer type
    let integer = char as u8;

    println!("character = {}", character);
    println!("integer = {}", integer);
}
```

## Type Conversion: Integer to Character in Rust

We can also convert integer type to a character type. For example,
```rust
fn main() {
    // only u8 integer data type can be converted into char
    let integer: u8 = 65;
  
    // convert integer to char using the as keyword
    let character = integer as char;

    println!("integer = {}" , integer);
    println!("character = {}", character);
}
```

### Error while Converting Integer to Character
es will be ready by tomorrow and text you when it is ready.
Please contact me again if you haven't received any message by tomorrow, sir. 
You can call me if you think it is more convenient for you.

This is my phone number 
010-7211-6113
We are only allowed to use `u8` integers while performing type casting between integer and character. If we use any other integer type and convert it to a character, we will get an error. For example,
```rust
fn main() {
    let integer: i32 = 65;
  
    // convert integer to char using the as keyword
    let character = integer as char;

    println!("integer = {}" , integer);
    println!("character = {}", character);
}
```
## Type Casting: Boolean to Integer in Rust

```rust
fn main() {
    let boolean1: bool = false;
    let boolean2: bool = true;
  
    // convert boolean type to integer
    let integer1 = boolean1 as i32;
    let integer2 = boolean2 as i32;

    println!("boolean1 = {}", boolean1);
    println!("boolean1 = {}", boolean2);
    println!("integer1 = {}", integer1);
    println!("integer2 = {}", integer2);
}
```

# Rust if Expression

An `if` expression executes the code block only if the condition is `true`. The syntax of the `if` expression in Rust is:

```rust
if condition {
    // code block to execute
}
```
If the **condition** evaluates to
- `true` - the code inside the `if` block is executed
- `false` - the code inside of the if block is not executed

## If .. else
The syntax for the `if..else` expression in Rust is:
```rust
if condition {
    // executes when condition is true
} else {
    // executes when condition is false
}
```

```rust
if condition1 {
    // code block 1
} else if condition2 {
    // code block 2
} else {
    // code block 3
}
```

# Rust Loop

```rust
fn main() {
    let mut number = 0;
    
    // infinite loop starts here
    loop {
        number += 1;
        println!("{}", number);
        
        if number >= 10 {
            // exit the loop
            break;
        }
    }
}
```

## While Loop

```rust
fn main() {
    let mut counter = 1;

    // usage of while loop
    while counter < 6 {
        println!("{}", counter);
        
        counter += 1;
    }
}
```

## For Loop

```rust
fn main() {
    // usage of for loop
    for i in 1..6 {
        println!("{}", i);
    }
}
```

## Continue / Break 

```rust
fn main() {
    let mut number = 0;

    loop {
        number += 1;

        // condition to skip the iteration
        if number == 3 {
            continue;
        }
        
        // condition to exit the loop
        if number > 5 {
            break;
        }
        
        println!("{}", number);
    }
}
```

# Rust Array

```rust
// array of natural numbers
let arr = [1, 2, 3, 4, 5];
```

```rust
fn main() {
    // initialization of array with data type
    let numbers: [i32; 5] = [1, 2, 3, 4, 5];
    
    println!("Array of numbers = {:?}", numbers);

	let numbers: [i32; 5] = [1, 2, 3, 4, 5];
}
```

## Array with Default Values in Rust

```rust
fn main() {
    // initialization of array with default values
    let numbers: [i32; 5] = [3; 5];
    
    println!("Array of numbers = {:?}", numbers);
}
```

## Access Elements of Rust Array

Each element in an array is associated with a unique sequence of numbers. This number is known as the **array index**.
```rust
fn main() {
    let colors = ["red", "green", "blue"];
    
    // accessing element at index 0
    println!("1st Color: {}", colors[0]);

    // accessing element at index 1
    println!("2nd Color: {}", colors[1]);

    // accessing element at index 2
    println!("3rd Color: {}", colors[2]);
}
```


## Mutable Array in Rust

In Rust, an array is immutable, which means we cannot change its elements once it is created. However, we can create a mutable array by using the `mut` keyword before assigning it to a variable. For example,
```rust
fn main() {
    let mut numbers: [i32; 5] = [1, 2, 3, 4, 5];
    
    println!("original array = {:?}", array);
    
    // change the value of the 3rd element in the array
    numbers[2] = 0;
    
    println!("changed array = {:?}", numbers);
}
```

# Rust Slice

A Rust slice is a data type used to access portions of data stored in collections like arrays, vectors and strings. Suppose we have an array,
```rust
let numbers = [1, 2, 3, 4, 5];
```

Now, if we want to extract the **2nd** and **3rd** elements of this array. We can slice the array like this,

```rust
let slice = &array[1..3];
```

Here, let's look at the right-hand side of the expression,
- `&numbers` - specifies a reference to the variable `numbers` (not the actual value)
- `[1..3]` - is a notation for slicing the array from **start_index** `1` (inclusive) to **end_index** `3` (exclusive)

## Mutable Slice in Rust

We can create a mutable slice by using the `&mut` keyword.
```rust
let numbers = [1, 2, 3, 4, 5];
let slice = &mut numbers[1..4];
```

Once the slice is marked as mutable, we can change values inside the slice. Let's see an example,
```rust
fn main() {
    // mutable array
    let mut colors = ["red", "green", "yellow", "white"];
    
    println!("array = {:?}", colors);

    // mutable slice
    let sliced_colors = &mut colors[1..3];
    
    println!("original slice = {:?}", sliced_colors);

    // change the value of the original slice at the first index
    sliced_colors[1] = "purple";

    println!("changed slice = {:?}", sliced_colors);
}
```

# Rust Tuple

A tuple in Rust allows us to store values of different data types. For example,
```rust
let tuple = ('Hello', 5, 3.14);
```
Here, we have used the small bracket `( )` to create a tuple and it is able to store a string value, `Hello`, an integer value, `5`, and a floating-point value `3.14` together.

```rust
fn main() {
    // initialization of tuple without data type
    let tuple = ("Rust", "fun", 100);

    println!("Tuple contents = {:?}", tuple);
}
```

```rust
fn main() {
    let random_tuple = ("Hello", 200, 3.14);

    // accessing tuple element at index 0
    println!("Value at Index 0 = {}", random_tuple.0);
    
    // accessing tuple element at index 1
    println!("Value at Index 1 = {}", random_tuple.1);
    
    // accessing tuple element at index 2
    println!("Value at Index 2 = {}", random_tuple.2);
}
```

## Destructuring  a Tuple
```rust
fn main() {
    let mixture = ("Hello, World!", 16, 2.71828);
    
    // destructuring a tuple
    let (message, number, float) = mixture;
    
    println!("message = {}", message);
    println!("number = {}", number);
    println!("float = {}", float);
}
```

# Rust Struct

Rust structs or structures are user-defined data types used to store different types of data together. 

```rust
struct Person {
    name: String,
    age: u8,
    height: u8
}


```


## Instantiating Rust Struct
```rust
let person1 = Person {
    name: String::from("John Doe"),
    age: 18,
    height: 178
};
```

# Rust Variable Scope

In computer programming, a variable's scope defines the region in which the variable is available for use. For example,

```rust
fn main() {
    // this variable has scope inside the main function block
    let age = 31;
    …
}
```

Here, the age variable has scope inside the body `{...}` of the `main()` function,

## Variable Shadowing in Rust
In Rust, when a variable declared within a particular scope has the same name as a variable declared in the outer scope, it is known as **variable shadowing**. We can use the same variable name in different scope blocks in the same program.

Let's take a look at an example,
```rust
fn main() {
    let random = 100;

    // start of the inner block
    {
        println!("random variable before shadowing in inner block = {}", random);

        // this declaration shadows the outer random variable
        let random = "abc";

        println!("random after shadowing in inner block = {}", random);
    }
    // end of the inner block

    println!("random variable in outer block = {}", random);
}
```

Output:
```
random variable before shadowing in inner block = 100
random after shadowing in inner block = abc
random variable in outer block = 100
```

## Variable Freezing in Rust

We can freeze a variable in Rust by using shadowing and immutability. Once a variable is frozen, we cannot change the variable value in the inner scope.
Let's see an example.
```rust
fn main() {
    let mut age = 1;

    // start of the inner block
    {
        // shadowing by immutable age variable
        let age = age;

        // error, age variable is frozen in this scope
        age = 2;

        println!("age variable inner block = {}", age);
        // age variable goes out of scope
    }
    // end of the inner block

    // age variable is not frozen in outer block
    age = 3;

    println!("integer variable outer block = {}", age);
}
```

In doing this, we are shadowing the mutable `age` variable with an immutable variable named `age`. Now the _age variable freezes inside the inner block_ because the inner age variable is pointing to the same value as the age variable in the outer block. Thus, we cannot change the value of age inside the inner block and encounter an error. Once we get out of the inner block, the value of age can be changed. Let's look at the working version of the variable freezing example.

# Rust Closure

In this tutorial, you will learn about closures in Rust with the help of examples.

In Rust, closures are functions without names. They are also known as anonymous functions or lambdas.

## Defining a Closure in Rust

Here's how we create a closure in Rust,
```rust
// define a closure to print a text
let print_text = || println!("Defining Closure");
```
In the above example, we have created a closure that prints the text "**Defining Closure**". Here,
- `print_text` - variable to store the closure
- `||` - start of a closure
- `println!("Defining Closure")` - body of the closure

## Calling Closure

Once a closure is defined, we need to call it just like calling a function. To call a closure, we use the variable name to which the closure is assigned. For example,

```rust
// define a closure to print a text
let print_text = || println!("Defining Closure");

// call the closure
print_text();
```

## Rust Closure with Parameters

In Rust, we can also pass parameters to a closure. For example,
```rust
// define closure to add 1 to an integer
let add_one = |x: i32| x + 1;
```

Here,
- `let add_one` - is the name of the variable to store the the closure
- `|x: i32|` - is the parameter and its type that we pass to the closure
- `x + 1;` - is the body of the closure which returns `x + 1`

If we create a closure with parameters, we need to also pass the value while calling the closure.
```rust
// call the closure with value 2
add_one(2);
```

## Multi-line Closure in Rust

We can also include multiple statements inside a closure. In this case, we enclose those statements using curly braces `{}`. Let's look at an example.
```rust
fn main() {
    // define a multi-line closure
    let squared_sum = |x: i32, y: i32| {
    
        // find the sum of two parameters
        let mut sum: i32 = x + y;
        
        // find the squared value of the sum
        let mut result: i32 = sum * sum;
        
        return result;
    };
    
    // call the closure
    let result = squared_sum(5, 3);
    
    println!("Result = {}", result);
}
```

## Closure Environment Capturing in Rust

Closure has a unique feature that allows it to capture the environment. This means the closure can use the values in its scope. For example,
```rust
fn main() {
    let num = 100;
    
    // A closure that captures the num variable
    let print_num = || println!("Number = {}", num);
    
    print_num(); 
}
```

## Closure Environment Capturing Modes in Rust

Environment capturing of closures can be of 3 different modes based on the variable and the closure definition.

1. Variable is not modified inside closure
2. Variable is modified inside closure
3. Variable is moved inside closure

Let's look at each of these modes of environment capturing.

**1. Variable is not modified inside closure**
```rust
fn main() {
    let word = String::from("Hello");
    
    // immutable closure
    let print_str = || {
        println!("word = {}", word);
    };

    // immutable borrow is possible outside the closure
    println!("length of word = {}", word.len());
    
    print_str();
}
```
Here, the variable word is not modified inside the closure print_str. As the variable is immutable by default, we can make any number of immutable references of word inside the closure. Notice that the closure variable print_str is also immutable.

This mode of capture is also known as **Capture by Immutable Borrow**.

**2. Variable is modified inside closure**
```rust
fn main() {
    let mut word = String::from("Hello");
    
    // mutable closure
    let mut print_str = || {
        // value of word is changed here
        word.push_str(" World!");
        println!("word = {}", word);
    };
     
     // cannot immutable borrow because the variable is borrowed as mutable inside the closure
     // println!("length of word = {}", word.len());
    
    print_str();

    // can immutable borrow because the closure has been already used
    println!("length of word = {}", word.len());
}
```

**Output:**
```
word = Hello World!
length of word = 12
```

Here, the variable word is modified inside the closure print_str with `word.push_str("World!");`. Thus, we have to make the variable word mutable as well as the closure variable `print_str`. This means no other references of the word variable can exist unless the closure is used.

This mode of capture is also known as **Capture by Mutable Borrow**.

**3. Variable is moved inside closure**

```rust
fn main() {
    let word = String::from("Hello");

    // immutable closure
    let print_str = || {
        // word variable is moved to a new variable
        let new_word = word;
        println!("word = {}", new_word);
    };

    print_str();

    // cannot immutable borrow because word variable has moved inside closure
    // println!("length of word = {}", word.len());
}
```

**Output**
```
word = Hello
```

Here, we move the variable word to a new variable `new_word` inside the closure. As the variable is moved, we cannot use it anywhere else except for inside the closure.

This mode of capture is also known as **Capture by Move**.

