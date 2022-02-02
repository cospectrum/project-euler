"""
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
"""

from utils import get_factorization_dict


def get_product(dictionary) -> int:
    product = 1
    for key in dictionary:
        product *= key ** dictionary[key]
    return product


def get_max_union(dict_1, dict_2):
    keys = set(dict_1) | set(dict_2)
    result = {
        key: max(dict_1.get(key, 0), dict_2.get(key, 0))
        for key in keys
    }
    return result


def main():
    n = 20
    iterator = range(1, n + 1)
    factor_union = dict()
    for number in iterator:
        factor = get_factorization_dict(number)
        factor_union = get_max_union(factor_union, factor)
    answer = get_product(factor_union)
    print(answer)


if __name__ == '__main__':
    main()
