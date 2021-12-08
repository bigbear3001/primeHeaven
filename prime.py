# TODO this cache may use unlimited amounts of RAM, need to limit it in a later version
KNOWN_PRIMES = (2,)


def is_prime(number):
    if number < 2:
        return False
    global KNOWN_PRIMES
    if number in KNOWN_PRIMES:
        return True
    for i in find_primes(2, max(int(number/2), 2)):
        if number % i == 0:
            return False
    KNOWN_PRIMES += (number,)
    return True


def find_primes(start_with=0, end_with=None):
    if min(KNOWN_PRIMES) <= start_with and max(KNOWN_PRIMES) >= end_with:
        for p in  (p for p in KNOWN_PRIMES if start_with <= p <= end_with):
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
