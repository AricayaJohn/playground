#array and string

#runningsum
""" 
Write a function, running_sum, that takes in a list of numbers. The function should return a new list of the same length where each element contains the running sum up to that index of the original list.
"""

#Function to compute the running sum of a list of numbers
def runnning_sum(numbers):
#initialize a variable to keep the cumulative sum
    total = 0
#list to store the running sum at each step
    result = []
#iterate through each number in the input list
    for num in numbers:
#add the current number to the cumulative total
        total += num
#append the current total to the result list
        result.append(total)
#return the final list of running sums
    return result


# testcase:
print(running_sum([1, 2, 3, 4])) #output: [1 , 3, 6, 10 ]


#has subarray sum
"""
Write a function, has_subarray_sum, that takes in a list of numbers and a target_sum. The function should return a boolean indicating whether or not there exists a subarray of numbers that sums to the given target.

A subarray is a consecutive series of one or more elements of the list 
"""

#function to determine if there esists a contiguous subarray
#whose elements sum up to the given target_sum

def has_subarray_sum(numbers, target_sum):
#initialize prefix sums with a zero to handle subarrays starting at index 0
    prefix_sums = [0]
#variable to keep a running total of the sum of elements
    total = 0
#first pass: compute prefix sums
    for num in numbers:
        total += num
        prefix_sums.append(total)
#second pass: check all pairs of start and end indices
#if the difference of prefix sums equals target_sum, a subarray exists
    for start in range(0, len(prefix_sums)):
        for end in range(start + 1, len(prefix_sums)):
            if prefix_sums[end] - prefix_sums[start] == target_sum:
#found valid subarray
                return True 
#No valid subarray found
    return False

print(has_subarray_sum([1, 3, 2, 5, 1], 8)) #output: true
print(has_subarray_sum([1, 2, 3], 7)) #output: false


#subarray sum count
"""
write a function, subarray_sum_count, that takes in a list of numbers and a targetSum. The function should return the number of subarrays that sum to the given target.

A subarray is a consecutive series of one or more elements of the list.
"""

from collections import Counter
#function to count the humber of contigous subarrays
#that sum up to the given target_sum
def subarray_sum_count(numbers, target_sum):
#initialize prefix sums with 0 to handle subarray starting at index 0
    prefix_sums = [0]
    total = 0
#compute prefix sums from the original array
    for num in numbers:
        total += num
        prefix_sums.append(total)
#to store frequency of prefix sums encountered
    seen = Counter()
#to keep track of the total number of valid subarrays
    count = 0
#traverse the prefix sums

    for current in prefix_sums:
#check if there's a previous prefix sum such that:
#current - previous  = traget_sum -> subarray sum equals target_sum
        complement = current - target_sum
        count += seen[complement]
        seen[current] += 1

#record current prefix sum in the counter
    return count

print(subarray_sum_count([1, 2, 3], 3))         # Output: 2
# Explanation: Subarrays [1,2] and [3] sum to 3

print(subarray_sum_count([1, 1, 1], 2))         # Output: 2
# Explanation: Subarrays [1,1] at indices (0,1) and (1,2)

print(subarray_sum_count([1, 1, 1, 1], 2)) # -> 3




#merge






