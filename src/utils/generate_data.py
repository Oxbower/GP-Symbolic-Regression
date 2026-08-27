import numpy as np
import configs as cf

data = None
rng = np.random.default_rng()

def seed_random():
    if cf.ENABLE_SEED:
        print(f'Seeded Run -> {cf.SEED}')
    globals()['rng'] = np.random.default_rng(seed=cf.SEED) if cf.ENABLE_SEED else rng

def __regress_func(x):
    return 5 * np.sin(x)

def add_noise(size=0):
    rand_mat = rng.normal(loc=0, scale=cf.VARIANCE, size=size)
    return rand_mat * cf.VARIANCE

def __generate_data():
    print('Generate data...')
    x = np.linspace(start=cf.START, stop=cf.STOP, num=cf.NUM_SAMPLES, endpoint=True)
    y = __regress_func(x) + add_noise(x.shape[0])
    globals()['data'] = np.array(list(zip(x, y)))

def generate_data():
    if data is None:
        __generate_data()

def sample_data():
    if data is not None:
        return rng.choice(data, size=cf.SAMPLE_SIZE)