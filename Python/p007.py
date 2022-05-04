"""
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see 
that the 6th prime is 13.

What is the 10 001st prime number?
"""


# Brute force. For more performance see "Sieve of Eratosthenes" and problem №10
def prime_number_by(*, position: int) -> int:
    prev_primes = [2]
    new = prev_primes[-1]

    while len(prev_primes) != position:
        new += 1
        for p in prev_primes:
            if new % p == 0:
                break
        else:
            prev_primes.append(new)

    return prev_primes[-1]


if __name__ == '__main__':
    n = 10**4 + 1
    answer = prime_number_by(position=n)
    print(answer)

