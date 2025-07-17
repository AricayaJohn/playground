#linked list

#write a function, linked_list_values, that takes in the head of a linked list as an argument. The function should return a list containing all values of the nodes in the linked list.

#Iterative
#collect values from a linked list using a loop
def linked_list_values(head):
#create an empty list to store values
    values = []
#start at the head of the list 
    current = head
#loop until the end of the list
    while current is not None:
#Add current node's value to the list
        values.append(current.val)
#move to the next node
        current = current.next
#return the collected values
    return values


#Recursive
#collect values from a linked list using recursion
def linked_list_values(head):
#create an empty list to store values
    values = []
#call the helper function
    _linked_list_values(head, values)
#return the collected values
    return values

#helper function to do the recursion
def _linked_list_values(head, values):
#base case: if no more nodes, stop
    if head is None:
        return
#Add current node;s value
    values.append(head.val)
#recurse on the next node
    _linked_list_values(head.next, values)


#testCase:
class Node:
  def __init__(self, val):
    self.val = val
    self.next = None

#create a linked list: A->B ->C->D
a = Node("A")
b = Node("B")
c = Node("C")
d = Node("D")
a.next = b
b.next = c
c.next = d

#testCase
print(linked_list_values(a))




#sumlist
#write a function, sum_list, that takes in the head of a linked list containing numbers as an argument. The function should return the total sum of all values in the linked list.

#iterative solution
#calculate the sum of all values in a linkeed list using a loop

def sum_list(head):
#initialize sum to 0
    total_sum = 0
#start the head of the list
    current = head
#traverse the list
    while current is not None:
#add current node's value to the sum
        total_sum += current.val
#move to the next node
        current = current.next
#return the total sum
    return total_sum


#recursive solution
#calculate the sum of all values in a linked list using recursion
def sum_list(head):
#basecase: if the list is empty, return 0
    if head is None: 
        return 0
#add current value to sum of rest
    return head.val + sum_list(head.next)


#testCase:
class Node:
    def __init(self, val):
        self.val = val
        self.next = None

a = Node(2)
b = Node(8)
c = Node(3)
d = Node(-1)
e = Node(7)

a.next = b
b.next = c
c.next = d
d.next = e

print(sum_list(a)) #19


#linked list find
#write a function linked_list_find, that takes in the head of a linked list and a target value.
#the function should return a boolean indicating whether or not the linked list contains the target.

#Check if a target value exists in a linked list using a loop
def linked_list_find(head, target):
#start at the head of the list
    current = head
#Traverse until the head
    while current is not None:
#If current value matches target
        if current.val== target:
#return True if found
            return True
#move to next node
        current = current.next
#if loop ends, target was not found
    return False



#using recursion
def linked_list_find(head, target):
#BaseCase: if list is empty, return false
    if head is None:
        return False
#if current value matches target
    if head.val == target:
        return True
#recur on the rest of the list
    return linked_list_find(head.next, target)


#testcase:
class Node:
  def __init__(self, val):
    self.val = val
    self.next = None

a = Node("a")
b = Node("b")
c = Node("c")
d = Node("d")

a.next = b
b.next = c
c.next = d

#a -> b -> c -> d

print(linked_list_find(a, "q")) #False




#get node value
#write a function, get_node_value, that takes in the head of a linked list and an index. The function should return the value of the linked list at the specified index.

#Return the value at a specific index in a linked list using a loop
def get_node_value(head, index):
#start counting from 0
    count = 0
#begin at the head of the list
    current = head
#traverse until index matches target
    while current is not None:
#if current index matches target
        if count == index:
#return the value at this node
            return current.val
#move to the next node
        current = current.next
#Increase the index counter
        count += 1
#if index is out of bounds, return none
    return None


#using recursion
def get_node_value(head, index):
#baseCase: if list is empty, return None
    if head is None:
        return None
#if index is 0, return current node's value
    if index == 0:
        return head.val
#recur on the next node with a reduced index
    return get_node_value(head.next, index -1)


#testCase:
class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
    
a = Node('a')
b = Node('b')
c = Node('c')
d = Node('d')


a.next = B
b.next = C
c.next = D

# a -> b -> c -> d

get_node_value(a, 3) #'d




#reverselist
#write a function, reverse_list, that takes in the head of a linked list as an argument. The function should reverse the order of the nodes in the linked list in-place and return the new head of the reversed linked list.

#reverse a linked list using a loop
def reverse_list(head):
#this will become the new tail
    prev = None
#start at the head of the list
    current = head
    while current is not None:
#save the next node
        next = current.next
#reverse the link
        current.next = prev
#move prev forward
        prev = current
#moe current forwaerd
        current = next
#return the new head(previous tail)
    return prev


#Reversed a linked list using recursion
def reverse_list(head, prev = None):
#Base case: end of list, return new head
    if head is None: 
        return prev
#save the next node 
    next = head.next
#reverse the current node's link
    head.next = prev
#recur with next node and new prev
    return reverse_list(next, head)




#zipper list
#write a function, zipper_lists, that takes in the head of two linked lists as arguments. The function should zipper the two list together into single linked list by alternating nodes. If one of the linked lists is longer than the other, the resulting list should terminate with the remaining nodes. The function should return the head of the zippered linked likst.

#do this in-place, by mutating the original nodes.

#zipper two linked lists by alternating two nodes
def zipper_list(head_1, head_2):
#start the zipper at head_1
    tail = haid_1
#move to the next node in the list 1
    current_1 = head_1.next
#start at head of list 2
    current_2 = head_2
#use to alternate between lists
    count = 0

#loop while both lists still have nodes
    while current_1 is not None and current_2 is not None:
#even count: use a node from list 2
        if count % 2 == 0:
            tail.next = current_2
            current_2 = current_2.next
#odd count: use a node from list 1
        else:
            tail.next = current_1
            current_1 = current_1.next
#move the tail forward
        tail = tail.next
        count += 1
#attached remaining nodes if one list is longer
    if current_1 is not None:
        tail.next = current_1
    if current_2 is not None:
        tail.next = current_2
#return the head of the new zipped list
    return head_1



#zipper two linked lists using recursion
def zipper_lists(head_1, head_2):
#if both lists empty
    if head_1 is None and head_2 is None:
        return None
#if list 1 is empty
    if head_1 is None:
        return head_2
#if lists is empty
    if head_2 is None:
        return head_1
#save next node in list1
    next_1 = head_1.next
#save next node in list2
    next_2  = head_2.next
#link head_1 to head_2
    head_1.next = head_2
#recur for the rest
    head_2.next = zipper_lists(next_1, next_2)
#return the new head of the zipped list
    return head_1




#merge lists
#write a function, merge_lists, that takes in the head of two sorted linkedlists as arguments. The function should merge the two lists together into single sorted linked list. The function should return the head of the merged linked list.

#merge two sorted linked lists using iteration
def merge_lists(head_1, head_2):
#create a dummy node to simplify merging
    dummy_head = Node(None)
#tail keeps track of the last node in the merged list
    tail = dummy_head
#start the head of the first list
    current_1 = head_1
#start at the head of the second list
    current_2 = head_2

#loop until one list runs out
    while current_1 is not None and current_2 is not None:
        if current_1.val < current_2.val:
#attach node from list 1 
            tail.next = current_2.val:
#move to next node in list 1 
            current_1 = current_1.next
        else:
#attach node from list 2
            tail.next = current_2
#move to next node in list 2
            current_2 =current_2.next
        tail = tail.next
#attach the rest of whichever list is not empty
    if current_1 is not None:
        tail.next = current_1
    if current_2 is not None:
        tail.next = current_2
#return the merged list(skip dummy head)
    return dummy_head.next


#merge two sorted linked lists using recursion
def merged_lists(head_1, head_2):
    if head_1 is None and head_2 is None:
        return None
    if head_1 is None:
        return head_2
    if head_2 is None:
        return head_1
    
    if head_1.val < head_2.val:
#recursively merge the rest of list 1 and list 2
        head_1.next = merge_lists(head_1.next, head_2)
        return head_1
    else:
#recursively merge list 1 and the rest of the list 2
    head_2.next = merge_lists(head_1, head2.next)
    return head_2




#is univalue list
#write a function, is_unvalua_list, that takes in the head of a linked list is an argument. The function should return a boolean indicating whether or not the linked list contains exactly one unique value.

#check if all nodes in the linked list have the same value(Iterative)
def is_unvalua_list(head):
#start with the head node
    current = head
#traverse the list
    while current is not None:
#if any value differs from the head's value
        if current.val != head.val
#if its not a univalue list
            return False
#move to the next node
        current = current.next
#All the values matched so return True
    return True



#check if all nodes in the linked list have the same value.(recursively)
def is_univalue_list(head, prev_val = None):
#basecase end of the list
    if head is None:
        return True
    if prev_val is None or head.val == prev_val:
#continue with updated value
        return is_univalue_list(head.next, head.val)
    else:
#value doesnt match, not univalue
        return False




#longest streak
#write a function, longest_streak, that takes in the head of a linked list as an argument. The function should return the length of the longest consecutive streak of the same value within the list.

# Return the length of the longest consecutive streak of the same value in the linked list
def longest_streak(head):
  max_streak = 0           # Tracks the longest streak found so far
  current_streak = 0       # Tracks the current streak length
  prev_val = None          # Keeps track of the previous node's value
  
  current_node = head      # Start at the head of the list
  while current_node is not None:     # Traverse the entire list
    if current_node.val == prev_val:  # If current value matches previous
      current_streak += 1             # Increase the streak
    else:
      current_streak = 1              # Start a new streak

    prev_val = current_node.val       # Update the previous value

    if current_streak > max_streak:   # Check if current streak is the longest
      max_streak = current_streak     # Update the max streak

    current_node = current_node.next  # Move to the next node
    
  return max_streak                   # Return the longest streak found



#remove node
#Write a function, remove_node, that takes in the head of a linked list and a target value as arguments. The function should delete the node containing the target value from the linked list and return the head of the resulting linked list. If the target appears multiple times in the linked list, only remove the first instance of the target in the list.


def remove_node(head, target_val):
# If the head itself holds the target value, skip it and return the next node
  if head.val == target_val:
    return head.next

  current = head       # Start traversing from the head
  prev = None          # To keep track of the previous node

  while current is not None:
    if current.val == target_val:
      prev.next = current.next  # Remove the node by skipping it
      break                     # Exit the loop once node is removed
    prev = current              # Move prev to current
    current = current.next      # Move to the next node

  return head                   # Return the (possibly unchanged) head node




def remove_node(head, target_val):
  # Base case: if list is empty, return None
  if head is None:
    return None

  # If the current node has the target value, remove it by returning the next node
  if head.val == target_val:
    return head.next

  # Recursively call remove_node on the next node
  head.next = remove_node(head.next, target_val)

  return head  # Return the head after updates




#insert node
#Write a function, insert_node, that takes in the head of a linked list, a value, and an index. The function should insert a new node with the value into the list at the specified index. Consider the head of the linked list as index 0. The function should return the head of the resulting linked list.

# This class defines a node in the linked list
class Node:
  def __init__(self, val):
# Store the value
    self.val = val
# Pointer to the next node (initially None)
    self.next = None

# -------- Iterative Version --------
def insert_node(head, value, index):
# If inserting at the beginning
  if index == 0:
    new_head = Node(value)       # Create a new node
    new_head.next = head         # Point new node to the current head
    return new_head              # New node becomes the new head
    
  count = 0                      # Counter to track position
  current = head                 # Start from the head

  while current is not None:
# Check if we're at the position just before the desired index
    if count == index - 1:
      temp = current.next               # Save the current next node
      current.next = Node(value)        # Insert the new node
      current.next.next = temp   # Link the new node to the rest of the list
      break                             # Stop after inserting
    
    count += 1                  # Move to the next position
    current = current.next      # Move to the next node
    
  return head                   # Return the updated head



# -------- Recursive Version --------
def insert_node(head, value, index, count = 0):
# If inserting at the beginning
  if index == 0:
    new_head = Node(value)      # Create a new node
    new_head.next = head        # Point new node to the current head
    return new_head             # New node becomes the new head
  
# Base case: if the list ends before reaching the index
  if head is None:
    return None
  
# If we're at the node just before the desired index
  if count == index - 1:
    temp = head.next                  # Save the current next node
    head.next = Node(value)          # Insert the new node
    head.next.next = temp        # Link the new node to the rest of the list
    return head                      # Return head after insertion
  
# Recursive call to move to the next node
  insert_node(head.next, value, index, count + 1)
  return head                   # Return head after recursive call completes



#what two properties are typically stored in the nodes of a singly linked-list
#'value' and 'next'. The 'value' is the data being stored and 'next' is a reference to the next sequential node in the list

#what term is commonly used to describe the 'first node' of a linked list?
#head

#what is the optimal complexity we can achieve for searching for a target value in a standard, singly linked-list?
#O(n) time and O(1) space if we do it iteratively. The recursive solution would be less optimal at O(n) time and O(n) space.

#why might the expression 'current.next.val' be unsafe?
# if the current is the tail node, the expression throws an error because 'current.next' is null and null does not have a val property

#what is the 'dummy head' pattern for linked lists?
#the 'dummy head' pattern is where we use a fake node to act as the head of the linked list. The dummy node is used to simplify edge cases such as inserting the first node into an empty linked list.

#What term is commenly used to describe the 'last node' of a linked list?
#tail


