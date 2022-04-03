/*
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
*/

#include <stdio.h>
#include <stdlib.h>

void get_factorization(int* elements, size_t len, int n);
int max(int a, int b);
int power(int base, int exp);
void max_union(int* max_elements, int* elements, size_t len);
int get_smallest(int n);

int main()
{
    int n = 20;
    int answer = get_smallest(n);

    printf("%i", answer);
    return 0;
}

int get_smallest(int n)
{
    size_t len = n + 1;
    int* array = calloc(2 * len, sizeof(int));

    int* max_elements = array;
    int* elements = &array[len];

    for (int k = 2; k < len; ++k) {
        get_factorization(elements, len, k);
        max_union(max_elements, elements, len);
    }

    int product = 1;
    for (int i = 0; i < len; ++i) {
        if (max_elements[i] != 0)
            product *= power(i, max_elements[i]);
    }
    free(array);
    return product;
}

void get_factorization(int* array, size_t len, const int n)
{
    // index = base, value = exp
    // 12 = 2^2 * 3^1 -> int *array = {0, 0, 2, 1, 0, 0, ..., 0}

    int num = n;
    int exp;

    for (int p = 2; p < len; ++p) {
        exp = 0;
        while ((num % p) == 0) {
            ++exp;
            num /= p;
        }
        array[p] = exp;
    }
}

int power(int base, int exp)
{
    int result = 1;
    for (int i = 0; i < exp; ++i)
        result *= base;

    return result;
}

int max(int a, int b)
{
    if (a > b)
        return a;
    return b;
}

void max_union(int* max_elements, int* elements, size_t len)
{
    for (size_t i = 0; i < len; ++i)
        max_elements[i] = max(max_elements[i], elements[i]);
}
