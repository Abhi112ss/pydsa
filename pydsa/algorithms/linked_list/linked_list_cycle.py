METADATA = {
    "id": 141,
    "name": "Linked List Cycle",
    "slug": "linked-list-cycle",
    "category": "Linked List",
    "aliases": [],
    "tags": ["two_pointers", "fast_slow_pointers"],
    "difficulty": "easy",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Determine if a linked list has a cycle in it using Floyd's Cycle-Finding Algorithm.",
}

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def solve(head: ListNode) -> bool:
    """
    Args:
        head: The head of a singly-linked list.

    Returns:
        True if there is a cycle in the linked list, False otherwise.
    """
    if not head:
        return False

    slow_pointer = head
    fast_pointer = head

    while fast_pointer and fast_pointer.next:
        slow_pointer = slow_pointer.next
        fast_pointer = fast_pointer.next.next

        if slow_pointer == fast_pointer:
            return True

    return False