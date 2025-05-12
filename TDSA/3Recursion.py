#recursion
# -> A function that calls itself

function countdown(n):
#base case 
    if n == 0:
        return
#recursive step
#behavior entering count  print [5, 4 ,3, 2, 1]
    print("entering " + str(n))
    countdown(n-1)
#behavior returning count 
    print("return from" + str(n))


#sum numbers recursive
#Write a function sum_numbers_recursive that takes in an array of numbers and returns the sum of all the numbers in the array. All elements must be integers. 

def sum_numbers_recursive(numbers):
# 1) Base Case: if the list is empty, return 0
    if len(numbers) == 0
        return 0
# 2) Add the first number to the result of a recursive call on the rest of the list
    return numbers[0] + sum_numbers_recursive(numbers[1:])

print(sum_numbers_recursive([1, 2, 3, 4, 5])) #15
print(sum_numbers_recursive([])) # 0


#factorial 
#write a function, factorial, that takes in a number n and returns the factorial of that number. The factorial of n is the product of all the positive numbers less than or equal to n. 

def factorial(n):
#base case: when n is 0 return 1 by definition of a factorial
    if n == 0:
        return 1 
#recursive step : multiply n by factorial of (n-1)
#if n != 0 then return n-1 factorial * n
    return n * factorial(n - 1)

#test
print(factorial(3))



#sum of lengths 
#write a function sumOfLengths that takes in a list of strings and returns the total length of the strings

def sumOfLengths(strings):
#BaseCase: if the list is empty, return 0
    if len(strings) == 0
        return 0
#Recursive step: return the length of first string + sum of lenghts of the rest
    return len(string[0]) + sumOfLengths(string[1:])

#test
print(sum_of_lengths(['goat', 'cat', 'purple'])) # -> 13
print(sum_of_lengths([])) # -> 0




#reverse string recursive
#write a function, reverese_string, that takes in a string as an argument. The function should return the string with its characters in reverse order. 

#define a function that takes a string 's
def reverse_string(s):
#Base case: if the string is empty, return an empty string
    if len(s) == 0:
        return ""
#call the function again with the rest of the string (without the first character)
#then add the first character to the end - this reverses the order
    return reverse_string(s[1:]) + s[0]

#test
print(reverse_string("hello"))




#palindrome recursive
#write a function, palindrome, that takes in a string and returns a boolean indicating whether or not the string is the same forwards and backwards.

#define a function to check if a string 's' is a palindrome:
def palindrome(s):
#if the string is empty or has a one letter, its a palindrome
    if len(s) == 0 or len(s) == 1
        return True
#if the first and last characters dont match, it's not a palindrome
    if s[0] != s[-1]
        return False
#check the rest of the string(without the first and last characters)
    return palindrome(s[1:-1])

#test
print(palindrome("tacocat"))





#fibonacci
#write a function, fibonacci, that takes in a number argument, n, and returns the nth number of the fibonacci sequence
def fibonacci(n):
#base cese: if n is 0 or 1, return n (first two numbers of the sequence)
    if n == 0 or n == 1:
        return n
#recursive case: return the sum of the two previous fibonnaci numbers
    return fibonacci(n - 1) + fibonacci(n -2)

#test
print(fibonacci(2)) #1
print(fibonacci(3)) #2
print(fibonacci(4)) #3
print(fibonacci(5)) #5
print(fibonacci(6)) #8
