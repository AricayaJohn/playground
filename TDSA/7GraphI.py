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











