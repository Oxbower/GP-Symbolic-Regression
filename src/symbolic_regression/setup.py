import numpy as np
import configs as cf

from utils import gen, gp
from tgp import genetic_program as tgp

def regress_func(x):
    return np.sin(x)

def setup():
    print('Setting up...')
    rng = np.random.default_rng(seed=cf.SEED)
    x, data = gen.generate_data(
        rng=rng, 
        variance=cf.VARIANCE, 
        start=cf.START, 
        stop=cf.STOP, 
        num_samples=cf.NUM_SAMPLES, 
        fx=regress_func)

    best_program = run_model(rng=rng)

    # test data
    gp.scatter_plot(y=data, x=x)
    gp.save_plot()

def run_model(rng=None):
    print('Training...')
    model = tgp.genetic_program(
        rng=rng, 
        max_pop=cf.MAX_POP, 
        max_depth=cf.MAX_DEPTH, 
        max_generation=cf.GENERATION, 
        mutation=cf.MUTATION, 
        crossover=cf.CROSSOVER)
    best_program = model.train()