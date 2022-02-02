import time
from math import sqrt, ceil, factorial


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