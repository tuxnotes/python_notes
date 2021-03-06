
from collections import Iterable

class PrimeNumbers(Iterable):
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __iter__(self):
        for k in range(self.a, self.b +1):
            if self.is_prime(k):
                yield k

    def is_prime(self, k):
        # if k < 2:
        #    return False

        # [2, k-1]
        # for x in range(2, k):
        #    if k % x == 0:
        #        return False
        # return True
        return False if k < 2 else all(map(lambda x: k % x, range(2, k)))

pn = PrimeNumbers(1,30)
for n in pn:
    print(n)
