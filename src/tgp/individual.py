from collections import deque

from . import programs

class individual:
    def __init__(
        self,
        max_size=0,
        genotype=None
    ):
        self.max_size = max_size
        self.genotype = genotype if genotype else []

        # initialize the tree
        if len(self.genotype) <= 0:
            self.__initialize_individual()

    def __initialize_individual(self):
        self.__grow_tree()

    def __grow_tree(self):
        unvisited_nodes = deque()

        # generate genotype (DFS -> because makes recombination easier)
        prog = programs.random_program()
        gene = {'op': prog[2], 'num_args': prog[1], 'args': []}
        self.genotype.append(gene)
        unvisited_nodes.append(0)

        # build out non-leaf
        while len(self.genotype) < self.max_size:
            prog = programs.random_program()
            gene = {'op': prog[2], 'num_args': prog[1], 'args': []}
            pos = len(self.genotype)

            peek = self.genotype[unvisited_nodes[-1]]

            if len(peek['args']) < peek['num_args']:
                peek['args'].append(len(self.genotype))

            self.genotype.append(gene)
            unvisited_nodes.append(pos)

        # build out leaves
        while len(unvisited_nodes) > 0:
            top = unvisited_nodes[-1] # gene to fill out first
            gene = self.genotype[top]
            for index in range(gene['num_args']):
                if len(gene['args']) == (index + 1):
                    continue
                prog = programs.random_program(leaf=True)
                leaf = {'value': prog[2]()}
                pos = len(self.genotype)
                gene['args'].append(pos)
                self.genotype.append(leaf)
            unvisited_nodes.pop()

    def __phenotype(self, input):
        # stack based eval
        stack = deque()
        stack.append({'pos': 0, 'genome': self.genotype[0]})
        result = [None for i in range(len(self.genotype))]

        while len(stack) > 0:
            peek = stack[-1]['genome']

            # if tree is of size 1
            if 'value' in peek:
                return input if peek['value'] == 'input' else peek['value']

            args = []

            for index in peek['args']:
                gene = self.genotype[index]

                # if a leaf node
                if 'value' in gene:
                    result[index] = input if gene['value'] == 'input' else gene['value']
                    args.append(result[index])
                    continue

                # if not leaf node
                if result[index] is not None:
                    args.append(result[index])
                    continue

                stack.append({'pos': index, 'genome': gene})

            if len(args) >= len(peek['args']):
                result[stack[-1]['pos']] = peek['op'](*args)
                stack.pop()

        return result[0]
        

    def compute_tree(self, input):
        """ get output based on input, converts genotype to phenotype
        """
        return self.__phenotype(input)