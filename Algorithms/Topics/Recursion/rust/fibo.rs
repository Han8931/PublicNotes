fn main() {
    let a = fibo(5);
    println!("{a}");

}

fn fibo(n:i32)->i32{
    if n<2{
        n
    }
    else {
        fibo(n-2)+fibo(n-1)
    }
}
