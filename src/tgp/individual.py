from collections import deque
from copy import deepcopy

from . import node as td
from . import programs

class individual:
    def __init__(
        self, 
        rng, 
        max_size=0,
        mutation=0,
        crossover=0
    ):
        self.rng = rng
        self.max_size = max_size
        self.mutation = mutation
        self.crossover = crossover
        self.size = 0

        # initialize the tree
        self.__initialize_individual()

    def __initialize_individual(self):
        self.__grow_tree()

    def __grow_tree(self):
        # list of all nodes that need to be visited
        unvisited_nodes = deque()
        inputs = 0

        # generate root first (BFS)
        # (name, num arguments, function)
        prog = programs.random_program(rng=self.rng)
        root = td.node(res=0, op=prog[2])
        self.size += 1

        for args in range(prog[1]):
            arg = td.node()
            root.set_arg(n_node=arg)
            unvisited_nodes.append(arg)

        # visit all nodes in the tree and populate them
        while self.size < self.max_size:
            prog = programs.random_program(rng=self.rng)
            unode = unvisited_nodes.popleft()
            unode.set_op(op=prog[2])
            self.size += 1

            for args in range(prog[1]):
                arg = td.node()
                unode.set_arg(n_node=arg)
                unvisited_nodes.append(arg)

        while len(unvisited_nodes) > 0:
            prog = programs.random_program(rng=self.rng, leaf=True)
            unode = unvisited_nodes.popleft()
            unode.set_res(prog[2](rng=self.rng))
            self.size += 1

        self.root = root

    def __phenotype(self, input):
        # stack based eval
        stack = deque()
        stack.append(self.root)

        while len(stack) > 0:
            peek = stack[-1]
            all_leaves = True
            # store args that need to be computed
            for arg in peek.args:
                if arg.res is None:
                    stack.append(arg)
                    all_leaves = False
            # if all leaves allow computation of node
            if all_leaves:
                node = stack.pop()
                args = node.args
                res = [input if arg.res == 'input' else arg.res for arg in args]
                node.res = node.op(*res)
                # reset results after use
                for arg in args:
                    if arg.op is not None:
                        arg.res = None

        return self.root.res

    def compute_tree(self, input):
        """ get output based on input, converts genotype to phenotype
        """
        return self.__phenotype(input)