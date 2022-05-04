"""
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
"""

from utils import get_factorization_dict


def int_from_dict(d: dict) -> int:
    product = 1

    for key in d:
        product *= key ** d[key]

    return product


def max_union(dict_1, dict_2):
    keys = set(dict_1) | set(dict_2)

    result = {
        key: max(dict_1.get(key, 0), dict_2.get(key, 0))
        for key in keys
    }
    return result


def main():
    N = 20
    union = dict()

    for n in range(1, N + 1):
        factors = get_factorization_dict(n)
        union = max_union(union, factors)

    answer = int_from_dict(union)
    print(answer)
    return


if __name__ == '__main__':
    main()

