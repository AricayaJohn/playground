#heap
"""
binary tree data structure
stores items 
maintains order between items
similar to binary search tree
"""

#Min Heap
#Parent nodes must be less than or equal to their children

#Max Heap
#Parent nodes must be greater than or equal to their children


"""
Complete Binary Tree
Binary Tree where every level is filled except possibly the bottom level

The nodes at the bottom level must be as far left as possible
"""
"""
add new node to left-most position of bottom level
min heap - "sift up" the new node while it is less than its parent

max heap - "sift up" the new node while it is greater than its parent
"""
# left child: 2i + 1
# right child: 2i + 2 
#parent: floor((i-1)/2)

"""
Sift down
    min heap
    -if target node is greater than child
    -then swap target with the smaller of the two children
    max heap
    -if target node is less than children
    -then swap target with the larger of the two children
"""



#heap insertion
"""
Implement the insert method for the existing class. The method should properly add a given value into the heap, maintaining min heap order and height balance.
"""

class MinHeap:
#initializes an empty list to represent the heap
  def __init__(self):
      self.list = []
#returns True if the heap is empty else false
  def is_empty(self):
      return len(self.list) == 0
#returns the number of elements in the heap
  def size(self):
      return len(self.list)
#swaps two elements at the given indices. used during the heap adjustment process.
  def swap(self, index_1, index_2):
      self.list[index_1], self.list[index_2] = self.list[index_2], self.list[index_1]
#ensures that the heap property is maintained after inserting a new elements
#if the newly added element is smaller than its parent, it "sifts up" to the correct position
  def sift_up(self, index):
      current_index = index
      while current_index > 0:
          parent_index = (current_index - 1) // 2
          if self.list[current_index] < self.list[parent_index]:
              self.swap(current_index, parent_index)
              current_index = parent_index
          else:
              break
#adds a new value to the end of the list
#calls sift_up to maintain the Min Heap property
  def insert(self, val):
      self.list.append(val)
      self.sift_up(self.size() - 1)

# Create a heap and insert some values
heap = MinHeap()
heap.insert(5)
heap.insert(3)
heap.insert(8)
heap.insert(1)

print(heap.list)  # Expected min-heap structure: [1, 3, 8, 5]



#Heap deletion
"""
Implement the extract_min method for the existing class. The method should return and remove the smallest value in the heap, maintaining min heap order and height balance.
"""

#A class representing a Min Heap data structure
class MinHeap:
#initialize an empty heap list
    def __init__(self):
        self.list = []
#returns True if the heap is empty
    def is_empty(self):
        return len(self.list) == 0
#Returns the number of elements in the heap
    def size(self):
        return len(self.list)
#swaps the elements at two indices in the heap list
    def swap(self, index_1, index_2):
        self.list[index_1], self.list[index_2] = self.list[index_2], self.list[index_1]
#moves a newly inserted element up to maintain the min-heap property
    def sift_up(self, index):
        current_index = index
#keep moving up the element until the heap property is satisfied
        while current_index > 0:
#calculate the parent's index 
            parent_index = (current_index - 1 ) // 2
#if the current value is less than the parent's swap them
            if self.list[current_index] < self.list[parent_index]:
                self.swap(current_index, parent_index)
                current_index = parent_index
            else:
                break
#Inserts a new element into the heap
    def insert(self, val):
#add the value to the end of the list 
        self.list.append(val)
#restore the heap property by moving it up
        self.sift_up(self.size() - 1)

#Moves the element at the given index down to maintain the min-heap property
    def sift_down(self, index):
        current_index = index
#keep sifting down until the element is in the correct position
        while current_index < self.size() - 1:
#calculate the indices of the left and right children
          left_child_index = current_index * 2 + 1
          right_child_index = current_index * 2 + 2
#get the values of the children or infinity if out of bounds
          left_child_val = float("inf") if left_child_index >= self.size() else self.list[left_child_index]
          right_child_val = float("inf") if right_child_index >= self.size() else self.list[right_child_index]
#Identify the smaller of the two children
          smaller_child_val = left_child_val if left_child_val < right_child_val else right_child_val
          smaller_child_index = left_child_index if left_child_val < right_child_val else right_child_index
#if the current value is greater than the smaller child, swap them
          if self.list[current_index] > smaller_child_val:
              self.swap(current_index, smaller_child_index)
              current_index = smaller_child_index
          else:
              break
#removes and returns the smallest element from the heap
    def extract_min(self):
#if the heap is empty, return None
        if self.is_empty():
            return None
#if there's only one eleemnt, remove and return it
        if self.size() == 1:
            return self.list.pop()
#save the min value to return later
        min_val = self.list[0]
#move the last element to the root
        self.list[0] = self.list.pop()
#restore the heap property
        self.sift_down(0)
        return min_val

# Test case to verify MinHeap operations
heap = MinHeap()
heap.insert(10)
heap.insert(4)
heap.insert(15)
heap.insert(1)
heap.insert(8)

print(heap.list)  # Should represent a valid min-heap, e.g., [1, 4, 15, 10, 8]
print(heap.extract_min())  # Should print 1
print(heap.extract_min())  # Should print 4
print(heap.list)  # Remaining elements in min-heap order



#kth-largest
"""
Write a function, kth_largest, that takes in a list of numbers and a value, k. The function should return the k-th largest element of the list.
"""
def kth_largest(numbers, k):
#sorts the list in ascending order
    sorted_numbers = sorted(numbers)
#returns the k-th largest element by indexing from the end
    return sorted_numbers[-k]

print(kth_largest([10, 5, 8, 3, 9], 2))  
# Output: 9 (2nd largest number in the list)

#solution2
#importing pythins built-in heap utilities(using a min-heap by default)
import heapq

def kth_largest(numbers, k):
#initialize an empty heap
    heap = []
#iterate through all numbers in thelist
    for num in numbers:
#push the number onto the heap
        heapq.heappush(heap, num)
#if heap size exceeds k, remove the smallest number
        if len(heap) > k:
            heapq.heappop(heap)
#at the end, the heap contains the k largest numbers, and the smallest of them( at the root)
#return the smallest among the k largest => the k-th largest overall
    return heapq.heappop(heap)

"""
What built in module can we use to access a heap in python
The heapq module provides methods like heapq.heappush and heapq.heappop
"""
"""
What is the time complexity of performing a heap insertion
heap insertion is O(log(n))
"""
"""
Why do heap operations take O(log(n)) time?
A heap is a balanced binary tree. The height of a balanced tree is O(log(n))
heap operations will sift values up or down the full height of the tree in the worst case
"""
"""
What data structure is commonly used to implement a binary heap?
A binary heap is commonly implemented using an underlying array
"""
"""
What is max-heap propery for a binary tree?
Max-heap propery means that nodes are greater than or equal to their children
"""

#k-smallest
"""
Write a function that takes in a list of numbers and a value, k. The function should return the k smallest numbers in the list. The resulting list should be ordered from least to greatest.
"""
#sorting
def k_smallest(nums, k):
#sort the list in ascending order
    sorted_nums = sorted(nums)
#return the first 'k' element the (smallest ones)
    return sorted_nums[:k]

print(k_smallest([9, 2, 7, 4, 1], 3))
# Output: [1, 2, 4] → The 3 smallest numbers

import heapq

def k_smallest(nums, k):
#create an empty max heap(simulated using negative values)
    max_heap = []

    for v in nums:
#use a tuple to simulate a max heap with min heap tools
        item = (-v, v)
#push item onto heap
        heapq.heappush(max_heap, item)
#keep only the k smallest values
        if len(max_heap) > k:
#remove the largest(i.e top max heap)
            heapq.heappop(max_heap)

    result = []
#extract elements from heap
    while len(max_heap) > 0:
        item = heapq.heappop(max_heap)
#append the original value(positive)
        result.append(item[1])
#reverse to return in ascending order
    return result[::-1]

print(k_smallest([9, 2, 7, 4, 1], 3))
# Output: [1, 2, 4] → The 3 smallest numbers

