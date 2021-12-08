#!/usr/bin/env python3
from datetime import datetime
from prime import find_primes


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