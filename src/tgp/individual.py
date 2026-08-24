from . import programs

class individual:
    def __init__(
        self, 
        rng=None, 
        max_depth=0, 
        mutation=0, 
        crossover=0
    ):
        self.rng = rng
        self.max_depth = max_depth
        self.mutation = mutation
        self.crossover = crossover

        # initialize the tree
        self.initialize_individual()

    def initialize_individual(self):
        self.grow_tree()

    def grow_tree(self):
        pass
