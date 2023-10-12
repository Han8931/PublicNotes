---
tags: rust, ownership 
---
# What Is Ownership?

Ownership is a feature and convention of Rust that helps ensure the memory safety of programs without a garbage collector. It’s another way of tackling the problem of memory leaks in your code.

The Rust compiler checks if a program obeys the ownership rules at compile time. If the program follows these rules, it can run. If it doesn’t, the compiler refuses to produce an executable.

Rust verifies the ownership rules using the **borrow checker.** The borrow checker verifies the ownership model and decides if a value in memory ([stack or heap](https://www.makeuseof.com/stack-and-heap-memory-allocation/)) is out of scope or not. If a value is out of its scope, it’s not accessible to other parts of the program unless it’s borrowed.

# The Ownership Rules

In Rust, every variable owns the value it’s initialized with, and there can only be one owner. Once the owner is out of scope, the value is dropped. It’s important to understand the details of the ownership rules.

### First Rule
The first ownership rule is that every variable owns its initialized value.
- `let owner = String::from("one");` 
	- Create a `String` from a string literal using the `from` function.

The **`owner`** variable above owns the string **`one`** and, unlike languages such as Python and Go, that value will be dropped on variable reassignment.

### Second Rule
The second ownership rule is that two variables cannot point to the same memory location; _every value can have only one owner_.
- `let new_owner = owner;` 

The **`new_owner`** variable now owns the value stored at the memory location of the **`owner`** variable. If you try to use the **`owner`** variable, the compiler will panic, and it will refuse to generate an executable.

### Third Rule
The third ownership rule is that once a variable is out of the declared scope, the value gets dropped, and memory is deallocated.

```rust
{       
	let example = String::from("Here's a new scope");   
}       
print!("{}", example)
```

You cannot access the **`example`** variable outside its scope; trying to do so will cause the compiler to panic.

## Examples

Multiple variables can interact with the same data in different ways in Rust. Let’s look at an example using an integer.
```rust
let x = 5;     
let y = x;
```
We can probably guess what this is doing: “bind the value `5` to `x`; then make a copy of the value in `x` and bind it to `y`.” We now have two variables, `x` and `y`, and both equal `5`. This is indeed what is happening, because integers are simple values with a known, fixed size, and these two `5` values are pushed onto the stack.

Now let’s look at the `String` version:
```rust
let s1 = String::from("hello");     
let s2 = s1;
```
This looks very similar, so we might assume that the way it works would be the same: that is, the second line would make a copy of the value in `s1` and bind it to `s2`. But this isn’t quite what happens.


## Ownership and Functions

The mechanics of passing a value to a function are similar to those when assigning a value to a variable. Passing a variable to a function will move or copy, just as assignment does. Listing 4-3 has an example with some annotations showing where variables go into and out of scope.

```rust
fn main() {     
	let s = String::from("hello");  // s comes into scope      
	takes_ownership(s);             // s's value moves into the function...                                     
									// ... and so is no longer valid here      
	let x = 5;                      // x comes into scope      
	makes_copy(x);                  // x would move into the function,                                     
									// but i32 is Copy, so it's okay to still
									// use x afterward  
} // Here, x goes out of scope, then s. But because s's value was moved, nothing   
  // special happens.  
fn takes_ownership(some_string: String) { // some_string comes into scope     
	println!("{}", some_string); 
} // Here, some_string goes out of scope and `drop` is called. The backing   
  // memory is freed.  
fn makes_copy(some_integer: i32) { // some_integer comes into scope     
println!("{}", some_integer); 
} // Here, some_integer goes out of scope. Nothing special happens.
```
If we tried to use `s` after the call to `takes_ownership`, Rust would throw a compile-time error. These static checks protect us from mistakes. Try adding code to `main` that uses `s` and `x` to see where you can use them and where the ownership rules prevent you from doing so.

## Return Values and Scope
Returning values can also transfer ownership. The following example shows an example of a function that returns some value, with similar annotations as those in the following example.

```rust
fn main() {     
	let s1 = gives_ownership();         // gives_ownership moves its return                                         
										// value into s1      
	let s2 = String::from("hello");     // s2 comes into scope      
	let s3 = takes_and_gives_back(s2);  // s2 is moved into                                         
										// takes_and_gives_back, which also                                         
										// moves its return value into s3 
} // Here, s3 goes out of scope and is dropped. s2 was moved, so nothing   
  // happens. s1 goes out of scope and is dropped.  
fn gives_ownership() -> String {             // gives_ownership will move its                                                                                        // return value into the function                                                                                       // that calls it      
	let some_string = String::from("yours"); // some_string comes into scope      
	some_string                              // some_string is returned and                                             
											 // moves out to the calling                                              
											 // function 
}  
// This function takes a String and returns one 
fn takes_and_gives_back(a_string: String) -> String { // a_string comes into                                                                                                  // scope      
	a_string  // a_string is returned and moves out to the calling function 
}
```
The ownership of a variable follows the same pattern every time: assigning a value to another variable moves it. When a variable that includes data on the heap goes out of scope, the value will be cleaned up by `drop` unless ownership of the data has been moved to another variable.

While this works, taking ownership and then returning ownership with every function is a bit tedious. _What if we want to let a function use a value but not take ownership_? It’s quite annoying that anything we pass in also needs to be passed back if we want to use it again, in addition to any data resulting from the body of the function that we might want to return as well.

Rust does let us return multiple values using a tuple, as shown in the following example.
```rust
fn main() {     
	let s1 = String::from("hello");      
	let (s2, len) = calculate_length(s1);      
	println!("The length of '{}' is {}.", s2, len); 
}  
fn calculate_length(s: String) -> (String, usize) {     
	let length = s.len(); // len() returns the length of a String      
	(s, length) 
}
```
But this is too much ceremony and a lot of work for a concept that should be common. Luckily for us, Rust has a feature for using a value without transferring ownership, called _references_.

# References and Borrowing
The issue with the above tuple code is that we have to return the `String` to the calling function so we can still use the `String` after the call to `calculate_length`, because the `String` was moved into `calculate_length`. Instead, we can provide a reference to the `String` value. A _reference_ is like a pointer in that it’s an address we can follow to access the data stored at that address; that data is owned by some other variable. Unlike a pointer, a reference is guaranteed to point to a valid value of a particular type for the life of that reference.

Here is how you would define and use a `calculate_length` function that has a reference to an object as a parameter instead of taking ownership of the value:

```rust
fn main() {
    let s1 = String::from("hello");
    let len = calculate_length(&s1);
    println!("The length of '{}' is {}.", s1, len);
}

fn calculate_length(s: &String) -> usize {
    s.len()
}
```

Note that we pass `&s1` into `calculate_length` and, in its definition, we take `&String` rather than `String`. These ampersands represent _references_, and they allow you to refer to some value without taking ownership of it.

Let’s take a closer look at the function call here:

```rust
let s1 = String::from("hello");      
let len = calculate_length(&s1);
```

The `&s1` syntax lets us create a reference that _refers_ to the value of `s1` but does not own it. Because it does not own it, the value it points to will not be dropped when the reference stops being used.

Likewise, the signature of the function uses `&` to indicate that the type of the parameter `s` is a reference. Let’s add some explanatory annotations:

```rust
fn calculate_length(s: &String) -> usize { // s is a reference to a String 
	s.len() 
} // Here, s goes out of scope. But because it does not have ownership of what 
  // it refers to, it is not dropped.
```

The scope in which the variable `s` is valid is the same as any function parameter’s scope, but the value pointed to by the reference is not dropped when `s` stops being used, because `s` doesn’t have ownership. When functions have references as parameters instead of the actual values, we won’t need to return the values in order to give back ownership, because we never had ownership.

We call the action of creating a reference _borrowing_. As in real life, if a person owns something, you can borrow it from them. When you’re done, you have to give it back. You don’t own it.

So, what happens if we *try to modify something we’re borrowing*? Spoiler alert: **it doesn’t work!**

```rust
fn main() {
    let s = String::from("hello");
    change(&s);
}

fn change(some_string: &String) {
    some_string.push_str(", world");
}
```

## Mutable References
We can fix the code to allow us to modify a borrowed value with just a few small tweaks that use, instead, a _mutable reference_:

```rust
fn main() {
    let mut s = String::from("hello");

    change(&mut s);
}

fn change(some_string: &mut String) {
    some_string.push_str(", world");
}
```

First we change `s` to be `mut`. Then we create a mutable reference with `&mut s` where we call the `change` function, and update the function signature to accept a mutable reference with `some_string: &mut String`. This makes it very clear that the `change` function will mutate the value it borrows.

**Mutable references have one big restriction**: if you have a mutable reference to a value, you can have no other references to that value. This code that attempts to create two mutable references to `s` will fail:

```rust
$ cargo run
   Compiling ownership v0.1.0 (file:///projects/ownership)
error[E0499]: cannot borrow `s` as mutable more than once at a time
 --> src/main.rs:5:14
  |
4 |     let r1 = &mut s;
  |              ------ first mutable borrow occurs here
5 |     let r2 = &mut s;
  |              ^^^^^^ second mutable borrow occurs here
6 |
7 |     println!("{}, {}", r1, r2);
  |                        -- first borrow later used here

For more information about this error, try `rustc --explain E0499`.
error: could not compile `ownership` due to previous error
```

This error says that this code is invalid because _we cannot borrow `s` as mutable more than once at a time_. The first mutable borrow is in `r1` and must last until it’s used in the `println!`, but between the creation of that mutable reference and its usage, we tried to create another mutable reference in `r2` that borrows the same data as `r1`.

_The restriction preventing multiple mutable references to the same data at the same time allows for mutation but in a very controlled fashion_. It’s something that new Rustaceans struggle with because most languages let you mutate whenever you’d like. The benefit of having this restriction is that Rust can prevent data races at compile time. A _data race_ is similar to a race condition and happens when these three behaviors occur:

- Two or more pointers access the same data at the same time.
- At least one of the pointers is being used to write to the data.
- There's no mechanism being used to synchronize access to the data.

Data races cause undefined behavior and can be difficult to diagnose and fix when you're trying to track them down at runtime; Rust prevents this problem by refusing to compile code with data races!

As always, we can use curly brackets to create a new scope, allowing for multiple mutable references, just not _simultaneous_ ones:
```rust
fn main() {
    let mut s = String::from("hello");
    {
        let r1 = &mut s;
    } // r1 goes out of scope here, so we can make a new reference with no problems.

    let r2 = &mut s;
    println!("{r2}")
}
```
Rust enforces a similar rule for combining mutable and immutable references. This code results in an error:

```rust
    let mut s = String::from("hello");

    let r1 = &s; // no problem
    let r2 = &s; // no problem
    let r3 = &mut s; // BIG PROBLEM
```

```rust
$ cargo run
   Compiling ownership v0.1.0 (file:///projects/ownership)
error[E0502]: cannot borrow `s` as mutable because it is also borrowed as immutable
 --> src/main.rs:6:14
  |
4 |     let r1 = &s; // no problem
  |              -- immutable borrow occurs here
5 |     let r2 = &s; // no problem
6 |     let r3 = &mut s; // BIG PROBLEM
  |              ^^^^^^ mutable borrow occurs here
7 |
8 |     println!("{}, {}, and {}", r1, r2, r3);
  |                                -- immutable borrow later used here

For more information about this error, try `rustc --explain E0502`.
error: could not compile `ownership` due to previous error
```

Whew! We _also_ cannot have a mutable reference while we have an immutable one to the same value.

Users of an immutable reference don't expect the value to suddenly change out from under them! However, multiple immutable references are allowed because no one who is just reading the data has the ability to affect anyone else’s reading of the data.

Note that a reference's scope starts from where it is introduced and continues through the last time that reference is used. For instance, this code will compile because the last usage of the immutable references, the `println!`, occurs before the mutable reference is introduced:

```rust
    let mut s = String::from("hello");

    let r1 = &s; // no problem
    let r2 = &s; // no problem
    println!("{} and {}", r1, r2);
    // variables r1 and r2 will not be used after this point

    let r3 = &mut s; // no problem
    println!("{}", r3);
```

The scopes of the immutable references `r1` and `r2` end after the `println!` where they are last used, which is before the mutable reference `r3` is created. These scopes don’t overlap, so this code is allowed: the compiler can tell that the reference is no longer being used at a point before the end of the scope.

Even though borrowing errors may be frustrating at times, remember that it’s the Rust compiler pointing out a potential bug early (at compile time rather than at runtime) and showing you exactly where the problem is. Then you don’t have to track down why your data isn’t what you thought it was.

## Dangling References

In languages with pointers, it's easy to erroneously create a _dangling pointer_—a pointer that references a location in memory that may have been given to someone else—by freeing some memory while preserving a pointer to that memory. In Rust, by contrast, the compiler guarantees that references will never be dangling references: if you have a reference to some data, the compiler will ensure that the data will not go out of scope before the reference to the data does.

Let's try to create a dangling reference to see how Rust prevents them with a compile-time error:

```rust
fn main() {
    let reference_to_nothing = dangle();
}

fn dangle() -> &String { // dangle returns a reference to a String
    let s = String::from("hello"); // s is a new String
    &s // we return a reference to the String, s
} // Here, s goes out of scope, and is dropped. Its memory goes away.
```

Because `s` is created inside `dangle`, when the code of `dangle` is finished, `s` will be deallocated. But we tried to return a reference to it. That means this reference would be pointing to an invalid `String`. That’s no good! Rust won't let us do this.

The solution here is to return the `String` directly:

```rust
fn no_dangle() -> String {
    let s = String::from("hello");
    s
}
```

This works without any problems. Ownership is moved out, and nothing is deallocated.

# Slice Type

_Slices_ let you reference a contiguous sequence of elements in a collection rather than the whole collection. A slice is a kind of reference, so it does not have ownership.

Here’s a small programming problem: write a function that takes a string of words separated by spaces and returns the first word it finds in that string. If the function doesn’t find a space in the string, the whole string must be one word, so the entire string should be returned.

Let’s work through how we’d write the signature of this function without using slices, to understand the problem that slices will solve:
```rust
fn first_word(s: &String) -> ?
```
The `first_word` function has a `&String` as a parameter. We don’t want ownership, so this is fine. But **what should we return?** We don’t really have a way to talk about _part_ of a string. However, we could _return the index of the end of the word_, indicated by a space. Let’s try that, as shown in the following example.

```rust
fn first_word(s: &String) -> usize {
    let bytes = s.as_bytes();

    for (i, &item) in bytes.iter().enumerate() {
        if item == b' ' {
            return i;
        }
    }
    s.len()
}
```

Because we need to go through the `String` element by element and check whether a value is a space, we’ll convert our `String` to an array of bytes using the `as_bytes` method.

```rust
let bytes = s.as_bytes();
```
Next, we create an iterator over the array of bytes using the `iter` method: 
```rust
for (i, &item) in bytes.iter().enumerate() {
```
We'll discuss iterators in more detail in Chapter 13. For now, know that `iter` is a method that returns each element in a collection and that `enumerate` wraps the result of `iter` and returns each element as part of a tuple instead. The first element of the tuple returned from `enumerate` is the index, and the second element is a reference to the element. This is a bit more convenient than calculating the index ourselves.

Because the `enumerate` method returns a tuple, we can use patterns to get that tuple. We'll be discussing patterns more in Chapter 6. In the `for` loop, we specify a pattern that has `i` for the index in the tuple and `&item` for the single byte in the tuple. Because we get a reference to the element from `.iter().enumerate()`, we use `&` in the pattern.

Inside the `for` loop, we search for the byte that represents the space by using the byte literal syntax. If we find a space, we return the position. Otherwise, we return the length of the string by using `s.len()`.
```rust
	if item == b' ' {
		 return i;         
	 }     
 }      
 s.len()
```

We now have a way to find out the index of the end of the first word in the string, but there’s a problem. We’re returning a `usize` on its own, but it’s only a meaningful number in the context of the `&String`. In other words, because it’s a separate value from the `String`, there’s no guarantee that it will still be valid in the future. Consider the program in Listing 4-8 that uses the `first_word` function from Listing 4-7.

```rust
fn main() {
    let mut s = String::from("hello world");

    let word = first_word(&s); // word will get the value 5

    s.clear(); // this empties the String, making it equal to ""

    // word still has the value 5 here, but there's no more string that
    // we could meaningfully use the value 5 with. word is now totally invalid!
}
```

This program compiles without any errors and would also do so if we used `word` after calling `s.clear()`. Because `word` isn’t connected to the state of `s` at all, `word` still contains the value `5`. We could use that value `5` with the variable `s` to try to extract the first word out, but this would be a bug because the contents of `s` have changed since we saved `5` in `word`.

Having to worry about the index in `word` getting out of sync with the data in `s` is tedious and error prone! Managing these indices is even more brittle if we write a `second_word` function. Its signature would have to look like this:

```rust
fn second_word(s: &String) -> (usize, usize) {
```

Now we’re tracking a starting _and_ an ending index, and we have even more values that were calculated from data in a particular state but aren’t tied to that state at all. We have three unrelated variables floating around that need to be kept in sync.

Luckily, Rust has a solution to this problem: string slices.

## String Slices

A _string slice_ is a reference to part of a `String`, and it looks like this:

```rust
    let s = String::from("hello world");

    let hello = &s[0..5];
    let world = &s[6..11];
```

Rather than a reference to the entire `String`, `hello` is a reference to a portion of the `String`, specified in the extra `[0..5]` bit. We create slices using a range within brackets by specifying `[starting_index..ending_index]`, where `starting_index` is the first position in the slice and `ending_index` is one more than the last position in the slice. Internally, the slice data structure stores the starting position and the length of the slice, which corresponds to `ending_index` minus `starting_index`. So, in the case of `let world = &s[6..11];`, `world` would be a slice that contains a pointer to the byte at index 6 of `s` with a length value of `5`.

With Rust’s `..` range syntax, if you want to start at index 0, you can drop the value before the two periods. In other words, these are equal:

```rust
let s = String::from("hello");

let slice = &s[0..2];
let slice = &s[..2];
```

By the same token, if your slice includes the last byte of the `String`, you can drop the trailing number. That means these are equal:
```rust
let s = String::from("hello");

let len = s.len();

let slice = &s[3..len];
let slice = &s[3..];
```

You can also drop both values to take a slice of the entire string. So these are equal:

```rust
let s = String::from("hello");

let len = s.len();

let slice = &s[0..len];
let slice = &s[..];
```

With all this information in mind, let's rewrite `first_word` to return a **slice**. The type that signifies "**string slice**" is written as `&str`:

```rust
fn first_word(s: &String) -> &str {
    let bytes = s.as_bytes();

    for (i, &item) in bytes.iter().enumerate() {
        if item == b' ' {
            return &s[0..i];
        }
    }

    &s[..]
}
```

We get the index for the end of the word the same way we did in the previous code, by looking for the first occurrence of a space. When we find a space, we return a string slice using the start of the string and the index of the space as the starting and ending indices.

Now when we call `first_word`, we get back a single value that is tied to the underlying data. The value is made up of a reference to the starting point of the slice and the number of elements in the slice.

We now have a straightforward API that’s much harder to mess up because the compiler will ensure the references into the `String` remain valid. Remember the bug in the program, when we got the index to the end of the first word but then cleared the string so our index was invalid? That code was logically incorrect but didn’t show any immediate errors. The problems would show up later if we kept trying to use the first word index with an emptied string. Slices make this bug impossible and let us know we have a problem with our code much sooner. Using the slice version of `first_word` will throw a compile-time error:

```rust
fn main() {
    let mut s = String::from("hello world");

    let word = first_word(&s);

    s.clear(); // error!

    println!("the first word is: {}", word);
}
```

Here’s the compiler error:
```rust
$ cargo run
   Compiling ownership v0.1.0 (file:///projects/ownership)
error[E0502]: cannot borrow `s` as mutable because it is also borrowed as immutable
  --> src/main.rs:18:5
   |
16 |     let word = first_word(&s);
   |                           -- immutable borrow occurs here
17 |
18 |     s.clear(); // error!
   |     ^^^^^^^^^ mutable borrow occurs here
19 |
20 |     println!("the first word is: {}", word);
   |                                       ---- immutable borrow later used here

For more information about this error, try `rustc --explain E0502`.
error: could not compile `ownership` due to previous error
```

Recall from the borrowing rules that if we have an immutable reference to something, we cannot also take a mutable reference. Because `clear` needs to truncate the `String`, it needs to get a mutable reference. The `println!` after the call to `clear` uses the reference in `word`, so the immutable reference must still be active at that point. Rust disallows the mutable reference in `clear` and the immutable reference in `word` from existing at the same time, and compilation fails. Not only has Rust made our API easier to use, but it has also eliminated an entire class of errors at compile time!

### String Literals as Slices

Recall that we talked about string literals being stored inside the binary. Now that we know about slices, we can properly understand string literals:

`let s = "Hello, world!";`

The type of `s` here is `&str`: it’s a slice pointing to that specific point of the binary. This is also why string literals are immutable; `&str` is an immutable reference.

### String Slices as Parameters

Knowing that you can take slices of literals and `String` values leads us to one more improvement on `first_word`, and that’s its signature:

`fn first_word(s: &String) -> &str {`

A more experienced Rustacean would write the signature shown in Listing 4-9 instead because it allows us to use the same function on both `&String` values and `&str` values.

`fn first_word(s: &str) -> &str {`

If we have a string slice, we can pass that directly. If we have a `String`, we can pass a slice of the `String` or a reference to the `String`. This flexibility takes advantage of _deref coercions_.

Defining a function to take a string slice instead of a reference to a `String` makes our API more general and useful without losing any functionality:

```rust
fn main() {
    let my_string = String::from("hello world");

    // `first_word` works on slices of `String`s, whether partial or whole
    let word = first_word(&my_string[0..6]);
    let word = first_word(&my_string[..]);
    // `first_word` also works on references to `String`s, which are equivalent
    // to whole slices of `String`s
    let word = first_word(&my_string);

    let my_string_literal = "hello world";

    // `first_word` works on slices of string literals, whether partial or whole
    let word = first_word(&my_string_literal[0..6]);
    let word = first_word(&my_string_literal[..]);

    // Because string literals *are* string slices already,
    // this works too, without the slice syntax!
    let word = first_word(my_string_literal);
}
```

## Other Slices

String slices, as you might imagine, are specific to strings. But there’s a more general slice type too. Consider this array:

```rust
let a = [1, 2, 3, 4, 5];
```

Just as we might want to refer to part of a string, we might want to refer to part of an array. We’d do so like this:
```rust
let a = [1, 2, 3, 4, 5];

let slice = &a[1..3];

assert_eq!(slice, &[2, 3]);

```

This slice has the type `&[i32]`. It works the same way as string slices do, by storing a reference to the first element and a length. You'll use this kind of slice for all sorts of other collections. 

# Summary
The concepts of _ownership, borrowing, and slices ensure memory safety in Rust programs at compile time_. The Rust language gives you control over your memory usage in the same way as other systems programming languages, but having the owner of data automatically clean up that data when the owner goes out of scope means you don’t have to write and debug extra code to get this control.


