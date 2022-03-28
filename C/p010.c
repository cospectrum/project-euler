/*
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
*/

#include <stdlib.h>
#include <stdio.h>

typedef long long unsigned ui64;

struct array {
    short *values;
    size_t len;
};

struct array eratosthenes_sieve(size_t n);
ui64 sum(struct array sieve);
int isqrt(int x);

int main() {
    size_t n = -1 + 2000000;
    
    struct array sieve = eratosthenes_sieve(n);
    if (sieve.values == NULL)
        return -1;
   
    ui64 answer = sum(sieve);
    free(sieve.values);

    printf("%llu", answer);
    return 0;
}

ui64 sum(struct array sieve) {
    size_t len = sieve.len;
    short *primes = sieve.values;
    
    ui64 total = 0;
    for (int i = 0; i < len; ++i) {
        if (primes[i])
            total += i;
    }

    return total;
}

struct array eratosthenes_sieve(size_t n) {
    size_t len = n + 1;

    struct array sieve;
    sieve.len = len;
    sieve.values = malloc(len * sizeof(short));
    
    if (sieve.values == NULL)
        return sieve;

    for (size_t i = 0; i < len; ++i)
        sieve.values[i] = 1;
    
    sieve.values[0] = 0;
    sieve.values[1] = 0;

    short is_prime;
    int root = isqrt((int) n) + 1;

    for (int num = 0; num < root; ++num) {
        is_prime = sieve.values[num];
        if (!is_prime)
            continue;

        for (int next = num*num; next < len; next += num)
            sieve.values[next] = 0;
    }

    return sieve;
}

int isqrt(int x) {
    int i = 0;
    while (i * i <= x)
        ++i;
    return i - 1;
}

