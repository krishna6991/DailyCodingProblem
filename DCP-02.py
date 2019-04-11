#serialize and desiralize binary tree in python
#assert sediarilize(serialize(node).left.left.data == root.left.left.data)

import pickle

class Node:
    def __init__(self,data, left=None, right=None):
        self.left = left
        self.right= right
        self.data=data

root = Node('root', Node('left', Node('left.left')), Node('right'))

b=pickle.dumps(root)
c = pickle.loads(b)
print(c.left.left.data == root.left.left.data)
