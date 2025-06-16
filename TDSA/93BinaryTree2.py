

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

#function to flip (mirror) a binary tree
def flip_tree(root):
#basecase: if the current node is None, return None
    if root is None:
        return None
#recursively flip the left subtree
    left = flip_tree(root.left)
#recursively flip the right subtree
    right = flip_tree(root.right)

#swap the left and right children
    root.left = right
    root.right = left

#return the current node after flipping its children
    return root

# Define a simple binary tree node class
class Node:
  def __init__(self, val):
    self.val = val
    self.left = None
    self.right = None

# Helper function to print tree in-order for visual verification
def print_inorder(root):
  if root is None:
    return
  print_inorder(root.left)
  print(root.val, end=' ')
  print_inorder(root.right)

# Build a sample tree:
#     a
#    / \
#   b   c
#  /     \
# d       e

a = Node('a')
b = Node('b')
c = Node('c')
d = Node('d')
e = Node('e')

a.left = b
a.right = c
b.left = d
c.right = e

print("Original tree in-order:")
print_inorder(a)  # Output: d b a c e

# Flip the tree
flip_tree(a)

print("\nFlipped tree in-order:")
print_inorder(a)  # Output: e c a b d



#lefty nodes
"""
write a function, lefty_nodes, that takes in the root of a binary tree. The function should return a list containing the left-most value on every level of the tree. The list must be ordered in a top-down fashion where the root is the first item.
"""

#Function to collect the left-most node at each level of a binary tree
def lefty_nodes(root):
#list to store the left-most values at each level
    values = []
#start the traversal from root at level 0
    traverse(root, 0, values)
#return the collected left-most node values
    return values

#helper fuction to perform DFS traversal while tracking level and left-most nodes
def traverse(root, level, values):
#basecase: if the node is None, return
    if root is None:
        return 

#if this is the first node encountered at this level, it;s the left-most
    if len(values) == level:
        values.append(root.val)
#Recur on the left subtree first to ensure left-most node is seen first 
    traverse(root.left, level + 1, values)
#then recur on the righ subtree
    traverse(root.right, level + 1, values)

# Define a basic binary tree node class
class Node:
  def __init__(self, val):
    self.val = val
    self.left = None
    self.right = None

# Build the binary tree:
#       a
#      / \
#     b   c
#    /   / \
#   d   e   f
#          /
#         g

a = Node('a')
b = Node('b')
c = Node('c')
d = Node('d')
e = Node('e')
f = Node('f')
g = Node('g')

a.left = b
a.right = c
b.left = d
c.left = e
c.right = f
f.left = g

# Call the function and print result
print(lefty_nodes(a))  # Expected output: ['a', 'b', 'd', 'g']

