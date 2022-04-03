/*
Each new term in the Fibonacci sequence is generated by adding the previous two
terms. By starting with 1 and 2, the first 10 terms will be: 1, 2, 3, 5, 8, 13,
21, 34, 55, 89, ... By considering the terms in the Fibonacci sequence whose
values do not exceed four million, find the sum of the even-valued terms.
*/

#include <stdio.h>

int fib_numbers_iterator(void);
int sum_even_fib_numbers(int bound);

int main()
{
    int n = 4 * 1000000;
    int answer = sum_even_fib_numbers(n);

    printf("%i", answer);
    return 0;
}

int sum_even_fib_numbers(int bound)
{
    int sum = 0;

    int fib_number = fib_numbers_iterator();
    while (fib_number <= bound) {

        if (fib_number % 2 == 0)
            sum += fib_number;

        fib_number = fib_numbers_iterator();
    }

    return sum;
}

int fib_numbers_iterator()
{
    static int first = 0;
    static int second = 1;

    int fib_number = first + second;
    first = second;
    second = fib_number;

    return fib_number;
}
