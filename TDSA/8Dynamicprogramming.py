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


