

#Lowest common ancestor
"""
write a functiion, lowest_common_ancestor, that takes in the root of a binary tree and two values. The function should return the value of the lowest common ancestor of the two values in the tree.
"""

#Function to find the lowest common ancestor of two nodes in a binary tree
def lowest_common_ancestor(root, val1, val2):
#find path from root to val1
    path1 = find_path(root, val1)
#find path from root to val2
    path2 = find_path(root, val2)
#convert one path to a set for faster lookup
    set2 = set(path2)

#iterate through path1 and return the first node also in path2
    for val in path1:
        if val in set2:
            return val

#Helper function to find path from root to target_val
def find_path(root, target_val):
#basecase: return None if root is None
    if root is None:
        return None
#if root value is target_val, return a path containing just root
    if root.val == target_val:
        return [root.val]
#recursively search in left subtree
    left_path = find_path(root.left, target_val)
    if left_path is not None:
#append current node to path
        left_path.append(root.val)
        return left_path

#Recursively search in right subtree
    right_path = find_path(root.right, target_val)
    if right_path is not None:
#Append current node to path
        right_path.append(root.val)
        return right_path
#return None if target_val not found in either subtree
    return None

# Define a simple binary tree node class
class Node:
  def __init__(self, val):
    self.val = val
    self.left = None
    self.right = None

# Build sample tree:
#        a
#       / \
#      b   c
#     / \   \
#    d   e   f

a = Node('a')
b = Node('b')
c = Node('c')
d = Node('d')
e = Node('e')
f = Node('f')

a.left = b
a.right = c
b.left = d
b.right = e
c.right = f

# Find lowest common ancestor of 'd' and 'e'
print(lowest_common_ancestor(a, 'd', 'e'))  # -> 'b'

# Find lowest common ancestor of 'd' and 'f'
print(lowest_common_ancestor(a, 'd', 'f'))  # -> 'a'




#flip tree
"""
Write a function, flip_tree, that takes in the root of a binary tree. The function should flip the binary tree, turning left subtrees into right subtrees and vice-versa. This flipping should occur in-place by modifying the original tree. The function should return the root of the tree.
"""
