import numpy as np
import configs as cf

from utils import gen, gp
from tgp import genetic_program as tgp

def setup():
    print('Setting up...')
    gen.seed_random()
    gen.generate_data()

    best_program = run_model()

    # test data
    gp.scatter_plot(y=gen.data[:, 1], x=gen.data[:, 0])
    gp.save_plot()

def run_model():
    print('Training...')
    model = tgp.genetic_program(
        max_pop=cf.MAX_POP, 
        max_size=cf.MAX_SIZE, 
        max_generation=cf.GENERATION)
    best_program = model.train()