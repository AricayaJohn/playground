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




#merge sort
""" 
Write a function, merge_sort, that takes in a list of numbers as an argument. Thefunction should return a new list containing elements of the original list sorted in ascending order. Your function must implement the merge sort algorithm.
"""
#import deque for efficient popping from the front of lists
from collections import deque
#recursively merge sort function that divides and conquers
def merge_sort(nums):
#basecase: a list with 0 or 1 element is already sorted
    if len(nums) <= 1:
        return nums
#find the midpoint to split the list
    mid_idx = len(nums) // 2
#recursively sort the left and hald
    left_sorted = merge_sort(nums[:mid_idx])
#recursively sort the right half
    righ_sorted = merge_sort(nums[mid_idx:])
#merge the sorted halves and return the sorted list
    return merge(left_sorted, righ_sorted)

#helper function to merge two sorted lists into one sorted list
def merge(list_1, list_2):
#convert both lists to deques for 0(1) pops from the front
    list_1 = deque(list_1)
    list_2 = deque(list_2)
#this will hold the merged and sorted elements
    merged = []
#hile both deques have elements, pop the smallest front element into merged
    while list_1 and list_2:
        if list_1[0] < list_2[0]:
            merged.append(list_1.popleft())
        else:
            merged.append(list_2.popleft())
#append the remaining elements(if any) from both list
    merged += list_1
    merged += list_2
#return the final merged and sorted list
    return merged

#testcase:
print(merge_sort([4, 1, 6, 2, 5, 3])) #output: [1, 2, 3, 4, 5, 6]



#Combined Intervals
"""
Write a funtion, combined_intervals, that takes in a list of intervals as an argument. Each interval is a tuple containing a pair of numbers representing a start and endtime. Your function should combine overlapping intervals and return a list containing the combined intervals.
"""

#Function to combine overlapping intervals from a list of (start, end)
def combine_intervals(intervals):
#sort the intervals by their starting values
    sorted_intervals = sorted(intervals, key=lambda x :x[0])
#initialize the result list with the first interval
    combined = [sorted_intervals[0]]
#iterate over the remaining intervals
    for current_interval in sorted_intervals[1:]:
#Get the last interval in the combined list
        last_start, last_end = combined[-1]
#get the current interval's stsart and end
        current_start, current_end = current_interval
#check if current interval overlaps with the last one in combined
        if current_start <= last_end:
#if it does and the current interval extends further, merge them 
            if current_end > last_end:
                combined[-1] = (last_start, current_end)
        else:
#if it doesn't overlap, just add it to the combined list
            combined.append(current_interval)
#Return the final list of non-overlapping, merged intervals
    return combined

#testcase:
intervals = [(1, 3), (2, 6), (8, 10), (9, 12)]
print(combine_intervals(intervals)) #output: [(1,6), (8,12)]