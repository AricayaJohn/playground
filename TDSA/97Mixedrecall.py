#prefix product
"""
Write a function, prefixProduct, that takes in a list of numbers. The function should return a new list of the same length where each element contains the running product up to that index of the original list.
"""

def prefix_product(numbers):
    total = 1
    new_nums = []
    for i in numbers:
        total *= i
        new_nums.append(total)
    return new_nums

# testcase:
numbers = [1, 2, 3]
print(prefix_product([4, 2, 1, 6, 3, 6]))


#leaf layers 
"""
Write a function, leaf_layers that takes in the root of a binary tree. The function should return a 2D list where each sublist represents a "leaf layer of the tree.

To get a leaf layer, take all leaf nodes in tree. Then, conceptually "remove" them from the tree. This will create a new "leaves" repeat this process until the tree is empty.
"""

def leaf_layers(root):
  layers = []
  traverse(root, layers)
  return layers

def traverse(root, layers):
  if root is None:
    return -1

  left_height = traverse(root.left, layers)
  right_height = traverse(root.right, layers)
  height = 1 + max(left_height, right_height)

  if len(layers) == height:
    layers.append([])
  layers[height].append(root.val)
  return height
  

  #max increase subseq
  """
  Write a function, max_increasing_subseq, that takes in a list of numbers as an argument. The function should return the length of the longest  subsequence of strictly increasing numbers.

  A subsequence of a list can be created by deleting any items of the list, while maintaining the relative order of items.
  """

def max_increasing_subseq(numbers):
  return _max_increasing_subseq(numbers, 0, float('-inf'), {})

def _max_increasing_subseq(numbers, i, previous, memo):
  key = (i, previous)
  if key in memo:
    return memo[key]

  if i == len(numbers):
    return 0

  current = numbers[i]
  options = []
  dont_take_current = _max_increasing_subseq(numbers, i + 1, previous, memo)
  options.append(dont_take_current)

  if current > previous:
    take_current = 1 + _max_increasing_subseq(numbers, i + 1, current, memo )
    options.append(take_current)

  memo[key] = max(options)
  return memo[key]


  #knightly number
  """
  A knight is on a chess board. Can you figure out the total number of ways the knight can move to a target position in exactly m moves? On a single move, the knight can move in an "L" shape; two spaces in any direction, then one space in a perpendicular direction. This means that on a single move, a knight has eight possible positions it can move to.

Write a function, knightlyNumber, that takes in 6 arguments:

n, m, kr, kc, pr, pc

n = the length of the chess board
m = the number of moves that must be used
kr = the starting row of the knight
kc = the starting column of the knight
pr = the target row
pc = the target column
The function should return the number of "unique ways" the knight can move to the target in exactly m moves. The knight can revisit positions of the board if needed. The knight cannot move out-of-bounds of the board. You can assume that rows and columns are 0-indexed. This means that if n = 8, there are 8 rows and 8 columns numbered 0 to 7.

Note that a "unique way" the knight can move to the target is a unique series of positions that the knight can travel to the target.
"""

def knightly_number(n, m, kr, kc, pr, pc):
  return _knightly_number(n, m, kr, kc, pr, pc, {})

def _knightly_number(n, m, kr, kc, pr, pc, memo):
  key = (m, kr, kc)
  if key in memo:
    return memo[key]
  
  if kr < 0 or kr >= n or kc < 0 or kc >= n:
    return 0

  if m == 0:
    if (kr, kc) == (pr, pc):
      return 1
    else:
      return 0
    
  neighbors = [
    ( kr + 2, kc + 1 ),
    ( kr - 2, kc + 1 ),
    ( kr + 2, kc - 1 ),
    ( kr - 2, kc - 1 ),
    ( kr + 1, kc + 2 ),
    ( kr - 1, kc + 2 ),
    ( kr + 1, kc - 2 ),
    ( kr - 1, kc - 2 ),
  ]
  
  count = 0
  for neighbor in neighbors:
    neighbor_row, neighbor_col = neighbor
    count += _knightly_number(n, m - 1, neighbor_row, neighbor_col, pr, pc, memo)
  memo[key] = count
  return count


#all trips
"""
You are given a list of bus routes, a starting station, and an ending station. A bus route is a pair of two stations(a, b) such that the bus travels from a to b, but not from b to a.
"""

