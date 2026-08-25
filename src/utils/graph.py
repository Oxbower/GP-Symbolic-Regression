import matplotlib.pyplot as plt
import numpy as np

def save_plot():
    plt.savefig(f'./graph/random_data.png')
    plt.close()

def scatter_plot(x, y):
    plt.figure()
    plt.scatter(x, y)
    plt.title('Data Plot')