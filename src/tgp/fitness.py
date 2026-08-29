import numpy as np

from utils import gen, ut

def __fitness_evaluator(program):
    # measures average absolute error from actual to prediction
    samples = gen.sample_data()
    y_out = (np.vectorize(program.compute_tree))(samples[:, 0])
    abs_err = np.abs(samples[:, 1] - y_out)
    return abs_err

def fitness_rank(population):
    # have to define otype, was triggering generator over and over to discover dtype on its own
    total_error = (np.vectorize(__fitness_evaluator, otypes=[np.float64]))(population)
    sorted_index = np.argsort(total_error)
    sorted_err = total_error[sorted_index]
    sorted_pop = population[sorted_index]
    return np.array(list(zip(sorted_err, sorted_pop)))