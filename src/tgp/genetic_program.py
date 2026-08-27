import numpy as np

from utils import out, ut

from . import individual, fitness, crossover

class genetic_program:
    def __init__(
        self,
        max_pop=0, 
        max_size=0,
        max_generation=0,
    ):
        self.max_generation = max_generation
        self.max_pop = max_pop
        self.max_size = max_size
        self.population = np.array([
            individual.individual(max_size=self.max_size) for _ in range(self.max_pop)])

    def train(self):
        # size = crossover.subtree_size(self.population[0].root.args[1])
        # print(size)

        # for gen in range(self.max_generation):
        #     out.logger(
        #         msg = f"Generation: {gen + 1} / {self.max_generation}", 
        #         primer="\r", no_return=True, flush=True)

        # do evaluation
        # rank = fitness.fitness_rank(self.population)
        # print(rank[0][0], rank[0][1].genotype)
        # do crossovers (need some form of heuristic to decide which parent to combine)
        # for _ in range(2000):
        #     p1 = self.population[self.rng.integers(0, len(self.population))]
        #     p2 = self.population[self.rng.integers(1, len(self.population))]
        #     crossover.recombination(p1, p2)
        pass