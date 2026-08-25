import numpy as np

from utils import generate_data as gen

def __fitness_evaluator(program):
    # measures total absolute error from actual to prediction
    samples = gen.sample_data()
    y_out = (np.vectorize(program.compute_tree))(samples[:, 0])
    return np.sum(np.abs(samples[:, 1] - y_out))

def fitness_rank(population):
    # have to define otype, was triggering generator over and over to figure out dtype
    total_error = (np.vectorize(__fitness_evaluator, otypes=[np.float64]))(population)
    sorted_index = np.argsort(total_error)
    sorted_pop = population[sorted_index]
    return sorted_pop