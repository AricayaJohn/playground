#Binary tree

#Depth First Values
#write a function, depth_first_values, that takes in the root of a binary tree. The function should return a list containing all values of the tree in depth-first order.

def depth_first_values(root):
# If the tree is empty, return an empty list
  if not root:
    return []
# Initialize a stack with the root node (LIFO order for DFS)
  stack = [root]
# List to store the node values
  values = []
# Loop as long as there are nodes in the stack
  while stack:
# Pop the last node added (current node)
    node = stack.pop()
# Add its value to the results list
    values.append(node.val)
# Push right child first so left is processed first (stack = LIFO)
    if node.right:
      stack.append(node.right)
# Push left child to be processed next
    if node.left:
      stack.append(node.left)
# Return the collected values in DFS order
  return values



def depth_first_values(root):
# If the tree is empty, return an empty list
  if not root:
    return []
# Recursively get values from the left subtree
  left_values = depth_first_values(root.left)
# Recursively get values from the right subtree
  right_values = depth_first_values(root.right)
# Combine root value with left and right subtree values
  return [ root.val, *left_values, *right_values ]



class Node:
  def __init__(self, val):
    self.val = val
    self.left = None
    self.right = None

# Create the tree nodes
a = Node('a')
b = Node('b')
c = Node('c')
d = Node('d')
e = Node('e')
f = Node('f')

# Link the nodes
a.left = b
a.right = c
b.left = d
b.right = e
c.right = f

# Test the function
print(depth_first_values(a))  # Expected output: ['a', 'b', 'd', 'e', 'c', 'f']



#Breadth first values
#Write a function, breadth_first_values, that takes in the root of a binary tree the function should return a list containing all values of the tree in breadth-first order.

# Define a function to perform a breadth-first traversal on a binary tree
def breadth_first_values(root):
# If the tree is empty, return an empty list
  if root is None:
    return []
# Create an empty list to store the values we visit
  values = []
# Use a queue to keep track of nodes to visit (start with the root)
  queue = [root]
# Keep going as long as there are nodes in the queue
  while queue:
# Remove the first node from the queue
    current = queue.pop(0)
# Add the node's value to our result list
    values.append(current.val)
# If the node has a left child, add it to the queue
    if current.left:
      queue.append(current.left)
# If the node has a right child, add it to the queue
    if current.right:
      queue.append(current.right)
# Return the list of values we collected
  return values

#      a
#     / \
#    b   c
#   / \   \
#  d   e   f


class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

# Build the tree
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

# Call the function and print the result
print(breadth_first_values(a))  # Expected output: ['a', 'b', 'c', 'd', 'e', 'f']

# Import deque from collections to use as a queue
from collections import deque

# Define a function that performs breadth-first traversal on a binary tree
def breadth_first_values(root):
  # If the tree is empty, return an empty list
  if not root:
    return []

  # Create a queue and add the root node to it
  queue = deque([ root ])
  # This list will store the values of nodes in breadth-first order
  values = []

  # Keep looping until the queue is empty
  while queue:
    # Remove the node at the front of the queue
    node = queue.popleft()
    # Add the value of the current node to the result list
    values.append(node.val)

    # If the current node has a left child, add it to the queue
    if node.left:
      queue.append(node.left)
    
    # If the current node has a right child, add it to the queue
    if node.right:
      queue.append(node.right)
  
  # After visiting all nodes, return the list of values
  return values



#Tree sum
#write a function, tree_sum, that takes in the root of a binary tree that contains number values. The function should return the total sum of all values in the tree. 

# Define a function that returns the sum of all node values in a binary tree
def tree_sum(root):
# Base case: if the tree is empty, return 0
  if root is None:
    return 0
# Recursively add the value of the current node, the left subtree, and the right subtree
  return root.val + tree_sum(root.left) + tree_sum(root.right)



# Import deque from the collections module for efficient queue operations
from collections import deque
# Define a function that calculates the sum of all values in a binary tree
def tree_sum(root):
# If the tree is empty, return 0
  if not root:
    return 0
# Create a queue and add the root node to start BFS traversal
  queue = deque([ root ])
# Initialize the total sum to 0
  total_sum = 0
# Keep going as long as there are nodes in the queue
  while queue:
# Remove the node at the front of the queue
    node = queue.popleft()
# Add the value of the current node to the total sum
    total_sum += node.val
# If the node has a left child, add it to the queue
    if node.left:
      queue.append(node.left)
# If the node has a right child, add it to the queue
    if node.right:
      queue.append(node.right)
# After visiting all nodes, return the total sum
  return total_sum


#check test
class Node:
  def __init__(self, val):
    self.val = val
    self.left = None
    self.right = None
# Tree structure:
#      5
#     / \
#    3   7
#   / \
#  2   4

a = Node(5)
b = Node(3)
c = Node(7)
d = Node(2)
e = Node(4)

a.left = b
a.right = c
b.left = d
b.right = e

print(tree_sum(a))  # Output should be 5 + 3 + 7 + 2 + 4 = 21


#Tree includes
#write a function, tree_includes, that takes in the root of a binary and a target value. The function should return a boolean indicating whether or not the value is contained in the tree.


# Import deque from the collections module for efficient queue operations
from collections import deque
# Define a function to check if a target value exists in the binary tree
def tree_includes(root, target):
# If the tree is empty, return False
  if not root:
    return False
# Create a queue and add the root node to start BFS traversal
  queue = deque([ root ])
# Loop while there are nodes to process in the queue
  while queue:
# Remove the front node from the queue
    node = queue.popleft()
# If the current node's value matches the target, return True
    if node.val == target:
      return True
# If the current node has a left child, add it to the queue
    if node.left:
      queue.append(node.left) 
# If the current node has a right child, add it to the queue
    if node.right:
      queue.append(node.right) 
# If the loop finishes without finding the target, return False
  return False



# Define a function that checks if a target value is in the binary tree
def tree_includes(root, target):
  # If the current node is None (empty), return False
  if not root:
    return False
# If the current node's value matches the target, return True
  if root.val == target:
    return True
# Recursively check the left and right subtrees.
# If the target is found in either, return True
  return tree_includes(root.left, target) or tree_includes(root.right, target)


# Define the Node class
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

# Create a binary tree:
#        a
#       / \
#      b   c
#     /     \
#    d       e

a = Node('a')
b = Node('b')
c = Node('c')
d = Node('d')
e = Node('e')

a.left = b
a.right = c
b.left = d
c.right = e

# Run test cases
print(tree_includes(a, 'e'))  # Output: True
print(tree_includes(a, 'f'))  # Output: False



#tree min value
#write a function, tree_min_value, that takes in the root of a binary tree that contains number values. the function should return the minimum value within the tree.

