
# Hashing -> In Python, hashing means using dictionaries or sets to store and find things really fast.

# Think of a hashmap (like a Python dictionary) as a magic notebook where you can write down and look up information instantly. It’s perfect for problems where you need to count things, check if something exists, or find pairs.

#Clues That a Problem Needs Hashing
"Count how many times X appears"
(Example: Anagrams, Most Frequent Character)
"Find two things that add/multiply to Y"
(Example: Pair Sum, Pair Product)
"Check if something exists in a list quickly"
(Example: Intersection, Exclusive Items)
"Are all elements unique?"
(Example: All Unique)


#Strategy to Recognize Hashing Problems

Look for Keywords:
"Count", "frequency", "appear", "occurrence" → Use a dictionary.
"Find pairs", "sum", "product" → Track complements in a dictionary.
"Check existence", "common elements", "unique" → Use a set.

#How to Remember the Steps

# Step 1: Identify what you need to track (counts, pairs, existence).
# Step 2: Choose the right tool:
counts = {}     # for counting things
seen = set()    # for checking if something exists
# Step 3: Iterate/loop through the data once, updating your hash structure.
# Step 4: Use the hash structure to find your answer (compare counts, look up complements, etc.).


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


#Most frequent Char
#Write a function, most_frequent_char, that takes in a string as an argument. The function should return the most frequent character of the string. If there are ties, return the character that appears earlier in the string.

# 1) Define a function that takes a string (s) as an argument
def most_frequent_char(s):
# 2) Create an empty dictionary to count character frequencies
    count = {}
# 3) Loop through each character in the string
    for char in s:
# 4) If the character is not already in the dictionary, set its count to 0
        if char not in count:
            count[char] = 0
# 5) Increment the count of the character by 1
        count[char] += 1
 # 6) Create a variable to keep track of the most frequent character
    most_frequent_char = None
 # 7) Loop through each character in the string again
    for char in s:
# 8) If this is the first character or it has a higher count than the current most frequent one
        if most_frequent_char is None or count[char] > count[most_frequent_char]:
# 9) Update the most frequent character
            most_frequent_char = char
 # 10) Return the most frequent character
    return most_frequent_char


#pair sum
#write a function, pair_sum, that takes in a list and a target sum as arguments. The function should return a tuple containing a pair of indices whose elements sum to the given target. The indices returned must be unique.

#Be sure to return the indices, not the elemenets themselves.

#1) Define a function that takes a list of numbers and a target sum as arguments
def pair_sum(numbers, target_sum):
#2) Create an empty dictionary to store numbers we've seen and their indices
  previous_nums = {}
#3) Loop through each number and its index in the list
  for index, num in enumerate(numbers):
#4) Calculate the complement (what number would add up to target_sum)
    complement = target_sum - num
#5) If the complement exists in the dictionary
    if complement in previous_nums:
#6) Return a tuple of the complement's index and the current index
      return (previous_nums[complement], index)
#7) Otherwise, store the current number and its index in the dictionary
    previous_nums[num] = index

#8) Example usage: find two numbers in the list that add up to 6
numbers = [1, 2, 3, 4, 5, 6, 7]
target_sum = 6
target = pair_sum(numbers, target_sum)
print(target)


#pair product
#write a function, pair_product, that takes in a list and a target product as arguments. The function should return a tuple containing a pair of indices whose elements multiply to the given target. The indeces returned must be unique.

#be sure to return the inideces, not the elements themselves. 

#1) Define a function that takes a list of numbers and a target product as arguments
def pair_product(numbers, target_product):
#2) Create an empty dictionary to store numbers we've seen and their indices
  previous_nums = {}
#3) Loop through each number and its index in the list
  for index, num in enumerate(numbers):
#4) Calculate the complement (what number multiplied by num would equal target_product)
    complement = target_product / num
#5) If the complement exists in the dictionary
    if complement in previous_nums:
#6) Return a tuple of the current index and the complement's index
      return (index, previous_nums[complement])
#7) Otherwise, store the current number and its index in the dictionary
    previous_nums[num] = index

#test case
print(pair_product([3, 2, 5, 4], 10)) 



#intersection 
#write a function, intersection, that takes in two list, a,b as arguments. The function should return a new list containing elements that are in both of the two lists

# you may assume that each input list does not contain duplicate elements

#1) Define a function that takes two lists (a and b) as arguments
def intersection(a, b):
#2) Create an empty list to store common elements
  result = []
#3) Convert list a into a set for faster lookup
  item_set = set(a)
#4) Loop through each element in list b
  for elem in b:
#5) If the element exists in the set
    if elem in item_set:
#6) Add the element to the result list
      result.append(elem)
#7) Return the list of common elements
  return result

# def intersection(a, b):
#   set_a = set(a)
#   return [ item for item in b if item in set_a ]

print(intersection([1, 2, 3, 4], [3, 4, 5, 6]))
#[3,4]


#exclusive items
#Write a function, exlusive_items, that takes in two list, a,b as arguments. The Function should return a new list containing elements that are in either list but not both lists.

#you may assume that each list does not contain duplicate elements.

#1) Define a function that takes two lists (a and b) as arguments
def exclusive_items(a, b):
#2) Create an empty list to store items that are only in one list
  difference = []
#3) Convert list a into a set for faster lookup
  set_a = set(a)
#4) Convert list b into a set for faster lookup
  set_b = set(b)
#5) Loop through each item in list a
  for item in a:
#6) If the item is not in set b, add it to the difference list
    if item not in set_b:
      difference.append(item)
#7) Loop through each item in list b
  for item in b:
#8) If the item is not in set a, add it to the difference list
    if item not in set_a:
      difference.append(item)
#9) Return the list of exclusive items
  return difference

#test
print(exclusive_items([1, 2, 3, 4], [3, 4, 5, 6]))
#[1, 2, 5, 6]


#What can you use a 'hashmap' in python?
# A python dictionary can be used as a hashmap

#What is the time complexity of checking membership in a set?
#Checking membership in a set is O(1) time

#What are the two properties of sets?
#set elements are unique and unordered

#what is the time complexity of inserting an element into a set?
#set insertion is O(1) time

#What is the time complexity of checking membership in a list?
#checking membership in a list is O(n) time

#How is a set different from a map?
#Maps store key-value pairs while sets only store keys.


#all unique
#Write a function, all_unique, that takes in a list. The function should return a boolean indicating whether or not the list contains unique items.

#1) Define a function that takes a list (items) as an argument
def all_unique(items):
#2) Convert the list into a set to remove duplicates
  unique_items = set(items)
#3) Return True if the set size equals the list size (all items are unique), otherwise False
  return len(unique_items) == len(items)

#print(all_unique([1, 2, 3, 4]))         # True — all items are unique
# print(all_unique([1, 2, 2, 3, 4]))      # False — 2 appears twice
# print(all_unique(['a', 'b', 'c']))      # True
# print(all_unique(['a', 'b', 'a']))      #False


#intersection with dupes
#write a function, intersection_with_dupes, that takes in two lists, a,b as arguments. The function should return a new list containing elemets that are common to both input lists. The elements in the result should appear as many times as they occur in both input lists.

#you can return the result in any order.

#1) Import Counter from collections to easily count elements
from collections import Counter
#2) Define a function that takes two lists (a and b) as arguments
def intersection_with_dupes(a, b):
#3) Count the frequency of each element in list a
  count_a = Counter(a)
#4) Count the frequency of each element in list b
  count_b = Counter(b)
#5) Create an empty list to store the intersection with duplicates
  result = []
#6) Loop through each unique element in count_a
  for element in count_a:
#7) For the minimum times the element appears in both lists
    for i in range(0, min(count_a[element], count_b[element])):
#8) Add the element to the result list
      result.append(element)
#9) Return the list containing the intersection with duplicates
  return result

#test
print(intersection_with_dupes(["a", "b", "c", "b"], ["x", "y", "b", "b"]))


🎯 Summary:

You are in a hashing problem if:
You need to count something → use dict
You need to check if something exists fast → use set
You want fast access instead of looping again and again → use dict or set