import numpy as np

from utils import out

from . import individual, fitness

class genetic_program:
    def __init__(
        self, 
        rng,
        max_pop=0, 
        max_size=0, 
        max_generation=0, 
        mutation=0, 
        crossover=0
    ):
        self.rng = rng
        self.max_generation = max_generation
        self.max_pop = max_pop
        self.max_size = max_size
        self.population = np.array([individual.individual(
            rng=self.rng, 
            max_size=self.max_size, 
            mutation=mutation, 
            crossover=crossover) for _ in range(self.max_pop)])

    def train(self):
        pop_ranked = fitness.fitness_rank(self.population)

        # for gen in range(self.max_generation):
        #     out.logger(
        #         msg = f"Generation: {gen + 1} / {self.max_generation}", 
        #         primer="\r", no_return=True, flush=True)

        #     # do evaluation

        #     # do mutation and crossovers

