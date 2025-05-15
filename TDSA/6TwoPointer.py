#Two Pointer

#is palindrome
#Write a function, is_palindrome, that takes in a string and returns a boolean indicating whether or not the string is the same forwards and backwards.

def is_palindrome(s):
#initialize a pointer at the start of the string
    i = 0
#initialize a pointer at the end of the string
    j = len(s) - 1
#loop until the two pointers meet in the middle
    while i < j:
#if characters at the current pointers dont match, it's not a palindrome
    if s[i] != s[j]:
        return False
#move the start pointer forward
    i += 1
#move the end pointer backward
    j -= 1

#if the loop completes without finding mismatches, it's a palindrome
return True

#testCase:
print(is_palindrome("racecar"))
print(is_palindrome("hello"))




#uncompress
#write a function, uncompress, that takes in a string as an argument. 
#The input string will be formatted into multiple groups according to the following pattern
<number><char>

for example, '2c' or '3a'.

#The function should return an uncompressed version of the string where each 'char of a group is repeated 'number' times consecutively. You may assume that the input string is well-formed according to the previously mentioned pattern.

def uncompress(s):
#define the set of characters considered as digits
    numbers = '0123456789'
#this will store the final uncompressed string pieces
    result = []
#two pointers to track the current number and character
    i = 0
    j = 0
#loop until the end of the string
    while j < len(s):
#move the j forward as long as the character is a digit
        if s[j] in numbers:
            j += 1
        else:
#slice the substring between i and j to get the number
        num = int(s[i:j])
#multiply the character at position by j by the number and add to result
        result.append(s[j] * num)
#move to the next segment: set both i and j past the current character
        j += 1
        i = j
#join the list of strings into one string and return it
    return ''.join(result)

#testcase
print(uncompress("2c3a1t"))



#Compress
#write a function, compress, that takes in a string as an argument. The function should return a compressed version of the string where consecutive occurences of the same characters are compressed into the number of occurrences followed by the character. Single Character occurrences should not be changed.

'aaa' compresses to '3a'
'cc' compresses to '2c'
't' should remain as 't'

def compress(s):
#add a dummy character to ensure the last group is processed
    s += '!'
#this will store the compressed result as a list of strings
    result = []
#use two pointers to track the start and current charcter
    i = 0
    j = 0
#loop through the string
    while j < len(s):
#move the j forward as long as the character matches the one at i
        if s[i] == s[j]:
            j += 1
        else:
#number of times the character at s[i] repeats
            num = j - I
#if it appears only once, just add the character
            if num == 1:
                result.append(s[i])
            else: 
#if more than once, add the count followed by the character
                result.append(str(num))
                result.append(s[i])
#move the i to the start of the next group
            i = j
#join the list into a single string and return
    return ''.join(result)



#test case 
print(compress("ccaaat"))     # Output: "2c3a1t" → Actually, will output "2c3at"
print(compress("abc"))        # Output: "abc"
print(compress("ssssbb"))     # Output: "4s2b"




#five sort
#write a function, five_sort, that takes in a list of numbers as an argument. The function should rearrange elements of the list such that all 5s appear at the end. Your function should perform this operation in-place by mutating the original list. The function should return the list.

#elements that are not 5 can apear in any order in the output, as long as all 5s are at the end of the list.

#your function needs to mutate the original list in-place and should not return a new list. It will fail the test cases if you do not modify the original input list


def five_sort(nums):
#initialize two pointers: i from the start, j from the end
    i = 0
    j = len(nums) - 1

#continue until the two pointers meet
    while i < j:
#if the number at the end is already 5, move j left
      if nums[j] == 5:
            j -= 1
#if the number at the start is 5, swap it with nums[j]
      elif nums[i] == 5:
        nums[i], nums[j] = nums[j], nums[i]
#move i to right to check next position
        i += 1
#if nums[i] is not 5, just move i right
      else:
        i += 1
#after processing, return the modified list
    return nums

print(five_sort([12, 5, 1, 5, 12, 7, 5]))




#is subsequence
#write a function, is_subsequence, that takes in string_1 and string_2. The function should return a boolean indicating whether or not string_1 is a subsequence of string_2. 

#A subsequence is a string that can be formed by deleting 0 or more characters from another string.

def is_subsequence(string_1, string_2):
#intialize two pointers:
#i points to current character in string_1 (the potential subsequence)
#j points to current character in string_2 (the full string)
    i = 0
    j = 0
#loop through both strings until one of them ends
    while i < len(string_1) and j < len(string_2):
#if the characters match, move both pointers
    if string_1[i] == string_2[j]:
        i += 1
        j += 1
    else:
# if they dont match, move only the pointer in string_2
    j += 1
#if i has reached the end of string_1, then all its characters were found in order
    return i == len(string_1)

#testcase:
print(is_subsequence('ace', 'abcde')) # true
print(is_subsequence('aec', 'abcde')) # false

    

        
