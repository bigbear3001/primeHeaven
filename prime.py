from prime_cache import PrimeCache
KNOWN_PRIMES = PrimeCache(2)


def is_prime(number):
    if number < 2:
        return False
    global KNOWN_PRIMES
    if KNOWN_PRIMES.is_known_prime(number):
        return True
    for i in find_primes(2, max(int(number/2), 2)):
        if number % i == 0:
            return False
    KNOWN_PRIMES.add(number)
    return True


def find_primes(start_with=0, end_with=None):
    if KNOWN_PRIMES.already_know_all_of_them(start_with, end_with):
        for p in KNOWN_PRIMES.primes(start_with, end_with):
            yield p
        return
    if start_with <= 2:
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
