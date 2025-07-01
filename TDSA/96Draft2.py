

#knight attack
"""
A knight and a pawn are on a chess board. Can you figure out the minimum number of moves required for the knight to travel to the same position of the pawn? On a single move, the knight can move in an "L" shape; two spaces in any direction, then one space in a perpendicular direction. This means that on a single move, a knight has eight possible positions it can move to.

Write a function, knight_attack, that takes in 5 arguments:

n, kr, kc, pr, pc

n = the length of the chess board
kr = the starting row of the knight
kc = the starting column of the knight
pr = the row of the pawn
pc = the column of the pawn
The function should return a number representing the minimum number of moves required for the knight to land ontop of the pawn. The knight cannot move out-of-bounds of the board. You can assume that rows and columns are 0-indexed. This means that if n = 8, there are 8 rows and 8 columns numbered 0 to 7. If it is not possible for the knight to attack the pawn, then return None.
"""


#import deque from collections to use as a queue for BFS
from collections import deque

#function to calculate the minimum number of moves a knight needs to reach a target position
def knight_attack(n, kr, kc, pr, pc):
#create a set to track visited position
    visited = set()
#mark the knight's position as visited
    visited.add((kr, kc))
#initialize queue with starting position and step count 0
    queue = deque([ (kr, kc, 0)])
#continue BFS while there are positions to explore
    while len(queue) > 0:
#get the next position and step count from the queue
        r, c, step = queue.popleft()
#if the current position is the target, return the step count  
        if (r, c) == (pr, pc):
            return step
#get all valid knight moves from current position
        neighbors = get_knight_moves(n, r, c)
#iterate through each possible move
        for neighbor in neighbors:
#unpack the neighbor coordinates
            neighbor_row, neighbor_col = neighbor
#if the position hasnt been visited
            if neighbor not in visited:
#mark it as visited
                visited.add(neighbor)
#enqueue it with incremented steps
                queue.append((neighbor_row, neighbor_col, step + 1))
#if the queue is exhausted and the target is not reached return None
    return None

#Helper function to get all legal knight moves from a position on an n x n board
def get_knight_moves(n, r, c):
#all 8 possible l-shaped knight moves from (r, c)
    positions = [
        (r + 2, c + 1),
        (r - 2, c + 1),
        (r + 2, c - 1),
        (r - 2, c - 1),
        (r + 1, c + 2),
        (r - 1, c + 2),
        (r + 1, c - 2),
        (r - 1, c - 2),
    ]
#list to hold only the valid position within the board bounds
    inbounds_positions = []
#check each candidate move
    for pos in positions:
#unpack the row and column
        new_row, new_col = pos
#only include positions within the board
        if 0 <= new_row < n and 0 <= new_col < n:
#add valid move to the list
            inbounds_positions.append(pos)
#return list of legal knight moves
    return inbounds_positions

# Test Case
# ----------------------
# Board size: 8x8
# Knight starts at (0, 1)
# Target is at (7, 6)
# Expected output: 4 moves

print(knight_attack(8, 0, 1, 7, 6))  # Output: 4



#can color
"""
Write a function, can_color, that takes in a dictionary representing the adjacency list of an undirected graph. The function should return a boolean indicating whether or not it is possible to color noes of the graph using two colors in such a way that adjacent nodes are always different colors.
"""

# Function to determine if the graph is bipartite (2-colorable)
def can_color(graph):
  # Dictionary to store the color assigned to each node
  coloring = {}
  
  # Iterate through each node in the graph
  for node in graph:
    # If the node hasn't been colored yet, attempt to color it starting with False
    if node not in coloring:
      # If it's not possible to color this part of the graph, return False
      if not valid(graph, node, coloring, False):
        return False
      
  # If all nodes can be colored without conflict, return True
  return True

# Recursive helper function to attempt to color the graph using two colors
def valid(graph, node, coloring, current_color):
  # If the node is already colored, check if it matches the intended color
  if node in coloring:
    return current_color == coloring[node]
  
  # Assign the current color to the node
  coloring[node] = current_color
  
  # Recursively try to color all neighbors with the opposite color
  for neighbor in graph[node]:
    # If any neighbor cannot be properly colored, return False
    if not valid(graph, neighbor, coloring, not current_color):
      return False
    
  # If all neighbors are colored successfully, return True
  return True

# ---------- Test Case ----------
graph = {
  'a': ['b', 'c'],
  'b': ['a', 'd'],
  'c': ['a', 'd'],
  'd': ['b', 'c']
}

print(can_color(graph))  # Expected output: True
# Explanation:
# One possible coloring:
# a = False, b = True, c = True, d = False
# No two connected nodes share the same color.



#tolerant teams
""" 
write a function, tolerant_teams, that takes in a list of rivalries as an argument. A rivalry is a pair of people who should not be placed on the same team. The function should return a boolean indicating whether or not it is possible to separate people into two teams, without rivals being on the same team. The two teams formed do not have to be the same size.
"""

# Determines if the given rivalries can be divided into two tolerant teams (bipartite check)
def tolerant_teams(rivalries):
  # Convert the rivalries (edges) into an adjacency list graph
  graph = build_graph(rivalries)
  
  # Dictionary to store team assignments (colors)
  coloring = {}
  # Iterate through each person in the graph
  for node in graph:
    # If the person is not yet assigned a team, try to assign teams recursively
    if node not in coloring and not is_bipartite(graph, node, coloring, False):
      # If not possible to assign without conflict, return False
      return False
    
  # If all can be assigned into two teams without internal rivalries, return True
  return True

# Recursive helper to attempt 2-coloring (bipartite check)
def is_bipartite(graph, node, coloring, current_color):
  # If already colored, check if the color matches
  if node in coloring:
    return coloring[node] == current_color
  # Assign the current color to the node
  coloring[node] = current_color
  
  # Recurse on neighbors with opposite color
  for neighbor in graph[node]:
    # If any neighbor can't be colored properly, return False
    if not is_bipartite(graph, neighbor, coloring, not current_color):
      return False
    
  # All neighbors were colored successfully
  return True

# Build an adjacency list from the given list of rivalries (edges)
def build_graph(edges):
  graph = {}
  
  for edge in edges:
    a, b = edge
    # Initialize adjacency list if node not yet seen
    if a not in graph:
      graph[a] = []
    if b not in graph:
      graph[b] = []   
    # Add both directions since rivalries are mutual
    graph[a].append(b)
    graph[b].append(a)    
    
  return graph

# --------- Test Case ---------
rivalries = [
  ('anna', 'bob'),
  ('bob', 'claire'),
  ('claire', 'derek'),
  ('derek', 'anna')
]

print(tolerant_teams(rivalries))  # Expected output: True
# Explanation: These rivalries form a cycle of even length (4), which is bipartite.



#rare routing
"""
Write a function, rare_routing, that takes in a number of cities (n) and a list of tuples where each tuple represents a direct road that connects a pair of cities. The function should return a boolean indicating whether or not there exists a unique route for every pair of cities. A route is a sequence of roads that does not visit a city more than once.

Cities will be numbered 0 to n - 1.

You can assume that all roads are two-way roads. This means if there is a road between A and B, then you can use that road to go from A to B or go from B to A.
"""

# Determines if the given road network between cities forms a valid tree (i.e., connected and acyclic)
def rare_routing(n, roads):
  # Create an adjacency list from city connections
  graph = make_graph(n, roads)
  
  # Set to keep track of visited cities
  visited = set()

  # Start DFS traversal from city 0 and check for cycles
  valid = validate(graph, 0, visited, None)

  # Return True only if all cities are visited and no cycles were found
  return valid and len(visited) == n


# Helper function to perform DFS traversal and check for cycles
def validate(graph, node, visited, last_node):
  # If we've already visited this node, there's a cycle
  if node in visited:
    return False
  
  # Mark the node as visited
  visited.add(node)

  # Recurse on all neighboring cities
  for neighbor in graph[node]:
    # Skip the node we came from to avoid false positive cycle detection
    if neighbor != last_node and not validate(graph, neighbor, visited, node):
      return False
    
  # All paths from this node are valid
  return True

# Builds an undirected graph (adjacency list) from a list of roads
def make_graph(n, roads):
  graph = {}
  
  # Initialize an empty adjacency list for each city
  for city in range(n):
    graph[city] = []
    
  # Add both directions of each road to the graph
  for road in roads:
    a, b = road
    graph[a].append(b)
    graph[b].append(a)
    
  return graph

# --------- Test Case ---------
# n = 4 cities (0 through 3), and roads connecting them in a tree structure
roads = [
  (0, 1),
  (1, 2),
  (1, 3)
]

print(rare_routing(4, roads))  # Expected output: True
# Explanation: This forms a connected graph with no cycles (a valid tree)


#topological order
"""
Write a function, topological_order, that takes in a dictionary representing the adjacency list for a directed-acyclic graph. The function should return a list containing the topological-order of the graph. 
"""
# Returns a list of nodes in topological order for a Directed Acyclic Graph (DAG)
def topological_order(graph):
  # Initialize a dictionary to count the number of incoming edges (parents) for each node
  num_parents = {}
  for node in graph:
    num_parents[node] = 0
  
  # Count how many times each node appears as a child (i.e., has incoming edges)
  for node in graph:
    for child in graph[node]:
      num_parents[child] += 1

  # Start with nodes that have no parents (in-degree = 0)
  ready = [ node for node in graph if num_parents[node] == 0 ]

  # List to store the final topological order
  order = []

  # Process nodes with zero in-degree and reduce in-degree of their children
  while ready:
    node = ready.pop()         # Remove a ready node
    order.append(node)         # Add it to the final order

    # Decrease in-degree of each child
    for child in graph[node]:
      num_parents[child] -= 1
      # If child now has zero in-degree, it's ready to be processed
      if num_parents[child] == 0:
        ready.append(child)
    
  # Return the list of nodes in topological order
  return order

# --------- Test Case ---------
graph = {
  "a": ["b", "c"],
  "b": ["d"],
  "c": ["d"],
  "d": [],
  "e": ["f"],
  "f": []
}

print(topological_order(graph))
# Possible valid output: ['e', 'f', 'a', 'c', 'b', 'd'] or other valid topological order




#safe cracking
"""
Oh-no! You forgot the number combination that unlocks your safe. Luckily, you knew that you'd be forgetful so you previously wrote down a bunch of hints that can be used to determine the correct combination. Each hint is a pair of numbers 'x, y' that indicates you must enter digit 'x' before 'y' (but not necessarily immediately before y).

The keypad on the safe has digits 0-9. You can assume that the hints will generate exactly one working combination and that a digit can occur zero or one time in the answer.

Write a function, safe_cracking, that takes in a list of hints as an argument and determines the combination that will unlock the safe. The function should return a string representing the combination.
"""

# Returns the correct order of digits to open the safe based on precedence hints
def safe_cracking(hints):
  # Build a directed graph from the given hints
  graph = build_graph(hints)
  # Return the topological order of the graph (safe code)
  return topological_order(graph)

# Constructs a graph from directed edge pairs (a, b) where a must come before b
def build_graph(edges):
  graph = {}
  for edge in edges:
    a, b = edge
    # Initialize the list for node a if not present
    if a not in graph:
      graph[a] = [] 
    # Initialize the list for node b if not present
    if b not in graph:
      graph[b] = []
    # Add edge a → b (a must come before b)
    graph[a].append(b)
  return graph

# Returns a string representing topological sort (valid digit order)
def topological_order(graph):
  # Count how many parents (incoming edges) each node has
  num_parents = {}
  for node in graph:
    num_parents[node] = 0

  # Update parent count based on graph edges
  for node in graph:
    for child in graph[node]:
      num_parents[child] += 1

  # Start with nodes that have no parents (in-degree = 0)
  ready = [node for node in graph if num_parents[node] == 0]

  # The resulting code string
  order = ''

  # Process nodes in topological order
  while ready:
    node = ready.pop()
    order += str(node)
    # Decrease in-degree of children and check if they're ready
    for child in graph[node]:
      num_parents[child] -= 1
      if num_parents[child] == 0:
        ready.append(child)

  # Return the computed code order
  return order

# ---------- Test Case ----------
hints = [
  (7, 1),
  (1, 8),
  (7, 8),
]

print(safe_cracking(hints))  # Expected output: "718"



#String Search
"""
Write a function, string_search, that takes in a grid of letters and a string as arguments. The function should return a boolean indicating whether or not the string van be found in the grid as a path by connecting horizontal or vertical positions. The path can begin at any positions, but you cannot reuse a position more than once in the path.
"""

#returns True if the string 's' can be found in the grid following adjacent moves
def string_search(grid, s):
#iterate through each cell in the grid
    for r in the range(len(grid)):
        for c in range(len(grid[0])):
#start DFS from the current cell
            if dfs(grid, r, c, s):
                return True
#Return False if the string was not found starting from any cell
    return False

#Performs DFS to match the string starting from grid[r][c]
def dfs(grid, r, c, s):
#if the string is empty, we have matched all characters
    if s == '':
        return True
#chcek if the current row and column are within bounds
    row_inbounds = 0 <= r < len(grid)
    col_inbounds = 0 <= c < len(grid[0])
    if not row_inbounds or not col_inbounds:
        return False
#check if the current grid character matches the first character of the string
    char = grid[r][c]
    if char != s[0]:
        return False
#Remove the first character since it's matched
    suffix = s[1:]
#Mark the cell as visited to avoid revisiting during this path
    grid[r][c] = '*'

#explore all 4 possible directions: down, up, right, left
    result = ( 
        dfs(grid, r + 1, c, suffix) or
        dfs(grid, r - 1, c, suffix) or
        dfs(grid, r, c + 1, suffix) or
        dfs(grid, r, c - 1, suffix)
    )
#restore the original character for other DFS paths
    grid[r][c] = char
    return result


#union-find code I
"""
Write a function, count_components, that takes in a number of nodes(n) and a list of edges for an undirected graph. In the graph, nodes are labeled from 0 to n-1. The function should return the number of connected components in the given graph.
"""

#Helper function to find the root of a node with path compression
def find(roots, node):
#if the node is its own root, return it
    if node == roots[node]:
        return node
#recursively find the root of the node
    return find(roots,roots[node])

#Helper function to union two components by updating one root to point to the other
def union(roots, node_a, node_b):
#find the root of each node
    root_a = find(roots, node_a)
    root_b = find(roots, node_b)
#Make root_b point to root_a to merge the compinents
    roots[root_b] = root_a

#Main function to count the number of connected components in an undirected graph
def count_components(n, edges):
#initially, each node is its own root(component)
    roots = [ i  for i in range(0, n)]

#union the nodes for each edge to group them into components
    for edge in edges:
        node_a, node_b = edge
        union(roots, node_a, node_b)

#count how many nodes are still their own root
    count = 0
    for i in range(0, len(roots)):
        if i == roots[i]:
            count += 1

    return count

 # ---------- Test Case ----------
n = 5
edges = [[0, 1], [1, 2], [3, 4]]
print(count_components(n, edges))  # Expected output: 2   


#union-find code II
"""
Write a function, countComponents, that takes in a number of nodes(n) and a list of edges for an undirected graph. In the graph, nodes are labeled from 0 to n-1. The function shold return the number of connected components in the given graph.
"""
# Function to find the root of a node with path compression
def find(roots, node):
  # Base case: if node is its own root, return it
  if node == roots[node]:
    return node
  # Recursively find the root and compress the path
  found = find(roots, roots[node])
  roots[node] = found
  return found

# Function to perform union of two sets using union by size
def union(roots, sizes, node_a, node_b):
  # Find root of node_a
  root_a = find(roots, node_a)
  # Find root of node_b
  root_b = find(roots, node_b)

  # If both nodes are already in the same component, do nothing
  if root_a == root_b:
    return

  # Merge the smaller tree under the larger tree and update sizes
  if sizes[root_a] >= sizes[root_b]:
    roots[root_b] = root_a
    sizes[root_a] += sizes[root_b]
  else:
    roots[root_a] = root_b
    sizes[root_b] += sizes[root_a]

# Function to count the number of connected components in the graph
def count_components(n, edges):
  # Initialize each node to be its own root
  roots = [ i for i in range(0, n) ]
  # Initialize size of each component to 1
  sizes = [ 1 for i in range(0, n) ]

  # Union each edge's nodes
  for edge in edges:
    node_a, node_b = edge
    union(roots, sizes, node_a, node_b)
    
  # Count how many nodes are their own root (unique components)
  count = 0
  for i in range(0, len(roots)):
    if i == roots[i]:
      count += 1

  return count

# ----------- Test Case -----------
n = 6
edges = [[0, 1], [1, 2], [3, 4]]
print(count_components(n, edges))  # Expected output: 3

# Explanation:
# Component 1: 0-1-2
# Component 2: 3-4
# Component 3: 5 (disconnected node)



#province sizes
"""
Write a function, provinceSizes, that takes in a number of cities n and a list of roads which connects cities. Roads can be traveled in both directions. Cities are named from 0 to n.

A "province" is a grop of 1 or more cities that are connected by roads. The "size" of a province is the number of cities that make up that province.

you should return a list containing the sizes of the provinces. You may return the result in any order
"""

#function to find the root of a node with path compression
def find(roots, node):
#if the node is its own root, return it
    if node == roots[node]:
        return node
#Recursively find the root and compress the path
    found = find(roots, roots[node])
    roots[node] = found
    return found

#function to union two sets using union by size
def union(roots, sizes, node_a, node_b):
#find the root of node_a
    root_a = find(roots, node_a)
#find the root of node_b
    root_b = find(roots, node_b)

#if both nodes are already in the same component, no need to union
    if root_a == root_b:
        return
#union the smaller set into the larger set and update size
    if sizes[root_a] >= sizes[root_b]:
        roots[root_b] = root_a
        sizes[root_a] += sizes[root_b]
    else:
        roots[root_a] = root_b
        sizes[root_b] += sizes[root_a]

#main function to compute sizes of each connected component(province)
def province_sizes(n, roads):
    #initially, each node is its own root
    roots = [i for i in range(0, n)]
    #initializes sizes to 1 for each node
    sizes = [1 for i in range(0, n)]

#apply union operation for each road(edge)
    for road in roads:
        a, b = road
        union(roots, sizes, a, b)
    
    result = []
#collect sizes of components where the node is a root
    for i in range(0, n):
        if i == roots[i]:
            result.append(sizes[i])
    return result
    



#cable
"""
Write afunction that takes in number of num_computers and a list of cables that connect the computers. Computers have ids from 0 to num_computers - 1. The function should return a cable that can be safely removed. There will be multiple possible cables that can be chosen; you may return any of them
"""
#find the root of a node with path compression
def find(roots, node):
#if the node is its own root, return it
    if node == roots[node]:
        return node

#recursively find the root and compress the path
    found = find(roots, roots[node])
    roots[node] = found
    return found

#unions two sets by size and returns False if they're already connected
def union(roots, sizes, node_a, node_b):
#find the root of each node
    root_a = find(roots, node_a)
    root_b = find(roots, node_b)

#if they share the same root, a cycle is found; return False
    if root_a == root_b:
        return False
#merge the smaller tree into the larger one
    if sizes[root_a] >= sizes[root_b]:
        roots[root_b] = root_a
        sizes[root_a] += sizes[root_b]
    else:
        roots[root_a] = root_b
        sizes[root_b] += sizes[root_a]
#successfully connected
    return True
#identifies the first redundant cable(edge that creates a cycle)
def extra_cable(num_computers, cables):
#initialize each node as its own root
    roots = [i for i in range(0, num_computers)]
#set size of each component to 1 initially
    sizes = [1 for i in range(0, num_computers)]

#Go through each cable and try to union the two connected nodes
    for cable in cables:
        a, b = cable
#if union returns false, the cable is redundunt
        if not union(roots, sizes, a, b):
            return cable
    
    

#weighted graph min path
"""
Write a function that takes in the adjacency list for a weighted graph and two nodes, src and dst. The function should return the minimum cost path that travels from src to dst.

the cost of a path is the sum of the weights of edges traveled.
"""

#finds the minimum cost path between two nodes in a weighted directed graph
def weighted_graph_min_path(graph, src, dst):
#wrapper function that initialize an empty vvisited set
    return min_path(graph, src, dst, set())
#recursive helper to find the min cost from src to dst using dfs
def min_path(graph, src, dst, visited):
#if source and destination are the same, path cost is 0
    if src == dst:
        return 0
#if node is already visited, avoid cycle by returning infinite cost
    if src in visited:
        return float("inf")
#mark the node as visited
    visited.add(src)
#initialize minimum cost as infinity
    min_cost = float("inf")
#explore tall neighbors and compute path cost recursively
    for neighbor in graph[src]:
#get edge weight
        cost = graph[src][neighbor]
#total cost from src to dst via neighbor
        total_cost = cost + min_path(graph, neighbor, dst, visited)
#update min ocst
        min_cost = min(min_cost, total_cost)

#backtrack: unmark node as visited for other paths
    visited.remove(src)
    return min_cost



#lowest toll
"""
You are given the tolls for different highways. Each highway connects a pair of cities and has a particular cost that must be paid to use it.

Each highway toll is a triplet(cityA, cityB, cost). Every highway can be traveled in either direction

Write a function that takes in highway tolls and two cities. The function should return the lowest cost required to travel between the two cities. You can assume that there exists at least one way to travel between the two cities.
"""

#find the lowest toll cost to travel between two cities using DFS with backtracking
def lowest_toll(highway_tolls, start_city, end_city):
#build the graph as an adjacency list with toll costs
    graph = {}
    for city_a, city_b, cost in highway_tolls:
#initialize entries for each city if not alredy in graph
        if city_a  not in graph:
            graph[city_a] = {}
        if city_b not in graph:
            graph[city_b] = {}
#since tolls are bidirectional, store cost in both directions
        graph[city_a][city_b] = cost
        graph[city_b][city_a] = cost
#call helper function to find the minimum toll path
    return min_path(graph, start_city, end_city, set())
#helper function to compute minimum cost path from src to dst using dfs
def min_path(graph, src, dst, visited):
#basecase: if source is destination cost is 0
    if src == dst:
        return 0
#if city already visited, return infinite cost to avoid cycles
    if src in visited:
        return float("inf")
#mark the current city as visited
    visited.add(src)
#initialize the minimum cost to infinity
    min_cost = float("inf")
#explore all neighbors and recursively calculate cost to destination
    for neighbor in graph[src]:
        cost = graph[src][neighbor]
        total_cost = cost + min_path(graph, neighbor, dst, visited)
#update the min cost if a cheaper path is found
        if total_cost < min_cost:
            min_cost = total_cost
#backtrack: unmark the current city
    visited.remove(src)
#return the lowest cost path found 
    return min_cost


#union-find algorithm is useful for what types of graph problems?
"""
union-find is good for graph problems that deal with groups or connected-components
"""

#what general algorithm is best suited to find the shortest path between two nodes in an unweighted graph?
"""
Breadth-first is best suited because all directions are explored evenly. The first path found via breadth-first is the shortest path
"""

#in a graph of n nodes, how many edges can exist in the worst case?
"""
O(n^2) because an edge is a connection between a pair of nodes. In other words. O(e) = O(n^2)
"""

#What does topological order mean for graphs?
"""
Topological order is a sequence of nodes such that parents appear before their children in the sequence
"""

#What programming data structure is useful when implementing union-find?
"""
A simple list is useful to represent the roots and also the sizes during union-find
"""

#why is a visited set useful for graph traversal algorithms
"""
Visited sets are useful to avoid revisiting nodes and prevent infinite loops in traversal algorithms
"""