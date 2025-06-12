#linked list 2

#linked palindrome
"""
Write a function, linked_palindrome, that takes in the head of a linked list as an argument. The function should return a boolean indicating whether or not the linked list is a palindrome. A palindrome is a sequence that is the same both forwards and backwards.
"""
#Function to check if the singly linked list fors a palindrome
def linked_palindrome(head):
#list to store the values of the linked list nodes
    values = []
#pointer to traverse through the linked list starting from the head
    current = head
#loop through the linked list and collect the node values
    while current is not None:
#add the current node's value to the list
        values.append(current.val)
#move the next node in the list
        current = current.next
#check if the list of values is equal to its reverse
    return values == values[::-1]

#testcase:
class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

# Helper function to build a linked list from a list of values
def build_linked_list(values):
  if not values:
    return None
  head = Node(values[0])
  current = head
  for val in values[1:]:
    current.next = Node(val)
    current = current.next
  return head

# Create a palindrome linked list: 1 -> 2 -> 3 -> 2 -> 1
head = build_linked_list([1, 2, 3, 2, 1])
print(linked_palindrome(head))  # Output: True



#middle value 
"""
write a function, middle_value, that takes in the head of a linked list as an argument. The function should return the value of the middle node in the linked list. If the linked list has an even number of nodes, then return the value of the second middle node.
"""
#using list to store values
#function to return the middle value of a linked list using a list to store node values
def middle_value(head):
#list to store the values of each node
    values = []
#Pointer to traverse the linked list
    current = head
#traverse and collect values in the list
    while current is not None:
#append current node's value
        value.append(current.val)
#move to the next node
        current = current.next
#return the middle value using integer division for index
    return values[len(values) // 2]



#using fast and slow pointers 
#Function to return the middle value using two-pointer technique
def middle_value(head):
#slow pointer moves 1 step, fast pointer moves 2 steps
    slow = head
    fast = head
#continue until fast reaches the end of the list
    while fast is not None and fast.next is not None:
#move slow by 1 node
        slow = slow.next
#move fast by 2 nodes
        fast = fast.next.next
#when fast reaches the end, slow will be at the middle 
    return slow.val

#test case
#define a simple linked list node class
class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

#Helper to create alinked list from a list
def build_linked_list(values):
    if not values:
        return None
    head = Node(values[0])
    current = head
    for val in values[1:]:
        current.next = Node(val)
        current = current.next
    return head
#test with odd number
head = build_linked_list([1, 2, 3, 4, 5])
print(middle_value(head)) # output: 3

#test with even number of nodes: [10, 20, 30, 40]
head2 = build_linked_list([10, 20, 30, 40])
print(middle_value(head2)) #output 30



#linked list cycle
"""
Write a function, linked_list_cycle, that takes in the head of a linked list as an argument. The function should return a boolean indicating whether or not the linked list contains a cycle.
"""

#function to detect a cycle using a linked list using a set
def linked_list_cycle(head):
#set to store visited nodes
    nodes = set()
#pointer to traverse the linked list
    current = head
#iterate through the list
    while current is not None:
#if the current node has already been seen, a cycle exists
        if current in nodes:
            return True
#mark the current node as visited
        nodes.add(current)
#move to the next node
        current = current.next
#No Cycle detected
    return False


#Function to detect a cycle using fast and slow pointers(floyd's cycle detection)
def linked_list_cycle(head):
#boolean flag to ignore the initial match when both pointers start at the head
    first_iteration = True
#initialize slow and fast pointers
    slow = head
    fast = head
#traverse while fast and fast.next are valid
    while fast is not None and fast.next is not None:
#if slow and fast pointers meet again after the first iteration, cycle exists
        if slow is fast and not first_iteration:
            return True
#After the first comparison, turn off the first_iteration flag
        first_iteration = False
#move slow pointer one step
        slow = slow.next
#move fast pointer two steps
        fast = fast.next.next
#if no cycle is detected
    return False


# Define a simple linked list node class
class Node:
  def __init__(self, val):
    self.val = val
    self.next = None

# Create a list: 1 -> 2 -> 3 -> 4 -> 5
a = Node(1)
b = Node(2)
c = Node(3)
d = Node(4)
e = Node(5)

a.next = b
b.next = c
c.next = d
d.next = e

# No cycle
print(linked_list_cycle(a))  # Output: False

# Create a cycle: 5 -> 3 (loop back to node c)
e.next = c

# Cycle exists
print(linked_list_cycle(a))  # Output: True



#undupe sorted linked list
"""
Write a function that takes in a linked list that contains values in increasing order. The function should return a new linked list containing the original values, with duplicates removed. The relative order of values in the resulting linked list should be unchanged.
"""

#definition for a singly linked list node
class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

#Function to remove duplicates from a sorted linked list
def undupe_sorted_linked_list(head):
#create a dummy node to serve as the new list's starting point
    dummy_head = Node(None)
#tail will always point to the last node in the new deduplicated list
    tail = dummy_head
#current will traverse the input list
    current = head
#traverse the entire original linked list
    while current is not NoneL
#if the current value is different fromt he last added (tail) value it's unique
        if current.val != tail.val:
#create a new node with the current value and append it to the result list
            tail.next = Node(current.val)
#move the tail pointer to the newly added node
            tail = tail.next
#move to the next node in the original list
        current = current.next

#return the next node of the dummy head, which is the actual start of the deduplicated list
    return dummy_head.next

# Helper function to build a linked list from a list of values
def build_linked_list(values):
  if not values:
    return None
  head = Node(values[0])
  current = head
  for val in values[1:]:
    current.next = Node(val)
    current = current.next
  return head

# Helper function to print linked list values
def print_linked_list(head):
  current = head
  values = []
  while current:
    values.append(current.val)
    current = current.next
  print(values)

# Test: Deduplicate a sorted linked list with repeated values
original = build_linked_list([1, 1, 2, 2, 2, 3, 3, 4])
deduped = undupe_sorted_linked_list(original)
print_linked_list(deduped)  # Output: [1, 2, 3, 4]



#create linked list
"""
Write a function, create_linked_list, that takes in a list of values as an argument. The function should create a linked list containing each item of the list as the values of the noes. The function should return the head of the linked list.
"""

#node class to represent each element of the linked list
class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

#iterative version of create_linked_list
def create_linked_list(values):
#create a dummy head node to simplify edge cases
    dummy_head = Node(None)
#tail will point to the last node in the linked list
    tail = dummy_head
#iterate over all values to create nodes
    for val in values:
#create a new node with the curent value and link it
        tail.next = Node(val)
#move the tail to point to the newly added node
        tail = tail.next
#return the actual head(ignoring dummy head)
    return dummy_head.next


#recursive version of create_linked_list
def create_linked_list(values, i = 0):
#basecase: if index reaches the end of the list, return None
    if i == len(values):
        return None
#create a new node with the current value
    head = Node(values[i])
#recursively set the next node
    head.next = create_linked_list(values, i + 1)
#return the head of the linked list
    return head

# helper function to print linked list values for verification
def print_linked_list(head):
  current = head
  while current is not None:
    print(current.val, end=" -> ")
    current = current.next
  print("None")

# --- test cases ---

# testing iterative version
print("Iterative version:")
head1 = create_linked_list(["a", "b", "c"])  # should create a -> b -> c -> None
print_linked_list(head1)

# testing recursive version
print("Recursive version:")
head2 = create_linked_list(["x", "y", "z"])  # should create x -> y -> z -> None
print_linked_list(head2)




#Build a Queue
"""
Implement the enqueue and dequeue methods for the existing class. The enqueue method should add a given value into the queue. The dequeue should return and remove an item from the queue following first-in, first out order.
"""
#node class to represent each element of the linked list
class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

#iterative version of create_linked_list
def create_linked_list(values):
    #create a dummy head node to simplify edge cases
    dummy_head = Node(None)
    #tail will point to the last node in the linked list
    tail = dummy_head
    #iterate over all values to create nodes
    for val in values:
        #create a new node with the curent value and link it
        tail.next = Node(val)
        #move the tail to point to the newly added node
        tail = tail.next
    #return the actual head(ignoring dummy head)
    return dummy_head.next


#recursive version of create_linked_list
def create_linked_list(values, i = 0):
    #basecase: if index reaches the end of the list, return None
    if i == len(values):
        return None
    #create a new node with the current value
    head = Node(values[i])
    #recursively set the next node
    head.next = create_linked_list(values, i + 1)
    #return the head of the linked list
    return head

#define a node class to represent each element in the queue
class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

#Define the Queue class using a singly linked list
class Queue:
    def __init__(self):
        #points to the front of the queue
        self.head = None
        #points to the rear of the queue
        self.tail = None
        #tracks the number of elements in the queue
        self.size = 0

    #Method to add an element to the end of the queue
    def enqueue(self, val):
        if self.size == 0:
            #if the queue is empty, create the first node and assign both head and tail
            self.head = Node(val)
            self.tail = self.head
        else:
            #otherwise, append the new node to the end and update the tail
            self.tail.next = Node(val)
            self.tail = self.tail.next
        #increment the size of the queue
        self.size += 1

    #method to remove and return the element from the front of the queue
    def dequeue(self):
        if self.size == 0:
            #if the queue is empty, return None
            return None
        #store the value at the front of the queue
        value = self.head.val

        if self.size == 1:
            #if there is only one element, reset head and tail to None
            self.head = None
            self.tail = None
        else:
            #otherwise, move the head pointer to the next node
            self.head = self.head.next

        #decrement the size of the queue
        self.size -= 1
        #return the removed value
        return value

# Create a new queue
q = Queue()

# Enqueue some values
q.enqueue(10)
q.enqueue(20)
q.enqueue(30)

# Dequeue and print values
print(q.dequeue())  # Output: 10
print(q.dequeue())  # Output: 20

# Check the current size
print(q.size)       # Output: 1

# Dequeue the last element
print(q.dequeue())  # Output: 30

# Try dequeueing from an empty queue
print(q.dequeue())  # Output: None

# Final size
print(q.size)       # Output: 0


#add list
""" 
Write a function, add_lists, that takes in the head of two linked lists, each representing a number. The nodes of the linked lists contain digits as values. The nodes in the input lists area reversed this means that the least significant digit of the number is the head. The function should return the head of a new linked listed representing the sum of the input lists. The output list should have its digits reversed as well.
"""

#define a node class for linked list nodes
class node:
    def __init__(self, val):
        self.val = val
        self.next = None
#Recursive function to add two numbers represnted by linked lists
def add_lists(head_1, head_2, carry = 0):
#Base case: if both lists are exhausted and no carry remains, end recursion
    if head_1 is None and head_2 is None and carry == 0:
        return None
#Get the calues from the current nodes, or 0 if the node is none
    val_1 = 0 if head_1 is None else head_1.val
    val_2 = 0 if head_2 is None else head_2.val
#Compute the sum of the values and the carry 
    sum = val_1 + val_2 + carry
#Determine carry for the next digit(1 if sum is more than 9)
    next_carry = 1 if sum > 9 else 0
#extract the digit to store in the current node
    digit = sum % 10
#Create a new node with the computed digit
    result = Node(digit)
#Advance to the next nodes in both lists
    next_1 = None if head_1 is None else head_1.next
    next_2 = None if head_2 is None else head_2.next

#recursively add the rest of the list and attach the result to the current node
    result.next = add_lists(next_1, next_2, next_carry)

#return the current node, which is part of the final sum list 
    return result

# Helper function to create a linked list from a list of digits
def create_linked_list(values):
  dummy = Node(None)
  current = dummy
  for val in values:
    current.next = Node(val)
    current = current.next
  return dummy.next

# Helper function to print a linked list
def print_linked_list(head):
  vals = []
  while head:
    vals.append(str(head.val))
    head = head.next
  print(" -> ".join(vals))

# Create two linked lists representing 243 and 564 (3->4->2 and 4->6->5)
a = create_linked_list([3, 4, 2])  # 243
b = create_linked_list([4, 6, 5])  # 564

# Perform addition: 243 + 564 = 807
result = add_lists(a, b)

# Output the result list: should print 7 -> 0 -> 8
print_linked_list(result)


#iterative alternative:
def add_lists(head_1, head_2):
  dummy_head = Node(None)
  tail = dummy_head
  
  carry = 0
  current_1 = head_1
  current_2 = head_2
  while current_1 is not None or current_2 is not None or carry == 1:
    val_1 = 0 if current_1 is None else current_1.val
    val_2 = 0 if current_2 is None else current_2.val
    sum = val_1 + val_2 + carry
    carry = 1 if sum > 9 else 0
    digit = sum % 10
    
    tail.next = Node(digit)
    tail = tail.next
    
    if current_1 is not None:
      current_1 = current_1.next
      
    if current_2 is not None:
      current_2 = current_2.next
      
  return dummy_head.next
