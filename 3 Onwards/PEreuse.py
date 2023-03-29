from collections import Counter
import math


def is_palin(i):
    return str(i) == str(i)[::-1]


def prime_factorization(n: int):
    # Return a list containing all prime numbers found from [0-n]
    primes = []
    while n % 2 == 0:
        primes.append(2)
        n = n / 2

    for i in range(3, int(math.sqrt(n))+1, 2):

        while n % i == 0:
            primes.append(i)
            n = n / i
    if n > 2:
        primes.append(n)
    return primes
