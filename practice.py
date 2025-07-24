"""Hashing"""
def anagrams(s1, s2):
    def count_char(s):
        count = {}
        for char in s:
            if char not in count:
                count[char] = 0
            count[char] += 1
        return count
    return count_char(s1) == count_char(s2)

def most_frequent_char(s):
    count = {}
    for char in s:
        if char not in count:
            count[char] = 0
        count[char] += 1
    most_frequent_char = None
    for char in s:
        if most_frequent_char is None or count[char] > count[most_frequent_char]:
            most_frequent_char = char
    return most_frequent_char

"""Linked list"""

def linked_list_values(head):
    values = []
    current = head
    while current is not None:
        values.append(current.val)
        current = current.nexts
    return values

def sum_list(head):
    total_sum = 0
    current = head 

    while current is not None:
        total_sum += current.val
        current = current.next
    return total_sum


def sum_list(head):
    if head is None:
        return 0
    return head.val + sum_list(head.next)


def linked_list_find(head, target):
    current = head 
    while current is not None:
        if current.val == traget
            return True
        current = current.next
    return False

def linkd_list_find(head, target):
    if head is None:
        return False
    if head.val == target:
        return True
    return linked_list_find(head.next, target)



"""Dynamic programming"""
def fib(n):
    memo = {}
    return _fib(n, memo)

def _fib(n, memo):
    if n == 0 or n == 1:
        return n 

    if n in memo:
        return memo[n]

    memo[n] = _fib(n - 1, memo) + _fib(n - 2, memo)
    return memo[n] 






"""Stack"""


