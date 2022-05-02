/*
The sum of the squares of the first ten natural numbers is,
    1^2 + 2^2 + ... + 10^2 = 385
The square of the sum of the first ten natural numbers is,
    (1 + 2 + ... + 10)^2 = 55^2 = 3025
Hence the difference between the sum of the squares of the first ten natural
numbers and the square of the sum is 3025 - 385 = 2640.

Find the difference between the sum of the squares of the first one hundred
natural numbers and the square of the sum.
*/

fn main() {
    const N: u64 = 100;
    let answer = get_diff(N);

    assert_eq!(answer, brute_force(N));
    println!("{answer}");
}

fn get_diff(n: u64) -> u64 {
    square_of_sum(n) - sum_of_squares(n)
}

fn square_of_sum(n: u64) -> u64 {
    // (1 + 2 + ... + n) ^ 2
    let m = n * (n + 1);
    let m = m / 2;
    m * m
}

fn sum_of_squares(n: u64) -> u64 {
    // 1^2 + 2^2 + ... + n^2
    let m = n * (n + 1) * (2 * n + 1);
    m / 6
}

fn brute_force(n: u64) -> u64 {
    let sum: u64 = (1..=n).sum();
    let sq_of_sum = sum * sum;

    let sum_of_sq: u64 = (1..=n).map(|x| x * x).sum();
    sq_of_sum - sum_of_sq
}
