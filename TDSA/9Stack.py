#stacks

#reverse some chars
"""
write a function, reverse_some_chars, that takes in string and a list of characters. The function should return the string with the order of the sgiven characters in revers.
"""

#function to reverseonly specific characters in a string
def reverse_some_chars(s, chars):
#convert the list of characters to a set of 0(1) lookup
    char_set = set(chars)
#stack to store the characters that need to be reversed
    stack = []
#first pass: collect all characters in 's' that need to be reversed
    for ch in s:
        if ch in char_set:
            stack.append(ch)
#List to build the result string with reversed target characters
    result = []
#second pass: build the result by reversing only the specified characters
    for ch in s:
      if ch in char_set:
#pop from the stack to reverse the order of target characters
        result.append(stack.pop())
      else:
#leave all other characters as they are
        result.append(ch)
#join the list into a final string and return it
    return "".join(result)

#testcase:
print(reverse_some_chars("computer", ["a", "e", "i", "o", "u"])) # -> 'cemputor'



#paired parentheses 
"""
Write a function, paired _parentheses, that takes in a string as an argument. The function should return a boolean indicating whether or not the string has well-formed parentheses.
"""

#function to check if all parenthesis in a string are properly pared and nested
def paired_parentheses(string):
#initialize a counter to track open parentheses
    count = 0
#iterate through each character in the string
    for char in string:
#if the character is an opening parenthesis, increment the counter
        if char == '(':
            count += 1
#if it's a closing parenthesis
        elif char == ')':
#if there are no unmatched opening parenthesis, its's invalid
            if count == 0:
                return False
#otherwise, pair it with a previous opening parenthesis
            count -= 1
#if all parentheses are matched, count will be zero
    return count == 0

#testcases
print(paired_parentheses("(())()")) #true
print(paired_parentheses("(()))"))  #false



#befitting brackets
"""
Write a function, befitting_brackets, that takes in a string as an argument. The function should return a boolean indicating whether or not the string contains correctly matched brackets.
"""

#Function to determine if a string contains matched and ordered ordered brackets
def befitting_brackets(string):
#stack to keep track of expected closing brackets
    stack = []
#mapping of opening brackets to their corresponding closing brackets
    brackets = {
        '(' : ')',
        '[' : ']',
        '{' : '}',
    }
#iterate through each character in the string
    for char in string:
#if the character is an opening bracket, push its expected closing bracket
        if char in brackets:
            stack.append(brackets[char])
        else:
#if it's a closing bracket, check if it matches the last expected one
            if stack and stack[-1] == char:
#matched, remove it from the stack
                stack.pop()
            else:
#mismatch or no opening bracket to match
                return False
#if the stack is empty, all brackets were properly matched
    return len(stack) == 0

#testcases
print(befitting_brackets("({[]})"))       # True
print(befitting_brackets("({[)]}"))       # False


#decompress braces
"""
write a function, decompress_braces, that takes in a compressed string as an argument. The function should return the string decompressed.

The compression format of the input string is 'n{sub_string}', where the sub_string within braces should be repeated n times.

You may assume that every number n is guaranteed to be an integer between 1 through 9.

You may assume that the input is valid and the decompressed string will only contain alphabetic characters.
"""

#function to decompress a string with brace-enclosed patterns like '3{ab} => 'ababab'
def decompress_braces(string):
#allowed repeat counts (no zero or double digits)
    numbers = '123456789'
#stack to keep track of characters and repeat counts
    stack = []

    for char in string:
#if character is a number, convert to int and push to stack
        if char in numbers:
            stack.append(int(char))
        else:
#when encountering a closing brace, pop and build the segment
        if char == '}':
            segment = ''
#build the segment string until hitting a number
            while isinstance(stack[-1], str):
                popped = stack.pop()
#prepend to maintain order
                segment = popped + segment
#pop the number of times to repeat
            num = stack.pop()
#push repeat segment
            stack.append(segment * num)
        elif char != '{':
#if not a brace or number, just push character to stack
            stack.append(char)
#John everything in the stack to form the final result
    return ''.join(stack)

#testcase:
print(decompress_braces("2{ab}")) #output: "abab"



#nesting scrore
"""
write a funtion, nesting_score, that takes in a string of brackets as an argument. The function should return the score of the string according to the following rule:

- [] is worth 1 point
- XY is worth m + n points where X, Y are substrings of well-formed brackets and m, n are respective scores
-[S] is worth 2 * k points where S is a substring of well-formed brackets and k is the score of that substring

"""

#function to calculate the score of a nested bracket string
def nesting_score(string):
#initialize a stack with a base score of 0
    stack = [0]
    for char in string:
        if char == '[':
#open bracket: start a new nested level with score 0
            stack.append(0)
        else:
#close bracket: end current nesting level
          popped = stack.pop()
          if popped == 0:
#base case: empty pair '[]' ads 1 point
              stack[-1] += 1
          else:
#nested case: double the inner score and add the outer level
              stack[-1] += 2 * popped
#final score is the result on top of the stack
    return stack[0]

#testcase
print(nesting_score("[]")) # output 1
print(nesting_score("[[]][]")) # output 3