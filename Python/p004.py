"""
A palindromic number reads the same both ways. The largest palindrome made
from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""

from utils import is_palindrome


def brute_force():
    iterator = (x * y for y in range(100, 999+1) for x in range(100, 999+1))
    return max(n for n in iterator if is_palindrome(n))


if __name__ == '__main__':
    answer = brute_force()
    print(answer)

