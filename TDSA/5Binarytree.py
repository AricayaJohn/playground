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

# Define a function that finds the minimum value in a binary tree
def tree_min_value(root):
# If the current node is None (empty tree or leaf's child), return infinity (acts as a neutral value for min)
  if root is None:
    return float("inf")
# Recursively find the minimum value in the left subtree
  smallest_left_value = tree_min_value(root.left)
# Recursively find the minimum value in the right subtree
  smallest_right_value = tree_min_value(root.right)
# Return the smallest value among the current node's value, left subtree, and right subtree
  return min(root.val, smallest_left_value, smallest_right_value)



# Define a function to find the minimum value in a binary tree using depth-first search
def tree_min_value(root):
# Start with a stack containing the root node (for DFS traversal)
  stack = [ root ]
# Initialize the smallest value as infinity, so any real value will be smaller
  smallest = float("inf")
# Loop as long as there are nodes in the stack to process
  while stack:
# Remove the last node from the stack (LIFO behavior of DFS)
    current = stack.pop()
# If the current node's value is smaller than our smallest so far, update it
    if current.val < smallest:
      smallest = current.val
# If there is a left child, add it to the stack for later processing
    if current.left is not None:
      stack.append(current.left)
# If there is a right child, add it to the stack for later processing
    if current.right is not None:
      stack.append(current.right)
# After checking all nodes, return the smallest value found
  return smallest



# Import deque from collections for efficient queue operations
from collections import deque

# Define a function to find the smallest value in a binary tree using BFS
def tree_min_value(root):
# Initialize a queue with the root node to start breadth-first traversal
  queue = deque([ root ])
# Set the initial smallest value to infinity so any real node value will be smaller
  smallest = float("inf")
# Continue looping as long as there are nodes to process in the queue
  while queue:
# Remove the node at the front of the queue (FIFO behavior of BFS)
    current = queue.popleft()
# Update smallest if the current node's value is smaller
    if current.val < smallest:
      smallest = current.val
# If the current node has a left child, add it to the queue
    if current.left is not None:
      queue.append(current.left)
# If the current node has a right child, add it to the queue
    if current.right is not None:
      queue.append(current.right)
# After visiting all nodes, return the smallest value found
  return smallest



class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
#        5
#       / \
#      3   7
#     / \   \
#    1   4   8

# Build the tree
a = Node(5)
b = Node(3)
c = Node(7)
d = Node(1)
e = Node(4)
f = Node(8)

a.left = b
a.right = c
b.left = d
b.right = e
c.right = f

# Call the function and print result
print(tree_min_value(a))  # Output should be 1



#max root to leaf path sum
#Write a function, max_path_sum, that takes in the root of a binary tree that contains number values. The function should return the maximum sum of any root to leaf path within the tree.

#assume that the input tree is non-empty

# Define a function to find the maximum path sum from root to any leaf
def max_path_sum(root):
# If the current node is None (empty), return negative infinity to ignore this path
  if root is None:
    return float("-inf")

# If the current node is a leaf (no left or right children), return its value
  if root.left is None and root.right is None:
    return root.val

# Otherwise, return the current node's value plus the maximum path sum of either left or right subtree
  return root.val + max(max_path_sum(root.left), max_path_sum(root.right))


#      5
#     / \
#    11  3
#   / \   \
#  4   2   1


# Define a class for tree nodes
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

# Build the tree
a = Node(3)
b = Node(11)
c = Node(4)
d = Node(4)
e = Node(-2)
f = Node(1)

a.left = b
a.right = c
b.left = d
b.right = e
c.right = f

# Test the function
print(max_path_sum(a))  # Output should be 20



#tree path finder
#Write a function, path_finder, that takes in the root of a binary tree and a target value. The function should return an array representing a path to the target value. If the target value is not found in the tree, then return None.

#you may assume that the tree contains unique values

# This function finds a path from the root to the target node in a binary tree.
def path_finder(root, target):
  # If the tree is empty, return None
  if root is None:
    return None
# If the current node is the target, return a list with just this value
  if root.val == target:
    return [ root.val ]
# Recursively search for the path in the left subtree
  left_path = path_finder(root.left, target)
# If a valid path is found in the left subtree, add the current node to it and return
  if left_path is not None:
    return [ root.val, *left_path ]
# Otherwise, search in the right subtree
  right_path = path_finder(root.right, target)
# If a valid path is found in the right subtree, add the current node to it and return
  if right_path is not None:
    return [ root.val, *right_path ]
# If the target is not found in either subtree, return None
  return None



# This function wraps the recursive helper to reverse the path at the end
def path_finder(root, target):
# Call the helper function to find the path
  result = _path_finder(root, target)
# If no path was found, return None
  if result is None:
    return None
  else:
# If a path is found, reverse it so it's from root to target
    return result[::-1]
# This helper function works bottom-up and collects the path in reverse
def _path_finder(root, target):
  # If the tree is empty, return None
  if root is None:
    return None

# If this node is the target, return a list with just this value
  if root.val == target:
    return [ root.val ]
# Try to find the path in the left subtree
  left_path = _path_finder(root.left, target)
  if left_path is not None:
# If found, add the current node to the path and return it
    left_path.append(root.val)
    return left_path
# Try to find the path in the right subtree
  right_path = _path_finder(root.right, target)
  if right_path is not None:
# If found, add the current node to the path and return it
    right_path.append(root.val)
    return right_path

# If not found in either subtree, return None
  return None

#        a
#       / \
#      b   c
#     / \   \
#    d   e   f

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

# Build the tree
a = Node("a")
b = Node("b")
c = Node("c")
d = Node("d")
e = Node("e")
f = Node("f")

a.left = b
a.right = c
b.left = d
b.right = e
c.right = f

# Test the path_finder function
print(path_finder(a, "e"))  # Expected output: ['a', 'b', 'e']
print(path_finder(a, "f"))  # Expected output: ['a', 'c', 'f']
print(path_finder(a, "a"))  # Expected output: ['a']
print(path_finder(a, "x"))  # Expected output: None (target not found)



#tree value count
#write a function, tree_value_count, that takes in the root of a binary tree and a target value. The function should return the number of times that the target occurs in the tree.

# Define a function to count how many times `target` appears in the tree using recursion
def tree_value_count(root, target):
# If the current node is None (empty), return 0
  if root is None:
    return 0
# Check if the current node's value matches the target
  # If it matches, match = 1; otherwise, match = 0
  match = 1 if root.val == target else 0
# Recursively count matches in the left and right subtrees and add them to match
  return match + tree_value_count(root.left, target) + tree_value_count(root.right, target)



# Define a function to count how many times `target` appears in the tree using a stack
def tree_value_count(root, target):
  # If the tree is empty, return 0
  if root is None:
    return 0
# Start a counter at 0
  count = 0
# Initialize a stack with the root node to start DFS
  stack = [ root ]
# Loop as long as there are nodes to process
  while stack:
# Get the current node from the top of the stack
    current = stack.pop()

# If the current node's value matches the target, increment the counter
    if current.val == target:
      count += 1
# If the current node has a left child, add it to the stack to check later
    if current.left is not None:
      stack.append(current.left)
# If the current node has a right child, add it to the stack to check later
    if current.right is not None:
      stack.append(current.right)
# Return the total count after processing all nodes
  return count



def tree_value_count(root, target):
# If the tree is empty, return 0 immediately
  if root is None:
    return 0
# Start the count at 0
  count = 0
# Use a stack to perform depth-first traversal
  stack = [ root ]
# Loop through all nodes in the tree
  while stack:
# Pop the last node added to the stack (LIFO)
    current = stack.pop()
# If the current node's value matches the target, increment the count
    if current.val == target:
      count += 1
# If the current node has a left child, add it to the stack to visit later
    if current.left is not None:
      stack.append(current.left)
# If the current node has a right child, add it to the stack to visit later
    if current.right is not None:
      stack.append(current.right)
# Return the total count of target values found in the tree
  return count


#        a
#       / \
#      b   a
#     / \   \
#    a   c   a


# Define a basic binary tree node class
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

# Create the tree nodes
a = Node('a')
b = Node('b')
c = Node('c')
a2 = Node('a')
a3 = Node('a')
a4 = Node('a')

# Connect the nodes to form the tree
a.left = b
a.right = a2
b.left = a3
b.right = c
a2.right = a4

# Run the test
print(tree_value_count(a, 'a'))  # Expected output: 4


#How high
#write a function, how_high, that takes in the root of a binary tree. The function should return a number representing the height of the tree.

#the height of a binary tree is defined as the maximal number of the edges from the root node to any leaf node.

#if the tree is empty, return -1 


# This function returns the height of a binary tree (number of edges on the longest path from root to leaf)
def how_high(node):
# If the node is None (empty), return -1 (base case: height of empty tree is -1)
  if node is None:
    return -1
# Recursively calculate the height of the left subtree
  left_height = how_high(node.left)
# Recursively calculate the height of the right subtree
  right_height = how_high(node.right)
# Return 1 plus the greater of the two subtree heights (count current edge)
  return 1 + max(left_height, right_height)


# Define a simple binary tree node class
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

# Create a test tree:
#       a
#      / \
#     b   c
#    /
#   d

a = Node('a')
b = Node('b')
c = Node('c')
d = Node('d')

a.left = b
a.right = c
b.left = d

# Run the test
print(how_high(a))  # Expected output: 2 (edges in longest path: a -> b -> d)
