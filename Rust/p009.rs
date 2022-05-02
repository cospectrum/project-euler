/*
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
a^2 + b^2 = c^2

For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
*/

fn main() {
    const N: u64 = 1000;
    let (a, b, c) = find_triplet(N);
    let answer = a * b * c;

    println!("{}", answer);
}

fn find_triplet(n: u64) -> (u64, u64, u64) {
    for c in 0..n {
        for b in 0..c {
            if 2 * b * (n - b - c) == n * (n - 2 * c) {
                let a = n - b - c;
                return if a > b { (b, a, c) } else { (a, b, c) };
            }
        }
    }
    (0, 0, 0)
}
