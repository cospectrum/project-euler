/*
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
*/

fn main() {
    let n = 600851475143;
    let answer = prime_factor(n);

    println!("{answer}");
}

fn prime_factor(n: u64) -> u64 {
    match n {
        1..=3 => n,
        _ if n % 2 == 0 => prime_factor(n / 2),
        _ => {
            let mut factor = isqrt(n);
            while n % factor != 0 {
                factor -= 1;
            }
            return if factor == 1 {
                n
            } else {
                max(prime_factor(n / factor), prime_factor(factor))
            };
        }
    }
}

fn isqrt(n: u64) -> u64 {
    let mut i = 0;
    while i * i <= n {
        i += 1;
    }
    i - 1
}

fn max<T: PartialOrd>(a: T, b: T) -> T {
    if a > b {
        a
    } else {
        b
    }
}
