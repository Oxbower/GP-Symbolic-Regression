import numpy as np
import configs as cf

from copy import deepcopy
from utils import gen, ut
from collections import deque

def __slice_genome(genome):
    # subtree is always bounded by the next index listed relative to its position on the parent
    # i.e., if node 3 is chosen and the parent has child [3, 7, 13], then node 3 is bounded
    # [3, 7). can just slice the array to get entire subtree i.e., genome[3:7]

    genome_length = len(genome)

    # if just a single node (leaf)
    if genome_length <= 1:
        return [0], genome

    # 1 = Non-Leaf, 0 = Leaf 
    node_type = gen.rng.choice([1, 0], p=[.9, .1])

    possible_roots = []
    for idx, gene in enumerate(genome):
        if (not node_type and 'value' in gene) or (node_type and 'value' not in gene):
            possible_roots.append({'pos': idx, 'gene': gene})

    gene_slice = gen.rng.choice(possible_roots)
    spliced_gene = [gene_slice['pos']]

    if node_type:
        right_most_index = gene_slice['gene']['args'][-1]

        # O(len(right_most_branch)), upper bound is just n
        while True:
            if 'value' in genome[right_most_index]:
                spliced_gene.append(right_most_index)
                break
            right_most_index = genome[right_most_index]['args'][-1]
    
    return spliced_gene, genome[spliced_gene[0]:spliced_gene[-1] + 1]

def __combine_genome(parent_splice_sequence, parent, genome_sequence):
    """
        parent_splice_sequence: the range of the gene sequence removed from parent
        genome_sequence: replacement gene sequence
    """
    prefix_parent = parent[0: parent_splice_sequence[0]]
    postfix_parent = parent[parent_splice_sequence[-1] + 1: len(parent)]

    parent_length_gap = parent_splice_sequence[-1] - parent_splice_sequence[0] + 1
    
    # this is how much to adjust index for all values > parent_splice_sequence[0]
    # for the current parent
    index_adjustment = len(genome_sequence) - parent_length_gap

    # need to walk list and check arguements of prefix and make sure they are pointing 
    # to the correct next location if its > than len of the prefix gene sequence, same
    # for postfix
    for gene in prefix_parent:
        if 'value' not in gene:
            for idx, arg in enumerate(gene['args']):
                if arg > parent_splice_sequence[0]:
                    gene['args'][idx] += index_adjustment

    for gene in postfix_parent:
        if 'value' not in gene:
            for idx, arg in enumerate(gene['args']):
                gene['args'][idx] += index_adjustment

    gene_orig_pos = genome_sequence[0]['args'][0] - 1 if 'value' not in genome_sequence[0] else 0
    for gene_idx, gene in enumerate(genome_sequence):
        if 'value' not in gene:
            for arg_idx, arg in enumerate(gene['args']):
                gene['args'][arg_idx] = abs(gene_orig_pos - arg) + parent_splice_sequence[0]

    return prefix_parent + genome_sequence + postfix_parent


def recombination(parent_1, parent_2):
    # make deep copies so arrays can be modified without cascade
    parent_1 = deepcopy(parent_1)
    parent_2 = deepcopy(parent_2)

    p1_splice, genome_slice_p1 = __slice_genome(parent_1)
    p2_splice, genome_slice_p2 = __slice_genome(parent_2)

    p1_effective_size = len(parent_1) - len(genome_slice_p1) + len(genome_slice_p2)
    p2_effective_size = len(parent_2) - len(genome_slice_p2) + len(genome_slice_p1)

    if p1_effective_size >= cf.BLOAT_CONTROL or p2_effective_size >= cf.BLOAT_CONTROL:
        return parent_1, parent_2

    child_1_genome = __combine_genome(p1_splice, parent_1, genome_slice_p2)
    child_2_genome = __combine_genome(p2_splice, parent_2, genome_slice_p1)

    return child_1_genome, child_2_genome

