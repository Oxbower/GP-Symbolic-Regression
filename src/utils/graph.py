import matplotlib.pyplot as plt
import numpy as np

def save_plot(file_name):
    plt.savefig(f'./graph/{file_name}.png')
    plt.close()

def scatter_plot(**args):
    plt.figure()
    plt.scatter(args['x'], args['y'])
    plt.title(args['title'])