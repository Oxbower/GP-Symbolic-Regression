import numpy as np

def add_noise(rng, variance=0, size=0):
    rand_mat = rng.random((size,))
    return rand_mat * variance

def generate_data(rng, variance=0, start=0, stop=0, num_samples=0, fx=()):
    print('Generate data...')
    x = np.linspace(start=start, stop=stop, num=num_samples, endpoint=True)
    data = fx(x) + add_noise(rng, variance, x.shape[0])

    return (x, data)