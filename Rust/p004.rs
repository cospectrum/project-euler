/*
A palindromic number reads the same both ways. The largest palindrome made
from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
*/

fn main() {
    let answer = brute_force();
    println!("{answer}");
}

fn brute_force() -> u32 {
    let mut max = 0;
    let mut prod;

    for x in 100..1000 {
        for y in 100..1000 {
            prod = x * y;
            if prod > max && is_palindrome(prod) {
                max = prod;
            }
        }
    }

    max
}

fn is_palindrome(n: u32) -> bool {
    let digits: Vec<u8> = n
        .to_string()
        .chars()
        .map(|ch| ch.to_digit(10).unwrap() as u8)
        .collect();

    let len = digits.len();
    let half_len = len / 2;

    for i in 0..half_len {
        if digits[i] != digits[len - 1 - i] {
            return false;
        }
    }

    true
}
