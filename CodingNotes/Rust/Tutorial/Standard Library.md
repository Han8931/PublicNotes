---
tags: rust, stack, heap, vector, string, hashmap, hashset, iterator, hash
---
# Rust Stack and Heap

_Stack and Heap are parts of memory available to our Rust code to use at runtime_. Rust is a memory-safe programming language. To ensure that Rust is memory-safe, it introduces concepts like **ownership, references and borrowing**. To understand these concepts, we must first understand how to allocate and deallocate memory into the _Stack and Heap_.

## The Stack

The Stack can be thought of as a stack of books. When we add more books, we add them on the top of the pile. When we need a book, we take one from the top.

The stack inserts values in order. It gets them and removes the values in the opposite order.
- Adding data is called **pushing onto the stack**
- Removing data is called **popping off the stack**

This phenomenon is called **Last In, First Out (LIFO)** in programming. Data stored on the stack must have a fixed size during compile time. Rust, by default, allocates memory on the stack for primitive types. Let's visualize how memory is allocated and deallocated on the stack with an example.

```rust
fn foo() {
    let y = 999;
    let z = 333;
}

fn main() {
    let x = 111;
    foo();
}
```

In the above example, we first call the function `main()`. The `main()` function has one variable binding `x`.  When `main()` executes, we allocate a single 32-bit integer (`x`) to the stack frame.

|Address|Name|Value|
|---|---|---|
|0|x|111|

In the table, the **"Address"** column refers to the memory address of the RAM. It starts from **0** and goes to how much RAM (number of bytes) your computer has. The **"Name"** column refers to the variable, and the **"Value"** column refers to the variable's value.

When `foo()` is called a new stack frame is allocated. The `foo()` function has two variable bindings, `y` and `z`.

|Address|Name|Value|
|---|---|---|
|2|z|333|
|1|y|999|
|0|x|111|

The numbers **0**, **1**, and **2** do not use address values the computer will use in reality. In reality, the addresses are separated by some number of bytes based on the value.

After `foo()` is completed, its stack frame is deallocated.

|Address|Name|Value|
|---|---|---|
|0|x|111|

Finally, `main()` is completed, and everything goes away. Rust automatically does allocation and deallocation of memory in and out of the stack.

## The Heap

As opposed to the stack, most of the time, we will need to pass variables (memory) to different functions and keep them alive for longer than a single function's execution. This is when we can use the heap.

We can allocate memory on the heap using the `Box<T>` type. For example,
```rust
fn main() {
    let x = Box::new(100);
    let y = 222;
    
    println!("x = {}, y = {}", x, y);
}
```

**Output:**
```
x = 100, y = 222
```

Let's visualize the memory when `main()` is called in the above example.

|Address|Name|Value|
|---|---|---|
|1|y|222|
|0|x|???|

Like before, we allocate two variables, `x` and `y`, on the stack. However, the value of `x` is allocated on the heap when `Box::new()` is called. Thus, the actual value of `x` is a _pointer to the heap_. The memory now looks like this:

|Address|Name|Value|
|---|---|---|
|5678||100|
|…|…|…|
|1|y|222|
|0|x|→ 5678|

Here, the variable `x` holds a pointer to the address **→ 5678**, an arbitrary address used for demonstration. Heap can be allocated and freed in any order. Thus it can end up with different addresses and create holes between addresses.

So when `x` goes away, it first frees the memory allocated on the heap.

|Address|Name|Value|
|---|---|---|
|1|y|222|
|0|x|???|

Once the `main()` is completed, we free the stack frame, and everything goes away, freeing all the memory.

We can make the memory live longer by transferring ownership where the heap can stay alive longer than the function which allocates the `Box`. To learn more about ownership, visit [_Rust Ownership_](https://www.programiz.com/rust/ownership).

## Differences between Stack and Heap

|Stack|Heap|
|---|---|
|Accessing data in the stack is faster.|Accessing data in a heap is slower.|
|Managing memory in the stack is predictable and trivial.|Managing memory for the heap (arbitrary size) is non-trivial.|
|Rust stack allocates by default.|`Box` is used to allocate to the heap.|
|Primitive types and local variables of a function are allocated on the stack.|Data types that are dynamic in size, such as `String`, `Vector`, `Box`, etc., are allocated on the heap.|

# Rust Vector

Vector is a dynamic (resizable) data structure that can store a list of elements of the same type. Being a resizable data structure, vectors can grow and shrink at runtime.

## Create a Vector in Rust

In Rust, we can create a vector using the `vec!` macro. For example,
```rust
let v = vec![1, 2, 3];
```

Here, we are creating a vector using the `vec!` macro with some initial values.
- `let v` - the name of the variable
- `vec![1, 2, 3]` - initialize a vector with integer values **1**, **2**, **3**

By looking at the type of the values provided to the macro, Rust will automatically set the vector type. For example, the vector type of the above vector is `Vec<i32>`.

We can also define the vector type ourselves using the `vec!` macro.

```rust
let v: Vec<u8> = vec![1, 2, 3];
```

Here, we are creating a vector with type `u8`, which has elements **1**, **2** and **3**.
```rust
fn main() {    
    // vector creation with vec! macro
    let v = vec![1, 2, 3];
    
    println!("v = {:?}", v);
}
```

## Accessing Elements of a Vector in Rust

Each element in a vector is associated with a unique sequence of numbers. This number is known as the **vector index**. We can access elements of a vector using the vector index. Suppose we have a vector of colors.

```rust
fn main() {
    let colors = vec!["blue", "red", "green"];
    
    // method 1: access vector elements using vector index
    println!("first color = {}", colors[0]);
    println!("second color = {}", colors[1]);
    println!("third color = {}", colors[2]);
}
```


## Accessing Elements of a Vector using the get() method in Rust

We can also access the element of the vector with the `get()` method and the index of the element. Suppose we have a vector of colors:

```rust
let colors = vec!["blue", "red", "green"];
```

We can access the elements of this vector using `get()`. The `get()` method does not directly return the vector element but an enum with type `Option<T>`. The result is either a `Some(T)` or `None`.

- `colors.get(0)` - returns `Some` value at **index 0**
- `colors.get(1)` - returns `Some` value at **index 1**
- `colors.get(2)` - returns `Some` value at **index 2**

The advantage of using the `get()` method over just using the vector index to access the element directly is that it will not error if the vector index is out of range. Suppose we go out of the vector index range; then `get()` will return `None`. For example,

`colors.get(3)` will return `None`

```rust
fn main() {
    let colors = vec!["blue", "red", "green"];
    
    // method 2: access vector elements using get() method and vector index
    println!("first color = {:?}", colors.get(0));
    println!("second color = {:?}", colors.get(1));
    println!("third color = {:?}", colors.get(2));
}
```

Output:
```
first color = Some("blue")
second color = Some("red")
third color = Some("green")
```

As we can see, the output returns a value `Some("blue")`, `Some("red")` and `Some("green")` of the `Option<T>` type. To get the exact value from the `Option<T>` type, we need to unwrap the value. To learn about unwrap, visit [_Rust unwrap() and expect()_](https://www.programiz.com/rust/unwrap-and-expect).

## Adding Values to a Vector in Rust

We can add values to a Vector by creating a mutable vector in Rust. We can use the `mut` keyword before assigning a vector to a variable to make it mutable. For example,

```rust
// mutable vector
let mut v = vec![2, 4, 6, 8, 10];
```

We can add values to this vector using the `push()` method. Let's look at an example.

```rust
fn main() {
    let mut even_numbers = vec![2, 4, 6, 8, 10];
    
    println!("original vector = {:?}", v);
    
    // push values at the end of the vector
    even_numbers.push(12);
    even_numbers.push(14);
    
    println!("changed vector = {:?}", v);
}
```

**Output:**
```
original vector = [2, 4, 6, 8, 10]
changed vector = [2, 4, 6, 8, 10, 12, 14]
```

Here, we push values to the vector with the `push()` method. It is only possible because the variable holding the vector `even_numbers` is mutable.

```rust
even_numbers.push(12);
even_numbers.push(14);
```

As a result, the final vector includes **12** and **14** with the default elements.

## Removing Values from a Vector in Rust

We can remove values from a vector by making it mutable and with the `remove()` method. For example,

```rust
fn main() {
    let mut even_numbers = vec![2, 4, 6, 8, 10];
    
    println!("original vector = {:?}", even_numbers);
    
    // remove value from the vector in its second index
    even_numbers.remove(2);
    
    println!("changed vector = {:?}", even_numbers);
}
```

**Output:**
```
original vector = [2, 4, 6, 8, 10]
changed vector = [2, 4, 8, 10]
```
Here, we remove the value in the second index with the `even_numbers.remove(2)` method. Thus, the final result does not include the value **6** in the vector.

> **Note:** Removing an element will shift all other values in the vector by one (**-1** index).

## Looping Through a Vector in Rust

We can use the `for..in` loop to iterate through a vector. For example,

```rust
fn main() {
    let colors = vec!["blue", "red", "green"];
    
    // loop through a vector to print its index and value
    for index in 0..3 {
        println!("Index: {} -- Value: {}", index, colors[index]);
    }
}
```

**Output:**
```
Index: 0 -- Value: blue
Index: 1 -- Value: red
Index: 2 -- Value: green
```

## Creating a Vector using `Vec::new()` Method

Alternatively, we can create an empty vector using the `Vec::new()` method. For example,

```rust
let v: Vec<i32> = Vec::new();
```

Here, we are creating an empty vector to hold values of type `i32`.
- `let v` - the name of the variable
- `Vec<i32>` - type of the vector, where `i32` is the data type of all elements in the vector
- `Vec::new()` - initialize an empty vector with the `new()` method

### Example: Creating a Vector using Vec::new()
```rust
fn main() {
    // vector creation with Vec::new() method
    let mut v: Vec<i32> = Vec::new();

    // push values to a mutable vector
    v.push(10);
    v.push(20);

    println!("v = {:?}", v);
}
```

**Output:**
```
v = [10, 20]
```

Here, we create a mutable vector with `Vec::new()` and push values to it using the `push()` method of the vector.

# Rust String

A string in Rust is a sequence of Unicode characters encoded in UTF-8. For example, `"Rust Programming"` is a string in which each character is a valid Unicode character. i.e. `"R"`, `"u"`, `"s"`, `"t"`, `" "`, and so on.

#### String vs String Literal

The difference boils down to Rust's type inference.
```rust
// owned String, heap allocated
let x = String::from("Hi");

//  reference to string literal hardcoded in binary, 'static &str
let x = "Hi";
```

There is a lot of ergonomics talking going around about this theme, since the different types of string are not immediately obvious to newcomers.

## Creating a String in Rust

We can create a string with a default value using the `String::from()` method. For example,

```rust
// create a string with a default value
let word = String::from("Hello, World!");
```

Here, we create a new string and assign it to the word variable. We also provide a default value of `"Hello, World!"`.

> **Note:** A string is allocated in **heap memory and is dynamic (resizable) in size. Hence, the size of string is unknown at compile time.**

## Mutable String in Rust

We can create a mutable string in Rust by using the `mut` keyword before assigning a string to a variable. For example,

```rust
// mutable string
let mut word = String::from("cat");
```

We can make changes to this string. Let's look at an example,

```rust
fn main() {
    let mut word = String::from("cat");
    
    println!("original string = {}", word);
    
    // push a new string at the end of the initial string 
    word.push_str(" dog");
    
    println!("changed string = {}", word);
}
```

## String Slicing in Rust

We can slice a string in Rust to reference a part of the string. String slicing allows us to reference a part (portion) of a string. For example,

```rust
fn main() {
    let word = String::from("Hello, World!");

    // slicing a string
    let slice = &word[0..5];

    println!("string = {}", word);
    println!("slice = {}", slice);
}
```
Here, `&word[0..5]` is a notation for slicing the string stored in variable `word` from start index **0** (inclusive) to end index **5** (exclusive). The `&` (ampersand) in the slicing syntax signifies that it is a string reference. It is not actual data. Slicing is also used to access portions of data stored in arrays and vectors. To learn about Slice in Rust, visit [Rust Slice](https://www.programiz.com/rust/slice).


## Iterating over Strings

We can use the `chars()` method of the string type to iterate over a string. For example,

```rust
fn main() {
    let str = String::from("Hello");
    
    // Loop through each character in a string using chars() method
    for char in str.chars() {
        println!("{}", char);
    }
}
```

Here, we iterate through all the characters using the `chars()` method and print each of them.

## Creating an Empty String with String::new()

We can create an empty string, using the `String::new()` method. For example,

```rust
// create an empty string
let mut word = String::new();
```

We can then append a string to the word variable using the `push_str()` method.

```rust
word.push_str("Hello, World!");
```

Here, we push the string `"Hello, World!"` to the empty string variable word.

# Rust HashMap

The Rust HashMap data structure allows us to store data in **key-value pairs**. Here are some of the features of hashmap:
- Each value is associated with a corresponding key.
- Keys are unique, whereas values can duplicate.
- Values can be accessed using their corresponding keys.

## HashMap Operations

### Creating a HashMap in Rust

HashMap is part of the Rust standard collections library, so we must include the `HashMap` module in our program to use it.

```rust
use std::collections::HashMap;
```

We can import the `HashMap` module using the `use` declaration. It should be at the top of the program. Now, we can create a hashmap using the `new()` method in the `HashMap` module. For example,

```rust
let mut info: HashMap<i32, String> = HashMap::new();
```

Here,
- `let mut info` - declares a mutable variable `info`
- `HashMap<i32, String>` - type of the HashMap where the key is a Integer and the value is a String
- `HashMap::new()` - creates a new HashMap

```rust
// import HashMap from Rust standard collections library
use std::collections::HashMap;

fn main() {
    // create a new HashMap
    let mut info: HashMap<i32, String> = HashMap::new();
    
    println!("HashMap = {:?}", info);
}
```

**Output:**
```
HashMap = {}
```

### Add Elements to a HashMap in Rust

We can use the `insert()` to add an element (key-value pairs) to a hashmap. For example,
```rust
let mut fruits: HashMap<i32, String> = HashMap::new();

// insert elements to hashmap
fruits.insert(1, String::from("Apple"));
fruits.insert(2, String::from("Banana"));
```
Here, we insert two key-value pairs in the `HashMap` bound to the variable `fruits`. The `String::from()` method here creates a value of `String` type.

> **Note:** Adding a new key-value to the HashMap is only possible because of the `mut` variable declaration.

#### Example: Add Elements to a HashMap

```rust
use std::collections::HashMap;

fn main() {
    let mut fruits: HashMap<i32, String> = HashMap::new();
    
    // add key-value in a hashmap
    fruits.insert(1, String::from("Apple"));
    fruits.insert(2, String::from("Banana"));
    
    println!("fruits = {:?}", fruits);
}
```

**Output:**
```
fruits = {1: "Apple", 2: "Banana"}
```

### Access Values in a HashMap in Rust

We can use the `get()` to access a value from the given hashmap. For example,

```rust
let mut fruits: HashMap<i32, String> = HashMap::new();

fruits.insert(1, String::from("Apple"));
fruits.insert(2, String::from("Banana"));

let first_fruit = fruits.get(&1);
```

Here, we get a value out of the hashmap using the key `&1` and the `get()` method. We use the ampersand(`&`) and the key (`&1`) as the argument because `get()` returns us a reference of the value. It is not the actual value in the HashMap.

#### Example: Access Values in a HashMap

```rust
use std::collections::HashMap;

fn main() {
    let mut fruits: HashMap<i32, String> = HashMap::new();
    
    // insert elements in a hashmap
    fruits.insert(1, String::from("Apple"));
    fruits.insert(2, String::from("Banana"));
    
    // access values in a hashmap
    let first_fruit = fruits.get(&1);
    let second_fruit = fruits.get(&2);
    let third_fruit = fruits.get(&3);
    
    println!("first fruit = {:?}", first_fruit);
    println!("second fruit = {:?}", second_fruit);
    println!("third fruit = {:?}", third_fruit);
}
```

**Output:**
```
first fruit = Some("Apple")
second fruit = Some("Banana")
third fruit = None
```

Notice that we use the ampersand(`&`) and the key (`&1`, `&2`) as an argument to the `get()` method.
```rust
let first_fruit = fruits.get(&1);
let second_fruit = fruits.get(&2); 
```

The output of the `get()` method is an `Option` enum which means that if the key passed as an argument matches, it returns `Some` value, and if it doesn't, it returns `None`.

In the above example, `let third_fruit = fruits.get(&3)` returns `None` because the key `&3` doesn't match anything that's in the hashmap.

### Remove Elements from a HashMap in Rust

We can remove elements from a hashmap by providing a key to the `remove()` method. For example,
```rust
let mut fruits: HashMap<i32, String> = HashMap::new();

fruits.insert(1, String::from("Apple"));
fruits.insert(2, String::from("Banana"));

fruits.remove(&1);
```

Here, we remove a value from the hashmap using the key and the `remove()` method.

#### Example: Remove Elements in a HashMap

```rust
use std::collections::HashMap;

fn main() {
    let mut fruits: HashMap<i32, String> = HashMap::new();
    
    // insert values in a hashmap
    fruits.insert(1, String::from("Apple"));
    fruits.insert(2, String::from("Banana"));
    
    println!("fruits before remove operation = {:?}", fruits);

    // remove value in a hashmap
    fruits.remove(&1);
    
    println!("fruits after remove operation = {:?}", fruits);
}
```

**Output:**
```
fruits before remove operation = {1: "Apple", 2: "Banana"}
fruits after remove operation = {2: "Banana"}
```

Here, we remove an element in the hashmap with key `&1` using the `remove()` method.

### Change Elements of a HashMap in Rust

We can change/update elements of a hashmap by using the `insert()` method. For example,
```rust
let mut fruits: HashMap<i32, String> = HashMap::new();

// insert values in the hashmap
fruits.insert(1, String::from("Apple"));
fruits.insert(2, String::from("Banana"));

// update the value of the element with key 1
fruits.insert(1, String::from("Mango"));
```

Here, the final insert expression updates the initial value of the element with the key of **1**.

#### Example: Change Elements of a HashMap
```rust
use std::collections::HashMap;

fn main() {
    let mut fruits: HashMap<i32, String> = HashMap::new();
    
    // insert values in a hashmap
    fruits.insert(1, String::from("Apple"));
    fruits.insert(2, String::from("Banana"));
    
    println!("Before update = {:?}", fruits);
    
    // change value of hashmap with key of 1
    fruits.insert(1, String::from("Mango"));
    
    println!("After update = {:?}", fruits);
}
```

**Output:**
```
Before update = {1: "Apple", 2: "Banana"}
After update = {1: "Mango", 2: "Banana"}
```

### Other Methods of Rust HashMap
```rust
use std::collections::HashMap;

fn main() {
    let mut fruits: HashMap<i32, String> = HashMap::new();
    
    fruits.insert(1, String::from("Apple"));
    fruits.insert(2, String::from("Banana"));
    
    // loop and print values of hashmap using values() method
    for fruit in fruits.values() {
        println!("{}", fruit)
    }
    
    // print the length of hashmap using len() method
    println!("Length of fruits = {}", fruits.len());
}
```

# Rust HashSet

HashSet implements the set data structure in Rust. Just like a set, it allows us to store values without duplicates.

## Creating a HashSet in Rust

Hashset is part of the Rust standard collections library, so we must include the `HashSet` module in our program.

```rust
use std::collections::HashSet;
```

We have imported the `HashSet` module using the `use` declaration. It should be at the top of the program. Now, we can create a hashset using the `new()` method of the `HashSet` module. For example,

```rust
let mut color: HashSet<String> = HashSet::new();
```

Here,
- `let mut color` - declares a mutable variable `color`
- `HashSet<String>` - type of the hashset where the values are of type `String`
- `HashSet::new()` - creates a new hashset

```rust
// import HashSet from Rust standard collections library
use std::collections::HashSet;

fn main() {
    // create a new HashSet
    let mut color: HashSet<String> = HashSet::new();
    
    println!("HashSet = {:?}", color);
}
```

## HashSet Operations

### Add Values to a HashSet in Rust

We can use the `insert()` method to add an element to the hashset. For example,
```rust
let mut colors: HashSet<&str> = HashSet::new();

// insert elements to hashset
colors.insert("Red");
colors.insert("Yellow");
```

#### Example: Add Values to a HashSet

```rust
use std::collections::HashSet;

fn main() {
    let mut colors: HashSet<&str> = HashSet::new();
    
    // insert values in a HashSet
    colors.insert("Red");
    colors.insert("Yellow");
    colors.insert("Green");

    println!("colors = {:?}", colors);
}
```

### Check Value is Present in a HashSet in Rust

We use the `contains()` method to check if a value is present in a hashset. The method returns true if the specified element is present in the hashset, otherwise returns false. Let's see an example,

```rust
use std::collections::HashSet;

fn main() {
    let mut colors: HashSet<&str> = HashSet::new();

    colors.insert("Red");
    colors.insert("Yellow");

    println!("colors = {:?}", colors);

    // check for a value in a HashSet
    if colors.contains("Red") {
        println!("We have the color \"Red\" in the HashSet.")
    }
}
```

### Remove Values from a HashSet in Rust

We can use the `remove()` method to remove the specified element from the hashset. For example,

```rust
use std::collections::HashSet;

fn main() {
    let mut colors: HashSet<&str> = HashSet::new();

    colors.insert("Red");
    colors.insert("Yellow");
    colors.insert("Green");

    println!("colors before remove operation = {:?}", colors);

    // remove value from a HashSet
    colors.remove("Yellow");
    
    println!("colors after remove operation = {:?}", colors);
}
```

### Iterate over Values of a HashSet in Rust

We can use the [Rust for Loop](https://www.programiz.com/rust/for-loop) to iterate over values of a hashset. For example,

```rust
use std::collections::HashSet;

fn main() {
    let mut colors: HashSet<&str> = HashSet::new();
    
    colors.insert("Red");
    colors.insert("Yellow");
    colors.insert("Green");

    // iterate over a hashset
    for color in colors {
        // print each value in the hashset
        println!("{}", color);
    }
}
```

### HashSet with Default Values in Rust

We can also create a hashset with default values using the `from()` method when creating it. For example,
```rust
use std::collections::HashSet;

fn main() {
    // Create HashSet with default set of values using from() method
    let numbers = HashSet::from([2, 7, 8, 10]);
    
    println!("numbers = {:?}", numbers);
}
```

## Set Operations

The HashSet module also provides various methods used to perform different set operations.

### Union of two Sets

We can use the `union()` method to find the union of two sets. For example,

```rust
use std::collections::HashSet;

fn main() {
    let hashset1 = HashSet::from([2, 7, 8]);
    let hashset2 = HashSet::from([1, 2, 7]);
    
    // Union of hashsets
    let result: HashSet<_> = hashset1.union(&hashset2).collect();
    
    println!("hashset1 = {:?}", hashset1);
    println!("hashset2 = {:?}", hashset2);
    println!("union = {:?}", result);
}
```

**Output:**
```
hashset1 = {7, 8, 2}
hashset2 = {2, 7, 1}
union = {2, 7, 8, 1}
```

Here, we have used the `union()` method to find the union between two sets: hashset1 and hashset2.

```
hashset1.union(&hashset2).collect();
```

The `union()` method returns an iterator, so we have used the `collect()` method to get the actual result.

> **Note:** We have passed `&hashset2` as an argument to the `union()` method because it takes a reference as an argument.

### Intersection of two Sets

We can use the `intersection()` method to find the intersection between two sets. For example,

```rust
use std::collections::HashSet;

fn main() {
    let hashset1 = HashSet::from([2, 7, 8]);
    let hashset2 = HashSet::from([1, 2, 7]);
    
    // Intersection of hashsets
    let result: HashSet<_> = hashset1.intersection(&hashset2).collect();
    
    println!("hashset1 = {:?}", hashset1);
    println!("hashset2 = {:?}", hashset2);
    println!("intersection = {:?}", result);
}
```

**Output:**
```
hashset1 = {2, 7, 8}
hashset2 = {2, 1, 7}
intersection = {7, 2}
```


### Difference between two Sets

We can use the `difference()` method to find the difference between two sets. For example,

```rust
use std::collections::HashSet;

fn main() {
    let hashset1 = HashSet::from([1, 2, 3, 4]);
    let hashset2 = HashSet::from([4, 3, 2, 6]);
    
    // Difference between hashsets
    let result: HashSet<_> = hashset1.difference(&hashset2).collect();
    let result2: HashSet<_> = hashset2.difference(&hashset1).collect();
    
    println!("hashset1 = {:?}", hashset1);
    println!("hashset2 = {:?}", hashset2);
    println!("difference = {:?}", result);
    println!("difference = {:?}", result2);
}
```

**Output:**
```
hashset1 = {3, 4, 1, 2}
hashset2 = {2, 4, 3, 6}
difference = {1}
difference = {6}
```


### Symmetric Difference between two Sets

We can use the `symmetric_difference()` method to find the symmetric difference between two sets. The symmetric difference returns values from both sets except the ones in both.

```rust
use std::collections::HashSet;

fn main() {
    let hashset1 = HashSet::from([2, 7, 8]);
    let hashset2 = HashSet::from([1, 2, 7, 9]);
    
    // Symmetric difference of hashsets
    let result: HashSet<_> = hashset1.symmetric_difference(&hashset2).collect();
    
    println!("hashset1 = {:?}", hashset1);
    println!("hashset2 = {:?}", hashset2);
    println!("symmetric difference = {:?}", result);
}
```

**Output:**
```
hashset1 = {8, 7, 2}
hashset2 = {2, 9, 1, 7}
symmetric difference = {8, 9, 1}
```

# Rust Iterators

An iterator in Rust is responsible for creating a sequence of values and allows us to iterate over each item of the sequence. It is primarily used for looping and we can only loop over iterators in Rust. Let's look at a simple example on how we can loop through an array.

```rust
let numbers = [2, 1, 17, 99, 34, 56];
```

Now, let's change the array to an iterable array by calling the `iter()` method. If a data structure has the `iter()` method, it is called iterable.

```rust
let numbers_iterator = numbers.iter();
```

Finally, we can loop through the values and print them out.

```rust
for number in numbers_iterator {
    println!("{}", number);
}
```

> **Note:** Collections like Array, Vector, HashMap and HashSet are not iterable by default. We can use the `iter()` method to tell Rust that it can be used to loop over the values.

### Example: Iterator in Rust

```rust
fn main() {
    let numbers = [2, 1, 17, 99, 34, 56];
    
    // iterator
    let numbers_iterator = numbers.iter();
    
    for number in numbers_iterator {
        println!("{}", number);
    }
}
```

## next() Method of an Iterator in Rust

Another important method of iterator is the `next()` method. The `next()` method of an iterator can be used to traverse through the values in the iterator. Every iterator in Rust by definition will have the `next()` method. The `next()` method is used to fetch individual values from the iterator. Let's take a look at an example.

```rust
fn main() {
    let colors = vec!["Red", "Yellow", "Green"];
    
    // iterator
    let mut colors_iterator = colors.iter();
    println!("colors iterator = {:?}", colors_iterator);
    
    // fetch values from iterator one by one using next() method
    println!("{:?}", colors_iterator.next());
    println!("{:?}", colors_iterator.next());
    println!("{:?}", colors_iterator.next());
    println!("{:?}", colors_iterator.next());
}
```

**Output**
```
colors iterator = Iter(["Red", "Yellow", "Green"])
Some("Red")
Some("Yellow")
Some("Green")
None
```

Here, we fetch values from the iterator in colors_iterator using the `next()` method. The `next()` method either returns `Some` value or `None`. Notice that we need to make the colors_iterator a mutable variable because calling `next()` will change the internal state of the iterator. Each call to `next()` will consume an item from the iterator. The `next()` method returns `None` when the iterator reaches the end of the sequence.

## Ways to Create Iterator in Rust

We can create an iterator by converting a collection into an iterator. There are three ways to create an iterator.

1. Using `iter()` method
2. Using `into_iter()` method
3. Using `iter_mut()` method

All these methods provide different views of the data within the iterator.

### Using iter() method

Using the `iter()` method on a collection will borrow (reference) each element of the collection in each iteration. Thus, the collection will be available for use after we have looped through it. For example,

```rust
fn main() {
    let colors = vec!["Red", "Yellow", "Green"];
    
    // using iter() to iterate through a collection
    for color in colors.iter() {
        // reference to the items in the iterator
        println!("{}", color);
    }
    
    // the collection is untouched and still available here
    println!("colors = {:?}", colors);
}
```

**Output**
```
Red
Yellow
Green
colors = ["Red", "Yellow", "Green"]
```

Notice here that the colors variable is still available after the `iter()` method is used on it.

### Using into_iter() method

Using the `into_iter()` method on a collection will iterate on the same element of the collection in each iteration. Thus, the collection will no longer be available for reuse as the value moves within the loop. For example,

```rust
fn main() {
    let colors = vec!["Red", "Yellow", "Green"];
    
    // using into_iter() to iterate through a collection
    for color in colors.into_iter() {
        // the items in the collection move into this scope
        println!("{}", color);
    }
    // end of scope of for loop
    
    // error
    // the collection is not available here as the for loop scope ends above
    println!("colors = {:?}", colors);
}
```

Notice here that the `colors` variable is unavailable because the `into_iter()` method moves the actual data into the `for` loop and is not available outside of its scope.

> **Note:** By default the for loop will apply the `into_iter()` function to the collection. We don't have to use the `into_iter()` function to convert the collection to an iterator when using the for loop. For example, these two ways to loop through an iterator are the same.

```rust
for color in colors.into_iter() {
    // code
}

for color in colors {
    // code
}
```

### Using iter_mut() method

Using the `iter_mut()` method on a collection will mutably borrow each element of the collection in each iteration. It means we can modify the collection in place. For example,

```rust
fn main() {
    let mut colors = vec!["Red", "Yellow", "Green"];
    
    // using iter_mut() to iterate through a collection
    for color in colors.iter_mut() {
        // modify the item in the collection
        *color = "Black";
        println!("{}", color);
    }
    
    // the modified collection is available here
    println!("colors = {:?}", colors);
}
```

Notice here that we use `iter_mut()` method to change the original items in the collection with `*color = "Black"`. Thus, every item in the collection after the for loop is modified.

> **Note:** All of the ways to construct an iterator follow the concept of **Borrowing**. To learn more about Borrowing, visit [_Rust References and Borrowing_](https://www.programiz.com/rust/references-and-borrowing).

## Iterator Adapters in Rust

Iterator adapters are used to transform it into another kind of iterator by altering its behavior. For example, let's take a look at the `map()` adapter.

```rust
let numbers = vec![1, 2, 3];

numbers.iter().map(|i| i + 1);
```

Here, the `map()` method takes a _closure_ to call on each item on the vector numbers. However, we will have to use the `collect()` method on the `map()` adapter to collect the result. This is because iterator adapters do not produce the result directly (lazy) without calling the `collect()` method.

```rust
numbers.iter().map(|i| i + 1).collect();
```

This will return a vector containing each item from the original vector incremented by **1**.

### Example: Iterator Adapters

```rust
fn main() {
   let numbers: Vec<i32> = vec![1, 2, 3];
   
   // using the map iterator adapter
   let even_numbers: Vec<i32> = numbers.iter().map(|i| i * 2).collect();
   
   println!("numbers = {:?}", numbers);
   println!("even_numbers = {:?}", even_numbers);
}
```

## Range in Rust

One of the other ways to create an iterator is to use the range notation. An example of a range is `1..6` which is an iterator. For example,

```rust
fn main() {
    // looping through a range
    for i in 1..6 {
        println!("{}", i);
    }
}
```

Here, we loop through a range `1..6` which is inclusive on the left (starts at 1) and exclusive on the right (ends at 5). Range is usually used together with the `for` loop.