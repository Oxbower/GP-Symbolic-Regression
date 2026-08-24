import numpy as np

__eph_constant = None

def __add(x, y):
    return x + y

def __sub(x, y):
    return x - y

def __div(x, y):
    if y == 0:
        return 0
    return x / y

def __mult(x, y):
    return x * y

def __const(rng=None):
    low = 0
    high = 10
    return np.random.randint(low=low, high=high) if rng is None else rng.integer(low=low, high=high)

def __erc(rng=None, mutate=False):
    if __eph_constant != None or not mutate:
        return __eph_constant
    return np.random.rand() if rng is None else rng.random()

def random_program(rng=None, leaf=False):
    programs = [__add, __sub, __div, __mult]
    if leaf:
        programs = [__erc, __const]
    return np.random.choice(programs) if rng is None else rng.choice(programs)