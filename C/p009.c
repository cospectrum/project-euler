/*
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
a^2 + b^2 = c^2

For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
*/

#include <stdio.h>

struct tuple {
    int a, b, c;
};

struct tuple find_triplet(int n);
void swap(int* a, int* b);

int main()
{
    int n = 1000;
    struct tuple triplet = find_triplet(n);

    int a = triplet.a;
    int b = triplet.b;
    int c = triplet.c;

    int answer = a * b * c;
    printf("%i", answer);
}

struct tuple find_triplet(int n)
{
    /*
    a^2 + b^2 = c^2  &&  a + b + c = N
    => (a + b)^2 = (N - c)^2  =>  2ab = N^2 - 2cN
    => abc = c(N^2 - 2cN)/2
    =>  2(N - b - c)b = N(N - 2c)  &&  a = N - b - c
    */

    struct tuple triplet;
    triplet.a = 0;
    triplet.b = 0;
    triplet.c = 0;

    int a;
    for (int c = 0; c < n; ++c) {
        for (int b = 0; b < c; ++b) {
            if (2 * b * (n - b - c) == n * (n - 2 * c)) {
                a = n - b - c;
                if (a > b)
                    swap(&a, &b);
                triplet.a = a;
                triplet.b = b;
                triplet.c = c;
                return triplet;
            }
        }
    }

    return triplet;
}

void swap(int* a, int* b)
{
    int t = *a;
    *a = *b;
    *b = t;
}
