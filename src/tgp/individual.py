from collections import deque

from . import programs

class individual:
    def __init__(
        self,
        max_size=0,
    ):
        self.max_size = max_size
        self.genotype = []

        # initialize the tree
        self.__initialize_individual()

    def __initialize_individual(self):
        self.__grow_tree()

    def __grow_tree(self):
        unvisited_nodes = deque()

        # generate genotype (BFS)
        prog = programs.random_program()
        gene = {'op': prog[2], 'args': [i + 1 for i in range(prog[1])]}
        self.genotype.append(gene)
        unvisited_nodes.append(0)

        # build out non-leaf nodes
        while len(self.genotype) < self.max_size:
            peek = self.genotype[unvisited_nodes[0]]

            for index in peek['args']:
                prog = programs.random_program()
                gene = {'op': prog[2], 'args': []}
                unvisited_nodes.append(index)
                for args in range(prog[1]):
                    gene['args'].append((self.genotype[-1]['args'][-1] + 1) + args)
                self.genotype.append(gene)

            unvisited_nodes.popleft()

        # build leaves
        while len(unvisited_nodes) > 0:
            peek = self.genotype[unvisited_nodes[0]]
            prog = programs.random_program(leaf=True)
            for _ in peek['args']:
                gene = {'value': prog[2]()}
                self.genotype.append(gene)
            unvisited_nodes.popleft()

        # print(self.genotype)

    def __phenotype(self, input):
        # stack based eval
        stack = deque()
        stack.append({'pos': 0, 'genome': self.genotype[0]})
        result = [None for i in range(len(self.genotype))]

        while len(stack) > 0:
            peek = stack[-1]['genome']
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
                # print(peek['op'], args, peek['op'](*args))
                result[stack[-1]['pos']] = peek['op'](*args)
                stack.pop()

        # print(self.genotype)
        return result[0]
        

    def compute_tree(self, input):
        """ get output based on input, converts genotype to phenotype
        """
        return self.__phenotype(input)