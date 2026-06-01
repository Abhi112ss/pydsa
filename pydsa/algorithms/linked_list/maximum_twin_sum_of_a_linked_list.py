METADATA = {
    "id": 2130,
    "name": "Maximum Twin Sum of a Linked List",
    "slug": "maximum-twin-sum-of-a-linked-list",
    "category": "Linked List",
    "aliases": [],
    "tags": ["two_pointer", "linked_list"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Find the maximum sum of twin elements in a linked list by reversing the second half and iterating from both ends.",
}

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def solve(head: ListNode) -> int:
    """
    Args:
        head: The head of a singly linked list.

    Returns:
        The maximum twin sum of the linked list.
    """
    if not head:
        return 0

    slow = head
    fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    prev = None
    current = slow
    while current:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node

    max_sum = 0
    first_half_ptr = head
    second_half_ptr = prev

    while second_half_ptr:
        max_sum = max(max_sum, first_half_ptr.val + second_half_ptr.val)
        first_half_ptr = first_half_ptr.next
        second_half_ptr = second_half_ptr.next

    return max_sum