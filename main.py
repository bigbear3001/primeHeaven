#!/usr/bin/env python3
from datetime import datetime


def is_prime(number):
    if number < 2:
        return False
    for i in range(2, int(number/2)):
        if number % i == 0:
            return False
    return True


def find_primes(start_with=0, end_with=None):
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


def stat_prime_find_times(batch_size):
    start = datetime.now()
    primes_found = []
    for prime in find_primes(2, 1000000):
        primes_found.append(prime)
        if len(primes_found) == batch_size:
            end = datetime.now()
            print("found {batch_size:d} more primes (in {time:.2f} seconds): [{primes_found:s}, ...]".format(
                batch_size=batch_size,
                time=(end-start).total_seconds(),
                primes_found=", ".join([str(p) for p in primes_found][0:20]),
            ))
            primes_found = []
            start = end
    end = datetime.now()
    print("found {batch_size:d} more primes (in {time:.2f} seconds): [{primes_found:s}, ...]".format(
        batch_size=len(primes_found),
        time=(end - start).total_seconds(),
        primes_found=", ".join([str(p) for p in primes_found][0:20]),
    ))


if __name__ == '__main__':
    stat_prime_find_times(1000)