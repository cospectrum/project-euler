/*
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9.
The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
*/

fn main() {
    let n = 1000;
    let answer = sum_3_or_5(n);

    assert_eq!(answer, brute_force(n));
    println!("{answer}");
}

fn brute_force(n: u32) -> u32 {
    (1..n).filter(|x| x % 3 == 0 || x % 5 == 0).sum()
}

fn sum_3_or_5(n: u32) -> u32 {
    let count_3 = (n - 1) / 3;
    let count_5 = (n - 1) / 5;
    let count_15 = (n - 1) / 15;

    let sum_3 = 3 * count_3 * (count_3 + 1) / 2;
    let sum_5 = 5 * count_5 * (count_5 + 1) / 2;
    let sum_15 = 15 * count_15 * (count_15 + 1) / 2;

    sum_3 + sum_5 - sum_15
}
