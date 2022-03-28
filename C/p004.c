/*
A palindromic number reads the same both ways. The largest palindrome made
from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
*/

#include <stdio.h>
#include <stdlib.h>

typedef long long unsigned ui64;

struct array {
    char* elements;
    size_t len;
};

void free_array(struct array* arr);

ui64 power(int base, int exp);
size_t number_of_digits(int n);
struct array int_to_digits(int n);

int is_palindrome(int n);
int brute_force(void);

int main() {
    int answer = brute_force();

    printf("%i", answer);
    return 0;
}

int is_palindrome(int n) {
    struct array arr = int_to_digits(n);

    char* digits = arr.elements;
    size_t len = arr.len;
    size_t half_len = len / 2;

    size_t i;
    for (i = 0; i < half_len; ++i) {
        if (digits[i] != digits[len - i - 1]) {
            free_array(&arr);
            return 0;
        }
    }

    free_array(&arr);
    return 1;
}

int brute_force() {
    int max = 0;

    for (int x = 100; x < 1000; ++x) {
        for (int y = 100; y < 1000; ++y) {
            int prod = x * y;

            if ((prod > max) && is_palindrome(prod))
                max = prod;
        }
    }

    return max;
}

struct array int_to_digits(int n) {
    size_t len = number_of_digits(n);
    char* digits = malloc(len * sizeof(char));

    size_t i;
    for (i = 0; i < len; ++i) {
        digits[len - i - 1] = n % 10;
        n /= 10;
    }

    struct array arr;
    arr.elements = digits;
    arr.len = len;

    return arr;
}

size_t number_of_digits(int n) {
    int exp = 8 * sizeof(n) - 1;
    ui64 MAX_INT = power(2, exp) - 1;

    size_t num = 1;
    for (ui64 x = 10; x < MAX_INT; x *= 10) {
        if (x > n)
            break;
        ++num;
    }

    return num;
}

ui64 power(int base, int exp) {
    ui64 result = 1;

    for (int i = 0; i < exp; ++i)
        result *= base;

    return result;
}

void free_array(struct array* arr) {
    free(arr->elements);
}
