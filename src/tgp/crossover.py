import numpy as np
import configs as cf

from utils import gen, ut
from collections import deque

def __allowed_growth(tree_size):
    return cf.SIZE_CAP if tree_size > cf.SIZE_CAP else cf.CO_SIZE_DRIFT + tree_size

def __pick_subtree(tree, partner_size=None, replacement_subtree_size=None):
    # never trust current tree size always rebuild
    subtree = None
    return subtree

def recombination(parent_1, parent_2):
    # tree size is allowed to grow past max_size by at most + 2
    # however hard upper bound 64 (around depth of 6 in a full binary tree) to avoid bloat
    pick1 = __pick_subtree(tree=parent_1.root)
    parent_1_size = parent_1.root.size
    pick2 = __pick_subtree(
        tree=parent_2.root,
        partner_size=parent_1_size,
        replacement_subtree_size=pick1.size
    )
    ut.tree_size(parent_1.root)
    p1 = parent_1.root.size
    ut.tree_size(parent_2.root)
    p2 = parent_2.root.size
    print(f'Size: {p1} {pick1.op or pick1.res} <-> Size: {p2} {pick2.op or pick1.res}')