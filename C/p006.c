/*
The sum of the squares of the first ten natural numbers is,
    1^2 + 2^2 + ... + 10^2 = 385
The square of the sum of the first ten natural numbers is,
    (1 + 2 + ... + 10)^2 = 55^2 = 3025
Hence the difference between the sum of the squares of the first ten natural
numbers and the square of the sum is 3025 - 385 = 2640.

Find the difference between the sum of the squares of the first one hundred
natural numbers and the square of the sum.
*/

#include <stdio.h>

int square_of_sum(int n);
int sum_of_squares(int n);
int get_diff(int n);
int brute_force(int n); // for tests

int main() {
    int n = 100;
    int answer = get_diff(n);
    int answer2 = brute_force(n);

    if (answer != brute_force(n)) {
        printf("error: %i != %i", answer, answer2);
        return 1;
    }

    printf("%i", answer);
    return 0;
}

int get_diff(int n) {
    return square_of_sum(n) - sum_of_squares(n);
}

int square_of_sum(int n) {
    int sum = n * (n + 1) / 2;
    return sum * sum;
}

int sum_of_squares(int n) {
    int prod = n * (n + 1) * (2 * n + 1);
    return prod / 6;
}

int brute_force(int n) {
    int sum = 0;
    int squares = 0;

    int i = 0;
    for (i = 0; i < n + 1; ++i) {
        sum += i;
        squares += i * i;
    }

    return sum * sum - squares;
}
