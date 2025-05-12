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

def factorial 