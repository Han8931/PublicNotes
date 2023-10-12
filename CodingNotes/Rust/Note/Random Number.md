In Rust, there are several random number generator implementation crates. Below, we'll look at the popular random number generators, compare and contrast them, and explore their advantages and disadvantages and their use cases.

## Using Rand, a popular random number generator

Rand is the most popular random number generator crate in the Rust ecosystem. 


1. Generate random numbers from a range of numbers `.gen_range(1.0..100.0)`:
```rust
let mut rng = thread_rng();
let random_number = rng.gen_range(1.0..100.0);
println!("Random from range {}", random_number);
```
   
2. Generate a random number by shuffling an array:

```rust
let mut rng = rand::thread_rng();
let mut arr = (1..100).collect::<Vec<i32>>();
arr.shuffle(&mut rng);
println!("Shuffle array: {:?}", arr);
```
