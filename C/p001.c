/*
If we list all the natural numbers below 10 that are multiples of 3 or 5, we
get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
*/

#include <stdio.h>

int sum_3_or_5(int n);
int brute_force(int n);

int main() {
    int n = 1000;
    int answer = sum_3_or_5(n);
    int answer2 = brute_force(n);

    if (answer != answer2) {
        printf("error: %i != %i\n", answer, answer2);
        return 1;
    }

    printf("%i", answer);
    return 0;
}

int sum_3_or_5(int n) {
    if (n < 4)
        return n;

    int count_3 = (n - 1) / 3;
    int count_5 = (n - 1) / 5;
    int count_15 = (n - 1) / 15;

    int sum_3 = 3 * count_3 * (count_3 + 1) / 2;
    int sum_5 = 5 * count_5 * (count_5 + 1) / 2;
    int sum_15 = 15 * count_15 * (count_15 + 1) / 2;

    int sum = sum_3 + sum_5 - sum_15;
    return sum;
}

int brute_force(int n) {
    int sum = 0;

    for (int i = 0; i < n; ++i) {
        if ((i % 3 == 0) || (i % 5 == 0))
            sum += i;
    }

    return sum;
}
