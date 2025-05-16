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
    while current cuttent is not None:
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
        if current .val == target:
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
#write a 