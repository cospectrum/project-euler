"""
The sum of the squares of the first ten natural numbers is,
    1^2 + 2^2 + ... + 10^2 = 385
The square of the sum of the first ten natural numbers is,
    (1 + 2 + ... + 10)^2 = 55^2 = 3025
Hence the difference between the sum of the squares of the first ten natural
numbers and the square of the sum is 3025 - 385 = 2640.

Find the difference between the sum of the squares of the first one hundred
natural numbers and the square of the sum.
"""


# For tests
def brute_force(n: int) -> int:
    square_of_sum = sum(range(1, n + 1)) ** 2
    sum_of_squares = sum(x ** 2 for x in range(1, n + 1))

    return square_of_sum - sum_of_squares


def get_difference(n: int) -> int:
    return get_square_of_sum(n) - get_sum_of_squares(n)


def get_square_of_sum(n: int) -> int:
    # (1 + 2 + ... + n)^2
    return (n * (n + 1) // 2) ** 2


def get_sum_of_squares(n: int) -> int:
    # 1^2 + 2^2 + ... + n^2
    return n*(n + 1)*(2*n + 1) // 6


if __name__ == '__main__':
    n = 100
    answer = get_difference(n)
    
    assert answer == brute_force(n)
    print(answer)

