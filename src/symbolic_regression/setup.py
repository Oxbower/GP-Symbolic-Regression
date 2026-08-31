import time
import numpy as np
import configs as cf

from utils import gen, gp
from tgp import genetic_program as tgp

def setup():
    print('Setting up...')
    gen.seed_random()
    gen.generate_data()

    # test data
    gp.scatter_plot(y=gen.data[:, 1], x=gen.data[:, 0], title='Y Actual')
    gp.save_plot('y_actual')

    best_program = run_model()

    post_train_test(best_program)

def post_train_test(program):
    print('Testing...')
    x = gen.data[:, 0]
    y_actual = gen.data[:, 1]
    y = np.array([program.compute_tree(val) for val in x])
    abs_err = np.abs(y_actual - y)

    gp.scatter_plot(y=y, x=x, title='Y Prediction')
    gp.save_plot('y_pred')

    total_error = round(np.sum(abs_err) / len(abs_err), 2)
    print(f"Mean Absolute Error: {total_error}%")

def run_model():
    print('Training...')
    model = tgp.genetic_program(
        max_pop=cf.MAX_POP, 
        max_size=cf.MAX_SIZE,
        max_generation=cf.GENERATION,
        parent_percent=cf.PARENT_PERCENT,
        nf_parent_percent=cf.NON_FIT_PARENT_PERCENT)

    start_time = time.time()
    best_program = model.train()
    end_time = time.time()
    training_time = round((end_time - start_time) / 60, 2)

    print(f'\nTraining Time: {training_time} -- Program Length: {len(best_program.genotype)}')
    # print(np.array(best_program.genotype))

    return model.population[0]