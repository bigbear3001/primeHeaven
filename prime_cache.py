class PrimeCache:
    # TODO this cache may use unlimited amounts of RAM, need to limit it in a later version
    _known_primes = {2}
    min = 2
    max = 2

    def __init__(self, *known_primes):
        self._known_primes = {p for p in known_primes}
        self.min = min(known_primes)
        self.max = max(known_primes)

    def add(self, prime):
        self._known_primes.add(prime)
        self.min = min(self.min, prime)
        self.max = max(self.min, prime)

    def __iter__(self):
        return self._known_primes.__iter__()

    def already_know_all_of_them(self, start_with, end_with):
        return self.min <= start_with and self.max >= end_with

    def primes(self, start_with, end_with):
        return (p for p in self if start_with <= p <= end_with)

    def is_known_prime(self, number):
        return number in self._known_primes


