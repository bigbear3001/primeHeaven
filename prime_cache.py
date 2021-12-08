class PrimeCache:
    # TODO this cache may use unlimited amounts of RAM, need to limit it in a later version
    _known_primes = (2,)
    min = 2
    max = 2

    def __init__(self, *known_primes):
        self._known_primes = known_primes
        self.min = min(known_primes)
        self.max = max(known_primes)

    def add(self, prime):
        self._known_primes += (prime,)
        self.min = min(self.min, prime)
        self.max = max(self.min, prime)

    def __iter__(self):
        return self._known_primes.__iter__()


