#subsets
"""
Write a function, subsets, that takes in a list as an argument. The function should return a 2D list where each sublist represents one of the possible subsets of the list. 

The elements within the subsets and the subsets themselves may be returned in any order
"""

def subsets(elements):
#Basecase: if the input list is empty, return a list containing an empty list
    if not elements:
        return [[]]
#take the first element of the list
    first = elements[0]
#recursively find subsets of the remaining elements
    remaining_elements = elements[1:]
    subsets_without_first = subsets(remaining_elements)
#Add the first element to each of the subsets created without it
    subsets_with_first = []
    for sub in subsets_without_first:
#[first] + sub
        subsets_with_first.append([ first, *sub ])
#combine subsets with and without the first element
    return subsets_without_first + subsets_with_first

print(subsets(['a', 'b']))



#permutations
"""
write a function, permutation that takes in a list an argument. The function should return a 2d list where each sublist represents one of the possible permutations of the list.

The sublists may be returned in a ny order.
"""

def permutations(items):
#basecase: if the list is empty, return a list with an empty list(only one permutation)
    if not items:
        return [[]]
#take the first item
    first = items[0]
#recursively get permutations of the remaining items
    remaining = items[1:]
    perms = permutations(remaining)
#this will store all the new permutation
    result = []
#for each permutation of the remaining items
    for perm in perms:
#insert the first item into every possible position in the perm
        for i in range(len(perm) + 1):
            result.append([*perm[:i], first, *perm[i:]])
#return the full set of permutations
    return result

print(permutations(['a', 'b', 'c',]))



#create combinations
"""
Write a function, create_combinations, that takes in a list and a length as arguments. The function should return a 2D list representing all of the combinations of the specified length.

The items withing the combinations and the combinations themselves may be returned in any order.
"""

def create_combinations(items, k):
#if there arent enough items left to make a combination of size k, return empty
    if len(items) < k:
        return []
#base case: one valid combination is selecting 0 items(an empty list)
    if k == 0:
        return [[]]
#take the time frist item
    first = items[0]
#recursively get combinations that include the first item
    combos_with_first = []
    for combo in create_combinations(items[1:], k - 1):
        combos_with_first.append([first, *combo])
#recursively get combinations that do not include the first item
    combos_without_first = create_combinations(items[1:], k)
#return all combinations(with and without the first item)
    return combos_with_first + combos_without_first

#test:
print(create_combinations(['a', 'b', 'c', 'd'], 2))


#grocery budget
"""
write a function, grocery_budget, that takes in grocery_list and a number budget. Every item in grocery_list is a pair contining the item name, and price. Your function should return all possible ways to purchase items without spending more than the given budget.
"""
def grocery_budget(grocery_list, budget):
#if the budget becomes negative, this path is invalid, so return an empty list
    if budget < 0:
        return []
#if the grocery list is empty, return a list containing an empty list as the only valid combo
    if not grocery_list:
        return [[]]
#this will collect all valid item combinations
    all_lists = []
#get the name and price of the current grocery item
    current_item_name, current_item_price = grocery_list[0]
#recursive call: try including the current item
    for list_with_current_item in grocery_budget(grocery_list[1:], budget -current_item_price):
#add the current item to the combination
        list_with_current_item.append(current_item_name)
#save the updated combination
        all_lists.append(list_with_current_item)

#recursive call: try excluding the current item
    lists_without_current_item = grocery_budget(grocery_list[1:], budget)
#combine both sets of combinations
    all_lists += lists_without_current_item

    return all_lists

#test case
groceries = [
  ("apple", 3),
  ("bread", 4),
  ("milk", 2),
  ("cheese", 6)
]

budget = 7

result = grocery_budget(groceries, budget)
print(result)



#lining up
"""
write a function, lining_up, that takes in a list of people and a capacity number. We need to add people to the waitlist for a popular restaurant, but space is limited.
"""

def lining_up(people, capacity):
#basecases: if you ask for more people than available, it;s impossible
    if capacity > len(people):
        return []
#if capacity is 0, there's only one way to line up: an empty lin
    if capacity == 0:
        return [[]]
#this will hold all valid lineups
    all_lines = []

#take the first person from the list
    current_person = people[0]
    remaining_people = people[1:]
#include the current person in the lineup
    for line in lining_up(remaining_people, capacity - 1):
#insert current_person into every position of the smaller line
        for i in range(0, len(line) + 1):
            line_with_current = [*line[:i], current_person, *line[i:]]
            all_lines.append(line_with_current)
#exclude the current person and try the lineup without them
    for line_without_current in lining_up(remaining_people, capacity):
        all_lines.append(line_without_current)

    return all_lines

people = ["A", "B", "C"]
capacity = 2

result = lining_up(people, capacity)
print(result)



#possible paths
"""
Write a function that takes in a graph adjacency list, a source node, and a destination node. The function should return a list containing all possible paths that travel between the source and destination.
"""
