"""
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9.
The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
"""


# For tests
def brute_force(n: int) -> int:
    s = sum(x for x in range(n) if x % 3 == 0 or x % 5 == 0)
    return s


def sum_3_or_5(n: int) -> int:
    if n <= 3:
        return 0
    count_3 = (n - 1) // 3
    count_5 = (n - 1) // 5
    count_15 = (n - 1) // 15

    sum_3 = 3 * count_3 * (count_3 + 1) // 2
    sum_5 = 5 * count_5 * (count_5 + 1) // 2
    sum_15 = 15 * count_15 * (count_15 + 1) // 2

    result = sum_3 + sum_5 - sum_15
    return result


if __name__ == '__main__':
    n = 1000
    answer = sum_3_or_5(n)
    assert answer == brute_force(n)
    print(answer)

