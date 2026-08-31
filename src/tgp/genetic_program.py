import numpy as np

from utils import out, ut, gen
from . import individual, fitness, crossover

class genetic_program:
    def __init__(
        self,
        max_pop=0, 
        max_size=0,
        max_generation=0,
        parent_percent=0,
        nf_parent_percent=0
    ):
        self.max_generation = max_generation
        self.max_pop = max_pop
        self.max_size = max_size
        self.parent_percent = parent_percent
        self.nf_parent_percent = nf_parent_percent
        self.population = np.array([
            individual.individual(max_size=self.max_size) for _ in range(self.max_pop)])

    def train(self):
        for generation in range(self.max_generation):
            rank = fitness.fitness_rank(self.population)

            cutoff_index = int(len(rank) * self.parent_percent)
            top_performers = rank[0:cutoff_index]
            bottom_performers = gen.rng.choice(rank[cutoff_index: len(rank)], size=int(len(rank) * self.nf_parent_percent))
            
            new_population = np.concatenate([top_performers, bottom_performers])
            missing_offspring = self.max_pop - len(new_population)

            offspring = []
            for _ in range(missing_offspring):
                if len(offspring) >= missing_offspring:
                    break

                parents = gen.rng.choice(new_population, size=2)
                c1, c2 = crossover.recombination(parents[0].genotype, parents[1].genotype)
                offspring.append(individual.individual(max_size=self.max_size, genotype=c1))
                offspring.append(individual.individual(max_size=self.max_size, genotype=c2))

            offspring = offspring[0: missing_offspring]
            self.population = np.concatenate([new_population, offspring])

            out.logger(
                msg = f"Generation: {generation + 1} / {self.max_generation}", 
                primer="\r", no_return=True, flush=True)

        return self.population[0]