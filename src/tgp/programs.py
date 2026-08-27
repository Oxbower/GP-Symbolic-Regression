import numpy as np

from utils import gen

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

def __cos(x):
    return np.cos(x)

def __input():
    return 'input'

def __erc():
    values = [np.e, np.pi, gen.rng.random(), gen.rng.integers(low=-10, high=10)]
    return gen.rng.choice(values)

def random_program(leaf=False):
    """
        returns a random atomic program (uniform)

        attr:
            rng: to seed randomized programs (utilizes np default_rng)
            leaf: if want random leaf node

        returns:
            ('program name', # arguements of returned program, function call to program)
    """
    programs = [('add', 2, __add), ('sub', 2, __sub), ('div', 2, __div), ('mult', 2, __mult), ('cos', 1, __cos)]
    if leaf:
        programs = [('erc', 0, __erc), ('input', 0, __input)]
    return gen.rng.choice(programs)