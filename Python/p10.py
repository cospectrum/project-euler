"""
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
"""

from math import sqrt, ceil


def eratosthenes_sieve(n: int) -> tuple:
    sieve = [True]*(n + 1)
    sieve[0] = sieve[1] = False
    for num in range(ceil(sqrt(n)) + 1):
        is_prime = sieve[num]
        if not is_prime:
            continue
        for next_num in range(num*num, len(sieve), num):
            sieve[next_num] = False
    return tuple(x for x in range(len(sieve)) if sieve[x])


def main():
    n = -1 + 2*10**6
    primes = eratosthenes_sieve(n)
    answer = sum(primes)
    print(answer)


if __name__ == '__main__':
    main()
