/*
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see
that the 6th prime is 13.

What is the 10 001st prime number?
*/

#include <stdio.h>
#include <stdlib.h>

struct vector {
    int* elements;
    int len;
};

void push(struct vector* v, int element);
int pop(struct vector* v);
int get_prime_number(int position);

int main() {
    int n = 10001;
    int answer = get_prime_number(n);
    
    if (answer == -1)
        return -1;

    printf("%i", answer);
    return 0;
}

int get_prime_number(int position) {
    int bound = 2 + position / 2;
    int* buffer = malloc(bound * sizeof(int));
    if (buffer == NULL) {
        printf("error: not enough memory\n");
        return -1;
    }

    struct vector primes;
    primes.len = 0;
    primes.elements = buffer;
    push(&primes, 2);

    int i;
    int previous;
    int p = 2;
    while (primes.len != position) {
        ++p;
        for (i = 0; i < primes.len; ++i) {
            previous = primes.elements[i];
            if (p % previous == 0)
                break;
        }
        if (i == primes.len)
            push(&primes, p);
    }

    free(buffer);
    return pop(&primes);
}

void push(struct vector* v, int element) {
    v->elements[v->len] = element;
    v->len += 1;
}

int pop(struct vector* v) {
    v->len -= 1;
    return v->elements[v->len];
}
