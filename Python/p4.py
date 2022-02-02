"""
A palindromic number reads the same both ways. The largest palindrome made
from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""


def is_palindrome(n: int) -> bool:
    string = str(n)
    length = len(string)
    l_index = length // 2
    r_index = l_index
    if length % 2 == 1:
        r_index += 1
    l_slice = string[:l_index]
    r_slice = string[r_index:]
    return l_slice == r_slice[::-1]


def brute_force():
    iterator = (
        x * y for y in range(100, 999) for x in range(100, 999)
    )
    return max(n for n in iterator if is_palindrome(n))


if __name__ == '__main__':
    answer = brute_force()
    print(answer)
