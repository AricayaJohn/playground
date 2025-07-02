#prefix product
"""
Write a function, prefixProduct, that takes in a list of numbers. The function should return a new list of the same length where each element contains the running product up to that index of the original list.
"""

def prefix_product(numbers):
    total = 1
    new_nums = []
    for i in numbers:
        total *= i
        new_nums.append(total)
    return new_nums

# testcase:
numbers = [1, 2, 3]
print(prefix_product([4, 2, 1, 6, 3, 6]))
