#Max Value 
#Write a function, max_value, that takes in list of numbers as an argument. The function should return the largest number in the list

#1) Create a function that takes a list of numbers
def max_value(nums):
#2) Assume the first number is the maximum
  max_num = nums[0]
#3) Loop through each number in the list
  for i in nums:
#4) If the current number is greater than max_num
    if i > max_num:
#5) Update max_num to be the current number
      max_num = i
#6) Return the maximum number found
  return max_num

#check
nums = [5 ,3, 2, 6, 2, 9, 25]
print (max_value(nums))

#longest word
#write a function, longest_word, that takes in a sentence string as an argument. The function should return the longest word in the sentence. if there is a tie, return the word that occurs later in the sentence

#1) Create a function that takes a sentence (string)
def longest_word(sentence):
#2) Split the sentence into words using spaces
  words = sentence.split(" ")
#3) Set an empty string as the starting "longest" word
  longest = ""
#4) Loop through each word in the list of words
  for word in words:
#5) If the current word is longer than or equal to the longest word so far
    if len(word) >= len(longest):
#6) Update longest to be the current word
      longest = word
#7) Return the longest word found
  return longest

#test
sentence = "I am a software engineer"
print(longest_word(sentence))


#Is prime
#write a function, is_prime, that takes in a number as an argument. the function should return a boolean indicating whether or not the given number is prime.
# A prime number is a number that is only divisible by two distingt numbers: 1 and itself

#1) Define a function that takes a number (n) as an argument
def is_prime(n):
#2) If the number is less than 2, return False (not prime)
  if n < 2:
    return False
#3) If the number is greater than or equal to 2
  if n > 2:
#4) Loop through numbers starting from 2 up to (but not including) n
    for i in range(2, n):
#5) Use modulo to check if n is divisible by i
      if n % i == 0:
#6) If divisible, return False (not prime)
        return False
#7) If no divisibility found, return True (it is prime)
  return True
#8) Test the function with a list of numbers
test_numbers = [1, 2, 3, 4, 5, 6, 7]
for number in test_numbers:
#9) Call the function and print whether each number is prime
  result = is_prime(number)
  print(f"{number} is prime: {result}")
#solo test
n = 7
result = is_prime(n)
print(f"{n} is prime:{result}")

#fizzbuzz
#write a function, fizzbuz, that takes in a number n as an argument. The function should return a list containing numbers from 1 to n, replacing certain numbers according to the following rules:
 #-if the number is divisible by 3, make the elements "fizz"
 #-if the number is divisible by 5, make the elements "buzz"
 #-if the number is divisible by 3 and 5, make the elements "fizzbuzz"

#1) Define a function that takes a number (n) as an argument
def fizz_buzz(n):
#2) Create an empty list to store the results
  result = []
#3) Loop through numbers from 1 to n (inclusive)
  for i in range(1, n + 1):
#4) If the number is divisible by both 3 and 5
    if i % 3 == 0 and i % 5 == 0:
#5) Append "fizzbuzz" to the result list
      result.append("fizzbuzz")
#6) Else if the number is divisible only by 3
    elif i % 3 == 0:
#7) Append "fizz" to the result list
      result.append("fizz")
#8) Else if the number is divisible only by 5
    elif i % 5 == 0:
#9) Append "buzz" to the result list
      result.append("buzz")
#10) Else (number is not divisible by 3 or 5)
    else:
#11) Append the number itself to the result list
      result.append(i)
  #12) Return the final result list
  return result


#pairs 
#write a function, pairs, that takes in a list as an argument. The function should return a list containing all unique pairs of elements.

#You may return the pairs in any order and the order of elements within a single pair does not matter
#1) Define a function that takes a list (elements) as an argument
def pairs(elements):
#2) Create an empty list to store the result pairs
  result = []
#3) Loop through the list using index i (starting at 0)
  for i in range(0, len(elements)):
#4) For each i, loop through the list starting from i + 1
    for j in range(i + 1, len(elements)):
#5) Create a pair [elements[i], elements[j]]
      pair = [ elements[i], elements[j] ]
#6) Append the pair to the result list
      result.append(pair)
#7) Return the final list of pairs
  return result


#anagrams
#Write a function, anagrams, that takes in two strings as arguments. The function should return a boolean indicating whether or not the strings are anagrams. 
#Anagrams are strings that contain the same characters, but in any order.

#1)create a function that counts characters that take a str arg
def anagrams(s1, s2):
  def count_char(s):
  #2)count it in a dictionary {}
    count = {}
  #3)loop characters in str 
    for char in s:
  #4) if charecters is not in dictionary start at zero
      if char not in count:
        count[char] = 0
  #5)when we put it in dictionary we want to add +1 to each count 
      count[char] += 1
    return count
  #6) compare each string
  return count_char(s1) == count_char(s2)
    
print(anagrams("restful", "fluster"))

  #using hashmap. keyvalue pairs {a dictionary}
    #{r:1 e:1 s:1 t:1 f:1 u:1 l:1 } ==
    #{f:1 l:1 u:1 s:1 t:1 e:1 r:1}  return True/False