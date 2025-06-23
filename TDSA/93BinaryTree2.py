#Binary search tree
"""
All values to the left of a parent must be less than the parent
All values to the right of a parent must be greater than or equal to the parent
"""

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




#binary search tree includes
"""
Write a function, binary_search_tree_includes, that takes in the root of a binary search tree containing numbers and a target value. The function should return a boolean indicating whether or not the target is found within the tree.
"""

#Funtion to determine if a binary search tree(BST) contains a target
def binary_search_tree_includes(root, target):
#basecase: 
    if root is None:
        return False
#if the current node matches the target, return True
    if root.val == target:
        return True
#if the target is less than the current node's value, search the left subtree

    if target < root.val:
        return binary_search_tree_includes(root.left, target)
#if the target is greater than or equal to the current node's value, search the right subtree
    else:
        return binary_search_tree_includes(root.right, target)

# Define a basic binary tree node class
class Node:
  def __init__(self, val):
    self.val = val
    self.left = None
    self.right = None

# Construct the BST:
#       10
#      /  \
#     5   15
#    / \    \
#   2   7    20

a = Node(10)
b = Node(5)
c = Node(15)
d = Node(2)
e = Node(7)
f = Node(20)

a.left = b
a.right = c
b.left = d
b.right = e
c.right = f

# Test the function
print(binary_search_tree_includes(a, 7))   # Expected: True
print(binary_search_tree_includes(a, 13))  # Expected: False



#is binary search tree
"""
Write a function, is_binary_search_tree, that takes in the root of a binary tree. The function should return a boolean indicating whether or not the tree satisfies the binary search tree property.
"""
#function to check whether a binary tree is a binary search tree(BST)
def is_binary_search_tree(root):
#initialize an empty list to store in-order traversal values
    values = []
#perform in-order traversal to fill the list
    in_order_traversal(root, values)
#check if the resulting list is sorted
    return is_sorted(values)

#helper function to perferm in-order traversal and collect node values 

def in_order_traversal(root, values):
#basecase: if the node is None, return
    if root is None:
      return
#traverse left subtree
    in_order_traversal(root.left, values)
#visit current node
    values.append(root.val)
#traverse right subtree
    in_order_traversal(root.right, values)

#helper function to check if a list of numbers is sorted in ascending order
def is_sorted(numbers):
#Iterate through the list, comparing each element with the next
    for i in range(0, len(numbers) - 1):
        current = numbers[i]
        next = numbers[i + 1]
#if any element is greated than the next the list is not sorted
        if next < current:
          return False
#if no such case was found the list is sorted
    return True

# Define a basic binary tree node class
class Node:
  def __init__(self, val):
    self.val = val
    self.left = None
    self.right = None

# Valid BST example:
#       10
#      /  \
#     5   15
#    / \    \
#   2   7    20

a = Node(10)
b = Node(5)
c = Node(15)
d = Node(2)
e = Node(7)
f = Node(20)

a.left = b
a.right = c
b.left = d
b.right = e
c.right = f

# Should return True since the tree is a valid BST
print(is_binary_search_tree(a))  # Output: True

# Invalid BST example:
#       10
#      /  \
#     5    8  <- invalid because 8 is less than 10 but is in right subtree

x = Node(10)
y = Node(5)
z = Node(8)

x.left = y
x.right = z

# Should return False
print(is_binary_search_tree(x))  # Output: False



#post order
"""
Write a function, post_order, that takes in the root of a binary tree. The function should return a list containing the post-ordered values of the tree
"""

#function to perform post-order traversal on a binary tree
def post_order(root):
#initialize an empty list to collect node values
    values = []
#begin the recursive post-order traversal
    post_order_traversal(root, values)
#return the list of values after traversal
    return values
#helper function for recursive post-order traversal
def post_order_traversal(root, values):
#basecase: if current node is None, do nothing
    if root is None:
        return 
#recursively traverse the left subtree
    post_order_traversal(root.left, values)
#recursively traverse the right subtree
    post_order_traversal(root.right, values)
#after left and right children, visit the current node
    values.append(root.val)

# Define a simple binary tree node class
class Node:
  def __init__(self, val):
    self.val = val
    self.left = None
    self.right = None

# Construct the binary tree:
#       a
#      / \
#     b   c
#    / \   \
#   d   e   f

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

# Post-order traversal should visit nodes in this order: d, e, b, f, c, a
print(post_order(a))  # Output: ['d', 'e', 'b', 'f', 'c', 'a']


#build tree in post
"""
write a function, build_tree_in_post, that takes in a list of in-ordered values and a list of post-ordered values for a binary tree. The function should build a binary tree that has the given in-order and post-order traversal structure. The function should return the root of this tree.
"""

#function to reconstruct a binary tree from in-order and post-order traversals
def build_tree_in_post(in_order, post_order):
#basecase: if in-order is empty, there's no tree/subtree to build
    if len(in_order) == 0:
        return None
#the last value in order is the root of the current subtree
    value = post_order[-1]
    root = Node(value)
#Find the root's index in in-order to separate the left and right subtrees
    mid = in_order.index(value)
#extract left and right in-order slices
    left_in = in_order[:mid]
    right_in = in_order[mid + 1:]

#use the lengths to slice the post-order list accordingly
    left_post = post_order[:len(left_in)]
    right_post = post_order[len(left_in):-1]

#Recursively build the left and right subtrees
    root.left = build_tree_in_post(left_in, left_post)
    root.right = build_tree_in_post(right_in, right_post)

#return the reconstructed tree root
    return root

# Simple binary tree node class
class Node:
  def __init__(self, val):
    self.val = val
    self.left = None
    self.right = None

# Helper to print pre-order traversal (root-left-right) for verification
def print_pre_order(root):
  if root is None:
    return
  print(root.val, end=' ')
  print_pre_order(root.left)
  print_pre_order(root.right)

# Example:
# Tree structure:
#       A
#      / \
#     B   C
#        / \
#       D   E

in_order = ['B', 'A', 'D', 'C', 'E']
post_order = ['B', 'D', 'E', 'C', 'A']

# Build the tree
tree = build_tree_in_post(in_order, post_order)

# Print pre-order traversal to verify structure
print_pre_order(tree)  # Output should be: A B C D E



#build tree in pre
"""
Write a function, build_tree_in_pre, that takes in a list of in-ordered values and a list of pre-ordered values for a binary tree. The function should build a binary tree that has the given in-order traversal structure. The function should return the root of this tree. 
"""
#Builds a binary tree from in-order and pre-order traversals
def build_tree_in_pre(in_order, pre_order):
#basecase: if-inorder list is empty, there;s no tree/subtree to build
    if len(in_order) == 0:
        return None
#The first element of pre-order list is always the root of the (sub) tree
    value = pre_order[0]
    root = Node(value)
#Find the index of the root in the in-order list to split left/right subtrees
    mid = in_order.index(value)
#slice in-order list to get left and right subtree node values
    left_in_order = in_order[:mid]
    right_in_order = in_order[mid + 1:]

#calculate size of the left subtree to slice pre-order accordingly
    left_size = len(left_in_order)

#slice pre-order list to get left and right subtree values 
#skip index 0 because its the root
    left_pre_order = pre_order[1: 1 + left_size]
    right_pre_order = pre_order[1 + left_size:]

#recursively build the left subtree
    root.left = build_tree_in_pre(left_in_order, left_pre_order)
#recursively build the right subtree
    root.right = build_tree_in_pre(right_in_order, right_pre_order)
#return the root of the constructed binary tree
    return root

# Node class definition
class Node:
  def __init__(self, val):
    self.val = val
    self.left = None
    self.right = None

# Helper function to print pre-order traversal for verification
def print_pre_order(root):
  if root is None:
    return
  print(root.val, end=' ')
  print_pre_order(root.left)
  print_pre_order(root.right)

# Test input
in_order = ['B', 'A', 'D', 'C', 'E']
pre_order = ['A', 'B', 'C', 'D', 'E']

# Build tree and print pre-order to confirm structure
root = build_tree_in_pre(in_order, pre_order)
print_pre_order(root)  # Output: A B C D E

### On solution
"""
# Builds a binary tree from in-order and pre-order traversal lists
def build_tree_in_pre(in_order, pre_order):
  # Create a map from node value to its index in in-order for O(1) lookups
  in_order_index = {}
  for i in range(0, len(in_order)):
    ele = in_order[i]
    in_order_index[ele] = i

  # Call the recursive helper with index boundaries
  return _build_tree_in_pre(
    in_order, pre_order, in_order_index,
    0, len(in_order) - 1,     # in-order start and end
    0, len(pre_order) - 1     # pre-order start and end
  )

# Recursive helper function to build the tree
def _build_tree_in_pre(in_order, pre_order, in_order_index,
                       in_start, in_end, pre_start, pre_end):
  # Base case: no nodes to construct
  if in_end < in_start:
    return None

  # First element in pre-order is the root of current subtree
  value = pre_order[pre_start]
  root = Node(value)

  # Find the index of root in in-order to split left and right subtrees
  mid = in_order_index[value]

  # Number of nodes in left subtree
  left_size = mid - in_start

  # Recursively build the left subtree
  root.left = _build_tree_in_pre(
    in_order, pre_order, in_order_index,
    in_start, mid - 1,                      # in-order left subtree
    pre_start + 1, pre_start + left_size    # pre-order left subtree
  )

  # Recursively build the right subtree
  root.right = _build_tree_in_pre(
    in_order, pre_order, in_order_index,
    mid + 1, in_end,                        # in-order right subtree
    pre_start + left_size + 1, pre_end      # pre-order right subtree
  )

  # Return the constructed subtree rooted at current node
  return root
"""


#is tree balanced
"""
Write a function, is_tree_balanced, that takes in the root of a binary tree. The function should return a boolean indicating whether or not the tree is "balanced"

A "balanced" binary tree where the height between the left and right subtrees differ by at most 1 for every node.
"""

def check_height_balance(root):
#if the node is None(empty tree or leaf's child), its height is 0
    if root is None:
        return 0
#Recursively get the height of the left subtree
    left_height = check_height_balance(root.left)
#if left subtree is unbalanced, propagate -1 upward
    if left_height == -1:
        return -1
#Recursively get the height of the right subtree
    right_height = check_height_balance(root.right)
#if right substree is unbalanced, propogate -1 upward
    if right_height == -1:
        return -1
#If the current node's left and right subtrees differ in height by more than 1, it's unbalanced
    if abs(left_height - right_height) > 1:
        return -1
    else:
#return the height of this node as 1 + max height of its subtrees
        return 1 + max(left_height, right_height)
def is_tree_balanced(root):
    # Returns True if the tree is balanced (check_height_balance didn't return -1)
    return check_height_balance(root) > -1

# Define a basic binary tree Node class
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

# Constructing a balanced binary tree:
#       A
#      / \
#     B   C
#    /
#   D

root = Node('A')
root.left = Node('B')
root.right = Node('C')
root.left.left = Node('D')

print(is_tree_balanced(root))  # Output: True

# Making the tree unbalanced by adding more depth to one side
root.left.left.left = Node('E')
root.left.left.left.left = Node('F')

print(is_tree_balanced(root))  # Output: False
