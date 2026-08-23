import numpy as np

from utils import gen, gp

def regress_func(x):
    return np.sin(x*(np.pi)/4)

def setup():
    x, data = gen.generate_data(regress_func)

    # test data
    gp.scatter_plot(y=data, x=x)
    gp.save_plot()