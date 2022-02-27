def main():
    number = 2**1000
    answer = sum(int(digit) for digit in str(number))
    print(answer)


if __name__ == '__main__':
    main()

