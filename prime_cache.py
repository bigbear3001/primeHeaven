class PrimeCache:
    # TODO this cache may use unlimited amounts of RAM, need to limit it in a later version
    _known_primes = {2}
    _known_primes_list = [2]
    min = 2
    max = 2

    def __init__(self, *known_primes):
        self._known_primes = {p for p in known_primes}
        self._known_primes_list = list(known_primes)
        self.min = min(known_primes)
        self.max = max(known_primes)

    def add(self, prime):
        self._known_primes.add(prime)
        self._known_primes_list.append(prime)
        self.min = min(self.min, prime)
        self.max = max(self.min, prime)

    def __iter__(self):
        return self._known_primes.__iter__()

    def already_know_all_of_them(self, start_with, end_with):
        return self.min <= start_with and self.max >= end_with

    def primes(self, start_with, end_with):
        start_index = self.find_nearest_index(start_with)
        end_index = self.find_nearest_index(end_with, -1)
        if start_index is not None and end_index is not None:
            return self._known_primes_list[start_index:end_index + 1]
        # we keep the slow path for retrieving primes for a range, this should never hit, logically it would be
        # possible for the find_nearest_index to return None
        return (p for p in self._known_primes if start_with <= p <= end_with)

    def find_nearest_index(self, value, increment=1):
        index = None
        if value in self._known_primes:
            index = self._known_primes_list.index(value)
        else:
            while value:
                value += increment
                if value in self._known_primes:
                    index = self._known_primes_list.index(value)
                    value = None
        return index

    def is_known_prime(self, number):
        return number in self._known_primes


