
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


#DAG
#Directed Acyclic Graph
#Node/Nodes that is directed only to one directions

#Cyclic 
#Nodes that travel into a cylce

#topological order
#visiting parent node first before children nodes
#The topological ordering of a graph is a sequence where "parent nodes" appear before their "children" within the sequence.


"""
echo "Hello Command Line" >> hello_cli.txt to create a new file named hello_cli.txt and add Hello Command Line to that file. When you type ls, you should see the following:

cat hello_cli.txt to print the contents of the hello_cli.txt file to the terminal. You should see something like:
"""

#how to check on index
"""
 i < len(string argument)
"""

#The next command we’re going to look at is pwd, which stands for “print working directory.”
"""
terminal of folder check where the folder is type pwd
"""


#moving directories 2 up :
#To go from memory up 2 directories to 2015, we use ../.. such as:

#to move from one directory adjacent
# ../(folder adjacent)


#removing directory. 
#rmdir (media name)

#clear terminal
#to clear terminal type clear


#git
"""
version control system that allows us to track and manage changes to solved code.

repository track histry built history 
it allows SWE to collaborate and update code 
"""

#git init
#initialize

#git status 
""" to check if there is any added changes, files needed to commit"""


#git diff
# to check if there was any changes made in the text file 

#git add
#add the changes to the status
"""
The staging area is a place where Git gathers all the changes you want to include in your next commit. It's like preparing your shopping cart before checking out.

can add multiple file that is uncommitted after checking git status

$ git add disclaimer.txt instructions.txt warranty.txt 
"""



#git commit 
"""
A commit is the last step in our Git workflow. A commit permanently stores changes from the staging area inside the repository.
"""

#git log 
"""
Checks the log of commits
"""



#running a function through the terminal
"""
python3 (name of file to run)
"""


#splitting lines  
#using ->     variable_name.split('\n') 

#joining strings
"""
my_munequita = ['My', 'Spanish', 'Harlem', 'Mona', 'Lisa']
print(' '.join(my_munequita))
# => 'My Spanish Harlem Mona Lisa'
"""

#joining strings in a list with white spaces then seperating them in one line
"""
love_maybe_lines = ['Always    ', '     in the middle of our bloodiest battles  ', 'you lay down your arms', '           like flowering mines    ','\n' ,'   to conquer me home.    ']


love_maybe_lines_stripped = [line.strip() for line in love_maybe_lines]

print(love_maybe_lines_stripped)

love_maybe_full = '\n'.join(love_maybe_lines_stripped)
print(love_maybe_full)
"""

#using .replace
"""
with_spaces = "You got the kind of loving that can be so smooth"
with_underscores = with_spaces.replace(' ', '_')
print(with_underscores)
# 'You_got_the_kind_of_loving_that_can_be_so_smooth'
"""

#using format to replace parts of string:
"""
poem_description = "The poem {} is written by {}"

def poem_title_card(title, poet):
  return poem_description.format(title, poet)

print(poem_title_card("I Hear America Singing", "is written by Walt Whitman"))
"""

#specificity with .format
"""
def poem_description(publishing_date, author, title, original_work):
  poem_desc = "The poem {title} by {author} was originally published in {original_work} in {publishing_date}.".format(publishing_date=publishing_date, author=author, title=title, original_work=original_work)
  return poem_desc

my_beard_description = poem_description(author = "Shel Silerstein", title = "My Beard", original_work = "Where the Sidewalk Ends", publishing_date = "1974")

print(my_beard_description)
"""

#some notes
"""
highlighted_poems = "Afterimages:Audre Lorde:1997,  The Shadow:William Carlos Williams:1915, Ecstasy:Gabriela Mistral:1925,   Georgia Dusk:Jean Toomer:1923,   Parting Before Daybreak:An Qi:2014, The Untold Want:Walt Whitman:1871, Mr. Grumpledump's Song:Shel Silverstein:2004, Angel Sound Mexico City:Carmen Boullosa:2013, In Love:Kamala Suraiyya:1965, Dream Variations:Langston Hughes:1994, Dreamwood:Adrienne Rich:1987"

# print(highlighted_poems)

highlighted_poems_list = highlighted_poems.split(',')

# print(highlighted_poems_list)

highlighted_poems_stripped = [line.strip() for line in highlighted_poems_list]

# print(highlighted_poems_stripped)

highlighted_poems_details = []

for poem in highlighted_poems_stripped:
  details = poem.split(':')
  highlighted_poems_details.append(details)

# print(highlighted_poems_details)

titles = []
poets = []
dates = []


for poem in highlighted_poems_details:
  title, poet, date = poem
  titles.append(title)
  poets.append(poet)
  dates.append(date)

# print(highlighted_poems_details)

# def poem_format(poems):
#   for poem in poems:
#     title, poet, dates = poem
#     description = "The poem {} was published by {} in {}".format(title, poet, date)
#     print(description)

# print(poem_format(highlighted_poems_details))

for i in range(0,len(highlighted_poems_details)):
    print('The poem {} was published by {} in {}'.format(titles[i], poets[i], dates[i]))
"""