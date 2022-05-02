/*
The following iterative sequence is defined for the set of positive integers:
    n → n/2 (n is even)
    n → 3n + 1 (n is odd)
Using the rule above and starting with 13, we generate the following sequence:
    13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
It can be seen that this sequence (starting at 13 and finishing at 1) contains
10 terms. Although it has not been proved yet (Collatz Problem), it is thought
that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million.
*/

fn main() {
    const N: u64 = 1_000_000;

    let mut max_len = 0;
    let mut max_start = 1;

    for start in 1..N {
        let mut len = 0;
        for _ in collatz(start) {
            len += 1;
        }
        if len > max_len {
            max_len = len;
            max_start = start;
        }
    }

    let answer = max_start;
    println!("{}", answer);
}

fn collatz(start: u64) -> CollatzSeq {
    CollatzSeq {
        state: start,
        end: false,
    }
}

struct CollatzSeq {
    state: u64,
    end: bool,
}

impl Iterator for CollatzSeq {
    type Item = u64;

    fn next(&mut self) -> Option<Self::Item> {
        if self.end {
            return None;
        }

        let mut n = self.state;
        if n % 2 == 0 {
            n = n / 2;
        } else {
            n = 3 * n + 1;
        }
        self.state = n;

        if n == 1 {
            self.end = true;
        }
        Some(n)
    }
}
