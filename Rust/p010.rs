/*
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
*/

fn main() {
    const N: usize = 2_000_000;
    let primes = eratosthenes_sieve(N);
    let answer: u64 = primes.iter().sum();

    println!("{answer}");
}

fn eratosthenes_sieve(n: usize) -> Vec<u64> {
    let mut sieve = vec![true; n + 1];
    sieve[0] = false;
    sieve[1] = false;

    let mut index;
    let mut is_prime: bool;

    for num in 0..isqrt(n) {
        is_prime = sieve[num];
        if !is_prime {
            continue;
        }

        index = num * num;
        loop {
            if index > n {
                break;
            }
            sieve[index] = false;
            index += num;
        }
    }
    (0..n)
        .filter(|&x| sieve[x] == true)
        .map(|x| x as u64)
        .collect()
}

fn isqrt(x: usize) -> usize {
    let mut i = 0;
    while i * i <= x {
        i += 1;
    }
    i
}
