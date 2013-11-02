from collections import deque
#Iterative inorder traversal of a BST. Useless for this code.
def in_order_iter(root):
    stack = deque()
    curr = root
    while True:
        while curr:
            stack.appendleft(curr)
            curr = curr.left
        if len(stack):
            curr = stack.popleft()
            print curr.value
            curr = curr.right
        else:
            break

class Node:
    def __init__(self, value, left, right):
        self.right = right
        self.left = left
        self.value = value

def construct_bst_from_sorted_array(a, i, j):
    if j == i:
        return None
    mid = (i + j) / 2
    return Node(
        a[mid], 
        construct_bst_from_sorted_array(a, i, mid),
        construct_bst_from_sorted_array(a, mid + 1, j)
    )

def order(asc = True):
    def in_order(node):
        if node:
            small = node.left if asc else node.right
            large = node.right if asc else node.left
            for value in in_order(small):
                yield value
            yield node.value
            for value in in_order(large):
                yield value
    return in_order

a = [1, 6, 7, 15, 19, 21, 28]
tree = construct_bst_from_sorted_array(a, 0, len(a))
k = 26

asc_in_order = order(True)(tree)
dsc_in_order = order(False)(tree)

left = asc_in_order.next()
right = dsc_in_order.next()

while True:
    print left, right
    if left + right == k:
        print left, right
        break
    elif left + right < k:
        left = asc_in_order.next()
    else:
        right = dsc_in_order.next()
    


