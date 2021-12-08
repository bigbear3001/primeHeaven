from prime_cache import PrimeCache
KNOWN_PRIMES = PrimeCache(2)


def is_prime(number):
    if number < 2:
        return False
    global KNOWN_PRIMES
    if number in KNOWN_PRIMES:
        return True
    for i in find_primes(2, max(int(number/2), 2)):
        if number % i == 0:
            return False
    KNOWN_PRIMES.add(number)
    return True


def find_primes(start_with=0, end_with=None):
    if KNOWN_PRIMES.min <= start_with and KNOWN_PRIMES.max >= end_with:
        for p in (p for p in KNOWN_PRIMES if start_with <= p <= end_with):
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
