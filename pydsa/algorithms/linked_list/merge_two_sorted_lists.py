METADATA = {
    "id": 21,
    "name": "Merge Two Sorted Lists",
    "slug": "merge-two-sorted-lists",
    "category": "Linked List",
    "aliases": [],
    "tags": ["linked_list", "recursion", "iteration"],
    "difficulty": "easy",
    "time_complexity": "O(n + m)",
    "space_complexity": "O(1)",
    "description": "Merge two sorted linked lists into one sorted linked list.",
}

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def solve(list1: ListNode | None, list2: ListNode | None) -> ListNode | None:
    """
    Args:
        list1: The head of the first sorted linked list.
        list2: The head of the second sorted linked list.

    Returns:
        The head of the merged sorted linked list.
    """
    dummy_head = ListNode(0)
    current_pointer = dummy_head

    while list1 is not None and list2 is not None:
        if list1.val <= list2.val:
            current_pointer.next = list1
            list1 = list1.next
        else:
            current_pointer.next = list2
            list2 = list2.next
        current_pointer = current_pointer.next

    if list1 is not None:
        current_pointer.next = list1
    elif list2 is not None:
        current_pointer.next = list2

    return dummy_head.next