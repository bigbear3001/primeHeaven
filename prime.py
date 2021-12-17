from math import sqrt

from prime_cache import PrimeCache

KNOWN_PRIMES = PrimeCache(2, 3)


def is_possible_prime(number):
    if number % 2 == 0:
        return False
    if number == 5:
        return True
    if str(number)[-1] == "5":
        return False
    # fermat primality test with a=2:
    # Given an integer n, choose some integer a coprime to n and calculate an − 1 modulo n.
    # If the result is different from 1, then n is composite.
    # https://en.wikipedia.org/wiki/Primality_test
    if pow(2, number - 1, number) != 1:
        return False
    return True


def is_prime(number):
    if number < 2:
        return False
    global KNOWN_PRIMES
    if KNOWN_PRIMES.is_known_prime(number):
        return True
    if is_possible_prime(number):
        for i in find_primes(3, max(int(sqrt(number)), 3)):
            if number % i == 0:
                return False
        KNOWN_PRIMES.add(number)
        return True
    return False


def find_primes(start_with=0, end_with=None):
    if KNOWN_PRIMES.already_know_all_of_them(start_with, end_with):
        for p in KNOWN_PRIMES.primes(start_with, end_with):
            yield p
    else:
        if start_with >= KNOWN_PRIMES.min and KNOWN_PRIMES.max <= end_with:
            for p in KNOWN_PRIMES.primes(max(KNOWN_PRIMES.min, start_with), KNOWN_PRIMES.max):
                yield p
            # start checking with first number after the last number that could be prime
            number = KNOWN_PRIMES.max + 2
            increment = 2
        elif start_with <= 2:
            yield 2
            number = 3
            increment = 2
        else:
            number = start_with
            # till we find the first prime we increment with 1
            increment = 1
        while end_with is None or number <= end_with:
            if is_prime(number):
                yield number
                increment = 2
            number += increment
