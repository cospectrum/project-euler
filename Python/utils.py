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
            break
    else:
        return True
    return False


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
    dictionary = dict()
    if not isinstance(n, int) or n < 1:
        return dictionary
    while True:
        end = ceil(sqrt(n)) + 1
        for i in range(2, end + 1):
            if n % i == 0:
                n //= i
                dictionary.setdefault(i, 0)
                dictionary[i] += 1
                break
            if i == end:
                dictionary.setdefault(n, 0)
                dictionary[n] += 1
                return dictionary
        if n == 1:
            return dictionary


def binomial_coefficient(n: int, k: int) -> int:
    assert n >= 0 and n >= k
    return factorial(n) // (factorial(n - k) * factorial(k))


def max_product(iterable_obj, *, queue_len: int) -> Any:
    """Return greatest product of <queue_len> or less
    adjacent values in <iterable_obj>
    """
    assert queue_len > 0
    iterator = iter(iterable_obj)
    queue = deque()
    great_product = product = next(iterator)
    for _ in range(queue_len-1):
        num = next(iterator)
        if num == 0:
            queue = deque()
            great_product = max(num, great_product)
            continue
        if len(queue) == 0:
            product = num
        else:
            product *= num
        great_product = max(product, great_product)
        queue.append(num)
    for num in iterator:
        if num == 0:
            queue = deque()
            great_product = max(num, great_product)
            continue
        if len(queue) == 0:
            product = num
        else:
            product *= num/queue.popleft()
        great_product = max(product, great_product)
        queue.append(num)
    return great_product


def manhattan_distance(x: Sequence, y: Sequence) -> Any:
    """L1 distance between points in vector space"""
    assert len(x) == len(y)
    dim: int = len(x)
    return sum(abs(x[i]-y[i]) for i in range(dim))
