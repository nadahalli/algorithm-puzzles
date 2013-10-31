class Node:
    def __init__(self, value, left, right):
        self.value = value
        self.right = right
        self.left = left

    def __repr__(self):
        return str(self.value)

def insert_at_left(head, tail, value):
    new = Node(value, None, None)
    if head == None:
        return new, new
    else:
        head.left = new
        new.right = head
        return new, tail

def delete_node(head, tail, node):
    if head == node:
        if node.right != None:
            head = node.right
            node.right.left = None
        else:
            head = None
        del node
    else:
        if node.right == None:
            node.left.right = None
            tail = node.left
        else:
            node.left.right = node.right
            node.right.left = node.left
        del node
    return head, tail

def print_dll(head):
    while head != None:
        print head.value, ' -> ', 
        head = head.right
    print 'X'

tail = head = None
seen = {}

a = [1, 1, 2, 3, 4, 5, 2, 3]

for i in a:
    if i not in seen:
        head, tail = insert_at_left(head, tail, i)
        seen[i] = head
    else:
        head, tail = delete_node(head, tail, seen[i])
        del seen[i]
    print i, tail.value if tail else 'None', seen
