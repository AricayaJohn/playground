
#syntaxERror 
    #-> means that there is something wrong with the way your program is writen -- puntuation that does not belong, a command where it is not expected, or missing parenthesis can all trigger a syntax err


#NameError 
    #-> A NameError occurs when the Python interpreter sees a word it does not recognize. Code that contains something that looks like a variable but was never defined will throw a NameError.


# supperscript exponents using **
#     2^2 = 4 == 2 ** 2
#     4^2 = 16 == 4 ** 2


"""
python offers a solution: 
Preview: Docs A string is a sequence of characters contained within a pair of single quotes or double quotes.
multi-line strings
. By using three quote-marks "(""" """ or ''' ''')" instead of one, we tell the program that the string doesnt end until the next triple-quote. 

"""
"(** \n must be inside a print statement)"
" using \n to seperate descriotions"
" using \n\n to add 2 enters"


# : colon -> tells the computer that what's coming next is what should be executed if the condition is met.

"""
syntax error means there is something wromg with the way your program is written -- punctuation that does not belong, a command where it is not expected, or a missing parenthesis can all trigger a syntax error
"""


"""
Name error:
when interpreter detects a variable that is unknown
if a variable is used before it has been assigned a value or a variable name is spelled differently than the point at which it was defined
"""

"""
TypeError: 
is reported by the python interpreter when an operation is applied to a varriable of an inappropriate type
"""

"""
Index error:
Accessing an element that does not exist produces an IndexError.
"""

# importing random
"""
import random
#create the range
random.randint(1, 9)
"""

#append
#adds value to the end of the list


"""
Python list methods
.count()- A list method to count the number of occurences of an element in a list
   
   letters = ["m", "i", "s", "s", "i", "s", "s", "i", "p", "p", "i"]
    num_i = letters.count("i")
print(num_i) #4

.insert()- A list method to insert an element into a specific index of a list
    The order and number of the inputs is important. The .insert() method expects two inputs, the first being a numerical index, followed by any value as the second input
    e.g
     store_line.insert(2, "Vikor")
print(store_line) 

.pop() - A list method to remove an element
         from a SPECIFIC INDEX or from the END of the list 
range() - A built in python function to create a sequence of integers
   
   If we use a third input, we can create a list that “skips” numbers.
    my_range2 = range(2, 9, 2)
print(list(my_range2))
    [2, 4, 6, 8]
    
len() - A built in python function to get the length of a list 


.sort()/sorted() - A method and a builtin function to sort a list 
Often, we will want to sort a list in either numerical (1, 2, 3, …) or alphabetical (a, b, c, …) order.
sort in REVERSE:
names.sort(reverse=True)
print(names)



Slicing:
start is the index of the first element that we want to include in our selection. In this case, we want to start at "b", which has index 1.
end is the index of one more than the last index that we want to include. The last element we want is "f", which has index 5, so end needs to be 6.

letters = ["a", "b", "c", "d", "e", "f", "g"]
sliced_list = letters[1:6]
print(sliced_list)
["b", "c", "d", "e", "f"]

Slicing is exclusive. which means that pring until 6 but not including 6 index

list[start:end]
start: The index where slicing begins (INCLUSIVE).
end: The index where slicing stops (EXCLUSIVE – meaning the element at this index is not included).
"""

#combining list using zip
"""
names = ["Jenny", "Alexus", "Sam", "Grace"]
heights = [61, 70, 67, 64]

names_and_heights = zip(names, heights)
print(names_and_heights)
# <zip objects at 0x7f1631e86b48
converted_list = list(names_and_heights)
print(converted_list)
[('Jenny', 61), ('Alexus', 70), ('Sam', 67), ('Grace', 64)]
"""

#using break
#When the program hits a break statement it immediately terminates a loop. For example:

"""
using continue 

for i in big_number_list:
  if i <= 0:
    continue
  print(i)

When our loop first encountered an element (-1) that met the conditions of the if statement, it checked the code inside the block and saw the continue. When the loop then encounters a continue statement it immediately skips the current iteration and moves onto the next element in the list (4).
"""

#Difference between Parameters VS Arguments
"""
Parameters are the "variables" in a function definition.
Arguments are the actual values passed into the function.
"""
"""
Arguments:
1. Positional Arguments

These are the most basic type of arguments.
They are called "positional" because their values are assigned to the parameters in the function based on their order (position) when the function is called.
The number of arguments and their order must match the function's definition.
Example:

python
def greet(name, age):
    print(f"Hello {name}, you are {age} years old.")

# Calling the function with positional arguments
greet("Alice", 25)
"Alice" is assigned to name (first position).
25 is assigned to age (second position).
Output:

text
Hello Alice, you are 25 years old.
If you change the order, the meaning changes:
python
greet(25, "Alice")  # Incorrect! Now name=25, age="Alice"
2. Keyword Arguments

These are arguments passed to a function by explicitly specifying the parameter name and its value.
Order does not matter because the arguments are identified by their names.
Useful for improving readability and skipping optional arguments.
Example:

python
def greet(name, age):
    print(f"Hello {name}, you are {age} years old.")

# Calling the function with keyword arguments
greet(age=25, name="Alice")
Even though the order is reversed, the correct values are assigned because we used parameter names.
Output:

text
Hello Alice, you are 25 years old.
Keyword arguments are especially helpful in functions with many parameters to avoid confusion.
3. Default Arguments

These are parameters that have a default value assigned in the function definition.
If the caller doesn't provide a value for that argument, the default value is used.
Default arguments must be defined after non-default arguments in the function definition.
Example:

python
def greet(name, age=30):  # age has a default value of 30
    print(f"Hello {name}, you are {age} years old.")

# Calling the function without providing 'age'
greet("Bob")  # age will use the default value (30)

# Calling the function and overriding the default
greet("Charlie", 40)
Output:

text
Hello Bob, you are 30 years old.
Hello Charlie, you are 40 years old.
"""

#using built in round function
"""
The round() built-in function takes in two arguments. The first argument is the number we want to round, followed by an argument on how many decimal places we want to round it.

Here is an example:

rounded_zero = round(10.54, 0)
rounded_one = round(10.54, 1)

print(rounded_zero)
print(rounded_one)

Copy to Clipboard

Would output:

11.00
10.5
"""

#"Range"
"""
range(3): runs the indented block of code 3 times (once for each number in range(3)).

# Write your function here
def append_sum(my_list):
  for i in range(3):
    last2 = my_list[-1] + my_list[-2]
    my_list.append(last2)
  return my_list

# Uncomment the line below when your function is done
print(append_sum([1, 1, 2]))

"""

"""
using list() to create a list of range 
We can generate the numbers in a certain range by a certain increment using the range() function. In order to convert the range sequence into a list, we can pass it into the list() function.
def every_three_nums(start):
  return list(range(start, 101, 3))
"""
