"""
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
"""


def sqrt(number) -> float:
    return number ** 0.5


def get_factor(num: int) -> int:
    if num in (1, 2, 3):
        return num
    if num % 2 == 0:
        return get_factor(num // 2)
    factor = int(sqrt(num))
    while num % factor:
        factor -= 1
        if factor == 1:
            return num
    return max(get_factor(num // factor), get_factor(factor))


if __name__ == '__main__':
    n = 600851475143
    answer = get_factor(n)
    print(answer)
