import numpy as np
import configs as cf

data = None
default_rng = np.random.default_rng()

def seed_random():
    if cf.ENABLE_SEED:
        print(f'Seeded Run -> {cf.SEED}')
    rng = np.random.default_rng(seed=cf.SEED) if cf.ENABLE_SEED else default_rng
    return rng

def regress_func(x):
    return np.sin(x)

def add_noise(rng, variance=0, size=0):
    rand_mat = rng.random((size,))
    return rand_mat * variance

def __generate_data(rng):
    print('Generate data...')
    x = np.linspace(start=cf.START, stop=cf.STOP, num=cf.NUM_SAMPLES, endpoint=True)
    data = regress_func(x) + add_noise(rng, cf.VARIANCE, x.shape[0])
    return np.array(list(zip(x, data)))

def generate_data(rng):
    if data is None:
        return __generate_data(rng)
    return data