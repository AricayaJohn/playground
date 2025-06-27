

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