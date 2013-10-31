class Node:
    def __init__(self, value, left, right, size):
        self.value = value
        self.left = left
        self.right = right
        self.size = size
        
def find_ith_node(root, i):
    if i == root.size - 1:
        return root
    else:
        left_order = root.left.size 
        if i < left_order:
            return find_ith_node(root.left, i)
        elif i >= left_order:
            return find_ith_node(root.right, i - left_order)

import random
def select_random(root):
    i = random.choice(range(0, root.size))
    return find_ith_node(root, i)
