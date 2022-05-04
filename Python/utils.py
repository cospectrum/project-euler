import time
from math import sqrt, ceil, factorial
from collections import deque
from typing import Any, Sequence, List, Iterator, Union


def benchmark(func):
    
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()

        parsed_args = [f'{arg}' for arg in args]
        parsed_kwargs = [f'{key}={value}' for key, value in kwargs.items()]
        args_str = ', '.join(parsed_args + parsed_kwargs)

        f_string = f'{func.__name__}({args_str}): {end - start} s'
        print(f_string)
        return result

    return wrapper


def factors_generator(number: int) -> Iterator[int]:
    m = 1
    while m*m < number:
        if number % m == 0:
            yield m
            yield number // m
        m += 1
    
    if m*m == number:
        yield m


def is_palindrome(seq: Union[Sequence, int]) -> bool:
    if isinstance(seq, int):
        seq = str(seq)
    
    length = len(seq)
    half_len = length//2
    
    for i in range(half_len):
        if seq[i] != seq[length-1-i]:
            return False
    
    return True


def get_factorization_list(n: int) -> list:
    seq = []
    if not isinstance(n, int) or n < 1:
        return seq
    
    while True:
        end = ceil(sqrt(n)) + 1
        for i in range(2, end + 1):
            if n % i == 0:
                n //= i
                seq.append(i)
                break
            if i == end:
                seq.append(n)
                return seq
        if n == 1:
            return seq


def get_factorization_dict(n: int) -> dict:
    """{primes: powers}
    get_factorization_dict(12) = {2: 2, 3: 1}, since 12 = 2^2 * 3^1
    """
    
    d = dict()
    if not isinstance(n, int) or n < 1:
        return d
    
    while True:
        end = ceil(sqrt(n)) + 1
        for i in range(2, end + 1):
            if n % i == 0:
                n //= i
                d.setdefault(i, 0)
                d[i] += 1
                break
            if i == end:
                d.setdefault(n, 0)
                d[n] += 1
                return d
        if n == 1:
            return d


def binomial_coefficient(n: int, k: int) -> int:
    assert n >= 0 and n >= k
    return factorial(n) // (factorial(n - k) * factorial(k))

