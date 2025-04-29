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

