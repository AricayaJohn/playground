#linked list 

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

