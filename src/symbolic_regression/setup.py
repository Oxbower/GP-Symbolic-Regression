import numpy as np
import configs as cf

from utils import gen, gp
from tgp import genetic_program as tgp

def setup():
    print('Setting up...')
    rng = gen.seed_random()
    data = gen.generate_data(rng)

    best_program = run_model(rng=rng)

    # test data
    gp.scatter_plot(y=data[:, 1], x=data[:, 0])
    gp.save_plot()

def run_model(rng):
    print('Training...')
    model = tgp.genetic_program(
        rng=rng, 
        max_pop=cf.MAX_POP, 
        max_size=cf.MAX_SIZE, 
        max_generation=cf.GENERATION, 
        mutation=cf.MUTATION, 
        crossover=cf.CROSSOVER)
    best_program = model.train()