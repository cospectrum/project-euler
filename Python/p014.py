"""
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
"""

from typing import Iterator


def collatz(start: int) -> Iterator[int]:
    n = start
    yield n

    while n != 1:
        if n % 2 == 0:
            n = n//2
            yield n
        else:
            n = 3*n + 1
            yield n


def chain_len(start_number: int) -> int:
    return sum(1 for num in collatz(start_number))


def get_max_start(end: int) -> int:
    return max(range(1, end), key=lambda start: chain_len(start))


def main():
    end = 10**6
    
    answer = get_max_start(end=end)
    print(answer)


if __name__ == '__main__':
    main()

