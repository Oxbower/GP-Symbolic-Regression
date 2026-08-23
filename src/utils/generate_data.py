import numpy as np

import configs as cf

def add_noise(size):
    np.random.seed(cf.SEED)
    return np.random.rand(size,) * cf.VARIANCE

def generate_data(fx):
    print('Generate data...')
    x = np.linspace(start=cf.START, stop=cf.STOP, num=cf.NUM_SAMPLES, endpoint=True)

    data = fx(x) + add_noise(x.shape[0])

    return (x, data)