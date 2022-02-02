"""
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
a^2 + b^2 = c^2

For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
"""


def find_triplet(n: int) -> tuple:
    """a^2 + b^2 = c^2  &&  a + b + c = N
    => (a + b)^2 = (N - c)^2  =>  2ab = N^2 - 2cN
    => abc = c(N^2 - 2cN)/2
    =>  2(N - b - c)b = N(N - 2c)  &&  a = N - b - c
    """
    for c in range(n):
        for b in range(c):
            if 2*b*(n - b - c) == n*(n - 2*c):
                a = n - b - c
                if a > b:
                    a, b = b, a
                return a, b, c
    return tuple()


if __name__ == '__main__':
    n = 1000
    a, b, c = find_triplet(n)
    assert a + b + c == n
    answer = a * b * c
    print(answer)
