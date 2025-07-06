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
def all_trips(routes, start_station, end_station):
  graph = build_graph(routes)
  paths = get_paths(graph, start_station, end_station)
  return [ path[::-1] for path in paths ]

def get_paths(graph, src, dst):
  if src == dst:
    return [ [src] ]

  all_paths = []
  for neighbor in graph[src]:
    neighbor_paths = get_paths(graph, neighbor, dst)
    for neighbor_path in neighbor_paths:
      neighbor_path.append(src)
      all_paths.append(neighbor_path)
  return all_paths

def build_graph(edges):
  graph = {}
  for edge in edges:
    a, b = edge
    if a not in graph:
      graph[a] = []
    if b not in graph:
      graph[b] = []
    graph[a].append(b)
  return graph



  #has path sum
  """
  Write a function, has_path_sum, that takes in the root of a binary tree and a target number. The function should return a boolean indicating whether or not there is a path through the tree that sums to the target
  """
  def has_path_sum(root, target):
  if root is None:
    return False

  if root.left is None and root.right is None and root.val == target:
    return True

  return has_path_sum(root.left, target - root.val) or has_path_sum(root.right, target - root.val)


#Knapsack
"""
Write a function, knapsack that takes in a list of item values, a list of item weights, and a weight limit. The i-th item has a value of values[i] and weight of weights[i]. Your job is to pick items to pack into your knapsack so that its total weight does not exceed the limit and the value of the items is maximized. You may either take an item once or not at all. You cannot take the same item multiple times. 

Return the maximum total value of items you can pack into the knapsack.
"""
def _knapsack(values, weights, weight_limit, i, memo):
  if weight_limit < 0:
    return -float("inf")

  if i == len(values):
    return 0

  key = (weight_limit, i)
  if key in memo:
    return memo[key]

  memo[key] = max(
    values[i] + _knapsack(values, weights, weight_limit - weights[i], i + 1, memo), _knapsack(values, weights, weight_limit, i + 1, memo)
  )
  return memo[key]

def knapsack(values, weights, weight_limit):
  return _knapsack(values, weights, weight_limit, 0, {})


#virus spread. 
"""
Write a function, virus_spread, that takes in a grid. In the grid, 0's are empty spaces, 1's are clean computers, adn 2's are infected computers. Every hour , the virus spreads from infected computers to immediately adjacents clean computers. The virus can only spread to adjacent computers that are up, dow, left, or right.

The function should return the number of hours it will take for all computers to be infected. If it is impossible for all computers to become infected, then return -1
"""
from collections import deque

def virus_spread(grid):
    clean_computers = 0
    queue = deque([])
    visited = set()
    for r in range(0, len(grid)):
        for c in range(0, len(grid[0])):
            if grid[r][c] == 1:
                clean_computers += 1
            elif grid[r][c] == 2:
                visited.add((r, c))
                queue.append((r, c, 0))

    deltas = [(0, 1), (0, -1), (1,0), (-1, 0)]
    max_t = 0
    while queue:
        r, c, t = queue.popleft()
        max_t = t
        for delta in deltas:
            delta_r, delta_c = delta
            neighbor_r = r + delta_r
            neighbor_c = c + delta_c
            neighbor_pos = (neighbor_r, neighbor_c)
            if 0 <= neighbor_r < len(grid) and 0 <= neighbor_c < len(grid[0]) and grid[neighbor_r][neighbor_c] != 0 and neighbor_pos not in visited:
                clean_computers -= 1
                visited.add(neighbor_pos)
                queue.append((*neighbor_pos, t + 1))

    if clean_computers > 0:
        return -1
    else:
        return max_t

