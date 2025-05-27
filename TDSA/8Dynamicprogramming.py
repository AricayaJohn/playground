#dynamic programming

#wrtie a function fib that takes in a number argument, n, and returns the n-th number of the fibonacci sequence.

#the 0th number of the sequence is 0

#the 1st number of the sequence is 1

#To generate further numbers of the sequence, calculate the sum of previous two numbers.

#computes the nth fibonacci number using memoization
def fib(n):
#create an empty dictionary to store previously computed values
  memo = {}
#call the helper function with the memoization dictionary
  return _fib(n, memo)

#helper function that does the actual recursive calculation
def _fib(n, memo):
#base case: return n if n is 0 and 1 (f(0=0, F(1)= 1))
  if n == 0 or n == 1 :
    return n
#if weve already computed fib(n), return it from memo to avoid redundant work

  if n in memo:
    return memo[n]

#otherwise, compute fib(n -1 ) and fib(n-2), store result in memo, and return it

  memo[n] = _fib(n - 1, memo) + _fib(n - 2, memo)
  return memo[n]

# ---------- Test Case ----------

# Compute the 10th Fibonacci number (expected output: 55)
print(fib(10))  # Output: 55

# Compute the 0th Fibonacci number (expected output: 0)
print(fib(0))   # Output: 0

# Compute the 1st Fibonacci number (expected output: 1)
print(fib(1))   # Output: 1

# Compute the 50th Fibonacci number to show efficiency with memoization
print(fib(50))  # Output: 12586269025



#Tribonacci 
#write a tibonacci that takes in a number argument, n, and returns the n-th number of the tribonacci sequence.

#calculates the nth Tribonacci number using memozation
def tribonacci(n):
#call the helper function with an empty memo dictionary
    return _tribonacci(n, {})

#helper function that performs the recursive computation
def _tribonacci(n, memo):
#if result is already computed, return it to avoid redundant work
    if n in memo:
        return memo[n]
#BaseCase: T(0) and T(1) are defined as 0
    if n == 0 or n == 1:
        return 0
#base case: T(2) is defined as 1
    if n == 2:
        return 1
#recursively compute T(n) = T(n - 1) + T(n-2) + T(n - 3) and store in memo
    memo[n] = _tribonacci(n - 1, memo) + _tribonacci(n -2, memo) + _tribonacci(n - 3, memo)
#return the computed result
    return memo[n]

#test case:
#compute the 0th Tribonacci number(expected output: 0)
print(tribonacci(0)) #Output: 0

#compute the 4th tribonacci number(expected number: 0 + 1 + 1 = 2 )
print(tribonacci(4)) # output: 2


#sum possible
#write a function, sum_possible that takes in an amount and a list of positive numbers. The function should return a boolean indicating whether or not it is possible to create  the amount by summing numbers of the list. You may reuse numbers of the list as many times as necessary. 

#determines if the target amount can be sumed using elements from the list
def sum_possible(amount, numbers):
#call the helper function with a memoization dictionary
    return _sum_possible(amount, numbers, {})
#helper function with memoization to avoid redundant computation
def _sum_possible(amount, numbers, memo):
#return previously computed result if available
    if amount in memo:
        return memo[amount]
#if amount is negative, it's not possible to form the sum
    if amount < 0:
        return False
#if amount is zero, it means we've found a valid combination
    if amount == 0:
        return True
#Try subtracting each number from the amount recursively
    for num in numbers:
        if _sum_possible(amount - num, numbers, memo):
#if recursive path returns True, memoize and return True
          memo[amount] = True
          return True
#if no valid combination is found, memoize and return False
    memo[amount] = False
    return False

#testCase:
#check if 8 can be formed using [5,3,4]
print(sum_possible(8,[5, 3, 4])) # true(5 + 3)

#check if 11 can be formed using [5, 3, 4, 7]
print(sum_possible(11, [5, 3, 4, 7])) #True (4 + 7)


#mini change
#write a function min_change that takes in an ammount and list of coins. The function should return the minimum number of coins required to create the amount. You may use each coin as many times as necessary. 

#if it is not possible to create the amount, then return -1

#finds the minimum number of coins needed to make the target amount
def min_change(amount, coins):
#call the helper function with memoization
    ans = _min_change(amount, coins, {})
#if the answer is infinity, it means its not possible to form the amount
    if ans == float('inf'):
        return -1
    else:
        return ans
#helper function to compute the minimum coins recursively with memoization
def _min_change(amount, coins, memo):
#return cached result if already computed
    if amount in memo:
        return memo[amount]
#basecase: 0 coins needed to make amount 0
    if amount == 0:
        return 0
#if amount is negative, it's not a valid solution
    if amount < 0:
        return float('inf')
#initialize with infinity to find the minimum
    min_coins = float('inf')
#try every coin and compute the number of coins needed
    for coin in coins:
#recursive call for the remaining amount after choosing the coin
        num_coins = 1 + _min_change(amount - coin, coins, memo)
#update the minimum coins needed
        min_coins = min(min_coins, num_coins)
#Store the result in the memo bedore returning
    memo[amount] = min_coins
    return min_coins

#testCase:
#minimum coins to make 8 from [1, 5, 4, 12]
print(min_change(8, [1, 5, 4, 12])) #expected output: 2 (2 + 4 or 5 +1 +1 +1)

#no combination can make 7 using only coins[2, 4]
print(min_change(7, [2, 4])) #expected output -1 

#make 0 required 0 coins
print(min_change(0, [1, 2, 5]))

#mincoins to make 8 form [1, 5, 4, 12]
print(min_change(8, [1, 5, 4, 12])) #expected output: 2 (4 + 4 or 5 + 1 +1 +1)

# No combination can make 7 using only coins [2, 4]
print(min_change(7, [2, 4]))  # Expected output: -1

# Make 0 requires 0 coins
print(min_change(0, [1, 2, 5]))  # Expected output: 0



#count paths
#write a function, count_paths, that takes in a grid as an argument. In the grid, 'X' Represents walls and 'O' represents open spaces. You may only move down or to the right and cannot pass through walls. The function should return the number of ways possible to travel from the top-left corner of the grid to the bottom-right corner. 

#Returns the number of unique paths from top-left to bottom-right in a grid,
#avoiding obstacles marked as 'X'
def count_path(grid):
#start recursive seaerch from position(0, 0) with memoization
    return _count_path(grid, 0, 0, {})
#helper function to recursively count paths using memoization
def _count_path(grid, r, c, memo):
#store the current position as a tuple
    pos = (r, c)
#if result is already computed for this position, return it
    if pos in memo:
        return memo[pos]
#if position is out of bounds or an obstacle, return 0(no path)
    if r == len(grid) or c == len(grid[0]) or grid[r][c] == 'X':
        return 0
#if destination(bottom-right) is reached, return 1(valid path)
    if r == len(grid) - 1 and c == len(grid[0]) - 1:
        return 1
#store the total number of paths by exploring right and down
    memo[pos] = _count_path(grid, r + 1, c, memo) + _count_path(grid, r, c + 1, memo)
    return memo[pos]

#testcase:
grid = [
    ['O','O','O'],
    ['O','X','O'],
    ['O','O','O'],
]
#there are 2 unique paths from top-left to bottom-right avoiding 'X'
print(count_path(grid)) #expected output: 2



#max path sum
#write a function, max_path_sum, that takes in a grid as an argument. The function should return the maximmum sum possible by traveling a path from the top-left corner to the bottom-right corner. You may only travel through the grid by moving down or right

# you can assume that all nubers are non-negative.
# returns the maximum sum possible from top-left to bottom-right in a grid
def max_path_sum(grid):
#start recursive helpber from position (0, 0) with memoization
    return _max_path_sum(grid, 0, 0, {})
#helper function that uses memoization to compute max path sum
def _max_path_sum(grid, r, c, memo):
#current position as a tuple
    pos = (r, c)
#return memoized result if already computed
    if pos in memo:
        return memo[pos]
#if out of bounds, return negative infinity to indicate invalid path
    if r == len(grid) or c == len(grid[0]):
    return float('-inf')
#if destination(bottom-right) is reached, return its value
    if r == len(grid) - 1 and c == len(grid[0]) - 1:
        return grid[r][c]
#recursively calculate maxsum by moving either down or right
    down = _max_path_sum(grid, r + 1, c, memo)
    right = _max_path_sum(grid, r, c + 1, memo)
#store the result in memo: current cell value + max of down/right
    memo[pos] = grid[r][c] + max(down, right)
    return memo[pos]


#testCase:
grid = [
    [1, 3, 12],
    [5, 2, 2],
    [1, 1, 1]
]

print(max_path_sum(grid)) #expected output: 18

grid = [
  [1, 2, 8,  1],
  [3, 1, 12, 10],
  [4, 0, 6,  3],
]
print(max_path_sum(grid)) # -> 36


#non adjacent sum
#write a function, non_adjacent_sum, that takes in a list of numbers as an argument. The function should return the maximum sum of non-adjacent items in the list. There is no limit on how many items can be taken into the sum as long as they are not adjacent. 

#Returns the maximum sum of non-adjacent elements in the list
def non_adjacent_sum(nums):
#start recursion at index 0 with an empty memoization dictionary
    return _non_adjacent_sum(nums, 0, {})
#Helper function that uses memoization and recursion
def _non_adjacent_sum(nums, i, memo):
#return memoized results if already computed for index i
    if i in memo:
        return memo[i]
#base case: if index is beyond the end of the list, return 0
    if i >= len(nums):
        return 0
#include current number and recurse by skipping the next one(i +2)
    include = nums[i] + _non_adjacent_sum(nums, i + 2, memo)
#exclude current number and recurse to the next one (i + 1)
    exclude = _non_adjacent_sum(nums, i + 1, memo)
#store the maximum of including or excluding the current number
    memo[i] = max(include, exclude)
    return memo[i]


#testcase
nums = [2, 4, 5, 12, 7]
#optimal non-adjacent sum: 2 + 5 + 7 = 14 or 4 + 12 = 16 max is 16
print(non_adjacent_sum(nums)) #expected output: 16 




#summing squares
#write a function, summing_squares, that takes a target number as an argument. The function should return the minimum number of perfect squares that sum to the target. A perfect square is a number of the form(i * i) where i >= 1 

import math

#returns the minimum number of perfect squares that sum to 'n'
def summing_squares(n):
#start recursion with memoization dictionary
    return _summing_squares(n, {})
#helper function that uses recursion with memoization
def _summing_squares(n, memo):
#Return memoized result if already computed
    if n in memo:
        return memo[n]
#base case: 0 requires 0 squares
    if n == 0:
        return 0
#initialize with infinity to find minimum
    min_squares = float('inf')
#try all square numbers <= n
    for i in range(1, math.floor(math.sqrt(n) + 1)):
#compute the square
        square = i * i 
#recursive call: 1 square used + best result for (n - square)
        num_squares = 1 + _summing_squares(n - square, memo)
#track the minimum number of squares
        min_squares = min(min_squares, num_squares)
#memoize and return the results
    memo[n] = min_squares
    return min_squares

#testcase:
print(summing_squares(8)) #expected output: 2
print(summing_squares(12)) #expected output: 3