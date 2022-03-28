"""
2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

What is the sum of the digits of the number 2^1000?
"""


def main():
    number = 2**1000
    
    answer = sum(int(digit) for digit in str(number))
    print(answer)


if __name__ == '__main__':
    main()

