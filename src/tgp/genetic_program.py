from . import individual
from utils import out

class genetic_program:
    def __init__(
        self, 
        rng=None, 
        max_pop=0, 
        max_depth=0, 
        max_generation=0, 
        mutation=0, 
        crossover=0
    ):
        self.rng = rng
        self.max_generation = max_generation
        self.max_pop = max_pop
        self.max_depth = max_depth
        self.population = [individual.individual(
            rng=self.rng, 
            max_depth=self.max_depth, 
            mutation=mutation, 
            crossover=crossover) for _ in range(self.max_pop)]

    def train(self):
        for gen in range(self.max_generation):
            out.logger(
                msg = f"Generation: {gen + 1} / {self.max_generation}", 
                primer="\r", no_return=True, flush=True)

            # do mutation and crossovers

            # do evaluation
