#graphs
#collection of nodes + edges

n = nodes
e = edges #ede is the connection of nodes

# directed graphs 
# - with arrow heads

#udirected graphs 
# -without arrow heads

#neigbor nodes
#is a node accessible to a node by edge

#adjecency list -used to explain a graph

#has path
#Write a function, has_path, that takes in a dictionary representing the adjacency list of a directed acyclic graph and two nodes(src, dst). The function should return a boolean indicating whether or not there exists a directed path between the source and destination nodes.

#acyclic = no cycles
#cycle = can return to original node

#Depth-First Search(DFS Recursive)
def has_path(graph, src, dst):
  if src == dst:
    return True
#Explore all neighbors(edges) of the current node
  for neighbor in graph[src]:
#recursively check if a path exists from neighbor to destination
    if has_path(graph, neighbor, dst) == True:
      return True
#If no path is found after exploring all neighbors, return false
  return False




#Breadth-first search(BFS-Iterative)
from collections import deque

def has_path(graph, src, dst):
#initialize a queue with the starting node
  queue = deque([ src ])
#continue exploring while there are nodes in the queue
  while queue:
#remove the front node from the queue
    current = queue.popleft()
#if we reach the destination, return True
    if current == dst:
      return True
#add all neighbors of the current node to the queue
    for neighbor in graph[current]:
      queue.append(neighbor)
#If the queue is empty and destination wasn't found, return false
  return False


#testcase
graph = {
  'a': ['b', 'c'],
  'b': ['d'],
  'c': ['e'],
  'd': ['f'],
  'e': [],
  'f': []
}

print(has_path(graph, 'a', 'f')) #True(a -> b -> d ->f)
print(has_path(graph, 'a', 'e')) #True(a -> c -> e)



#undirectpath
#write a function, undirected_path, that takes in a list of edges for an undirected graph and two nodes(node_A, node_B). The function should return a boolean indicating wheter or not there exists a path between node_A and node_B

def undirected_path(edges, node_A, node_B):
#Build the graph from the edge list
  graph = build_graph(edges)
#use DFS to check if a path exists from node_A to node_B
  return has_path(graph, node_A, node_B, set())

#helper to build_graph
def build_graph(edges):
#create an empty dictionary to store the graph
  graph = {}
#loop through each edge (pair of connected nodes)
  for edge in edges:
    a, b = edge
#if node 'a' is not yet in the graph, add it with an empty list
    if a not in graph:
      graph[a] = []
#if node 'b' is not yet in the graph, add it with an empty list
    if b not in graph:
      graph[b] = []
#Add each node to the other's adjacency list(undirected graph)
    graph[a].append(b)
    graph[b].append(a)
#return the build graph
  return graph

#DFS helper function:
def has_path(graph, src, dst, visited):
#if the current node is the destination, path exists
  if src == dst:
    return True
#if the current node was already visited, skip it
  if src in visited:
    return False
#mark the current node as visited
  visited.add(src)
#recursively check all neighbors for a path to destination
  for neighbor in graph[src]:
    if has_path(graph, neighbor, dst, visited) == True:
      return True
#if none of the path worked out, return False
  return False



#testCase:
edges = [
  ['i', 'j'],
  ['k', 'i'],
  ['m', 'k'],
  ['k', 'l'],
  ['o', 'n']
]

print(undirected_path(edges, 'j', 'm')) #True(j-i-k-m)
print(undirected_path(edges, 'j', 'o')) #False(disconnected graph)



#connected components count
#Write a function, connected_components_count, that takes in the adjacency list of an undirected graph. The function should return the number of connected compinents within the graph

#function depth first search
def connected_components_count(graph):
#keep track of all visited nodes so we dont revisit them
  visited = set()
#initialize the count of connected components
  count = 0
#loop through every node in the graph
  for node in graph:
#if exploring this node leads to discovering a new component
    if explore(graph, node, visited) == True:
#increase the component count
      count += 1
#return the total number of connected components
  return count

#helper function
def explore(graph, current, visited):
#if the node is already visited, it's part of a known component
  if current in visited:
    return False
#mark the node as visited
  visited.add(current)
#recursively visit all connected neighbors
  for neighbor in graph[current]:
    explore(graph, neighbor, visited)
#returning True means we explored a new component
  return True



#testCase:
graph = {
  0: [8, 1, 5],
  1: [0],
  5: [0, 8],
  8: [0, 5],
  2: [3, 4],
  3: [2, 4],
  4: [3, 2],
}

print(connected_components_count(graph)) #output: 2



#largest component
#write a function, largest_coponent, that takes in the adjacency list of an undirected graph. The function should return the size of the largest connected component in the graph

#Returns the size of the largest connected component in the graph
def largest_component(graph):
#keeps track of the visited nodes   
    visited = set()
#store the size of the largest component found so far
    largest = 0
#Iterate over each node in the graph
    for node in graph:
#explore the component size only if the node hasnt been visited
      size = explore_size(graph, node, visited)
#update the largest if this component is bigger
      if size > largest:
          largest = size
    return largest

#Helper function to explore the size of a component starting from a node
def explore_size(graph, node, visited):
  if node in visited:
    return 0
#mark node as visited
  visited.add(node)
#count the current node
  size = 1
#Recursively explore all neighbors
  for neighbor in graph[node]:
    size += explore_size(graph, neighbor, visited)

  return size


#test case 
graph = {
  0: [8, 1, 5],
  1: [0],
  5: [0, 8],
  8: [0, 5],
  2: [3, 4],
  3: [2, 4],
  4: [3, 2]
}

#component 1: {0,1,5,8} (size 4)
#component 2: {2, 3, 4} (size 3)
print(largest_component(graph)) #output: 4



#shortest path 
#write a function, shortest_path, that takes in a list of edges for an undirected graph and two nodes(node_A, node_B), The function should return the length of the shortest path between A and B. .Consider the length as the number of edges in the path, not the number of nodes. If there is no path between A and B, then return -1. You can assume that A and B exist as nodes in the graph.


from collections import deque



#island count
#write a funtion, island_count, that takes in a grid containing Ws and Ls. W representing water and L representing land. The function should return the number of islands on the grid. An Island is a vertically or horizontally connected region of land.


#counts the number of distinct islands in a grid
def island_count(grid):
  visited = set()
  count = 0
#Traverse each cell in the grid
  for r in range(len(grid)):
    for c in range(len(grid[0])):
#if we find a new land cell that hasnt been visited, explore visited
      if explore(grid, r, c, visited):
#increment the island count
        count += 1
  return count
#explore connected land titles using DFS
def explore(grid, r, c, visited):
#check if the row and column are within bounds
  row_inbounds = 0 <= r < len(grid)
  col_inbounds = 0 <= c < len(grid[0])
  if not row_inbounds or not col_inbounds:
    return False

#return False if the current call is water
  if grid[r][c] == 'W':
    return False

  pos = (r, c)
#return False if we've already visited this cell
  if pos in visited:
    return False
#mark the cell as visited
  visited.add(pos)
#recursively explore all four directions
  explore(grid, r - 1, c, visited) # up
  explore(grid, r + 1, c, visited) # down
  explore(grid, r, c - 1, visited) # left
  explore(grid, r, c + 1, visited) # right
#Found new land - part of an island
  return True


#testcase:
grid = [
  ['W', 'L', 'W', 'W', 'W'],
  ['W', 'L', 'W', 'W', 'W'],
  ['W', 'W', 'W', 'L', 'W'],
  ['W', 'W', 'L', 'L', 'W'],
  ['L', 'W', 'W', 'L', 'L'],
  ['L', 'L', 'W', 'W', 'W'],
]

#expected result: 3 islands
print(island_count(grid)) #output: 3



#minimum island
#Write a function, minimum_island, that takes in a grid containing Ws and Ls. W represents water and L represent land. The function should return the size of the smallest island. An island is a vertically or horizontally connected region of land

#return the size of the smallest island in the grid
def minimum_island(grid):
  visited = set()
#start with infinity as a minimum
  min_size = float("inf")
#iterate over every cell in the grid
  for r in range(len(grid)):
    for c in range(len(grid[0])):
#explore the size of an island starting at this cell
      size = explore_size(grid, r, c, visited)
#if its a land cell and smaller than current min, update min
      if size > 0 and size < min_size:
        min_size = size
  return min_size

#recursively explore all connected land tiles and return island size
def explore_size(grid, r, c, visited):
#check bounds
  row_inbounds = 0 <= r < len(grid)
  col_inbounds = 0 <= c < len(grid[0])
  if not row_inbounds or not col_inbounds:
    return 0

#water cell has size 
  if grid[r][c] == 'W':
    return 0

  pos = (r, c)
#already visited
  if pos in visited:
    return 0
  visited.add(pos)

#count this tile and explore in all 4 directions
  size = 1
  size += explore_size(grid, r - 1, c, visited) # up
  size += explore_size(grid, r + 1, c, visited) # down
  size += explore_size(grid, r, c - 1, visited) # left
  size += explore_size(grid, r, c + 1, visited) # right
  return size


#testCase:
grid = [
  ['W', 'L', 'W', 'W', 'W'],
  ['W', 'L', 'W', 'W', 'W'],
  ['W', 'W', 'W', 'L', 'W'],
  ['W', 'W', 'L', 'L', 'W'],
  ['L', 'W', 'W', 'L', 'L'],
  ['L', 'L', 'W', 'W', 'W'],
]


#expected island sized:
# - one size 2 (top-left island)
# - one size 5 (center-right island)
# - one size 4 (bottom-left island)
#so the smallest is 2

print(minimum_island(grid)) #2 




#closest carrot
#Write a function, closest_carrot, that takes in a grid, a starting row, and a starting column. 
#In the grid, 'X's are walls, 'O's are open spaces, and 'C's are carrots. The function should return a number representing the length of the shortest path from the starting position to a carrot. You may move up, down, left, right, but cannot pass through walls(X). if there is no possible path to a carrot, then reutn -1. 

from collections import deque  # Import deque for efficient FIFO queue operations

def closest_carrot(grid, starting_row, starting_col):
# Initialize a set to keep track of visited positions
  visited = set([ (starting_row, starting_col) ])
# Initialize a queue with the starting position and distance 0
  queue = deque([ (starting_row, starting_col, 0) ])
  
# Continue while there are positions to explore in the queue
  while queue:
# Dequeue the front element: current row, column, and distance
    row, col, distance = queue.popleft()
    
# If the current position has a carrot, return the distance
    if grid[row][col] == 'C':
      return distance
    
# Define possible movement directions: down, up, right, left
    deltas = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    
# Iterate through all possible movement directions
    for delta in deltas:
# Extract row and column offsets
      delta_row, delta_col = delta
# Calculate the new row and column
      neighbor_row = row + delta_row
      neighbor_col = col + delta_col      
# Create a position tuple
      pos = (neighbor_row, neighbor_col)
# Check if the new row is within the grid bounds
      row_inbounds = 0 <= neighbor_row < len(grid)
# Check if the new column is within the grid bounds
      col_inbounds = 0 <= neighbor_col < len(grid[0])
# If position is in bounds, not visited, and not a wall
      if row_inbounds and col_inbounds and pos not in visited and grid[neighbor_row][neighbor_col] != 'X':
# Mark the position as visited
        visited.add(pos)
# Enqueue the new position with incremented distance
        queue.append((neighbor_row, neighbor_col, distance + 1))
        
# Return -1 if no carrot is reachable
  return -1


# ---------- Test Case ----------
grid = [
  ['O', 'O', 'O', 'O', 'C'],
  ['O', 'X', 'X', 'O', 'O'],
  ['O', 'O', 'O', 'X', 'O'],
  ['C', 'X', 'O', 'O', 'O'],
]

# Starting at (0, 0), the closest carrot is at (0, 4) and distance is 4
print(closest_carrot(grid, 0, 0))  # Output: 4



#longest path
#write a function, longest_path. that takes in a n adjacency list for a directed acyclic graph. The function should return the length of the longest path within the graph. A path mayy start and end at any two nodes. The length of a path is considered the number of edges in the path, not the number of nodes. 

# Returns the length of the longest path in a directed acyclic graph
def longest_path(graph):
  # Dictionary to memoize the longest distance from each node
  distance = {}

  # Initialize distance of leaf nodes (nodes with no outgoing edges) to 0
  for node in graph:
    if len(graph[node]) == 0:
      distance[node] = 0

  # Traverse each node to compute the longest path from that node
  for node in graph:
    traverse_distance(graph, node, distance)

  # Return the maximum value from the distance dictionary
  return max(distance.values())

# Helper function to compute the longest path starting from a given node
def traverse_distance(graph, node, distance):
  # If node's distance is already computed, return it (memoization)
  if node in distance:
    return distance[node]
  
  # Initialize variable to track the longest path from current node
  largest = 0

  # Explore all neighbors of the current node
  for neighbor in graph[node]:
    # Recursively compute the distance from each neighbor
    attempt = traverse_distance(graph, neighbor, distance)
    # Update largest if a longer path is found
    if attempt > largest:
      largest = attempt

  # Store the computed distance (1 + longest neighbor path) for current node
  distance[node] = 1 + largest
  return distance[node]


# --------- Test Case ---------
# Sample graph: Directed Acyclic Graph (DAG)
# a -> b -> d
#  \        ^
#   -> c ---|
graph = {
  'a': ['b', 'c'],
  'b': ['d'],
  'c': ['d'],
  'd': []
}

# Longest path: a -> b -> d or a -> c -> d (length = 2)
# Including the starting node: path length is 2 (edges)
print(longest_path(graph))  # Output: 2
