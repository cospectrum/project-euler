/*
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see
that the 6th prime is 13.

What is the 10 001st prime number?
*/

fn main() {
    const N: usize = 10_001;
    let answer = prime_number_by_position(N);
    println!("{answer}");
}

// Brute force. For more performance see "Sieve of Eratosthenes" and problem №10
fn prime_number_by_position(position: usize) -> u64 {
    let mut prev_primes = vec![2];
    let mut new_prime = 2;

    let mut is_prime: bool;
    while prev_primes.len() != position {
        new_prime += 1;
        is_prime = true;
        for p in &prev_primes {
            if new_prime % p == 0 {
                is_prime = false;
                break;
            }
        }
        if is_prime {
            prev_primes.push(new_prime);
        }
    }
    prev_primes.pop().unwrap()
}
