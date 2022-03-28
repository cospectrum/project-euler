"""
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see 
that the 6th prime is 13.

What is the 10 001st prime number?
"""


# Brute force. For more performance see "Sieve of Eratosthenes" and problem №10
def get_prime_number_by(*, position: int) -> int:
    assert isinstance(position, int) and position > 0

    previous_primes = [2]
    new_prime = previous_primes[-1]
    
    while len(previous_primes) != position:
        new_prime += 1
        for prev_prime in previous_primes:
            if new_prime % prev_prime == 0:
                break
        else:
            previous_primes.append(new_prime)
    
    return previous_primes[-1]


if __name__ == '__main__':
    n = 10**4 + 1
    answer = get_prime_number_by(position=n)
    print(answer)

