/*
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
*/

#include <stdio.h>

typedef long long i64;

i64 max(i64, i64);
i64 isqrt(i64 n);
i64 get_prime_factor(i64 n);

int main()
{
    i64 n = 600851475143;
    i64 answer = get_prime_factor(n);

    printf("%lli", answer);
    return 0;
}

i64 get_prime_factor(i64 n)
{
    if ((n == 1) || (n == 2) || (n == 3))
        return n;
    if (n % 2 == 0)
        return get_prime_factor(n / 2);

    i64 factor = isqrt(n);
    while (n % factor)
        --factor;

    if (factor == 1)
        return n;

    return max(get_prime_factor(n / factor), get_prime_factor(factor));
}

i64 isqrt(i64 n)
{
    i64 i = 0;
    while (i * i <= n)
        ++i;
    return i - 1;
}

i64 max(i64 a, i64 b)
{
    if (a > b)
        return a;
    return b;
}
