
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